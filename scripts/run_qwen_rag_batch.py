"""Run sequential Qwen retrieval -> governed prompt -> answer requests."""

from __future__ import annotations

import argparse
import csv
import json
import os
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from rag_manything.answer.service import AnswerService  # noqa: E402
from rag_manything.config import Settings  # noqa: E402
from rag_manything.models import RetrievedChunk  # noqa: E402

DEFAULT_QUERIES = (
    PROJECT_ROOT
    / "data"
    / "virhe4qa_subset"
    / "ViRHE4QA_v2_all_contexts_297"
    / "queries_100.csv"
)


def post_json(
    url: str,
    payload: dict[str, Any],
    *,
    headers: dict[str, str] | None = None,
    timeout: float,
) -> dict[str, Any]:
    request_headers = {"Content-Type": "application/json"}
    if headers:
        request_headers.update(headers)
    request = Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=request_headers,
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail[:500]}") from exc
    except URLError as exc:
        raise RuntimeError(f"Connection failed: {exc.reason}") from exc


def load_queries(path: Path, limit: int) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = [dict(row) for row in csv.DictReader(stream)]
    rows = [row for row in rows if str(row.get("question", "")).strip()]
    if not rows:
        raise ValueError(f"No non-empty questions found in {path}")
    return rows[:limit]


def source_from_payload(payload: dict[str, Any]) -> str | None:
    for key in ("source_url", "source", "title", "document_id"):
        value = payload.get(key)
        if value is not None and str(value).strip():
            return str(value)
    return None


def percentile(values: list[float], fraction: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = min(round((len(ordered) - 1) * fraction), len(ordered) - 1)
    return round(ordered[index], 4)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    load_dotenv(PROJECT_ROOT / ".env")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--collection", default=os.getenv(
        "QWEN_QDRANT_COLLECTION", "virhe4qa_qwen_api_30_fdd19f"
    ))
    parser.add_argument("--qdrant-url", default=os.getenv("QDRANT_URL", "http://localhost:6333"))
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=600)
    parser.add_argument("--run-name")
    args = parser.parse_args()
    if args.limit < 1 or args.top_k < 1 or args.timeout <= 0:
        parser.error("limit, top-k, and timeout must be positive")

    rag_api_url = os.getenv("RAG_API_URL", "").rstrip("/")
    rag_api_key = os.getenv("RAG_API_KEY", "")
    if not rag_api_url or not rag_api_key:
        parser.error("Set RAG_API_URL and RAG_API_KEY in .env")
    if not os.getenv("QWEN_API_URL", "").strip():
        os.environ["QWEN_API_URL"] = f"{rag_api_url}/v1/generate"
    if not os.getenv("QWEN_API_TOKEN", "").strip():
        os.environ["QWEN_API_TOKEN"] = rag_api_key

    settings = Settings()
    if settings.input_guardrail_enabled or settings.output_guardrail_enabled:
        parser.error("Set INPUT_GUARDRAIL_ENABLED=false and OUTPUT_GUARDRAIL_ENABLED=false")

    query_rows = load_queries(args.queries.resolve(), args.limit)
    run_name = args.run_name or f"qwen_prompt_answer_{len(query_rows)}_{datetime.now():%Y%m%d_%H%M%S}"
    output_dir = PROJECT_ROOT / "data" / "retrieval_runs" / run_name
    if output_dir.exists() and any(output_dir.iterdir()):
        parser.error(f"Output directory is not empty: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = output_dir / "per_query_checkpoint.jsonl"

    auth_headers = {"Authorization": f"Bearer {rag_api_key}"}
    qdrant_headers: dict[str, str] = {}
    qdrant_key = os.getenv("QDRANT_API_KEY", "")
    if qdrant_key:
        qdrant_headers["api-key"] = qdrant_key

    records: list[dict[str, Any]] = []
    run_started = time.perf_counter()
    with AnswerService(settings) as answer_service:
        for position, row in enumerate(query_rows, start=1):
            question = str(row["question"]).strip()
            query_started = time.perf_counter()
            record: dict[str, Any] = {
                "query_number": position,
                "source_index": row.get("index"),
                "split": row.get("split"),
                "question": question,
                "reference_extractive_answer": row.get("extractive answer"),
                "reference_abstractive_answer": row.get("abstractive answer"),
            }
            try:
                started = time.perf_counter()
                embedding_response = post_json(
                    f"{rag_api_url}/v1/embeddings",
                    {"texts": [question], "is_query": True},
                    headers=auth_headers,
                    timeout=args.timeout,
                )
                embedding_s = time.perf_counter() - started
                vectors = embedding_response.get("embeddings", [])
                if len(vectors) != 1:
                    raise RuntimeError("Embedding API did not return exactly one vector")

                collection_url = (
                    f"{args.qdrant_url.rstrip('/')}/collections/"
                    f"{quote(args.collection, safe='')}/points/query"
                )
                started = time.perf_counter()
                search_response = post_json(
                    collection_url,
                    {"query": vectors[0], "limit": args.top_k, "with_payload": True},
                    headers=qdrant_headers,
                    timeout=args.timeout,
                )
                search_s = time.perf_counter() - started
                points = search_response.get("result", {}).get("points", [])
                if not points:
                    raise RuntimeError("Qdrant returned no retrieval hits")

                chunks: list[RetrievedChunk] = []
                hits: list[dict[str, Any]] = []
                for rank, point in enumerate(points, start=1):
                    payload = dict(point.get("payload", {}) or {})
                    chunk_id = str(payload.get("chunk_id", point.get("id")))
                    text = str(payload.get("text", "")).strip()
                    if not text:
                        raise RuntimeError(f"Retrieved hit {rank} has no payload.text")
                    chunks.append(RetrievedChunk(
                        chunk_id=chunk_id,
                        content=text,
                        source=source_from_payload(payload),
                    ))
                    hits.append({
                        "rank": rank,
                        "point_id": point.get("id"),
                        "chunk_id": chunk_id,
                        "score": point.get("score"),
                        "payload": payload,
                    })

                started = time.perf_counter()
                answer = answer_service.answer(question, chunks)
                answer_s = time.perf_counter() - started
                record.update({
                    "status": "ok",
                    "hits": hits,
                    "answer_result": answer.model_dump(mode="json"),
                    "timings_s": {
                        "query_embedding_api": round(embedding_s, 4),
                        "qdrant_search": round(search_s, 4),
                        "prompt_and_answer": round(answer_s, 4),
                        "end_to_end": round(time.perf_counter() - query_started, 4),
                    },
                })
            except Exception as exc:
                record.update({
                    "status": "error",
                    "error_type": type(exc).__name__,
                    "error": str(exc)[:500],
                    "timings_s": {
                        "end_to_end": round(time.perf_counter() - query_started, 4),
                    },
                })

            records.append(record)
            with checkpoint_path.open("a", encoding="utf-8") as stream:
                stream.write(json.dumps(record, ensure_ascii=False) + "\n")
            print(
                f"[{position}/{len(query_rows)}] {record['status']} | "
                f"{record['timings_s']['end_to_end']:.2f}s"
            )

    completed = [record for record in records if record["status"] == "ok"]
    durations = [record["timings_s"]["end_to_end"] for record in completed]
    summary = {
        "run_name": run_name,
        "output_dir": str(output_dir),
        "queries_file": str(args.queries.resolve()),
        "collection": args.collection,
        "requested_queries": len(query_rows),
        "completed_queries": len(completed),
        "error_queries": len(records) - len(completed),
        "top_k": args.top_k,
        "guardrails_enabled": False,
        "pipeline": "Qwen embedding -> Qdrant dense -> PromptBuilder -> Qwen generate",
        "timing_s": {
            "total": round(time.perf_counter() - run_started, 4),
            "mean_per_completed_query": round(statistics.mean(durations), 4) if durations else None,
            "p50": percentile(durations, 0.50),
            "p95": percentile(durations, 0.95),
        },
    }
    with (output_dir / "per_query.jsonl").open("w", encoding="utf-8") as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
    (output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if len(completed) == len(records) else 2


if __name__ == "__main__":
    raise SystemExit(main())
