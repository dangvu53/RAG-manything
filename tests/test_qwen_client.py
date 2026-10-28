import json

import httpx
import pytest

from rag_manything.answer.client import QwenClient, QwenError


def test_request_contract_and_retry(settings, monkeypatch):
    calls = []
    monkeypatch.setattr("rag_manything.answer.client.time.sleep", lambda _: None)

    def handler(request):
        calls.append(request)
        assert request.headers["Authorization"] == "Bearer test-token"
        assert json.loads(request.content)["max_new_tokens"] == 1024
        if len(calls) == 1:
            return httpx.Response(503)
        return httpx.Response(200, json={"text": "answer", "model": "Qwen/Qwen3-4B"})

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        assert QwenClient(settings, client).generate("prompt") == "answer"
    assert len(calls) == 2


def test_timeout_is_bounded_and_sanitized(settings, monkeypatch):
    calls = []
    monkeypatch.setattr("rag_manything.answer.client.time.sleep", lambda _: None)

    def handler(request):
        calls.append(request)
        raise httpx.ReadTimeout("test-token secret URL", request=request)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        with pytest.raises(QwenError) as error:
            QwenClient(settings, client).generate("prompt")
    assert len(calls) == 3
    assert "test-token" not in str(error.value)
    assert error.value.__context__ is None


@pytest.mark.parametrize("status,payload", [
    (401, {"secret": "test-token"}),
    (302, {}),
    (200, {"text": "", "model": "Qwen/Qwen3-4B"}),
    (200, {"text": "answer", "model": "wrong-model"}),
    (200, {"unexpected": "payload"}),
])
def test_permanent_errors_do_not_retry(settings, status, payload):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(status, json=payload)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        with pytest.raises(QwenError):
            QwenClient(settings, client).generate("prompt")
    assert len(calls) == 1
