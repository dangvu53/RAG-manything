"""Collect responses and latency, then evaluate four answer-only metrics offline."""

import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter

from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

from rag_manything.answer.service import AnswerService
from rag_manything.config import Settings
from rag_manything.models import RetrievedChunk


class EvaluationRow(BaseModel):
    user_input: str = Field(min_length=1)
    retrieved_contexts: list[str] = Field(min_length=1)
    response: str = ""
    reference: str = Field(min_length=1)
    latency_ms: float | None = Field(default=None, ge=0)


class EvaluationSettings(BaseSettings):
    # Evaluating saved answers needs no Qwen or guardrail credentials.
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", hide_input_in_errors=True)
    openai_api_key: str = Field(min_length=1, repr=False)
    openai_eval_model: str = Field(min_length=1)
    openai_embedding_model: str = "text-embedding-3-small"
    openai_timeout_seconds: float = Field(default=30, gt=0)


def load_rows(path: Path, require_response: bool = True) -> list[EvaluationRow]:
    rows = [
        EvaluationRow.model_validate_json(line)
        for line in path.read_text(encoding="utf-8").splitlines() if line.strip()
    ]
    if not rows:
        raise ValueError("Dataset must contain at least one row")
    if require_response and any(not row.response.strip() for row in rows):
        raise ValueError("Missing responses: run --generate first")
    return rows


def collect_responses(rows: list[EvaluationRow], service: AnswerService) -> list[EvaluationRow]:
    completed = []
    for row in rows:
        chunks = [
            RetrievedChunk(chunk_id=f"doc-{i:02d}", content=context)
            for i, context in enumerate(row.retrieved_contexts, 1)
        ]
        # Preserve exactly the context visible to the generator after truncation.
        prompt = service.builder.build(row.user_input, chunks)
        started = perf_counter()
        result = service.answer(row.user_input, chunks)
        measured_latency = round((perf_counter() - started) * 1000, 2)
        completed.append(row.model_copy(update={
            "response": result.answer,
            "retrieved_contexts": [c.content for c in prompt.chunks],
            "latency_ms": getattr(result, "latency_ms", None) or measured_latency,
        }))
    return completed


def latency_summary(rows: list[EvaluationRow]) -> dict:
    values = sorted(row.latency_ms for row in rows if row.latency_ms is not None)
    if not values:
        return {"count": 0, "mean": None, "p50": None, "p95": None, "min": None, "max": None}

    def percentile(fraction: float) -> float:
        position = (len(values) - 1) * fraction
        lower = math.floor(position)
        upper = math.ceil(position)
        if lower == upper:
            return values[lower]
        weight = position - lower
        return values[lower] * (1 - weight) + values[upper] * weight

    return {
        "count": len(values),
        "mean": round(sum(values) / len(values), 2),
        "p50": percentile(0.5),
        "p95": percentile(0.95),
        "min": values[0],
        "max": values[-1],
    }


def run_evaluation(rows: list[EvaluationRow], settings: EvaluationSettings) -> dict:
    # Optional heavy dependencies must never be imported by the answer pipeline.
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from langsmith import tracing_context
    from ragas import EvaluationDataset, evaluate
    from ragas.embeddings import LangchainEmbeddingsWrapper
    from ragas.llms import LangchainLLMWrapper
    from ragas.metrics import (
        FactualCorrectness,
        Faithfulness,
        ResponseRelevancy,
        SemanticSimilarity,
    )
    from ragas.run_config import RunConfig

    llm = LangchainLLMWrapper(ChatOpenAI(
        model=settings.openai_eval_model, api_key=settings.openai_api_key,
        timeout=settings.openai_timeout_seconds, max_retries=1,
    ))
    embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings(
        model=settings.openai_embedding_model, api_key=settings.openai_api_key,
        request_timeout=settings.openai_timeout_seconds, max_retries=1,
    ))
    # Offline evaluation content goes to OpenAI, but is not copied into LangSmith traces.
    with tracing_context(enabled=False):
        result = evaluate(
            dataset=EvaluationDataset.from_list([row.model_dump() for row in rows]),
            metrics=[
                Faithfulness(),
                ResponseRelevancy(),
                FactualCorrectness(),
                SemanticSimilarity(),
            ],
            llm=llm, embeddings=embeddings,
            run_config=RunConfig(timeout=settings.openai_timeout_seconds, max_retries=1),
            raise_exceptions=True,
        )
    scores = result.scores
    names = list(scores[0])
    per_row = [
        {name: float(score[name]) if math.isfinite(float(score[name])) else None for name in names}
        for score in scores
    ]
    averages = {}
    for name in names:
        values = [score[name] for score in per_row if score[name] is not None]
        averages[name] = sum(values) / len(values) if values else None
    return {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "evaluator_model": settings.openai_eval_model,
        "embedding_model": settings.openai_embedding_model,
        "row_count": len(rows),
        "averages": averages,
        "latency_ms": latency_summary(rows),
        "scores": per_row,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect answers or run offline RAGAS evaluation")
    parser.add_argument("dataset", type=Path, help="UTF-8 JSONL")
    parser.add_argument("--generate", action="store_true", help="Generate answers; skip scoring")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.dataset.resolve() == args.output.resolve():
            raise ValueError("Output must differ from input")
        rows = load_rows(args.dataset, require_response=not args.generate)
        if args.generate:
            with AnswerService(Settings()) as service:
                completed = collect_responses(rows, service)
            content = "\n".join(row.model_dump_json() for row in completed) + "\n"
        else:
            report = run_evaluation(rows, EvaluationSettings())
            content = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
        print(f"Saved {args.output}")
        return 0
    except ValidationError:
        print("Invalid dataset or missing evaluation/service configuration.", file=sys.stderr)
    except Exception:
        # Third-party API exceptions may include submitted content or credentials.
        print("Evaluation failed. Check dataset, API configuration and installed extras.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
