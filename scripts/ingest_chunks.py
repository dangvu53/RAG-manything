"""Embed parsed/chunked JSONL rows with BGE-M3 and upsert them into Qdrant."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import unicodedata
import uuid
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from qdrant_client import QdrantClient, models

DENSE_VECTOR_NAME = "bge_m3_dense"
SPARSE_VECTOR_NAME = "bge_m3_sparse"
BGE_M3_DENSE_SIZE = 1024
POINT_ID_NAMESPACE = uuid.UUID("cbb86f89-26ef-4e48-8c9f-a1f3da45786b")
VECTOR_FIELDS = {"dense", "sparse", "embedding", "vector"}


def normalize_chunk(row: dict[str, Any], line_number: int) -> dict[str, Any]:
    """Validate a JSONL row and normalize its metadata into Qdrant payload fields."""
    metadata = row.get("metadata", {})
    if not isinstance(metadata, dict):
        raise ValueError(f"Line {line_number}: 'metadata' must be a JSON object")

    chunk_id = row.get("chunk_id")
    document_id = row.get("document_id") or metadata.get("document_id")
    text = row.get("text")
    if chunk_id is None or not str(chunk_id).strip():
        raise ValueError(f"Line {line_number}: missing 'chunk_id'")
    if document_id is None or not str(document_id).strip():
        raise ValueError(f"Line {line_number}: missing 'document_id'")
    if not isinstance(text, str) or not text.strip():
        raise ValueError(f"Line {line_number}: 'text' must be a non-empty string")

    # Accept either flat metadata (the existing baseline format) or a nested
    # metadata object. Reserved fields and supplied vectors are not payload data.
    reserved = {"chunk_id", "document_id", "text", "search_text", "metadata"} | VECTOR_FIELDS
    flat_fields = {key: value for key, value in row.items() if key not in reserved}
    payload = {
        **metadata,
        **flat_fields,
        "chunk_id": str(chunk_id),
        "document_id": str(document_id),
        "text": text.strip(),
    }
    title = payload.get("title")
    search_text = row.get("search_text") or (f"{title}\n{text}" if title else text)

    return {
        "chunk_id": str(chunk_id),
        "document_id": str(document_id),
        "text": text.strip(),
        "search_text": str(search_text).strip(),
        "payload": payload,
    }


def load_csv_chunks(path: Path) -> list[dict[str, Any]]:
    """Read the ViRHE4QA mock CSV as one indexed chunk per context row."""
    chunks = []
    seen_ids: set[tuple[str, str]] = set()
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or "context" not in reader.fieldnames:
            raise ValueError("CSV input must contain a 'context' column")

        for row_number, row in enumerate(reader, start=2):
            text = row.get("context")
            if not isinstance(text, str) or not text.strip():
                raise ValueError(f"CSV row {row_number}: 'context' must be non-empty")

            canonical_text = unicodedata.normalize(
                "NFC", text.replace("\r\n", "\n").replace("\r", "\n").strip()
            )
            digest = hashlib.sha256(canonical_text.encode("utf-8")).hexdigest()[:20]
            document_id = f"virhe4qa_{digest}"
            chunk_id = "chunk_0001"
            metadata = {
                "source_dataset": "ViRHE4QA_v2",
                "source_split": row.get("split", ""),
                "source_index": row.get("index", ""),
                "source_label": row.get("label", ""),
            }
            chunk = normalize_chunk(
                {
                    "document_id": document_id,
                    "chunk_id": chunk_id,
                    "text": text,
                    "metadata": metadata,
                },
                row_number,
            )
            logical_id = (chunk["document_id"], chunk["chunk_id"])
            if logical_id in seen_ids:
                raise ValueError(
                    f"CSV row {row_number}: duplicate context produces duplicate chunk ID"
                )
            seen_ids.add(logical_id)
            chunks.append(chunk)

    if not chunks:
        raise ValueError(f"No chunks found in {path}")
    return chunks


def load_chunks(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(f"Chunks file not found: {path}")
    if path.suffix.lower() == ".csv":
        return load_csv_chunks(path)

    chunks = []
    seen_ids: set[tuple[str, str]] = set()
    with path.open("r", encoding="utf-8-sig") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Line {line_number}: invalid JSON: {exc}") from exc
            if not isinstance(row, dict):
                raise ValueError(f"Line {line_number}: each JSONL row must be an object")

            chunk = normalize_chunk(row, line_number)
            logical_id = (chunk["document_id"], chunk["chunk_id"])
            if logical_id in seen_ids:
                raise ValueError(f"Line {line_number}: duplicate chunk_id {chunk['chunk_id']!r}")
            seen_ids.add(logical_id)
            chunks.append(chunk)

    if not chunks:
        raise ValueError(f"No chunks found in {path}")
    return chunks


def point_id(document_id: str, chunk_id: str) -> str:
    """Create a stable Qdrant UUID while allowing chunk IDs local to each document."""
    return str(uuid.uuid5(POINT_ID_NAMESPACE, f"{document_id}:{chunk_id}"))


def sparse_vector(weights: dict[str, float]) -> models.SparseVector:
    pairs = sorted(
        (int(token_id), float(weight))
        for token_id, weight in weights.items()
        if float(weight) != 0.0
    )
    return models.SparseVector(
        indices=[token_id for token_id, _ in pairs],
        values=[weight for _, weight in pairs],
    )


def ensure_collection(client: QdrantClient, collection: str) -> None:
    if not client.collection_exists(collection):
        client.create_collection(
            collection_name=collection,
            vectors_config={
                DENSE_VECTOR_NAME: models.VectorParams(
                    size=BGE_M3_DENSE_SIZE,
                    distance=models.Distance.COSINE,
                )
            },
            sparse_vectors_config={
                SPARSE_VECTOR_NAME: models.SparseVectorParams(),
            },
        )

    # These keyword fields are useful for document-level and corpus filters.
    for field in ("document_id", "product", "document_type", "version"):
        client.create_payload_index(
            collection_name=collection,
            field_name=field,
            field_schema=models.PayloadSchemaType.KEYWORD,
            wait=True,
        )


def build_points(embedder: Any, chunks: list[dict[str, Any]]) -> list[models.PointStruct]:
    encoded = embedder.encode(
        [chunk["search_text"] for chunk in chunks],
        return_dense=True,
        return_sparse=True,
        return_colbert_vecs=False,
    )
    points = []
    for chunk, dense, sparse in zip(
        chunks, encoded["dense_vecs"], encoded["lexical_weights"], strict=True
    ):
        dense_values = dense.tolist()
        if len(dense_values) != BGE_M3_DENSE_SIZE:
            raise ValueError(
                f"BGE-M3 dense vector must have {BGE_M3_DENSE_SIZE} dimensions; "
                f"got {len(dense_values)}"
            )
        points.append(
            models.PointStruct(
                id=point_id(chunk["document_id"], chunk["chunk_id"]),
                vector={
                    DENSE_VECTOR_NAME: dense_values,
                    SPARSE_VECTOR_NAME: sparse_vector(sparse),
                },
                payload=chunk["payload"],
            )
        )
    return points


def batches(items: list[Any], size: int):
    for start in range(0, len(items), size):
        yield items[start : start + size]


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    load_dotenv(project_root / ".env")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "chunks_file", type=Path, help="CSV mock dataset or JSONL file containing parsed chunks"
    )
    parser.add_argument("--collection", default=os.getenv("QDRANT_COLLECTION", "rag_chunks"))
    parser.add_argument("--batch-size", type=int, default=8)
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error("--batch-size must be at least 1")

    try:
        chunks = load_chunks(args.chunks_file)
        qdrant = QdrantClient(
            url=os.getenv("QDRANT_URL", "http://localhost:6333"),
            api_key=os.getenv("QDRANT_API_KEY") or None,
            timeout=60,
            check_compatibility=False,
        )
        ensure_collection(qdrant, args.collection)

        from FlagEmbedding import BGEM3FlagModel

        model = BGEM3FlagModel(
            os.getenv("EMBEDDING_MODEL", "BAAI/bge-m3"),
            use_fp16=os.getenv("EMBEDDING_FP16", "false").lower() == "true",
        )
        total = 0
        for batch in batches(chunks, args.batch_size):
            points = build_points(model, batch)
            qdrant.upsert(collection_name=args.collection, points=points, wait=True)
            total += len(points)
            print(f"Upserted {total}/{len(chunks)} chunks")
        print(f"Done: {total} chunks ingested into collection '{args.collection}'")
        return 0
    except Exception as exc:
        print(f"Ingestion failed: {exc}", file=sys.stderr)
        print("Check that Qdrant is running (docker compose up -d qdrant).", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
