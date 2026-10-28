import pytest
from pydantic import ValidationError

from rag_manything.config import Settings


@pytest.mark.parametrize("input_on,output_on", [(True, False), (False, True), (True, True)])
def test_enabled_guardrails_require_openai(input_on, output_on):
    with pytest.raises(ValidationError):
        Settings(
            _env_file=None, qwen_api_url="https://qwen.example/generate", qwen_api_token="token",
            input_guardrail_enabled=input_on, output_guardrail_enabled=output_on,
            openai_api_key="",
        )


@pytest.mark.parametrize(
    "field,input_on,output_on",
    [
        ("openai_input_guardrail_model", True, False),
        ("openai_output_guardrail_model", False, True),
    ],
)
def test_each_enabled_guardrail_requires_its_model(field, input_on, output_on):
    values = {
        "_env_file": None,
        "qwen_api_url": "https://qwen.example/generate",
        "qwen_api_token": "token",
        "openai_api_key": "key",
        "input_guardrail_enabled": input_on,
        "output_guardrail_enabled": output_on,
        field: "",
    }
    with pytest.raises(ValidationError):
        Settings(**values)


def test_disabled_guardrails_need_no_openai_and_env_flags_load(tmp_path, monkeypatch):
    for key in ("INPUT_GUARDRAIL_ENABLED", "OUTPUT_GUARDRAIL_ENABLED", "LANGSMITH_TRACING"):
        monkeypatch.delenv(key, raising=False)
    env = tmp_path / ".env"
    env.write_text(
        "QWEN_API_URL=https://qwen.example/generate\nQWEN_API_TOKEN=token\n"
        "INPUT_GUARDRAIL_ENABLED=false\nOUTPUT_GUARDRAIL_ENABLED=false\n"
        "LANGSMITH_TRACING=false\n", encoding="utf-8",
    )
    settings = Settings(_env_file=env)
    assert not settings.input_guardrail_enabled and not settings.output_guardrail_enabled
    assert settings.qwen_api_token.get_secret_value() == "token"


@pytest.mark.parametrize("url", ["http://remote.example/generate", "https://token@host/generate", "https://host/generate?key=token"])
def test_rejects_insecure_or_credential_urls(settings, url):
    with pytest.raises(ValidationError):
        Settings(**(settings.model_dump() | {"qwen_api_url": url}))
