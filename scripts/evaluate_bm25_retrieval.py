"""Evaluate a small BM25 baseline on the 100 ViRHE4QA queries."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))
if str(PROJECT_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from evaluate_qdrant_retrieval import evaluate_rankings, read_rows, write_csv  # noqa: E402
from rag_manything.search.bm25 import BM25Index  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--artifacts-dir",
        type=Path,
        default=PROJECT_ROOT / "data/kaggle_artifacts/virhe4qa_model_sweep",
    )
    parser.add_argument("--ks", default="1,3,5,10,20,50,100")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--k1", type=float, default=1.5)
    parser.add_argument("--b", type=float, default=0.75)
    parser.add_argument("--error-k", type=int, default=20)
    parser.add_argument("--run-name", default="bm25_100")
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT / "data/retrieval_runs")
    args = parser.parse_args()

    ks = sorted({int(value.strip()) for value in args.ks.split(",") if value.strip()})
    if not ks or any(value < 1 for value in ks):
        parser.error("ks must contain positive integers")
    if args.limit < max(ks) or args.error_k < 1:
        parser.error("limit must be at least max(ks), and error-k must be positive")

    artifacts_dir = args.artifacts_dir.resolve()
    query_rows = read_rows(artifacts_dir / "queries_manifest.csv")
    with (artifacts_dir / "chunks_manifest.csv").open(
        "r", encoding="utf-8-sig", newline=""
    ) as stream:
        chunk_rows = [dict(row) for row in csv.DictReader(stream)]
    if not chunk_rows:
        raise ValueError("No chunk rows found")

    index_started = time.perf_counter()
    index = BM25Index(
        [row["text"] for row in chunk_rows],
        k1=args.k1,
        b=args.b,
    )
    index_elapsed = time.perf_counter() - index_started

    rankings: list[list[dict[str, Any]]] = []
    result_rows: list[dict[str, Any]] = []
    search_started = time.perf_counter()
    for query_number, query in enumerate(query_rows, start=1):
        scores = index.scores(query["question"])
        order = sorted(
            (index for index, score in enumerate(scores) if score > 0),
            key=lambda item: (-scores[item], chunk_rows[item]["chunk_id"]),
        )[: args.limit]
        ranking: list[dict[str, Any]] = []
        for rank, item_index in enumerate(order, start=1):
            chunk = chunk_rows[item_index]
            item = {
                "rank": rank,
                "chunk_id": chunk["chunk_id"],
                "document_id": chunk["document_id"],
                "score": float(scores[item_index]),
                "text": chunk["text"],
            }
            ranking.append(item)
            result_rows.append(
                {
                    "query_id": query["query_id"],
                    "question": query["question"],
                    "gold_chunk_id": query["gold_chunk_id"],
                    "rank": rank,
                    "chunk_id": item["chunk_id"],
                    "document_id": item["document_id"],
                    "score": item["score"],
                    "is_gold": item["chunk_id"] == query["gold_chunk_id"],
                    "text": item["text"],
                }
            )
        rankings.append(ranking)
        print(f"Retrieved {query_number}/{len(query_rows)} queries", flush=True)
    search_elapsed = time.perf_counter() - search_started

    gold_by_query = [{query["gold_chunk_id"]} for query in query_rows]
    metrics, first_ranks = evaluate_rankings(rankings, gold_by_query, ks)
    output_dir = (args.output_root / args.run_name).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    config = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "bm25",
        "k1": args.k1,
        "b": args.b,
        "tokenizer": "unicode_word_tokens_nfc_lowercase",
        "ks": ks,
        "query_count": len(query_rows),
        "collection_point_count": len(chunk_rows),
        "max_retrieved_per_query": args.limit,
        "index_build_seconds": index_elapsed,
        "search_elapsed_seconds": search_elapsed,
        "elapsed_seconds": index_elapsed + search_elapsed,
        "average_query_seconds": search_elapsed / len(query_rows),
        "query_processor_enabled": False,
        "reranking_enabled": False,
        "artifact_dir": str(artifacts_dir),
    }
    (output_dir / "run_config.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (output_dir / "metrics.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_csv(
        output_dir / "metrics.csv",
        ["metric", "value"],
        [{"metric": key, "value": value} for key, value in metrics.items()],
    )
    write_csv(
        output_dir / "ranks.csv",
        ["query_id", "gold_chunk_id", "first_gold_rank"],
        [
            {
                "query_id": query["query_id"],
                "gold_chunk_id": query["gold_chunk_id"],
                "first_gold_rank": rank or "",
            }
            for query, rank in zip(query_rows, first_ranks, strict=True)
        ],
    )
    write_csv(
        output_dir / "retrieved_results.csv",
        [
            "query_id",
            "question",
            "gold_chunk_id",
            "rank",
            "chunk_id",
            "document_id",
            "score",
            "is_gold",
            "text",
        ],
        result_rows,
    )
    with (output_dir / "retrieved_results.jsonl").open("w", encoding="utf-8") as stream:
        for query, ranking, first_rank in zip(query_rows, rankings, first_ranks, strict=True):
            stream.write(
                json.dumps(
                    {
                        "query_id": query["query_id"],
                        "question": query["question"],
                        "gold_chunk_id": query["gold_chunk_id"],
                        "first_gold_rank": first_rank,
                        "results": ranking,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    error_k = min(args.error_k, args.limit)
    failures = []
    for query, ranking in zip(query_rows, rankings, strict=True):
        top = ranking[:error_k]
        if not any(item["chunk_id"] == query["gold_chunk_id"] for item in top):
            failures.append(
                {
                    "query_id": query["query_id"],
                    "question": query["question"],
                    "gold_chunk_id": query["gold_chunk_id"],
                    "retrieved_chunk_ids": json.dumps(
                        [item["chunk_id"] for item in top], ensure_ascii=False
                    ),
                    "retrieved_scores": json.dumps([item["score"] for item in top]),
                }
            )
    errors_dir = output_dir / "errors"
    errors_dir.mkdir(exist_ok=True)
    write_csv(
        errors_dir / f"fail@{error_k}.csv",
        ["query_id", "question", "gold_chunk_id", "retrieved_chunk_ids", "retrieved_scores"],
        failures,
    )

    print(json.dumps({"output_dir": str(output_dir), **metrics}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
