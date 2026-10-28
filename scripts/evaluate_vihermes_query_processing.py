"""Compare full-query BGE-M3 retrieval with heuristic query decomposition on ViHERMES."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))

from evaluate_qdrant_retrieval import evaluate_rankings  # noqa: E402


NUMBERED_MARKER = re.compile(r"(?<!\w)\(?\d+\)?[\.:)]")
CLAUSE_BREAK = re.compile(
    r"\s*(?:;|\btrong khi\b|\bbên cạnh\b|\bngoài ra\b|\bđồng thời\b|"
    r"\bmặt khác\b|\bcũng như\b|\bvà\s+)\s*",
    flags=re.IGNORECASE,
)


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    csv.field_size_limit(sys.maxsize)
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = [dict(row) for row in csv.DictReader(stream)]
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def decompose_question(question: str) -> list[str]:
    """Split explicit numbered requests, then obvious discourse-level clauses."""
    matches = list(NUMBERED_MARKER.finditer(question))
    if len(matches) >= 2:
        prefix = question[: matches[0].start()].strip(" \r\n:-")
        parts = []
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(question)
            body = question[match.end() : end].strip(" \r\n:-")
            if body:
                parts.append(f"{prefix} {body}".strip() if prefix else body)
        if len(parts) >= 2:
            return parts

    parts = [part.strip(" \r\n:-") for part in CLAUSE_BREAK.split(question) if part.strip()]
    if len(parts) >= 2 and all(len(part.split()) >= 4 for part in parts):
        return parts
    return [question.strip()]


class OnnxDenseEncoder:
    def __init__(self, model_dir: Path, tokenizer_dir: Path) -> None:
        import onnxruntime as ort  # noqa: PLC0415
        from transformers import AutoTokenizer  # noqa: PLC0415

        started = time.perf_counter()
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_dir, local_files_only=True)
        self.session = ort.InferenceSession(
            str(model_dir / "model.onnx"),
            providers=["CPUExecutionProvider"],
        )
        self.model_load_seconds = time.perf_counter() - started

    def encode(
        self,
        texts: list[str],
        *,
        batch_size: int,
        max_length: int,
        label: str,
    ) -> tuple[np.ndarray, float]:
        started = time.perf_counter()
        batches: list[np.ndarray] = []
        for start in range(0, len(texts), batch_size):
            encoded = self.tokenizer(
                texts[start : start + batch_size],
                truncation=True,
                max_length=max_length,
                padding=True,
                return_tensors="np",
            )
            (_, sentence_embeddings) = self.session.run(
                ["token_embeddings", "sentence_embedding"],
                {
                    "input_ids": encoded["input_ids"].astype(np.int64),
                    "attention_mask": encoded["attention_mask"].astype(np.int64),
                },
            )
            batches.append(np.asarray(sentence_embeddings, dtype=np.float32))
            completed = min(start + batch_size, len(texts))
            if completed == len(texts) or completed % max(batch_size * 25, 100) == 0:
                print(f"Encoded {label}: {completed}/{len(texts)}", flush=True)
        return np.concatenate(batches, axis=0), time.perf_counter() - started


def make_rankings(scores: np.ndarray, chunk_ids: list[str], limit: int) -> list[list[dict[str, Any]]]:
    rankings = []
    for row in scores:
        order = np.argsort(-row, kind="stable")[:limit]
        rankings.append(
            [
                {"rank": rank, "chunk_id": chunk_ids[index], "score": float(row[index])}
                for rank, index in enumerate(order, start=1)
            ]
        )
    return rankings


def evaluate_strategy(
    rankings: list[list[dict[str, Any]]],
    gold_sets: list[set[str]],
    hops: list[str],
    ks: list[int],
) -> dict[str, Any]:
    overall, first_ranks = evaluate_rankings(rankings, gold_sets, ks)
    by_hop: dict[str, Any] = {}
    for hop in sorted(set(hops), key=int):
        indexes = [index for index, value in enumerate(hops) if value == hop]
        hop_metrics, _ = evaluate_rankings(
            [rankings[index] for index in indexes],
            [gold_sets[index] for index in indexes],
            ks,
        )
        by_hop[f"hop_{hop}"] = {"query_count": len(indexes), **hop_metrics}
    return {"overall": overall, "by_hop": by_hop, "first_ranks": first_ranks}


def save_rankings(path: Path, rows: list[dict[str, str]], rankings: list[list[dict[str, Any]]]) -> None:
    with path.open("w", encoding="utf-8") as stream:
        for row, ranking in zip(rows, rankings, strict=True):
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset-dir",
        type=Path,
        default=PROJECT_ROOT / "data/benchmark_datasets/ViHERMES",
    )
    parser.add_argument(
        "--model-dir",
        type=Path,
        required=True,
        help="Local BGE-M3 ONNX directory containing model.onnx and model.onnx_data.",
    )
    parser.add_argument("--tokenizer-dir", type=Path, required=True)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "data/retrieval_runs/query_processing/vihermes_bge_m3",
    )
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--prefetch-limit", type=int, default=100)
    parser.add_argument("--ks", default="1,3,5,10,20,50,100")
    parser.add_argument("--max-queries", type=int, default=None)
    args = parser.parse_args()
    if args.batch_size < 1 or args.max_length < 1 or args.prefetch_limit < 1:
        parser.error("batch-size, max-length and prefetch-limit must be positive")

    ks = sorted({int(value.strip()) for value in args.ks.split(",") if value.strip()})
    if not ks or any(value < 1 for value in ks) or max(ks) > args.prefetch_limit:
        parser.error("ks must contain positive values no greater than prefetch-limit")

    dataset_dir = args.dataset_dir.resolve()
    context_rows = read_csv_rows(dataset_dir / "contexts.csv")
    query_rows = read_csv_rows(dataset_dir / "qa.csv")
    if args.max_queries:
        query_rows = query_rows[: args.max_queries]

    context_ids = [row["context_id"] for row in context_rows]
    context_texts = [f"{row['title']}\n{row['text']}" for row in context_rows]
    questions = [row["question"] for row in query_rows]
    subqueries_by_query = [decompose_question(question) for question in questions]
    subqueries = [subquery for group in subqueries_by_query for subquery in group]
    subquery_counts = [len(group) for group in subqueries_by_query]

    encoder = OnnxDenseEncoder(args.model_dir.resolve(), args.tokenizer_dir.resolve())
    context_dense, context_seconds = encoder.encode(
        context_texts,
        batch_size=args.batch_size,
        max_length=args.max_length,
        label="contexts",
    )
    query_dense, query_seconds = encoder.encode(
        questions,
        batch_size=args.batch_size,
        max_length=args.max_length,
        label="full queries",
    )
    subquery_dense, subquery_seconds = encoder.encode(
        subqueries,
        batch_size=args.batch_size,
        max_length=args.max_length,
        label="subqueries",
    )

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    np.save(output_dir / "context_dense.npy", context_dense)
    np.save(output_dir / "query_dense.npy", query_dense)
    np.save(output_dir / "subquery_dense.npy", subquery_dense)
    with (output_dir / "subqueries.jsonl").open("w", encoding="utf-8") as stream:
        offset = 0
        for row, group in zip(query_rows, subqueries_by_query, strict=True):
            stream.write(
                json.dumps(
                    {"query_id": row["id"], "subqueries": group}, ensure_ascii=False
                )
                + "\n"
            )
            offset += len(group)

    # Full-query dense baseline.
    similarity = query_dense @ context_dense.T
    baseline_rankings = make_rankings(similarity, context_ids, args.prefetch_limit)

    # Decomposition uses RRF over each subquery's independent dense ranking.
    decomposed_rrf_scores: list[np.ndarray] = []
    decomposed_max_scores: list[np.ndarray] = []
    subquery_offset = 0
    rrf_k = 60.0
    for count in subquery_counts:
        query_subs = subquery_dense[subquery_offset : subquery_offset + count]
        subquery_offset += count
        sub_scores = query_subs @ context_dense.T
        rrf = np.zeros(len(context_rows), dtype=np.float32)
        for sub_score in sub_scores:
            order = np.argsort(-sub_score, kind="stable")[: args.prefetch_limit]
            for rank, context_index in enumerate(order, start=1):
                rrf[context_index] += 1.0 / (rrf_k + rank)
        decomposed_rrf_scores.append(rrf)
        decomposed_max_scores.append(np.max(sub_scores, axis=0))
    rrf_rankings = make_rankings(np.vstack(decomposed_rrf_scores), context_ids, args.prefetch_limit)
    max_rankings = make_rankings(np.vstack(decomposed_max_scores), context_ids, args.prefetch_limit)

    gold_sets = [set(json.loads(row["gold_context_ids"])) for row in query_rows]
    hops = [row["hop_level"] for row in query_rows]
    evaluations = {
        "full_query_dense": evaluate_strategy(baseline_rankings, gold_sets, hops, ks),
        "decomposed_rrf": evaluate_strategy(rrf_rankings, gold_sets, hops, ks),
        "decomposed_max": evaluate_strategy(max_rankings, gold_sets, hops, ks),
    }
    for item in evaluations.values():
        item.pop("first_ranks", None)

    save_rankings(output_dir / "full_query_dense_rankings.jsonl", query_rows, baseline_rankings)
    save_rankings(output_dir / "decomposed_rrf_rankings.jsonl", query_rows, rrf_rankings)
    save_rankings(output_dir / "decomposed_max_rankings.jsonl", query_rows, max_rankings)
    with (output_dir / "query_manifest.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=["query_id", "hop_level", "question", "subquery_count"],
        )
        writer.writeheader()
        writer.writerows(
            {
                "query_id": row["id"],
                "hop_level": row["hop_level"],
                "question": row["question"],
                "subquery_count": count,
            }
            for row, count in zip(query_rows, subquery_counts, strict=True)
        )

    config = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "dataset": "ViHERMES",
        "context_count": len(context_rows),
        "query_count": len(query_rows),
        "subquery_count": len(subqueries),
        "subquery_count_distribution": {
            str(count): subquery_counts.count(count) for count in sorted(set(subquery_counts))
        },
        "hop_distribution": {hop: hops.count(hop) for hop in sorted(set(hops), key=int)},
        "model": "BAAI/bge-m3",
        "backend": "onnxruntime",
        "model_dir": str(args.model_dir.resolve()),
        "tokenizer_dir": str(args.tokenizer_dir.resolve()),
        "batch_size": args.batch_size,
        "max_length": args.max_length,
        "prefetch_limit": args.prefetch_limit,
        "rrf_k": rrf_k,
        "timings": {
            "model_load_seconds": encoder.model_load_seconds,
            "context_encode_seconds": context_seconds,
            "full_query_encode_seconds": query_seconds,
            "subquery_encode_seconds": subquery_seconds,
            "total_encode_seconds": context_seconds + query_seconds + subquery_seconds,
        },
        "evaluations": evaluations,
    }
    (output_dir / "run_config.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (output_dir / "metrics.json").write_text(
        json.dumps(evaluations, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"output_dir": str(output_dir), **evaluations}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
