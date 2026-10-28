import pytest

from rag_manything.config import Settings
from rag_manything.models import RetrievedChunk


@pytest.fixture
def settings():
    return Settings(
        _env_file=None, qwen_api_url="https://qwen.example/generate",
        qwen_api_token="test-token", openai_api_key="test-openai",
        openai_input_guardrail_model="test-input-guardrail",
        openai_output_guardrail_model="test-output-guardrail",
        langsmith_tracing=False,
    )


@pytest.fixture
def chunks():
    return [RetrievedChunk(chunk_id="doc-01", content="Thư viện mở cửa lúc 08:00.", source="a.md")]
