from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class RetrievedChunk(BaseModel):
    model_config = ConfigDict(frozen=True)
    chunk_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
    content: str
    source: str | None = None


class AnswerRequest(BaseModel):
    question: str
    chunks: list[RetrievedChunk]


class InputGuardrailDecision(BaseModel):
    """Strict GPT-4o mini result for validation and retrieval-query rewriting."""

    model_config = ConfigDict(extra="forbid", strict=True)
    allowed: bool
    reason: str
    rewritten_question: str | None

    @model_validator(mode="after")
    def validate_rewrite(self):
        if self.allowed and (
            self.rewritten_question is None or not self.rewritten_question.strip()
        ):
            raise ValueError("Allowed input requires a rewritten question")
        if not self.allowed and self.rewritten_question is not None:
            raise ValueError("Blocked input must not include a rewritten question")
        return self


class GuardrailDecision(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    allowed: bool
    reason: str
    safe_message: str | None


class Citation(BaseModel):
    chunk_id: str
    source: str | None = None


class AnswerResult(BaseModel):
    answer: str
    citations: list[Citation] = Field(default_factory=list)
    status: Literal["answered", "blocked", "insufficient_context"]
    reason: str | None = None
    prompt_version: str = "answer-v1"
    model: str
    rewritten_question: str | None = None
    latency_ms: float | None = Field(default=None, ge=0)
