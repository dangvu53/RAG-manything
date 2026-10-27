"""Dense, sparse, and Qdrant-fused candidate retrieval."""

from __future__ import annotations

from typing import Any

from qdrant_client import models

from .models import QueryRepresentation, RetrievalConfig
from .qdrant_store import QdrantStore


class HybridSearcher:
    """Dispatch one query representation to the configured Qdrant branch(es)."""

    def __init__(self, store: QdrantStore, config: RetrievalConfig):
        self.store = store
        self.config = config

    def search(
        self,
        representation: QueryRepresentation,
        *,
        query_filter: models.Filter | None = None,
        limit: int | None = None,
    ) -> list[Any]:
        result_limit = limit or self.config.final_limit
        dense_name = representation.dense_vector_name or self.config.dense_vector_name
        sparse_name = representation.sparse_vector_name or self.config.sparse_vector_name

        if self.config.search_mode == "dense":
            if representation.dense is None:
                raise ValueError("Dense search was selected but the query has no dense vector")
            return self.store.dense_search(
                representation.dense,
                vector_name=dense_name,
                limit=result_limit,
                query_filter=query_filter,
            )

        if self.config.search_mode == "sparse":
            if representation.sparse is None:
                raise ValueError("Sparse search was selected but the query has no sparse vector")
            return self.store.sparse_search(
                representation.sparse,
                vector_name=sparse_name,
                limit=result_limit,
                query_filter=query_filter,
            )

        return self.store.hybrid_search(
            dense_query=representation.dense,
            sparse_query=representation.sparse,
            dense_vector_name=dense_name if representation.dense is not None else None,
            sparse_vector_name=sparse_name if representation.sparse is not None else None,
            limit=result_limit,
            prefetch_limit=max(self.config.prefetch_limit, result_limit),
            fusion=self.config.fusion,
            query_filter=query_filter,
        )

