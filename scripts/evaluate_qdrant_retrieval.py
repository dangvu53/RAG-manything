"""Evaluate Qdrant retrieval on the 100 Kaggle query vectors.

The metric names and binary-relevance calculations mirror ViRE's evaluator.
Each prepared query currently has one gold chunk, but the calculation keeps
the multi-gold form so the output remains compatible with the benchmark style.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from rag_manything.retrieval import (  # noqa: E402
    HybridSearcher,
    QdrantStore,
    QueryRepresentation,
    RetrievalConfig,
)
from rag_manything.retrieval.models import sparse_vector_from_mapping  # noqa: E402


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = [dict(row) for row in csv.DictReader(stream)]
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def load_sparse_queries(path: Path) -> dict[str, Any]:
    vectors: dict[str, Any] = {}
    with path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            item = json.loads(line)
            query_id = str(item["id"])
            if query_id in vectors:
                raise ValueError(f"Duplicate sparse query at line {line_number}: {query_id}")
            vectors[query_id] = sparse_vector_from_mapping(
                dict(zip(item["indices"], item["values"], strict=True))
            )
    return vectors


def parse_ks(raw: str) -> list[int]:
    values = sorted({int(value.strip()) for value in raw.split(",") if value.strip()})
    if not values or any(value < 1 for value in values):
        raise ValueError("ks must contain positive integers")
    return values


def evaluate_rankings(
    rankings: list[list[dict[str, Any]]],
    gold_by_query: list[set[str]],
    ks: list[int],
) -> tuple[dict[str, float | None], list[int | None]]:
    first_ranks: list[int | None] = []
    for ranking, gold in zip(rankings, gold_by_query, strict=True):
        first_rank = next(
            (item["rank"] for item in ranking if item["chunk_id"] in gold),
            None,
        )
        first_ranks.append(first_rank)

    metrics: dict[str, float | None] = {}
    for k in ks:
        precision_values: list[float] = []
        recall_values: list[float] = []
        mrr_values: list[float] = []
        ndcg_values: list[float] = []
        map_values: list[float] = []
        hit_values: list[float] = []

        for ranking, gold in zip(rankings, gold_by_query, strict=True):
            top = ranking[:k]
            relevant_ranks = [
                index + 1 for index, item in enumerate(top) if item["chunk_id"] in gold
            ]
            hit_count = len(relevant_ranks)
            relevant_total = len(gold)
            denominator = min(k, len(ranking)) or k
            precision_values.append(hit_count / denominator)
            recall_values.append(hit_count / relevant_total if relevant_total else 0.0)
            hit_values.append(1.0 if hit_count else 0.0)

            first_rank = relevant_ranks[0] if relevant_ranks else None
            mrr_values.append(1.0 / first_rank if first_rank else 0.0)

            dcg = sum(1.0 / math.log2(rank + 1) for rank in relevant_ranks)
            ideal_count = min(relevant_total, k)
            idcg = sum(1.0 / math.log2(rank + 1) for rank in range(1, ideal_count + 1))
            ndcg_values.append(dcg / idcg if idcg else 0.0)

            ap_sum = 0.0
            running_hits = 0
            for rank in relevant_ranks:
                running_hits += 1
                ap_sum += running_hits / rank
            ap_denominator = min(relevant_total, k)
            map_values.append(ap_sum / ap_denominator if ap_denominator else 0.0)

        metrics[f"HitRate@{k}"] = float(np.mean(hit_values))
        metrics[f"Precision@{k}"] = float(np.mean(precision_values))
        metrics[f"Recall@{k}"] = float(np.mean(recall_values))
        metrics[f"MRR@{k}"] = float(np.mean(mrr_values))
        metrics[f"nDCG@{k}"] = float(np.mean(ndcg_values))
        metrics[f"MAP@{k}"] = float(np.mean(map_values))

    rprec_values: list[float] = []
    for ranking, gold in zip(rankings, gold_by_query, strict=True):
        relevant_total = len(gold)
        if not relevant_total:
            rprec_values.append(0.0)
            continue
        top_r = ranking[:relevant_total]
        rprec_values.append(
            sum(item["chunk_id"] in gold for item in top_r) / len(top_r)
            if top_r
            else 0.0
        )
    metrics["R-Precision"] = float(np.mean(rprec_values))

    finite_ranks = [rank for rank in first_ranks if rank is not None]
    metrics["MeanFirstRelRank"] = float(np.mean(finite_ranks)) if finite_ranks else None
    metrics["MedianFirstRelRank"] = float(np.median(finite_ranks)) if finite_ranks else None
    metrics["FirstRelFoundRate"] = (
        len(finite_ranks) / len(first_ranks) if first_ranks else 0.0
    )
    return metrics, first_ranks


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--artifacts-dir",
        type=Path,
        default=PROJECT_ROOT / "data/kaggle_artifacts/virhe4qa_model_sweep",
    )
    parser.add_argument("--collection", default="virhe4qa_297")
    parser.add_argument("--qdrant-url", default="http://localhost:6333")
    parser.add_argument("--mode", choices=("hybrid", "dense", "sparse"), default="hybrid")
    parser.add_argument("--fusion", choices=("rrf", "dbsf"), default="rrf")
    parser.add_argument("--dense-vector-name", default="bge_m3_dense")
    parser.add_argument(
        "--query-dense-file",
        default="bge_m3_query_dense.npy",
        help="Dense query embedding filename relative to --artifacts-dir.",
    )
    parser.add_argument("--ks", default="1,3,5,10,20,50,100")
    parser.add_argument("--prefetch-limit", type=int, default=100)
    parser.add_argument("--output-root", type=Path, default=PROJECT_ROOT / "data/retrieval_runs")
    parser.add_argument("--run-name", default=None)
    parser.add_argument("--error-k", type=int, default=20)
    args = parser.parse_args()

    ks = parse_ks(args.ks)
    if args.prefetch_limit < max(ks):
        parser.error("prefetch-limit must be at least max(ks)")
    if args.error_k < 1:
        parser.error("error-k must be positive")

    artifact_dir = args.artifacts_dir.resolve()
    query_rows = read_rows(artifact_dir / "queries_manifest.csv")
    query_dense = np.load(artifact_dir / args.query_dense_file, mmap_mode="r")
    sparse_by_query = load_sparse_queries(artifact_dir / "bge_m3_query_sparse.jsonl")
    if query_dense.shape[0] != len(query_rows):
        raise ValueError(f"Dense query count {query_dense.shape[0]} != manifest count {len(query_rows)}")
    if set(sparse_by_query) != {row["query_id"] for row in query_rows}:
        raise ValueError("Sparse query IDs do not match queries_manifest.csv")

    run_name = args.run_name or f"bge_m3_{args.mode}_{args.fusion}"
    output_dir = (args.output_root / run_name).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    config = RetrievalConfig(
        collection_name=args.collection,
        search_mode=args.mode,
        fusion=args.fusion,
        enable_query_processing=False,
        enable_reranking=False,
        prefetch_limit=args.prefetch_limit,
        final_limit=max(ks),
        rerank_limit=max(20, max(ks)),
        dense_vector_name=args.dense_vector_name,
    )
    store = QdrantStore.from_url(args.qdrant_url, collection_name=args.collection)
    searcher = HybridSearcher(store, config)
    collection_count = int(store.client.count(args.collection, exact=True).count)
    if collection_count < len(query_rows):
        raise ValueError(
            f"Collection '{args.collection}' has {collection_count} points; "
            f"expected at least {len(query_rows)}"
        )

    rankings: list[list[dict[str, Any]]] = []
    result_rows: list[dict[str, Any]] = []
    started = time.perf_counter()
    for index, row in enumerate(query_rows):
        query_id = row["query_id"]
        representation = QueryRepresentation(
            query_text=row["question"],
            dense=query_dense[index].tolist(),
            sparse=sparse_by_query[query_id],
            dense_vector_name=args.dense_vector_name,
            sparse_vector_name="bge_m3_sparse",
            query_id=query_id,
        )
        points = searcher.search(representation, limit=max(ks))
        ranking: list[dict[str, Any]] = []
        for rank, point in enumerate(points, start=1):
            payload = dict(point.payload or {})
            item = {
                "rank": rank,
                "chunk_id": str(payload.get("chunk_id", point.id)),
                "document_id": str(payload.get("document_id", "")),
                "score": float(point.score),
                "text": str(payload.get("text", "")),
            }
            ranking.append(item)
            result_rows.append({
                "query_id": query_id,
                "question": row["question"],
                "gold_chunk_id": row["gold_chunk_id"],
                "rank": rank,
                "chunk_id": item["chunk_id"],
                "document_id": item["document_id"],
                "score": item["score"],
                "is_gold": item["chunk_id"] == row["gold_chunk_id"],
                "text": item["text"],
            })
        rankings.append(ranking)
        print(f"Retrieved {index + 1}/{len(query_rows)} queries", flush=True)

    elapsed = time.perf_counter() - started
    gold_by_query = [{row["gold_chunk_id"]} for row in query_rows]
    metrics, first_ranks = evaluate_rankings(rankings, gold_by_query, ks)

    config_payload = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "collection": args.collection,
        "qdrant_url": args.qdrant_url,
        "mode": args.mode,
        "fusion": args.fusion,
        "dense_vector_name": args.dense_vector_name,
        "query_dense_file": args.query_dense_file,
        "ks": ks,
        "prefetch_limit": args.prefetch_limit,
        "query_count": len(query_rows),
        "collection_point_count": collection_count,
        "max_retrieved_per_query": max(ks),
        "elapsed_seconds": elapsed,
        "average_query_seconds": elapsed / len(query_rows),
        "query_processor_enabled": False,
        "reranking_enabled": False,
        "artifact_dir": str(artifact_dir),
    }
    (output_dir / "run_config.json").write_text(
        json.dumps(config_payload, ensure_ascii=False, indent=2), encoding="utf-8"
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
                "query_id": row["query_id"],
                "gold_chunk_id": row["gold_chunk_id"],
                "first_gold_rank": rank or "",
            }
            for row, rank in zip(query_rows, first_ranks, strict=True)
        ],
    )
    write_csv(
        output_dir / "retrieved_results.csv",
        [
            "query_id", "question", "gold_chunk_id", "rank", "chunk_id",
            "document_id", "score", "is_gold", "text",
        ],
        result_rows,
    )
    with (output_dir / "retrieved_results.jsonl").open("w", encoding="utf-8") as stream:
        for row, ranking, first_rank in zip(query_rows, rankings, first_ranks, strict=True):
            stream.write(
                json.dumps(
                    {
                        "query_id": row["query_id"],
                        "question": row["question"],
                        "gold_chunk_id": row["gold_chunk_id"],
                        "first_gold_rank": first_rank,
                        "results": ranking,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    error_k = min(args.error_k, max(ks))
    failures = []
    for row, ranking in zip(query_rows, rankings, strict=True):
        top = ranking[:error_k]
        if not any(item["chunk_id"] == row["gold_chunk_id"] for item in top):
            failures.append({
                "query_id": row["query_id"],
                "question": row["question"],
                "gold_chunk_id": row["gold_chunk_id"],
                "retrieved_chunk_ids": json.dumps(
                    [item["chunk_id"] for item in top], ensure_ascii=False
                ),
                "retrieved_scores": json.dumps([item["score"] for item in top]),
            })
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

