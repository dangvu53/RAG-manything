"""Load Kaggle embedding artifacts into a local Qdrant named-vector collection.

The Kaggle notebook writes document vectors in the same row order as
``chunks_manifest.csv``. Query vectors and reranker scores stay as offline
evaluation artifacts; only chunk vectors and payloads are ingested here.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import uuid
from pathlib import Path
from typing import Any

import numpy as np
from qdrant_client import models

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from rag_manything.retrieval.models import sparse_vector_from_mapping  # noqa: E402
from rag_manything.retrieval.qdrant_store import QdrantStore  # noqa: E402


POINT_ID_NAMESPACE = uuid.UUID("cbb86f89-26ef-4e48-8c9f-a1f3da45786b")
SPARSE_FILE = "bge_m3_sparse.jsonl"
DENSE_FILES = {
    "bge_m3_dense.npy": "bge_m3_dense",
    "qwen3_embedding_0_6b_dense.npy": "qwen_0_6b_dense",
    "qwen3_embedding_4b_dense.npy": "qwen_4b_dense",
}


def point_id(document_id: str, chunk_id: str) -> str:
    return str(uuid.uuid5(POINT_ID_NAMESPACE, f"{document_id}:{chunk_id}"))


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        rows = [dict(row) for row in reader]
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def load_chunks(artifacts_dir: Path) -> list[dict[str, str]]:
    path = artifacts_dir / "chunks_manifest.csv"
    if not path.is_file():
        raise FileNotFoundError(f"Missing Kaggle artifact: {path}")
    rows = read_csv_rows(path)
    required = {"chunk_id", "document_id", "text"}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"chunks_manifest.csv is missing columns: {sorted(missing)}")
    seen: set[str] = set()
    for row in rows:
        chunk_id = row["chunk_id"]
        if chunk_id in seen:
            raise ValueError(f"Duplicate chunk_id in manifest: {chunk_id}")
        if not row["text"].strip():
            raise ValueError(f"Empty chunk text: {chunk_id}")
        seen.add(chunk_id)
    return rows


def load_dense_arrays(artifacts_dir: Path, row_count: int) -> dict[str, np.ndarray]:
    arrays: dict[str, np.ndarray] = {}
    for filename, vector_name in DENSE_FILES.items():
        path = artifacts_dir / filename
        if not path.is_file():
            continue
        array = np.load(path, mmap_mode="r")
        if array.ndim != 2 or array.shape[0] != row_count:
            raise ValueError(
                f"{filename} must have shape (N, D) with N={row_count}; got {array.shape}"
            )
        arrays[vector_name] = array
    if "bge_m3_dense" not in arrays:
        raise FileNotFoundError("bge_m3_dense.npy is required")
    return arrays


def load_sparse_rows(artifacts_dir: Path, chunk_ids: set[str]) -> dict[str, models.SparseVector]:
    path = artifacts_dir / SPARSE_FILE
    if not path.is_file():
        raise FileNotFoundError(f"Missing Kaggle artifact: {path}")
    rows: dict[str, models.SparseVector] = {}
    with path.open("r", encoding="utf-8-sig") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            item = json.loads(line)
            item_id = str(item["id"])
            if item_id in rows:
                raise ValueError(f"Duplicate sparse vector id at line {line_number}: {item_id}")
            rows[item_id] = sparse_vector_from_mapping(
                dict(zip(item["indices"], item["values"], strict=True))
            )
    if set(rows) != chunk_ids:
        missing = sorted(chunk_ids - set(rows))[:5]
        extra = sorted(set(rows) - chunk_ids)[:5]
        raise ValueError(f"Sparse IDs do not match chunks; missing={missing}, extra={extra}")
    return rows


def build_points(
    chunks: list[dict[str, str]],
    dense_arrays: dict[str, np.ndarray],
    sparse_rows: dict[str, models.SparseVector],
    start: int,
    stop: int,
) -> list[models.PointStruct]:
    points: list[models.PointStruct] = []
    for index in range(start, stop):
        row = chunks[index]
        chunk_id = row["chunk_id"]
        payload: dict[str, Any] = dict(row)
        payload["chunk_id"] = chunk_id
        payload["document_id"] = row["document_id"]
        payload["text"] = row["text"]
        vectors: dict[str, Any] = {
            name: np.asarray(array[index], dtype=np.float32).tolist()
            for name, array in dense_arrays.items()
        }
        vectors["bge_m3_sparse"] = sparse_rows[chunk_id]
        points.append(
            models.PointStruct(
                id=point_id(row["document_id"], chunk_id),
                vector=vectors,
                payload=payload,
            )
        )
    return points


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifacts_dir", type=Path)
    parser.add_argument("--collection", default="rag_chunks")
    parser.add_argument("--qdrant-url", default="http://localhost:6333")
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--recreate", action="store_true")
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error("--batch-size must be positive")

    artifacts_dir = args.artifacts_dir.resolve()
    chunks = load_chunks(artifacts_dir)
    dense_arrays = load_dense_arrays(artifacts_dir, len(chunks))
    sparse_rows = load_sparse_rows(artifacts_dir, {row["chunk_id"] for row in chunks})

    store = QdrantStore.from_url(
        args.qdrant_url,
        collection_name=args.collection,
    )
    store.ensure_collection(
        {name: int(array.shape[1]) for name, array in dense_arrays.items()},
        sparse_vectors=["bge_m3_sparse"],
        recreate=args.recreate,
        payload_indexes=["document_id", "split", "label"],
    )

    for start in range(0, len(chunks), args.batch_size):
        stop = min(start + args.batch_size, len(chunks))
        store.upsert(build_points(chunks, dense_arrays, sparse_rows, start, stop))
        print(f"Upserted {stop}/{len(chunks)} chunks")
    print(
        f"Done: {len(chunks)} chunks in '{args.collection}' with vectors "
        f"{sorted(dense_arrays)} + ['bge_m3_sparse']"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

