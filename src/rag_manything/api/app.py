"""FastAPI service for BM25 retrieval and answer generation."""

from __future__ import annotations

import csv
import os
from contextlib import asynccontextmanager
from pathlib import Path
from time import perf_counter
from typing import Literal

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from prometheus_client import make_asgi_app

from rag_manything.answer.service import AnswerService
from rag_manything.config import Settings
from rag_manything.monitoring.metrics import (
    ANSWER_RESULTS,
    EMPTY_RETRIEVALS,
    HTTP_DURATION,
    HTTP_REQUESTS,
    RETRIEVED_CHUNKS,
)
from rag_manything.monitoring.observability import MetricsObservability
from rag_manything.observability import Observability
from rag_manything.search.bm25 import BM25Index, BM25Retriever


DEFAULT_CORPUS = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "kaggle_artifacts"
    / "virhe4qa_model_sweep"
    / "chunks_manifest.csv"
)


class AnswerAPIRequest(BaseModel):
    question: str = Field(min_length=1, max_length=4000)
    top_k: int = Field(default=3, ge=1, le=20)


class AnswerAPIResponse(BaseModel):
    answer: str
    status: Literal["answered", "blocked", "insufficient_context"]
    reason: str | None = None
    citations: list[dict[str, str | None]]
    model: str
    retrieval: Literal["bm25"] = "bm25"
    latency_ms: float | None = None


class InstrumentedBM25Retriever(BM25Retriever):
    def retrieve(self, query: str, *, limit: int | None = None):
        hits = super().retrieve(query, limit=limit)
        RETRIEVED_CHUNKS.observe(len(hits))
        if not hits:
            EMPTY_RETRIEVALS.inc()
        return hits


def load_corpus(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = [dict(row) for row in csv.DictReader(stream)]
    required = {"chunk_id", "document_id", "text"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError(f"BM25 corpus must contain {sorted(required)}: {path}")
    return rows


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    corpus_path = Path(os.getenv("BM25_CORPUS_PATH", str(DEFAULT_CORPUS))).expanduser()
    if not corpus_path.is_file():
        raise RuntimeError(f"BM25 corpus file does not exist: {corpus_path}")
    rows = load_corpus(corpus_path)
    index = BM25Index.from_rows(
        rows,
        k1=float(os.getenv("BM25_K1", "1.5")),
        b=float(os.getenv("BM25_B", "0.75")),
    )
    app.state.retriever = InstrumentedBM25Retriever(index)
    app.state.corpus_size = len(rows)
    metrics_observability = MetricsObservability(Observability(settings))
    app.state.metrics_observability = metrics_observability
    app.state.answer_service = AnswerService(settings, observability=metrics_observability)
    try:
        yield
    finally:
        app.state.answer_service.close()
        metrics_observability.close()


app = FastAPI(title="RAG-manything BM25 baseline", version="0.1.0", lifespan=lifespan)


@app.middleware("http")
async def collect_http_metrics(request: Request, call_next):
    started = perf_counter()
    endpoint = request.url.path
    if endpoint not in {"/health", "/ready", "/v1/answer", "/metrics"}:
        endpoint = "unmatched"
    status = "error"
    try:
        response = await call_next(request)
        status = "success" if response.status_code < 400 else "error"
        return response
    finally:
        if not endpoint.startswith("/metrics"):
            HTTP_REQUESTS.labels(endpoint=endpoint, status=status).inc()
            HTTP_DURATION.labels(endpoint=endpoint).observe(perf_counter() - started)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready(request: Request):
    if not hasattr(request.app.state, "answer_service"):
        raise HTTPException(status_code=503, detail="RAG service is not ready")
    return {
        "status": "ready",
        "retrieval": "bm25",
        "corpus_chunks": request.app.state.corpus_size,
    }


@app.post("/v1/answer", response_model=AnswerAPIResponse)
def answer(body: AnswerAPIRequest, request: Request):
    retriever: BM25Retriever = request.app.state.retriever
    service: AnswerService = request.app.state.answer_service
    try:
        result = service.answer_with_retrieval(
            body.question,
            retriever,
            retrieval_limit=body.top_k,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail="Answer generation failed") from exc

    ANSWER_RESULTS.labels(status=result.status).inc()
    return AnswerAPIResponse(
        answer=result.answer,
        status=result.status,
        reason=result.reason,
        citations=[citation.model_dump() for citation in result.citations],
        model=result.model,
        latency_ms=result.latency_ms,
    )


app.mount("/metrics", make_asgi_app())
