import json

import httpx
from openai import OpenAI

from rag_manything.answer.client import QwenClient
from rag_manything.answer.guardrails import OpenAIGuardrail
from rag_manything.answer.service import AnswerService


def test_pipeline_with_real_sdk_parsing_and_mock_transports(settings, chunks):
    events = []

    def openai_handler(request):
        body = json.loads(request.content)
        assert body["text"]["format"]["type"] == "json_schema"
        assert body["text"]["format"]["strict"] is True
        assert body["store"] is False
        payload = json.loads(body["input"])
        if "answer" in payload:
            events.append("output")
            assert body["model"] == "test-output-guardrail"
            decision = {"allowed": True, "reason": "allowed", "safe_message": None}
        else:
            events.append("input")
            assert body["model"] == "test-input-guardrail"
            decision = {
                "allowed": True,
                "reason": "allowed",
                "rewritten_question": "Thư viện mở cửa lúc mấy giờ?",
            }
        return httpx.Response(200, json={
            "id": "resp_test", "object": "response", "created_at": 1,
            "status": "completed", "model": "test-guardrail",
            "output": [{"type": "message", "id": "msg_test", "role": "assistant",
                        "status": "completed", "content": [
                            {"type": "output_text", "text": json.dumps(decision), "annotations": []}
                        ]}],
        })

    def qwen_handler(request):
        events.append("qwen")
        assert chunks[0].content in json.loads(request.content)["prompt"]
        return httpx.Response(200, json={
            "text": "Thư viện mở cửa lúc 08:00 [doc-01].", "model": "Qwen/Qwen3-4B",
        })

    with httpx.Client(transport=httpx.MockTransport(openai_handler)) as oa_http:
        with OpenAI(api_key="test", http_client=oa_http) as oa:
            with httpx.Client(transport=httpx.MockTransport(qwen_handler)) as qwen_http:
                service = AnswerService(settings, QwenClient(settings, qwen_http),
                                        OpenAIGuardrail(settings, oa))
                result = service.answer("Thư viện mở cửa lúc mấy giờ?", chunks)
    assert events == ["input", "qwen", "output"]
    assert result.status == "answered"
    assert result.citations[0].chunk_id == "doc-01"
