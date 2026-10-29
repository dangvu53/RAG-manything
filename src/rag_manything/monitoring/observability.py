"""Prometheus instrumentation that preserves optional LangSmith tracing."""

from __future__ import annotations

from contextlib import contextmanager
from time import perf_counter
from typing import Any

from rag_manything.monitoring.metrics import STAGE_DURATION


class MetricsObservability:
    def __init__(self, delegate: Any):
        self.delegate = delegate

    @contextmanager
    def span(self, name: str, **metadata):
        started = perf_counter()
        try:
            with self.delegate.span(name, **metadata) as output:
                yield output
        finally:
            STAGE_DURATION.labels(stage=name).observe(perf_counter() - started)

    def close(self) -> None:
        self.delegate.close()
