"""Configurable query -> hybrid retrieval -> reranking pipeline."""

from __future__ import annotations

from dataclasses import replace
from typing import Any

from .hybrid import HybridSearcher
from .models import ProcessedQuery, QueryRepresentation, RetrievedChunk, RetrievalConfig
from .query import QueryEncoder, QueryProcessor, apply_query_processor
from .reranking import Reranker, rerank_candidates


def _to_retrieved_chunk(point: Any) -> RetrievedChunk:
    payload = dict(point.payload or {})
    chunk_id = str(payload.get("chunk_id", point.id))
    text = str(payload.get("text", ""))
    return RetrievedChunk(
        point_id=point.id,
        chunk_id=chunk_id,
        text=text,
        payload=payload,
        retrieval_score=float(point.score),
    )


class RetrievalPipeline:
    """Composable retrieval service with independent processing/reranking toggles."""

    def __init__(
        self,
        *,
        searcher: HybridSearcher,
        query_encoder: QueryEncoder,
        config: RetrievalConfig,
        query_processor: QueryProcessor | None = None,
        reranker: Reranker | None = None,
    ):
        self.searcher = searcher
        self.query_encoder = query_encoder
        self.config = config
        self.query_processor = query_processor
        self.reranker = reranker
        if config.enable_query_processing and query_processor is None:
            raise ValueError("enable_query_processing=True requires query_processor")
        if config.enable_reranking and reranker is None:
            raise ValueError("enable_reranking=True requires reranker")

    def retrieve(self, query: str, *, limit: int | None = None) -> list[RetrievedChunk]:
        processed = (
            apply_query_processor(self.query_processor, query)
            if self.config.enable_query_processing
            else ProcessedQuery(text=query)
        )
        representation = self.query_encoder.encode(processed.text)
        if not isinstance(representation, QueryRepresentation):
            raise TypeError("query_encoder.encode must return QueryRepresentation")
        if processed.query_id and representation.query_id != processed.query_id:
            representation = replace(representation, query_id=processed.query_id)

        final_limit = limit or self.config.final_limit
        candidate_limit = self.config.rerank_limit if self.config.enable_reranking else final_limit
        points = self.searcher.search(
            representation,
            query_filter=processed.qdrant_filter,
            limit=candidate_limit,
        )
        candidates = [_to_retrieved_chunk(point) for point in points]
        if self.config.enable_reranking:
            candidates = rerank_candidates(
                self.reranker,  # type: ignore[arg-type]
                processed.text,
                candidates,
                query_id=processed.query_id,
            )
        return candidates[:final_limit]

