"""Trace metadata only: no question, context, model text or credentials are captured."""

from contextlib import contextmanager
from time import perf_counter

from langsmith import Client, trace, tracing_context

from rag_manything.config import Settings


class Observability:
    def __init__(self, settings: Settings):
        self.enabled = settings.langsmith_tracing
        self.project = settings.langsmith_project
        self.client = (
            Client(api_key=settings.langsmith_api_key.get_secret_value()) if self.enabled else None
        )

    @contextmanager
    def span(self, name: str, **metadata):
        if not self.enabled:
            yield {}
            return
        output = {}
        start = perf_counter()
        with tracing_context(enabled=True, client=self.client, project_name=self.project):
            with trace(name, inputs={}, metadata=metadata, client=self.client) as run:
                try:
                    yield output
                finally:
                    output["latency_ms"] = round((perf_counter() - start) * 1000, 2)
                    run.end(outputs=output)

    def close(self) -> None:
        if self.client:
            self.client.flush()
