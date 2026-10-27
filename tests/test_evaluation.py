from types import SimpleNamespace

import pytest

from rag_manything.evaluation.ragas_eval import (
    EvaluationRow, EvaluationSettings, collect_responses, load_rows, run_evaluation,
)


def test_sample_dataset_is_twenty_real_question_seeds():
    from pathlib import Path

    rows = load_rows(Path("examples/evaluation_seed.jsonl"), require_response=False)
    assert len(rows) == 20
    assert all(not row.response for row in rows)
    assert len({row.user_input for row in rows}) == 20


def test_missing_responses_are_rejected(tmp_path):
    path = tmp_path / "rows.jsonl"
    path.write_text(EvaluationRow(user_input="q", retrieved_contexts=["c"], reference="r").model_dump_json())
    with pytest.raises(ValueError, match="generate"):
        load_rows(path)


def test_collection_uses_service_and_actual_visible_context():
    from unittest.mock import Mock

    from rag_manything.prompt.builder import PromptBuilder

    service = Mock()
    service.builder = PromptBuilder(30)
    service.answer.return_value = SimpleNamespace(answer="real answer")
    rows = [EvaluationRow(user_input="q", retrieved_contexts=["c" * 100], reference="r")]
    completed = collect_responses(rows, service)
    assert completed[0].response == "real answer"
    assert len(completed[0].retrieved_contexts[0]) < 100
    assert rows[0].response == ""
    assert completed[0].latency_ms is not None
    service.answer.assert_called_once()


def test_evaluation_wires_four_answer_metrics_latency_and_configured_models(monkeypatch):
    ragas = pytest.importorskip("ragas")
    pytest.importorskip("langchain_openai")

    def fake_evaluate(**kwargs):
        assert len(kwargs["metrics"]) == 4
        assert {m.name for m in kwargs["metrics"]} == {
            "faithfulness", "answer_relevancy", "factual_correctness",
            "semantic_similarity",
        }
        assert kwargs["llm"].langchain_llm.model_name == "test-eval"
        assert kwargs["embeddings"].embeddings.model == "test-embedding"
        assert kwargs["raise_exceptions"] is True
        return SimpleNamespace(scores=[{
            "faithfulness": 1.0,
            "answer_relevancy": 0.5,
            "factual_correctness": float("nan"),
            "semantic_similarity": 0.8,
        }])

    monkeypatch.setattr(ragas, "evaluate", fake_evaluate)
    report = run_evaluation([
        EvaluationRow(
            user_input="q", retrieved_contexts=["c"], response="a", reference="r",
            latency_ms=125.0,
        ),
    ], EvaluationSettings(
        _env_file=None, openai_api_key="test", openai_eval_model="test-eval",
        openai_embedding_model="test-embedding",
    ))
    assert report["row_count"] == 1
    assert report["averages"]["faithfulness"] == 1
    assert report["averages"]["factual_correctness"] is None
    assert report["latency_ms"]["mean"] == 125.0
    assert report["latency_ms"]["p95"] == 125.0
