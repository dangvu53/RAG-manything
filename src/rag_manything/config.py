"""Environment configuration, validated before any remote calls."""

from typing import Self

from pydantic import Field, HttpUrl, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore", hide_input_in_errors=True
    )

    qwen_api_url: HttpUrl
    qwen_api_token: SecretStr
    qwen_model: str = "Qwen/Qwen3-4B"
    qwen_timeout_seconds: float = Field(default=60, gt=0)
    qwen_max_retries: int = Field(default=2, ge=0, le=2)
    qwen_max_new_tokens: int = Field(default=1024, ge=1, le=4096)
    qwen_temperature: float = Field(default=0.1, ge=0, le=2)
    openai_api_key: SecretStr | None = None
    openai_input_guardrail_model: str = "gpt-4o-mini"
    openai_output_guardrail_model: str = "gpt-5-mini"
    openai_eval_model: str = ""
    openai_timeout_seconds: float = Field(default=30, gt=0)
    openai_embedding_model: str = "text-embedding-3-small"
    input_guardrail_enabled: bool = False
    output_guardrail_enabled: bool = False
    max_question_chars: int = Field(default=4000, ge=1)
    max_context_chars: int = Field(default=16000, ge=128)
    langsmith_tracing: bool = False
    langsmith_api_key: SecretStr | None = None
    langsmith_project: str = "rag-manything-prompt-answer"

    @model_validator(mode="after")
    def validate_credentials(self) -> Self:
        if not self.qwen_api_token.get_secret_value().strip():
            raise ValueError("QWEN_API_TOKEN is required")
        if self.qwen_api_url.username or self.qwen_api_url.password or self.qwen_api_url.query:
            raise ValueError("QWEN_API_URL must not contain credentials or query parameters")
        if self.qwen_api_url.scheme != "https" and self.qwen_api_url.host not in {
            "localhost", "127.0.0.1", "[::1]"
        }:
            raise ValueError("QWEN_API_URL requires HTTPS (except localhost)")
        if self.input_guardrail_enabled or self.output_guardrail_enabled:
            if not self.openai_api_key or not self.openai_api_key.get_secret_value().strip():
                raise ValueError("Enabled guardrails require OPENAI_API_KEY")
        if self.input_guardrail_enabled and not self.openai_input_guardrail_model.strip():
            raise ValueError("Input guardrail requires OPENAI_INPUT_GUARDRAIL_MODEL")
        if self.output_guardrail_enabled and not self.openai_output_guardrail_model.strip():
            raise ValueError("Output guardrail requires OPENAI_OUTPUT_GUARDRAIL_MODEL")
        if self.langsmith_tracing and (
            not self.langsmith_api_key or not self.langsmith_api_key.get_secret_value().strip()
        ):
            raise ValueError("Enabled tracing requires LANGSMITH_API_KEY")
        return self
