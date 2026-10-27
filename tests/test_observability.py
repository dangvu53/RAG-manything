from contextlib import contextmanager

from rag_manything.observability import Observability


def test_trace_hierarchy_records_metadata_without_content(settings, monkeypatch):
    events = []
    stack = []

    class Run:
        def end(self, **kwargs):
            events.append(kwargs)

    @contextmanager
    def fake_trace(name, **kwargs):
        events.append({"name": name, "parent": stack[-1] if stack else None, **kwargs})
        stack.append(name)
        yield Run()
        stack.pop()

    monkeypatch.setattr("rag_manything.observability.trace", fake_trace)
    monkeypatch.setattr("rag_manything.observability.Client", lambda **_: object())
    observer = Observability(settings.model_copy(update={
        "langsmith_tracing": True, "langsmith_api_key": settings.qwen_api_token,
    }))
    with observer.span("answer_request", chunk_count=1) as root:
        with observer.span("build_prompt") as child:
            child["context_chars"] = 100
        root["status"] = "answered"
    child_event = next(event for event in events if event.get("name") == "build_prompt")
    assert child_event["parent"] == "answer_request"
    assert child_event["inputs"] == {}
    assert "test-token" not in str(events)
    assert any("latency_ms" in e.get("outputs", {}) for e in events)
