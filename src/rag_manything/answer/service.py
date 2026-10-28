from time import perf_counter
from typing import Any, Mapping, Protocol

from rag_manything.answer.client import QwenClient
from rag_manything.answer.guardrails import (
    INVALID_QUESTION_MESSAGE,
    SAFE_MESSAGE,
    OpenAIGuardrail,
    block_input,
    check_output_structure,
    citation_ids,
)
from rag_manything.config import Settings
from rag_manything.models import (
    AnswerResult,
    Citation,
    GuardrailDecision,
    InputGuardrailDecision,
    RetrievedChunk,
)
from rag_manything.observability import Observability
from rag_manything.prompt.builder import PROMPT_VERSION, PromptBuilder

INSUFFICIENT_CONTEXT = "Không đủ thông tin trong tài liệu để trả lời câu hỏi này."


class Generator(Protocol):
    def generate(self, prompt: str) -> str: ...


class Guardrail(Protocol):
    def check_input(self, question: str) -> InputGuardrailDecision: ...

    def check_output(
        self, question: str, answer: str, chunks: tuple[RetrievedChunk, ...]
    ) -> GuardrailDecision: ...


class Retriever(Protocol):
    def retrieve(self, query: str, *, limit: int | None = None) -> list[Any]: ...


def _source_from_payload(payload: Mapping[str, Any]) -> str | None:
    for key in ("source_url", "source", "title", "document_id"):
        value = payload.get(key)
        if value is not None and str(value).strip():
            return str(value)
    return None


def _answer_chunks(retrieved: list[Any]) -> list[RetrievedChunk]:
    """Adapt retrieval results without coupling answer code to retrieval internals."""

    chunks = []
    for item in retrieved:
        payload = dict(getattr(item, "payload", {}) or {})
        chunks.append(
            RetrievedChunk(
                chunk_id=str(item.chunk_id),
                content=str(item.text),
                source=_source_from_payload(payload),
            )
        )
    return chunks


class AnswerService:
    def __init__(
        self,
        settings: Settings,
        qwen: Generator | None = None,
        guardrail: Guardrail | None = None,
        observability: Observability | None = None,
    ):
        self.settings = settings
        self.qwen = qwen or QwenClient(settings)
        self.guardrail = guardrail
        if self.guardrail is None and (
            settings.input_guardrail_enabled or settings.output_guardrail_enabled
        ):
            self.guardrail = OpenAIGuardrail(settings)
        self.builder = PromptBuilder(settings.max_context_chars)
        self.observability = observability or Observability(settings)
        self._owns_qwen = qwen is None
        self._owns_guardrail = guardrail is None
        self._owns_observability = observability is None

    def _blocked_input(self, decision: InputGuardrailDecision) -> AnswerResult:
        return AnswerResult(
            answer=INVALID_QUESTION_MESSAGE,
            status="blocked",
            reason=decision.reason,
            model=self.settings.qwen_model,
        )

    def _blocked_output(
        self, decision: GuardrailDecision, rewritten_question: str
    ) -> AnswerResult:
        return AnswerResult(
            answer=decision.safe_message or SAFE_MESSAGE,
            status="blocked",
            reason=decision.reason,
            model=self.settings.qwen_model,
            rewritten_question=rewritten_question,
        )

    def _prepare_question(self, question: str) -> InputGuardrailDecision:
        with self.observability.span("input_guardrail") as span:
            stripped = question.strip()
            if not stripped or len(question) > self.settings.max_question_chars:
                decision = block_input("invalid_question")
            elif self.settings.input_guardrail_enabled:
                decision = self.guardrail.check_input(question)
            else:
                decision = InputGuardrailDecision(
                    allowed=True,
                    reason="disabled",
                    rewritten_question=stripped,
                )
            span.update(allowed=decision.allowed, reason=decision.reason)
            return decision

    def _generate_answer(
        self, rewritten_question: str, chunks: list[RetrievedChunk]
    ) -> AnswerResult:
        with self.observability.span("build_prompt", prompt_version=PROMPT_VERSION) as span:
            prompt = self.builder.build(rewritten_question, chunks)
            span.update(chunk_count=len(prompt.chunks), context_chars=prompt.context_chars)
        if not prompt.chunks:
            return AnswerResult(
                answer=INSUFFICIENT_CONTEXT,
                status="insufficient_context",
                reason="empty_context",
                model=self.settings.qwen_model,
                rewritten_question=rewritten_question,
            )
        with self.observability.span("qwen_generate", model=self.settings.qwen_model):
            answer = self.qwen.generate(prompt.text)
        with self.observability.span("output_guardrail") as span:
            decision = check_output_structure(answer, prompt.chunks)
            if decision.allowed and self.settings.output_guardrail_enabled:
                decision = self.guardrail.check_output(
                    rewritten_question, answer, prompt.chunks
                )
            span.update(
                allowed=decision.allowed,
                reason=decision.reason,
                gpt_enabled=self.settings.output_guardrail_enabled,
            )
            if not decision.allowed:
                return self._blocked_output(decision, rewritten_question)
        by_id = {chunk.chunk_id: chunk for chunk in prompt.chunks}
        return AnswerResult(
            answer=answer,
            status="answered",
            model=self.settings.qwen_model,
            rewritten_question=rewritten_question,
            citations=[
                Citation(chunk_id=chunk_id, source=by_id[chunk_id].source)
                for chunk_id in citation_ids(answer)
            ],
        )

    def _run(
        self,
        question: str,
        *,
        chunks: list[RetrievedChunk] | None = None,
        retriever: Retriever | None = None,
        retrieval_limit: int | None = None,
    ) -> AnswerResult:
        started = perf_counter()
        with self.observability.span(
            "answer_request",
            prompt_version=PROMPT_VERSION,
            model=self.settings.qwen_model,
            retrieval_enabled=retriever is not None,
        ) as root:
            input_decision = self._prepare_question(question)
            if not input_decision.allowed:
                result = self._blocked_input(input_decision)
            else:
                rewritten = input_decision.rewritten_question
                if retriever is not None:
                    with self.observability.span("retrieval") as span:
                        hits = retriever.retrieve(rewritten, limit=retrieval_limit)
                        chunks = _answer_chunks(hits)
                        span.update(chunk_count=len(chunks))
                result = self._generate_answer(rewritten, chunks or [])
            root.update(status=result.status, reason=result.reason)
        return result.model_copy(
            update={"latency_ms": round((perf_counter() - started) * 1000, 2)}
        )

    def answer(self, question: str, chunks: list[RetrievedChunk]) -> AnswerResult:
        """Answer from caller-provided chunks, useful for tests and offline evaluation."""

        return self._run(question, chunks=chunks)

    def answer_with_retrieval(
        self,
        question: str,
        retriever: Retriever,
        *,
        retrieval_limit: int | None = None,
    ) -> AnswerResult:
        """Run rewrite -> configured hybrid retrieval/reranking -> answer."""

        return self._run(
            question,
            retriever=retriever,
            retrieval_limit=retrieval_limit,
        )

    def close(self) -> None:
        if self._owns_qwen:
            self.qwen.close()
        if self._owns_guardrail and self.guardrail:
            self.guardrail.close()
        if self._owns_observability:
            self.observability.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()
