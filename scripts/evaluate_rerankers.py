"""Evaluate precomputed reranker scores on saved retrieval candidates."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from evaluate_qdrant_retrieval import evaluate_rankings, read_rows, write_csv  # noqa: E402


RERANKERS = {
    "bge_reranker_v2_m3": "bge_reranker_v2_m3_scores.npy",
    "qwen3_reranker_0_6b": "qwen3_reranker_0_6b_scores.npy",
    "qwen3_reranker_4b": "qwen3_reranker_4b_scores.npy",
}


def load_jsonl_run(path: Path) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    with (path / "retrieved_results.jsonl").open("r", encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                item = json.loads(line)
                rows[str(item["query_id"])] = item
    if not rows:
        raise ValueError(f"No retrieval results found in {path}")
    return rows


def load_timing_rows(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return [
            {
                **row,
                "seconds": float(row["seconds"]),
                "items": float(row["items"]) if row["items"] else None,
                "items_per_second": (
                    float(row["items_per_second"]) if row["items_per_second"] else None
                ),
            }
            for row in csv.DictReader(stream)
        ]


def timing_for_model(timings: list[dict[str, Any]], model: str) -> dict[str, Any]:
    rows = [row for row in timings if row["model"] == model]
    score_row = next((row for row in rows if row["phase"].startswith("score ")), None)
    load_row = next((row for row in rows if row["phase"] == "load model"), None)
    total_row = next((row for row in rows if row["phase"] == "total measured time"), None)
    if score_row is None:
        raise ValueError(f"No reranker scoring timing found for {model}")
    candidate_pairs = 100 * 100
    measured_pairs = score_row["items"] or 0.0
    estimated_score_seconds = score_row["seconds"] * candidate_pairs / measured_pairs
    return {
        "model": model,
        "measured_pair_count": measured_pairs,
        "measured_score_seconds": score_row["seconds"],
        "measured_pairs_per_second": score_row["items_per_second"],
        "model_load_seconds": load_row["seconds"] if load_row else None,
        "total_measured_seconds": total_row["seconds"] if total_row else None,
        "candidate_pair_count": candidate_pairs,
        "estimated_candidate_score_seconds": estimated_score_seconds,
        "estimated_load_plus_score_seconds": estimated_score_seconds
        + (load_row["seconds"] if load_row else 0.0),
        "timing_note": (
            "Score time is a linear estimate for 10,000 pairs from the measured "
            "29,700-pair Kaggle run; it is not a new model inference run."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scores-dir",
        type=Path,
        default=PROJECT_ROOT / "data/kaggle_artifacts/virhe4qa_model_sweep_full",
    )
    parser.add_argument("--candidate-run", type=Path, required=True)
    parser.add_argument("--reranker", choices=sorted(RERANKERS), required=True)
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT / "data/retrieval_runs")
    parser.add_argument("--run-name", required=True)
    parser.add_argument("--candidate-limit", type=int, default=100)
    parser.add_argument("--ks", default="1,3,5,10,20,50,100")
    parser.add_argument("--error-k", type=int, default=20)
    args = parser.parse_args()

    ks = sorted({int(value.strip()) for value in args.ks.split(",") if value.strip()})
    if not ks or any(value < 1 for value in ks) or max(ks) > args.candidate_limit:
        parser.error("ks must contain positive values no greater than candidate-limit")
    if args.candidate_limit < 1:
        parser.error("candidate-limit must be positive")

    scores_dir = args.scores_dir.resolve()
    query_rows = read_rows(scores_dir / "queries_manifest.csv")
    chunk_rows = read_rows(scores_dir / "chunks_manifest.csv")
    pair_rows = read_rows(scores_dir / "reranker_pair_manifest.csv")
    score_matrix = np.load(scores_dir / RERANKERS[args.reranker], mmap_mode="r")
    expected_shape = (len(query_rows), len(chunk_rows))
    if tuple(score_matrix.shape) != expected_shape:
        raise ValueError(f"Expected score shape {expected_shape}, got {score_matrix.shape}")

    query_ids = [row["query_id"] for row in query_rows]
    chunk_ids = [row["chunk_id"] for row in chunk_rows]
    chunk_index = {chunk_id: index for index, chunk_id in enumerate(chunk_ids)}
    if len(chunk_index) != len(chunk_ids):
        raise ValueError("Duplicate chunk IDs in chunks_manifest.csv")
    expected_pairs = len(query_ids) * len(chunk_ids)
    if len(pair_rows) != expected_pairs:
        raise ValueError(f"Expected {expected_pairs} pair rows, got {len(pair_rows)}")
    for pair_index, pair in enumerate(pair_rows):
        expected_query = query_ids[pair_index // len(chunk_ids)]
        expected_chunk = chunk_ids[pair_index % len(chunk_ids)]
        if pair["query_id"] != expected_query or pair["chunk_id"] != expected_chunk:
            raise ValueError("reranker_pair_manifest.csv is not row-major aligned with score matrices")

    candidate_run = args.candidate_run.resolve()
    candidates_by_query = load_jsonl_run(candidate_run)
    if set(candidates_by_query) != set(query_ids):
        raise ValueError("Candidate run query IDs do not match queries_manifest.csv")

    timing = timing_for_model(
        load_timing_rows(scores_dir / "model_timings.csv"),
        {
            "bge_reranker_v2_m3": "BAAI/bge-reranker-v2-m3",
            "qwen3_reranker_0_6b": "Qwen/Qwen3-Reranker-0.6B",
            "qwen3_reranker_4b": "Qwen/Qwen3-Reranker-4B",
        }[args.reranker],
    )

    rankings: list[list[dict[str, Any]]] = []
    result_rows: list[dict[str, Any]] = []
    missing_candidate_chunks = 0
    gold_missing_from_candidates = 0
    started = time.perf_counter()
    for query_index, query_row in enumerate(query_rows):
        query_id = query_row["query_id"]
        candidates = candidates_by_query[query_id]["results"][: args.candidate_limit]
        if query_row["gold_chunk_id"] not in {str(item["chunk_id"]) for item in candidates}:
            gold_missing_from_candidates += 1
        reranked: list[dict[str, Any]] = []
        for candidate in candidates:
            chunk_id = str(candidate["chunk_id"])
            column = chunk_index.get(chunk_id)
            if column is None:
                missing_candidate_chunks += 1
                continue
            reranked.append(
                {
                    "chunk_id": chunk_id,
                    "document_id": str(candidate.get("document_id", "")),
                    "text": str(candidate.get("text", "")),
                    "retrieval_rank": int(candidate.get("rank", 0)),
                    "retrieval_score": float(candidate.get("score", 0.0)),
                    "reranker_score": float(score_matrix[query_index, column]),
                }
            )
        reranked.sort(
            key=lambda item: (-item["reranker_score"], item["chunk_id"])
        )
        ranking: list[dict[str, Any]] = []
        for rank, item in enumerate(reranked, start=1):
            result = {"rank": rank, "score": item["reranker_score"], **item}
            ranking.append(result)
            result_rows.append(
                {
                    "query_id": query_id,
                    "question": query_row["question"],
                    "gold_chunk_id": query_row["gold_chunk_id"],
                    "rank": rank,
                    "chunk_id": item["chunk_id"],
                    "document_id": item["document_id"],
                    "reranker_score": item["reranker_score"],
                    "retrieval_rank": item["retrieval_rank"],
                    "retrieval_score": item["retrieval_score"],
                    "is_gold": item["chunk_id"] == query_row["gold_chunk_id"],
                    "text": item["text"],
                }
            )
        rankings.append(ranking)

    elapsed = time.perf_counter() - started
    metrics, first_ranks = evaluate_rankings(
        rankings,
        [{row["gold_chunk_id"]} for row in query_rows],
        ks,
    )

    output_dir = (args.output_root / args.run_name).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    run_config = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "precomputed_reranker_scores",
        "reranker": args.reranker,
        "candidate_run": str(candidate_run),
        "candidate_limit": args.candidate_limit,
        "query_count": len(query_rows),
        "candidate_count": len(rankings[0]) if rankings else 0,
        "missing_candidate_chunks": missing_candidate_chunks,
        "gold_missing_from_candidates": gold_missing_from_candidates,
        "ks": ks,
        "evaluation_seconds": elapsed,
        "timing": timing,
        "scores_dir": str(scores_dir),
    }
    (output_dir / "run_config.json").write_text(
        json.dumps(run_config, ensure_ascii=False, indent=2), encoding="utf-8"
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
            {"query_id": row["query_id"], "gold_chunk_id": row["gold_chunk_id"], "first_gold_rank": rank or ""}
            for row, rank in zip(query_rows, first_ranks, strict=True)
        ],
    )
    write_csv(
        output_dir / "retrieved_results.csv",
        [
            "query_id", "question", "gold_chunk_id", "rank", "chunk_id",
            "document_id", "reranker_score", "retrieval_rank", "retrieval_score",
            "is_gold", "text",
        ],
        result_rows,
    )
    with (output_dir / "retrieved_results.jsonl").open("w", encoding="utf-8") as stream:
        for query_row, ranking, first_rank in zip(query_rows, rankings, first_ranks, strict=True):
            stream.write(
                json.dumps(
                    {
                        "query_id": query_row["query_id"],
                        "question": query_row["question"],
                        "gold_chunk_id": query_row["gold_chunk_id"],
                        "first_gold_rank": first_rank,
                        "results": ranking,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    error_k = min(args.error_k, max(ks))
    failures = []
    for query_row, ranking in zip(query_rows, rankings, strict=True):
        if not any(item["chunk_id"] == query_row["gold_chunk_id"] for item in ranking[:error_k]):
            failures.append(
                {
                    "query_id": query_row["query_id"],
                    "question": query_row["question"],
                    "gold_chunk_id": query_row["gold_chunk_id"],
                    "retrieved_chunk_ids": json.dumps(
                        [item["chunk_id"] for item in ranking[:error_k]], ensure_ascii=False
                    ),
                }
            )
    errors_dir = output_dir / "errors"
    errors_dir.mkdir(exist_ok=True)
    write_csv(
        errors_dir / f"fail@{error_k}.csv",
        ["query_id", "question", "gold_chunk_id", "retrieved_chunk_ids"],
        failures,
    )

    print(json.dumps({"output_dir": str(output_dir), **metrics, "timing": timing}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
