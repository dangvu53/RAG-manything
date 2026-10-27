"""Optional candidate reranking adapters."""

from __future__ import annotations

import csv
from collections.abc import Callable, Iterable, Mapping, Sequence
from pathlib import Path
from typing import Protocol

from .models import RetrievedChunk


class Reranker(Protocol):
    """Score the candidate chunks for one query."""

    def score(
        self,
        query: str,
        candidates: Sequence[RetrievedChunk],
        *,
        query_id: str | None = None,
    ) -> Sequence[float]: ...


class PairReranker:
    """Adapt a function that scores ``(query, chunk_text)`` pairs."""

    def __init__(self, scorer: Callable[[Sequence[tuple[str, str]]], Sequence[float]]):
        self._scorer = scorer

    def score(
        self,
        query: str,
        candidates: Sequence[RetrievedChunk],
        *,
        query_id: str | None = None,
    ) -> Sequence[float]:
        del query_id
        pairs = [(query, candidate.text) for candidate in candidates]
        return self._scorer(pairs)


class FlagEmbeddingReranker:
    """Adapter for ``FlagEmbedding.FlagReranker`` (for BGE reranker models)."""

    def __init__(self, model: object, *, normalize: bool = True):
        self.model = model
        self.normalize = normalize

    def score(
        self,
        query: str,
        candidates: Sequence[RetrievedChunk],
        *,
        query_id: str | None = None,
    ) -> Sequence[float]:
        del query_id
        pairs = [[query, candidate.text] for candidate in candidates]
        values = self.model.compute_score(pairs, normalize=self.normalize)  # type: ignore[attr-defined]
        if isinstance(values, (int, float)):
            return [float(values)]
        return [float(value) for value in values]


class PrecomputedReranker:
    """Use Kaggle's long-form ``query_id, chunk_id, score`` artifact locally."""

    def __init__(
        self,
        scores: dict[tuple[str, str], float],
        *,
        query_id_by_text: Mapping[str, str] | None = None,
    ):
        self._scores = scores
        self._query_id_by_text = dict(query_id_by_text or {})

    @classmethod
    def from_csv(
        cls,
        path: str | Path,
        *,
        query_id_by_text: Mapping[str, str] | None = None,
    ) -> "PrecomputedReranker":
        scores: dict[tuple[str, str], float] = {}
        with Path(path).open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            required = {"query_id", "chunk_id", "score"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise ValueError(f"Reranker CSV must contain {sorted(required)}")
            for row in reader:
                scores[(str(row["query_id"]), str(row["chunk_id"]))] = float(row["score"])
        return cls(scores, query_id_by_text=query_id_by_text)

    @classmethod
    def from_artifacts(
        cls,
        scores_csv: str | Path,
        queries_manifest: str | Path,
    ) -> "PrecomputedReranker":
        """Load scores and the exact question -> query_id mapping from Kaggle."""
        query_id_by_text: dict[str, str] = {}
        with Path(queries_manifest).open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            required = {"query_id", "question"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise ValueError(f"queries_manifest.csv must contain {sorted(required)}")
            for row in reader:
                query_id_by_text[str(row["question"])] = str(row["query_id"])
        return cls.from_csv(scores_csv, query_id_by_text=query_id_by_text)

    def score(
        self,
        query: str,
        candidates: Sequence[RetrievedChunk],
        *,
        query_id: str | None = None,
    ) -> Sequence[float]:
        query_id = query_id or self._query_id_by_text.get(query)
        if query_id is None:
            raise ValueError("PrecomputedReranker requires ProcessedQuery.query_id")
        values = []
        for candidate in candidates:
            key = (query_id, candidate.chunk_id)
            if key not in self._scores:
                raise KeyError(f"No precomputed score for query/chunk {key}")
            values.append(self._scores[key])
        return values


def rerank_candidates(
    reranker: Reranker,
    query: str,
    candidates: Iterable[RetrievedChunk],
    *,
    query_id: str | None = None,
) -> list[RetrievedChunk]:
    """Score, attach, and sort candidates in descending reranker order."""
    items = list(candidates)
    scores = list(reranker.score(query, items, query_id=query_id))
    if len(scores) != len(items):
        raise ValueError(f"Reranker returned {len(scores)} scores for {len(items)} candidates")
    ranked = [
        RetrievedChunk(
            point_id=item.point_id,
            chunk_id=item.chunk_id,
            text=item.text,
            payload=item.payload,
            retrieval_score=item.retrieval_score,
            rerank_score=float(score),
        )
        for item, score in zip(items, scores, strict=True)
    ]
    ranked.sort(key=lambda item: item.rerank_score or float("-inf"), reverse=True)
    return ranked

