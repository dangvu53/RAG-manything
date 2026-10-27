"""Optional query processing and query-vector adapters."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, Protocol

from qdrant_client import models as qdrant_models

from .models import (
    ProcessedQuery,
    QueryRepresentation,
    sparse_vector_from_mapping,
)


class QueryProcessor(Protocol):
    """External query rewrite/filter pipeline contract."""

    def process(self, query: str) -> ProcessedQuery | str | Mapping[str, Any]: ...


class NoOpQueryProcessor:
    """Keep the original query unchanged."""

    def process(self, query: str) -> ProcessedQuery:
        return ProcessedQuery(text=query)


class CallableQueryProcessor:
    """Adapt a plain callable to the query-processor protocol."""

    def __init__(self, function: Callable[[str], ProcessedQuery | str | Mapping[str, Any]]):
        self._function = function

    def process(self, query: str) -> ProcessedQuery | str | Mapping[str, Any]:
        return self._function(query)


def apply_query_processor(
    processor: QueryProcessor | Callable[[str], ProcessedQuery | str | Mapping[str, Any]] | None,
    query: str,
) -> ProcessedQuery:
    """Normalize an injected processor result into ``ProcessedQuery``."""
    if processor is None:
        return ProcessedQuery(text=query)

    result = processor.process(query) if hasattr(processor, "process") else processor(query)
    if isinstance(result, ProcessedQuery):
        return result
    if isinstance(result, str):
        return ProcessedQuery(text=result)
    if isinstance(result, Mapping):
        text = result.get("text", result.get("query", result.get("query_text")))
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Query processor mapping must contain non-empty 'text' or 'query'")
        qdrant_filter = result.get("qdrant_filter", result.get("filter"))
        metadata = result.get("metadata", {})
        if qdrant_filter is not None and not isinstance(qdrant_filter, qdrant_models.Filter):
            raise TypeError("Query processor filters must be a qdrant_client.models.Filter")
        if not isinstance(metadata, Mapping):
            raise TypeError("Query processor metadata must be a mapping")
        return ProcessedQuery(
            text=text,
            query_id=str(result["query_id"]) if result.get("query_id") is not None else None,
            qdrant_filter=qdrant_filter,
            metadata=metadata,
        )
    raise TypeError("Query processor must return ProcessedQuery, str, or a mapping")


class QueryEncoder(Protocol):
    """Turn one processed query into vectors for the configured Qdrant branches."""

    def encode(self, query: str) -> QueryRepresentation: ...


class CallableQueryEncoder:
    """Adapt a callable returning a ``QueryRepresentation``."""

    def __init__(self, function: Callable[[str], QueryRepresentation]):
        self._function = function

    def encode(self, query: str) -> QueryRepresentation:
        return self._function(query)


def _as_float_vector(value: Any) -> list[float]:
    if hasattr(value, "tolist"):
        value = value.tolist()
    if len(value) > 0 and isinstance(value[0], (list, tuple)):
        value = value[0]
    return [float(item) for item in value]


class BgeM3QueryEncoder:
    """Adapter for a loaded ``FlagEmbedding.BGEM3FlagModel`` instance."""

    def __init__(
        self,
        model: Any,
        *,
        dense_vector_name: str = "bge_m3_dense",
        sparse_vector_name: str = "bge_m3_sparse",
    ):
        self.model = model
        self.dense_vector_name = dense_vector_name
        self.sparse_vector_name = sparse_vector_name

    def encode(self, query: str) -> QueryRepresentation:
        encoded = self.model.encode(
            query,
            return_dense=True,
            return_sparse=True,
            return_colbert_vecs=False,
        )
        dense = encoded.get("dense_vecs")
        sparse = encoded.get("lexical_weights")
        if dense is None or sparse is None:
            raise ValueError("BGE-M3 encoder must return dense_vecs and lexical_weights")
        return QueryRepresentation(
            query_text=query,
            dense=_as_float_vector(dense),
            sparse=sparse_vector_from_mapping(sparse),
            dense_vector_name=self.dense_vector_name,
            sparse_vector_name=self.sparse_vector_name,
        )

