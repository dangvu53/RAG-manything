"""Tune and save full-query plus decomposed-query dense fusion for ViHERMES."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))

from evaluate_qdrant_retrieval import evaluate_rankings  # noqa: E402
from evaluate_vihermes_query_processing import evaluate_strategy  # noqa: E402


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return [dict(row) for row in csv.DictReader(stream)]


def make_rankings(scores: np.ndarray, context_ids: list[str], limit: int) -> list[list[dict[str, Any]]]:
    result = []
    for row in scores:
        order = np.argsort(-row, kind="stable")[:limit]
        result.append(
            [
                {"rank": rank, "chunk_id": context_ids[int(index)], "score": float(row[index])}
                for rank, index in enumerate(order, start=1)
            ]
        )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--artifact-dir",
        type=Path,
        default=PROJECT_ROOT / "data/retrieval_runs/query_processing/vihermes_bge_m3",
    )
    parser.add_argument(
        "--dataset-dir",
        type=Path,
        default=PROJECT_ROOT / "data/benchmark_datasets/ViHERMES",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "data/retrieval_runs/query_processing/vihermes_bge_m3_full_plus_decomposition",
    )
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--ks", default="1,3,5,10,20,50,100")
    args = parser.parse_args()
    if args.alpha < 0 or args.limit < 1:
        parser.error("alpha must be non-negative and limit must be positive")
    ks = sorted({int(value.strip()) for value in args.ks.split(",") if value.strip()})
    if not ks or any(value < 1 for value in ks) or max(ks) > args.limit:
        parser.error("ks must contain positive values no greater than limit")

    artifact_dir = args.artifact_dir.resolve()
    dataset_dir = args.dataset_dir.resolve()
    query_rows = read_rows(dataset_dir / "qa.csv")
    context_rows = read_rows(dataset_dir / "contexts.csv")
    manifests = [
        json.loads(line)
        for line in (artifact_dir / "subqueries.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if len(manifests) != len(query_rows):
        raise ValueError("subqueries.jsonl and qa.csv have different row counts")

    context_dense = np.load(artifact_dir / "context_dense.npy", mmap_mode="r")
    query_dense = np.load(artifact_dir / "query_dense.npy", mmap_mode="r")
    subquery_dense = np.load(artifact_dir / "subquery_dense.npy", mmap_mode="r")
    context_ids = [row["context_id"] for row in context_rows]
    full_scores = np.asarray(query_dense @ context_dense.T, dtype=np.float32)
    max_scores = np.empty_like(full_scores)
    offset = 0
    for index, manifest in enumerate(manifests):
        count = len(manifest["subqueries"])
        max_scores[index] = np.max(
            subquery_dense[offset : offset + count] @ context_dense.T,
            axis=0,
        )
        offset += count

    gold_sets = [set(json.loads(row["gold_context_ids"])) for row in query_rows]
    hops = [row["hop_level"] for row in query_rows]
    grid = []
    holdout_indexes = [index for index in range(len(query_rows)) if index % 5 == 0]
    train_indexes = [index for index in range(len(query_rows)) if index % 5 != 0]
    holdout_grid = []
    for alpha in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0]:
        rankings = make_rankings(full_scores + alpha * max_scores, context_ids, args.limit)
        metrics, _ = evaluate_rankings(rankings, gold_sets, ks)
        grid.append({"alpha": alpha, **metrics})
        train_metrics, _ = evaluate_rankings(
            [rankings[index] for index in train_indexes],
            [gold_sets[index] for index in train_indexes],
            ks,
        )
        holdout_grid.append({"alpha": alpha, **train_metrics})
    selected_alpha = max(
        holdout_grid,
        key=lambda row: (row.get("Recall@10", 0.0), row.get("MRR@10", 0.0)),
    )["alpha"]

    fused_rankings = make_rankings(full_scores + args.alpha * max_scores, context_ids, args.limit)
    evaluation = evaluate_strategy(fused_rankings, gold_sets, hops, ks)
    baseline_rankings = make_rankings(full_scores, context_ids, args.limit)
    selected_rankings = make_rankings(
        full_scores + selected_alpha * max_scores, context_ids, args.limit
    )
    holdout_baseline, _ = evaluate_rankings(
        [baseline_rankings[index] for index in holdout_indexes],
        [gold_sets[index] for index in holdout_indexes],
        ks,
    )
    holdout_selected, _ = evaluate_rankings(
        [selected_rankings[index] for index in holdout_indexes],
        [gold_sets[index] for index in holdout_indexes],
        ks,
    )
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "metrics.json").write_text(
        json.dumps(evaluation, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (output_dir / "fusion_grid.json").write_text(
        json.dumps(grid, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (output_dir / "holdout_validation.json").write_text(
        json.dumps(
            {
                "split": "index % 5 == 0",
                "train_count": len(train_indexes),
                "holdout_count": len(holdout_indexes),
                "selected_alpha_from_train": selected_alpha,
                "train_grid": holdout_grid,
                "holdout_baseline": holdout_baseline,
                "holdout_selected_fusion": holdout_selected,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    with (output_dir / "fusion_grid.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(grid[0]))
        writer.writeheader()
        writer.writerows(grid)
    with (output_dir / "rankings.jsonl").open("w", encoding="utf-8") as stream:
        for row, ranking in zip(query_rows, fused_rankings, strict=True):
            stream.write(
                json.dumps(
                    {
                        "query_id": row["id"],
                        "question": row["question"],
                        "hop_level": row["hop_level"],
                        "gold_context_ids": json.loads(row["gold_context_ids"]),
                        "results": ranking,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
    (output_dir / "run_config.json").write_text(
        json.dumps(
            {
                "created_at_utc": datetime.now(timezone.utc).isoformat(),
                "strategy": "full_query_dense_plus_alpha_times_decomposed_max_dense",
                "alpha": args.alpha,
                "limit": args.limit,
                "ks": ks,
                "query_count": len(query_rows),
                "context_count": len(context_rows),
                "source_artifact_dir": str(artifact_dir),
                "dataset_dir": str(dataset_dir),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps({"output_dir": str(output_dir), **evaluation["overall"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
