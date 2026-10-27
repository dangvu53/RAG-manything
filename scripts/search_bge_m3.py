"""Run BGE-M3 dense+sparse hybrid retrieval against local Qdrant.

Use ``--query-id`` to search with a query vector already exported by Kaggle,
or pass a new question to encode it with a local BGE-M3 model.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from rag_manything.retrieval import (  # noqa: E402
    BgeM3QueryEncoder,
    CallableQueryEncoder,
    HybridSearcher,
    QdrantStore,
    QueryRepresentation,
    RetrievalConfig,
    RetrievalPipeline,
)
from rag_manything.retrieval.models import sparse_vector_from_mapping  # noqa: E402


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return [dict(row) for row in csv.DictReader(stream)]


def load_kaggle_query(artifacts_dir: Path, query_id: str) -> tuple[str, QueryRepresentation]:
    queries = read_rows(artifacts_dir / "queries_manifest.csv")
    matches = [(index, row) for index, row in enumerate(queries) if row["query_id"] == query_id]
    if not matches:
        raise ValueError(f"Unknown query_id: {query_id}")
    index, row = matches[0]

    dense = np.load(artifacts_dir / "bge_m3_query_dense.npy", mmap_mode="r")[index].tolist()
    sparse_by_id: dict[str, dict[str, Any]] = {}
    with (artifacts_dir / "bge_m3_query_sparse.jsonl").open("r", encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                item = json.loads(line)
                sparse_by_id[str(item["id"])] = item
    sparse = sparse_by_id.get(query_id)
    if sparse is None:
        raise ValueError(f"No sparse query vector for: {query_id}")

    representation = QueryRepresentation(
        query_text=row["question"],
        dense=dense,
        sparse=sparse_vector_from_mapping(
            dict(zip(sparse["indices"], sparse["values"], strict=True))
        ),
        dense_vector_name="bge_m3_dense",
        sparse_vector_name="bge_m3_sparse",
        query_id=query_id,
    )
    return row["question"], representation


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    query_group = parser.add_mutually_exclusive_group(required=True)
    query_group.add_argument("question", nargs="?")
    query_group.add_argument("--query-id", help="Use a query vector from the Kaggle artifacts")
    parser.add_argument("--artifacts-dir", type=Path, default=PROJECT_ROOT / "data/kaggle_artifacts/virhe4qa_model_sweep")
    parser.add_argument("--collection", default="virhe4qa_297")
    parser.add_argument("--qdrant-url", default="http://localhost:6333")
    parser.add_argument("--embedding-model", default="BAAI/bge-m3")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--prefetch-limit", type=int, default=50)
    parser.add_argument("--text-chars", type=int, default=500)
    parser.add_argument("--fp16", action="store_true")
    args = parser.parse_args()
    if args.limit < 1 or args.prefetch_limit < 1 or args.text_chars < 0:
        parser.error("limit, prefetch-limit, and text-chars must be valid positive values")

    config = RetrievalConfig(
        collection_name=args.collection,
        search_mode="hybrid",
        enable_query_processing=False,
        enable_reranking=False,
        prefetch_limit=args.prefetch_limit,
        final_limit=args.limit,
    )
    store = QdrantStore.from_url(args.qdrant_url, collection_name=args.collection)

    if args.query_id:
        question, representation = load_kaggle_query(args.artifacts_dir, args.query_id)
        encoder = CallableQueryEncoder(lambda _: representation)
    else:
        question = args.question
        from FlagEmbedding import BGEM3FlagModel

        encoder = BgeM3QueryEncoder(
            BGEM3FlagModel(args.embedding_model, use_fp16=args.fp16)
        )

    pipeline = RetrievalPipeline(
        searcher=HybridSearcher(store, config),
        query_encoder=encoder,
        config=config,
    )
    results = pipeline.retrieve(question)
    print(f"Query: {question}")
    print(f"Collection: {args.collection}; results: {len(results)}")
    for rank, result in enumerate(results, start=1):
        text = result.text.replace("\n", " ")
        if len(text) > args.text_chars:
            text = text[: args.text_chars] + "..."
        print(json.dumps({
            "rank": rank,
            "score": result.score,
            "chunk_id": result.chunk_id,
            "document_id": result.payload.get("document_id"),
            "text": text,
        }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

