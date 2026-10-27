"""Data contracts shared by the retrieval pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, Mapping, Sequence

from qdrant_client import models as qdrant_models


def sparse_vector_from_mapping(weights: Mapping[Any, Any]) -> qdrant_models.SparseVector:
    """Convert BGE-M3 lexical weights into Qdrant's sparse-vector type."""
    pairs = sorted(
        (int(token_id), float(weight))
        for token_id, weight in weights.items()
        if float(weight) != 0.0
    )
    return qdrant_models.SparseVector(
        indices=[token_id for token_id, _ in pairs],
        values=[weight for _, weight in pairs],
    )


@dataclass(frozen=True, slots=True)
class ProcessedQuery:
    """Output of the optional query-processing stage."""

    text: str
    query_id: str | None = None
    qdrant_filter: qdrant_models.Filter | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.text or not self.text.strip():
            raise ValueError("Processed query text must be non-empty")


@dataclass(frozen=True, slots=True)
class QueryRepresentation:
    """Dense and/or sparse query vectors ready for Qdrant."""

    query_text: str
    dense: Sequence[float] | None = None
    sparse: qdrant_models.SparseVector | None = None
    dense_vector_name: str | None = None
    sparse_vector_name: str | None = None
    query_id: str | None = None

    def __post_init__(self) -> None:
        if not self.query_text or not self.query_text.strip():
            raise ValueError("Query representation text must be non-empty")
        if self.dense is None and self.sparse is None:
            raise ValueError("A query representation needs a dense or sparse vector")


@dataclass(frozen=True, slots=True)
class RetrievedChunk:
    """A Qdrant hit plus the optional post-retrieval reranking score."""

    point_id: str | int
    chunk_id: str
    text: str
    payload: Mapping[str, Any]
    retrieval_score: float
    rerank_score: float | None = None

    @property
    def score(self) -> float:
        """Return the score used for the final ordering."""
        return self.rerank_score if self.rerank_score is not None else self.retrieval_score


@dataclass(frozen=True, slots=True)
class RetrievalConfig:
    """Runtime switches and Qdrant vector names for one retrieval setup."""

    collection_name: str = "rag_chunks"
    search_mode: Literal["hybrid", "dense", "sparse"] = "hybrid"
    fusion: Literal["rrf", "dbsf"] = "rrf"
    dense_vector_name: str = "bge_m3_dense"
    sparse_vector_name: str = "bge_m3_sparse"
    enable_query_processing: bool = False
    enable_reranking: bool = False
    prefetch_limit: int = 50
    final_limit: int = 8
    rerank_limit: int = 20

    def __post_init__(self) -> None:
        if self.search_mode not in {"hybrid", "dense", "sparse"}:
            raise ValueError(f"Unsupported search mode: {self.search_mode}")
        if self.fusion not in {"rrf", "dbsf"}:
            raise ValueError(f"Unsupported fusion: {self.fusion}")
        if self.prefetch_limit < 1 or self.final_limit < 1 or self.rerank_limit < 1:
            raise ValueError("Search limits must be positive")
        if self.rerank_limit < self.final_limit:
            raise ValueError("rerank_limit must be at least final_limit")

