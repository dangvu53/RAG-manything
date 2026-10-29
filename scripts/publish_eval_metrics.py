"""Publish saved retrieval and RAGAS reports to a local Prometheus Pushgateway."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway


def read_json(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--retrieval-report", type=Path)
    parser.add_argument("--retrieval-config", type=Path)
    parser.add_argument("--answer-report", type=Path)
    parser.add_argument("--dataset", default="virhe4qa")
    parser.add_argument("--retrieval", default="bm25")
    parser.add_argument("--pushgateway", default="http://localhost:9091")
    parser.add_argument("--job", default="rag_evaluation")
    args = parser.parse_args()
    if not args.retrieval_report and not args.answer_report:
        parser.error("Provide --retrieval-report, --answer-report, or both")

    registry = CollectorRegistry()
    score = Gauge(
        "rag_evaluation_score",
        "Latest offline retrieval or answer quality score",
        ["dataset", "retrieval", "suite", "metric", "cutoff"],
        registry=registry,
    )
    query_count = Gauge(
        "rag_evaluation_queries",
        "Number of queries in the latest offline evaluation",
        ["dataset", "retrieval", "suite"],
        registry=registry,
    )
    latency = Gauge(
        "rag_evaluation_latency_seconds",
        "Latency statistics from the latest saved answer evaluation",
        ["dataset", "retrieval", "statistic"],
        registry=registry,
    )
    timestamp = Gauge(
        "rag_evaluation_timestamp_seconds",
        "Unix timestamp when the offline evaluation was published",
        ["dataset", "retrieval"],
        registry=registry,
    )

    if args.retrieval_report:
        report = read_json(args.retrieval_report)
        for name, value in report.items():
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                continue
            match = re.fullmatch(r"(.+?)(?:@(\d+))?", name)
            if match:
                metric, cutoff = match.group(1), match.group(2) or ""
                score.labels(args.dataset, args.retrieval, "retrieval", metric, cutoff).set(value)
        count = report.get("query_count")
        if isinstance(count, (int, float)):
            query_count.labels(args.dataset, args.retrieval, "retrieval").set(count)

    if args.retrieval_config:
        config = read_json(args.retrieval_config)
        count = config.get("query_count")
        if isinstance(count, (int, float)):
            query_count.labels(args.dataset, args.retrieval, "retrieval").set(count)
        for statistic, key in (
            ("index_build", "index_build_seconds"),
            ("search_total", "search_elapsed_seconds"),
            ("mean_query", "average_query_seconds"),
        ):
            value = config.get(key)
            if isinstance(value, (int, float)):
                latency.labels(args.dataset, args.retrieval, statistic).set(value)

    if args.answer_report:
        report = read_json(args.answer_report)
        averages = report.get("averages", {})
        if isinstance(averages, dict):
            for metric, value in averages.items():
                if isinstance(value, (int, float)) and not isinstance(value, bool):
                    score.labels(args.dataset, args.retrieval, "answer", metric, "").set(value)
        count = report.get("row_count")
        if isinstance(count, (int, float)):
            query_count.labels(args.dataset, args.retrieval, "answer").set(count)
        latency_summary = report.get("latency_ms", {})
        if isinstance(latency_summary, dict):
            for statistic in ("mean", "p50", "p95", "min", "max"):
                value = latency_summary.get(statistic)
                if isinstance(value, (int, float)):
                    latency.labels(args.dataset, args.retrieval, statistic).set(value / 1000)

    timestamp.labels(args.dataset, args.retrieval).set(
        datetime.now(timezone.utc).timestamp()
    )
    push_to_gateway(
        args.pushgateway,
        job=args.job,
        grouping_key={"evaluation_id": f"{args.dataset}__{args.retrieval}"},
        registry=registry,
    )
    print(
        f"Published evaluation metrics for dataset={args.dataset}, "
        f"retrieval={args.retrieval} to {args.pushgateway}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
