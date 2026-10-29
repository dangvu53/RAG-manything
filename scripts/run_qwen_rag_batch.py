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
SCRIPTS_ROOT = PROJECT_ROOT / "scripts"
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))

from evaluate_bm25_retrieval import BM25Index  # noqa: E402
from rag_manything.answer.guardrails import INVALID_QUESTION_MESSAGE, OpenAIGuardrail  # noqa: E402
from rag_manything.answer.service import AnswerService  # noqa: E402
from rag_manything.config import Settings  # noqa: E402
from rag_manything.models import AnswerResult, RetrievedChunk  # noqa: E402

DEFAULT_QUERIES = (
    PROJECT_ROOT
    / "data"
    / "virhe4qa_subset"
    / "ViRHE4QA_v2_all_contexts_297"
    / "queries_100.csv"
)
DEFAULT_BM25_CORPUS = (
    PROJECT_ROOT / "data" / "kaggle_artifacts" / "virhe4qa_model_sweep" / "chunks_manifest.csv"
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


def load_queries(
    path: Path,
    limit: int,
    query_index: str | None = None,
) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = [dict(row) for row in csv.DictReader(stream)]
    rows = [row for row in rows if str(row.get("question", "")).strip()]
    if query_index is not None:
        rows = [row for row in rows if str(row.get("index", "")).strip() == query_index]
    if not rows:
        if query_index is not None:
            raise ValueError(f"No question with index {query_index} found in {path}")
        raise ValueError(f"No non-empty questions found in {path}")
    return rows[:limit]


def load_bm25_corpus(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = [dict(row) for row in csv.DictReader(stream)]
    required = {"chunk_id", "document_id", "text"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError(f"BM25 corpus must contain {sorted(required)}: {path}")
    return rows


def fuse_rankings(
    dense_points: list[dict[str, Any]],
    bm25_rows: list[dict[str, Any]],
    *,
    rrf_k: float,
    limit: int,
) -> list[dict[str, Any]]:
    candidates: dict[str, dict[str, Any]] = {}
    for dense_rank, point in enumerate(dense_points, start=1):
        payload = dict(point.get("payload", {}) or {})
        chunk_id = str(payload.get("chunk_id", point.get("id")))
        candidates[chunk_id] = {
            "point_id": point.get("id"),
            "chunk_id": chunk_id,
            "payload": payload,
            "dense_rank": dense_rank,
            "dense_score": point.get("score"),
            "bm25_rank": None,
            "bm25_score": None,
            "rrf_score": 1.0 / (rrf_k + dense_rank - 1),
        }
    for bm25_rank, row in enumerate(bm25_rows, start=1):
        chunk_id = str(row["chunk_id"])
        payload = {
            "chunk_id": chunk_id,
            "document_id": row["document_id"],
            "text": row["text"],
        }
        candidate = candidates.setdefault(
            chunk_id,
            {
                "point_id": None,
                "chunk_id": chunk_id,
                "payload": payload,
                "dense_rank": None,
                "dense_score": None,
                "bm25_rank": None,
                "bm25_score": None,
                "rrf_score": 0.0,
            },
        )
        candidate["bm25_rank"] = bm25_rank
        candidate["bm25_score"] = row["score"]
        candidate["rrf_score"] += 1.0 / (rrf_k + bm25_rank - 1)
    ranking = sorted(
        candidates.values(),
        key=lambda item: (-item["rrf_score"], item["chunk_id"]),
    )[:limit]
    for rank, item in enumerate(ranking, start=1):
        item["rank"] = rank
    return ranking


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


def persist_record(
    records: list[dict[str, Any]],
    record: dict[str, Any],
    checkpoint_path: Path,
    position: int,
    total: int,
) -> None:
    records.append(record)
    checkpoint_path.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"[{position}/{total}] {record['status']} | "
        f"{record['timings_s']['end_to_end']:.2f}s"
    )
    if record["status"] in {"ok", "blocked"}:
        print("Answer:")
        print(record["answer_result"].get("answer", ""))


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    load_dotenv(PROJECT_ROOT / ".env")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--limit", type=int, default=30)
    query_source = parser.add_mutually_exclusive_group()
    query_source.add_argument(
        "--query-index",
        help="Run only the row whose source index matches this value",
    )
    query_source.add_argument(
        "--question",
        help="Run one free-form question instead of a benchmark row",
    )
    parser.add_argument("--collection", default=os.getenv(
        "QWEN_QDRANT_COLLECTION", "virhe4qa_qwen_api_30_fdd19f"
    ))
    parser.add_argument("--qdrant-url", default=os.getenv("QDRANT_URL", "http://localhost:6333"))
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--dense-candidates", type=int, default=100)
    parser.add_argument("--bm25-candidates", type=int, default=100)
    parser.add_argument("--bm25-corpus", type=Path, default=DEFAULT_BM25_CORPUS)
    parser.add_argument("--bm25-k1", type=float, default=1.5)
    parser.add_argument("--bm25-b", type=float, default=0.75)
    parser.add_argument("--rrf-k", type=float, default=2.0)
    parser.add_argument("--timeout", type=float, default=600)
    parser.add_argument("--run-name")
    parser.add_argument(
        "--enable-input-guardrail",
        action="store_true",
        help="Enable the OpenAI input safety check and query rewrite for this run",
    )
    parser.add_argument(
        "--enable-output-guardrail",
        action="store_true",
        help="Enable the OpenAI output safety and grounding check for this run",
    )
    args = parser.parse_args()
    if (
        args.limit < 1
        or args.top_k < 1
        or args.dense_candidates < args.top_k
        or args.bm25_candidates < args.top_k
        or args.rrf_k <= 0
        or args.timeout <= 0
    ):
        parser.error("limits, candidate counts, rrf-k, and timeout must be valid positive values")

    rag_api_url = os.getenv("RAG_API_URL", "").rstrip("/")
    rag_api_key = os.getenv("RAG_API_KEY", "")
    if not rag_api_url or not rag_api_key:
        parser.error("Set RAG_API_URL and RAG_API_KEY in .env")
    # This runner uses the embedding and generation routes from the same
    # combined Kaggle API, so stale QWEN_* values must not redirect generation.
    os.environ["QWEN_API_URL"] = f"{rag_api_url}/v1/generate"
    os.environ["QWEN_API_TOKEN"] = rag_api_key

    settings = Settings()
    # Keep .env untouched: explicit CLI flags opt the benchmark into guardrails.
    settings = settings.model_copy(update={
        "input_guardrail_enabled": (
            settings.input_guardrail_enabled or args.enable_input_guardrail
        ),
        "output_guardrail_enabled": (
            settings.output_guardrail_enabled or args.enable_output_guardrail
        ),
    })

    if args.question is not None:
        question = args.question.strip()
        if not question:
            parser.error("--question must not be empty")
        query_rows = [{"question": question}]
    else:
        query_rows = load_queries(
            args.queries.resolve(),
            args.limit,
            query_index=args.query_index,
        )
    bm25_corpus = load_bm25_corpus(args.bm25_corpus.resolve())
    bm25_index_started = time.perf_counter()
    bm25_index = BM25Index(
        [row["text"] for row in bm25_corpus],
        k1=args.bm25_k1,
        b=args.bm25_b,
    )
    bm25_index_s = time.perf_counter() - bm25_index_started
    run_name = args.run_name or (
        f"qwen_bm25_rrf_prompt_answer_{len(query_rows)}_{datetime.now():%Y%m%d_%H%M%S}"
    )
    output_dir = PROJECT_ROOT / "data" / "retrieval_runs" / run_name
    if output_dir.exists() and any(output_dir.iterdir()):
        parser.error(f"Output directory is not empty: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = output_dir / "checkpoint.json"

    auth_headers = {"Authorization": f"Bearer {rag_api_key}"}
    qdrant_headers: dict[str, str] = {}
    qdrant_key = os.getenv("QDRANT_API_KEY", "")
    if qdrant_key:
        qdrant_headers["api-key"] = qdrant_key

    records: list[dict[str, Any]] = []
    run_started = time.perf_counter()
    input_guardrail = (
        OpenAIGuardrail(settings) if settings.input_guardrail_enabled else None
    )
    # This runner does retrieval itself, so the input guardrail must run before
    # embedding/search. Disable the service's input check to avoid calling it twice.
    answer_settings = settings.model_copy(update={"input_guardrail_enabled": False})
    with AnswerService(answer_settings) as answer_service:
        for position, row in enumerate(query_rows, start=1):
            question = str(row["question"]).strip()
            query_started = time.perf_counter()
            input_guardrail_s = 0.0
            record: dict[str, Any] = {
                "query_number": position,
                "source_index": row.get("index"),
                "split": row.get("split"),
                "question": question,
                "gold_context": row.get("context"),
                "gold_answer": (
                    row.get("abstractive answer") or row.get("extractive answer")
                ),
                "reference_extractive_answer": row.get("extractive answer"),
                "reference_abstractive_answer": row.get("abstractive answer"),
            }
            try:
                retrieval_query = question
                if not question or len(question) > settings.max_question_chars:
                    blocked = AnswerResult(
                        answer=INVALID_QUESTION_MESSAGE,
                        status="blocked",
                        reason="invalid_question",
                        model=settings.qwen_model,
                    )
                    record.update({
                        "status": "blocked",
                        "retrieval_query": None,
                        "answer_result": blocked.model_dump(mode="json"),
                        "timings_s": {
                            "input_guardrail": 0.0,
                            "end_to_end": round(time.perf_counter() - query_started, 4),
                        },
                    })
                    persist_record(records, record, checkpoint_path, position, len(query_rows))
                    continue

                if input_guardrail is not None:
                    started = time.perf_counter()
                    decision = input_guardrail.check_input(question)
                    input_guardrail_s = time.perf_counter() - started
                    if not decision.allowed:
                        blocked = AnswerResult(
                            answer=INVALID_QUESTION_MESSAGE,
                            status="blocked",
                            reason=decision.reason,
                            model=settings.qwen_model,
                        )
                        record.update({
                            "status": "blocked",
                            "retrieval_query": None,
                            "answer_result": blocked.model_dump(mode="json"),
                            "timings_s": {
                                "input_guardrail": round(input_guardrail_s, 4),
                                "end_to_end": round(time.perf_counter() - query_started, 4),
                            },
                        })
                        persist_record(records, record, checkpoint_path, position, len(query_rows))
                        continue
                    retrieval_query = decision.rewritten_question or question

                started = time.perf_counter()
                embedding_response = post_json(
                    f"{rag_api_url}/v1/embeddings",
                    {"texts": [retrieval_query], "is_query": True},
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
                    {
                        "query": vectors[0],
                        "limit": args.dense_candidates,
                        "with_payload": True,
                    },
                    headers=qdrant_headers,
                    timeout=args.timeout,
                )
                search_s = time.perf_counter() - started
                points = search_response.get("result", {}).get("points", [])
                if not points:
                    raise RuntimeError("Qdrant returned no retrieval hits")

                started = time.perf_counter()
                bm25_scores = bm25_index.scores(retrieval_query)
                bm25_order = sorted(
                    range(len(bm25_corpus)),
                    key=lambda index: (-bm25_scores[index], bm25_corpus[index]["chunk_id"]),
                )[: args.bm25_candidates]
                bm25_hits = [
                    {**bm25_corpus[index], "score": float(bm25_scores[index])}
                    for index in bm25_order
                ]
                bm25_s = time.perf_counter() - started

                started = time.perf_counter()
                hits = fuse_rankings(
                    points,
                    bm25_hits,
                    rrf_k=args.rrf_k,
                    limit=args.top_k,
                )
                fusion_s = time.perf_counter() - started

                chunks: list[RetrievedChunk] = []
                for hit in hits:
                    payload = hit["payload"]
                    chunk_id = hit["chunk_id"]
                    text = str(payload.get("text", "")).strip()
                    if not text:
                        raise RuntimeError(f"Retrieved hit {hit['rank']} has no payload.text")
                    chunks.append(RetrievedChunk(
                        chunk_id=chunk_id,
                        content=text,
                        source=source_from_payload(payload),
                    ))

                started = time.perf_counter()
                answer = answer_service.answer(retrieval_query, chunks)
                answer_s = time.perf_counter() - started
                record.update({
                    "status": "blocked" if answer.status == "blocked" else "ok",
                    "retrieval_query": retrieval_query,
                    "hits": hits,
                    "answer_result": answer.model_dump(mode="json"),
                    "timings_s": {
                        "input_guardrail": round(input_guardrail_s, 4),
                        "query_embedding_api": round(embedding_s, 4),
                        "qdrant_dense_search": round(search_s, 4),
                        "bm25_search": round(bm25_s, 4),
                        "rrf_fusion": round(fusion_s, 4),
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
                        "input_guardrail": round(input_guardrail_s, 4),
                        "end_to_end": round(time.perf_counter() - query_started, 4),
                    },
                })

            persist_record(records, record, checkpoint_path, position, len(query_rows))

    if input_guardrail is not None:
        input_guardrail.close()

    completed = [record for record in records if record["status"] != "error"]
    answered = [record for record in records if record["status"] == "ok"]
    blocked = [record for record in records if record["status"] == "blocked"]
    durations = [record["timings_s"]["end_to_end"] for record in completed]
    pipeline_stages = []
    if settings.input_guardrail_enabled:
        pipeline_stages.append("Input guardrail/query rewrite")
    pipeline_stages.extend([
        "Qwen dense + local BM25 -> RRF",
        "PromptBuilder -> Qwen generate",
    ])
    if settings.output_guardrail_enabled:
        pipeline_stages.append("Output guardrail")
    summary = {
        "run_name": run_name,
        "output_dir": str(output_dir),
        "queries_file": str(args.queries.resolve()),
        "collection": args.collection,
        "requested_queries": len(query_rows),
        "completed_queries": len(completed),
        "answered_queries": len(answered),
        "blocked_queries": len(blocked),
        "error_queries": len(records) - len(completed),
        "top_k": args.top_k,
        "dense_candidates": args.dense_candidates,
        "bm25_candidates": args.bm25_candidates,
        "bm25": {
            "corpus": str(args.bm25_corpus.resolve()),
            "document_count": len(bm25_corpus),
            "k1": args.bm25_k1,
            "b": args.bm25_b,
            "index_build_seconds": round(bm25_index_s, 4),
        },
        "fusion": {"method": "rrf", "k": args.rrf_k, "weights": [1.0, 1.0]},
        "guardrails_enabled": (
            settings.input_guardrail_enabled or settings.output_guardrail_enabled
        ),
        "input_guardrail_enabled": settings.input_guardrail_enabled,
        "output_guardrail_enabled": settings.output_guardrail_enabled,
        "pipeline": " -> ".join(pipeline_stages),
        "timing_s": {
            "total": round(time.perf_counter() - run_started, 4),
            "mean_per_completed_query": round(statistics.mean(durations), 4) if durations else None,
            "p50": percentile(durations, 0.50),
            "p95": percentile(durations, 0.95),
        },
    }
    (output_dir / "per_query.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if len(completed) == len(records) else 2


if __name__ == "__main__":
    raise SystemExit(main())
