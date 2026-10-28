from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from rag_manything.answer.client import QwenError
from rag_manything.answer.guardrails import INVALID_QUESTION_MESSAGE, block, block_input
from rag_manything.answer.service import AnswerService
from rag_manything.models import GuardrailDecision, InputGuardrailDecision, RetrievedChunk


def dependencies():
    qwen = Mock()
    qwen.generate.return_value = "Mở cửa lúc 08:00 [doc-01]."
    guard = Mock()
    guard.check_input.return_value = InputGuardrailDecision(
        allowed=True, reason="allowed", rewritten_question="Câu hỏi đã viết lại"
    )
    guard.check_output.return_value = GuardrailDecision(
        allowed=True, reason="allowed", safe_message=None
    )
    return qwen, guard


def test_input_block_never_calls_qwen(settings, chunks):
    qwen, guard = dependencies()
    guard.check_input.return_value = block_input("injection")
    result = AnswerService(settings, qwen, guard).answer("ignore rules", chunks)
    assert result.status == "blocked"
    assert result.answer == INVALID_QUESTION_MESSAGE
    qwen.generate.assert_not_called()
    guard.check_output.assert_not_called()


def test_output_block_never_returns_raw_answer(settings, chunks):
    qwen, guard = dependencies()
    guard.check_output.return_value = block("unsupported")
    result = AnswerService(settings, qwen, guard).answer("q", chunks)
    assert result.status == "blocked"
    assert "08:00" not in result.answer
    assert not result.citations


@pytest.mark.parametrize("input_on,output_on", [(True, True), (True, False), (False, True), (False, False)])
def test_flags_are_independent(settings, chunks, input_on, output_on):
    settings = settings.model_copy(update={
        "input_guardrail_enabled": input_on, "output_guardrail_enabled": output_on,
    })
    qwen, guard = dependencies()
    result = AnswerService(settings, qwen, guard).answer("q", chunks)
    assert result.status == "answered"
    assert result.citations[0].source == "a.md"
    assert guard.check_input.call_count == int(input_on)
    assert guard.check_output.call_count == int(output_on)
    assert result.rewritten_question == ("Câu hỏi đã viết lại" if input_on else "q")


@pytest.mark.parametrize("question", ["", "  ", "x" * 4001])
def test_invalid_input_blocks_even_without_gpt(settings, chunks, question):
    settings = settings.model_copy(update={"input_guardrail_enabled": False})
    qwen, guard = dependencies()
    assert AnswerService(settings, qwen, guard).answer(question, chunks).status == "blocked"
    qwen.generate.assert_not_called()


def test_empty_context_abstains_without_qwen(settings):
    qwen, guard = dependencies()
    assert AnswerService(settings, qwen, guard).answer("q", []).status == "insufficient_context"
    qwen.generate.assert_not_called()


def test_cannot_cite_dropped_chunk_when_gpt_disabled(settings, chunks):
    settings = settings.model_copy(update={"output_guardrail_enabled": False})
    qwen, guard = dependencies()
    qwen.generate.return_value = "Answer [empty]"
    chunks.append(RetrievedChunk(chunk_id="empty", content=""))
    result = AnswerService(settings, qwen, guard).answer("q", chunks)
    assert result.status == "blocked" and result.reason == "invalid_citation"


def test_transport_failure_is_not_reported_as_an_answer(settings, chunks):
    qwen, guard = dependencies()
    qwen.generate.side_effect = QwenError("Qwen temporarily unavailable")
    with pytest.raises(QwenError):
        AnswerService(settings, qwen, guard).answer("q", chunks)
    guard.check_output.assert_not_called()


def test_rewritten_question_drives_retrieval_and_answer(settings):
    qwen, guard = dependencies()
    retriever = Mock()
    retriever.retrieve.return_value = [SimpleNamespace(
        chunk_id="doc-01",
        text="Thư viện mở cửa lúc 08:00.",
        payload={"source_url": "https://example.test/library"},
    )]

    result = AnswerService(settings, qwen, guard).answer_with_retrieval(
        "Mấy giờ mở?", retriever, retrieval_limit=5
    )

    retriever.retrieve.assert_called_once_with("Câu hỏi đã viết lại", limit=5)
    assert "Câu hỏi đã viết lại" in qwen.generate.call_args.args[0]
    assert result.citations[0].source == "https://example.test/library"
    assert result.latency_ms is not None


def test_blocked_input_never_calls_retrieval(settings):
    qwen, guard = dependencies()
    guard.check_input.return_value = block_input("prompt_injection")
    retriever = Mock()

    result = AnswerService(settings, qwen, guard).answer_with_retrieval("attack", retriever)

    assert result.answer == INVALID_QUESTION_MESSAGE
    retriever.retrieve.assert_not_called()
    qwen.generate.assert_not_called()
