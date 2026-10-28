"""Fuse two saved retrieval runs with weighted reciprocal rank fusion."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))

from evaluate_qdrant_retrieval import evaluate_rankings, write_csv  # noqa: E402


def load_run(path: Path) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    with (path / "retrieved_results.jsonl").open("r", encoding="utf-8") as stream:
        for line in stream:
            item = json.loads(line)
            rows[item["query_id"]] = item
    if not rows:
        raise ValueError(f"No retrieval rows found in {path}")
    return rows


def parse_weights(raw: str) -> list[float]:
    values = [float(value.strip()) for value in raw.split(",") if value.strip()]
    if len(values) != 2 or any(value <= 0 for value in values):
        raise ValueError("weights must contain two positive values")
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--left-run", type=Path, required=True)
    parser.add_argument("--right-run", type=Path, required=True)
    parser.add_argument("--left-name", default="left")
    parser.add_argument("--right-name", default="right")
    parser.add_argument("--k", type=float, default=2.0)
    parser.add_argument("--weights", default="1,1")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--ks", default="1,3,5,10,20,50,100")
    parser.add_argument("--error-k", type=int, default=20)
    parser.add_argument("--run-name", required=True)
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT / "data/retrieval_runs")
    args = parser.parse_args()

    if args.k <= 0 or args.limit < 1:
        parser.error("k and limit must be positive")
    ks = sorted({int(value.strip()) for value in args.ks.split(",") if value.strip()})
    if not ks or any(value < 1 for value in ks) or max(ks) > args.limit:
        parser.error("ks must contain positive values no greater than limit")
    weights = parse_weights(args.weights)

    left = load_run(args.left_run.resolve())
    right = load_run(args.right_run.resolve())
    if set(left) != set(right):
        raise ValueError("Input retrieval runs have different query IDs")

    fused: dict[str, dict[str, Any]] = {}
    for query_id in left:
        query = left[query_id]
        candidates: dict[str, dict[str, Any]] = {}
        for branch_index, branch in enumerate((left[query_id], right[query_id])):
            for item in branch["results"]:
                chunk_id = item["chunk_id"]
                candidate = candidates.setdefault(
                    chunk_id,
                    {
                        "chunk_id": chunk_id,
                        "document_id": item["document_id"],
                        "text": item["text"],
                        "score": 0.0,
                    },
                )
                candidate["score"] += weights[branch_index] / (
                    args.k + item["rank"] - 1
                )
        ranking = sorted(
            candidates.values(),
            key=lambda item: (-item["score"], item["chunk_id"]),
        )[: args.limit]
        for rank, item in enumerate(ranking, start=1):
            item["rank"] = rank
        first_rank = next(
            (item["rank"] for item in ranking if item["chunk_id"] == query["gold_chunk_id"]),
            None,
        )
        fused[query_id] = {
            "query_id": query_id,
            "question": query["question"],
            "gold_chunk_id": query["gold_chunk_id"],
            "first_gold_rank": first_rank,
            "results": ranking,
        }

    query_ids = list(left)
    rankings = [fused[query_id]["results"] for query_id in query_ids]
    gold_by_query = [{fused[query_id]["gold_chunk_id"]} for query_id in query_ids]
    metrics, first_ranks = evaluate_rankings(rankings, gold_by_query, ks)

    output_dir = (args.output_root / args.run_name).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    config = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "client_side_rrf",
        "fusion": "rrf",
        "rrf_k": args.k,
        "weights": weights,
        "branches": [
            {"name": args.left_name, "run_dir": str(args.left_run.resolve())},
            {"name": args.right_name, "run_dir": str(args.right_run.resolve())},
        ],
        "ks": ks,
        "query_count": len(query_ids),
        "collection_point_count": 297,
        "max_retrieved_per_query": args.limit,
        "query_processor_enabled": False,
        "reranking_enabled": False,
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
                "query_id": query_id,
                "gold_chunk_id": fused[query_id]["gold_chunk_id"],
                "first_gold_rank": rank or "",
            }
            for query_id, rank in zip(query_ids, first_ranks, strict=True)
        ],
    )

    result_rows: list[dict[str, Any]] = []
    with (output_dir / "retrieved_results.jsonl").open("w", encoding="utf-8") as stream:
        for query_id in query_ids:
            item = fused[query_id]
            stream.write(json.dumps(item, ensure_ascii=False) + "\n")
            for result in item["results"]:
                result_rows.append(
                    {
                        "query_id": query_id,
                        "question": item["question"],
                        "gold_chunk_id": item["gold_chunk_id"],
                        "rank": result["rank"],
                        "chunk_id": result["chunk_id"],
                        "document_id": result["document_id"],
                        "score": result["score"],
                        "is_gold": result["chunk_id"] == item["gold_chunk_id"],
                        "text": result["text"],
                    }
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

    error_k = min(args.error_k, args.limit)
    failures = []
    for query_id in query_ids:
        item = fused[query_id]
        top = item["results"][:error_k]
        if not any(result["chunk_id"] == item["gold_chunk_id"] for result in top):
            failures.append(
                {
                    "query_id": query_id,
                    "question": item["question"],
                    "gold_chunk_id": item["gold_chunk_id"],
                    "retrieved_chunk_ids": json.dumps(
                        [result["chunk_id"] for result in top], ensure_ascii=False
                    ),
                    "retrieved_scores": json.dumps([result["score"] for result in top]),
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
