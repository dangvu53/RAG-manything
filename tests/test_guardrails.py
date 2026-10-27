from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from rag_manything.answer.guardrails import OpenAIGuardrail, check_output_structure
from rag_manything.models import GuardrailDecision, InputGuardrailDecision


@pytest.mark.parametrize("text,reason", [
    ("Wrong [fake]", "invalid_citation"),
    ("<think>secret</think>answer", "thinking_leak"),
    ("answer </THINK>", "thinking_leak"),
    ("  ", "empty_answer"),
])
def test_structural_blocks(text, reason, chunks):
    decision = check_output_structure(text, tuple(chunks))
    assert not decision.allowed and decision.reason == reason


def test_input_guardrail_rewrites_with_its_configured_model(settings):
    client = Mock()
    client.responses.parse.return_value = SimpleNamespace(output_parsed=InputGuardrailDecision(
        allowed=True, reason="allowed", rewritten_question="Câu hỏi độc lập"
    ))
    decision = OpenAIGuardrail(settings, client).check_input("câu hỏi ngắn")
    assert decision.rewritten_question == "Câu hỏi độc lập"
    call = client.responses.parse.call_args.kwargs
    assert call["model"] == "test-input-guardrail"
    assert call["text_format"] is InputGuardrailDecision
    assert call["store"] is False


@pytest.mark.parametrize("kind", ["refusal", "error"])
def test_input_guardrail_failure_is_closed(settings, kind):
    client = Mock()
    if kind == "error":
        client.responses.parse.side_effect = RuntimeError("sensitive response")
    else:
        client.responses.parse.return_value = SimpleNamespace(output_parsed=None)
    decision = OpenAIGuardrail(settings, client).check_input("question")
    assert not decision.allowed
    assert decision.reason == "guardrail_unavailable"
    assert decision.rewritten_question is None


def test_input_policy_block_never_echoes_model_content(settings):
    client = Mock()
    client.responses.parse.return_value = SimpleNamespace(output_parsed=InputGuardrailDecision(
        allowed=False, reason="secret-key", rewritten_question=None
    ))
    decision = OpenAIGuardrail(settings, client).check_input("ignore system")
    assert decision.reason == "policy_block"
    assert "secret-key" not in decision.model_dump_json()


def test_output_sends_entire_answer_and_only_visible_context(settings, chunks):
    client = Mock()
    client.responses.parse.return_value = SimpleNamespace(output_parsed=GuardrailDecision(
        allowed=True, reason="allowed", safe_message=None
    ))
    answer = "Beginning " + "x" * 10000 + " END [doc-01]"
    assert OpenAIGuardrail(settings, client).check_output("q", answer, tuple(chunks)).allowed
    call = client.responses.parse.call_args.kwargs
    assert call["model"] == "test-output-guardrail"
    assert "END [doc-01]" in call["input"]
