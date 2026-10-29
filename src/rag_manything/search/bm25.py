"""Small in-memory BM25 index for the local retrieval baseline."""

from __future__ import annotations

import math
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass
from typing import Any, Mapping, Sequence


TOKEN_PATTERN = re.compile(r"[^\W_]+", flags=re.UNICODE)


def tokenize(text: str) -> list[str]:
    """Normalize Vietnamese text before splitting it into Unicode words."""

    normalized = unicodedata.normalize("NFC", text).lower()
    return TOKEN_PATTERN.findall(normalized)


@dataclass(frozen=True, slots=True)
class BM25Hit:
    chunk_id: str
    text: str
    payload: Mapping[str, Any]
    score: float


class BM25Index:
    """Minimal BM25 index with deterministic tie-breaking."""

    def __init__(
        self,
        documents: Sequence[str],
        *,
        rows: Sequence[Mapping[str, Any]] | None = None,
        k1: float = 1.5,
        b: float = 0.75,
    ):
        if k1 <= 0:
            raise ValueError("k1 must be positive")
        if not 0 <= b <= 1:
            raise ValueError("b must be in [0, 1]")
        if rows is not None and len(rows) != len(documents):
            raise ValueError("rows and documents must have the same length")
        self.k1 = k1
        self.b = b
        self.rows = [dict(row) for row in rows] if rows is not None else []
        self.term_frequencies = [Counter(tokenize(document)) for document in documents]
        self.document_lengths = [sum(counter.values()) for counter in self.term_frequencies]
        self.average_document_length = (
            sum(self.document_lengths) / len(self.document_lengths)
            if self.document_lengths
            else 0.0
        )
        document_frequency: Counter[str] = Counter()
        for frequencies in self.term_frequencies:
            document_frequency.update(frequencies.keys())
        document_count = len(documents)
        self.idf = {
            term: math.log(1.0 + (document_count - frequency + 0.5) / (frequency + 0.5))
            for term, frequency in document_frequency.items()
        }

    @classmethod
    def from_rows(
        cls,
        rows: Sequence[Mapping[str, Any]],
        *,
        k1: float = 1.5,
        b: float = 0.75,
    ) -> BM25Index:
        required = {"chunk_id", "document_id", "text"}
        if not rows or not required.issubset(rows[0]):
            raise ValueError(f"BM25 rows must contain {sorted(required)}")
        return cls([str(row["text"]) for row in rows], rows=rows, k1=k1, b=b)

    def scores(self, query: str) -> list[float]:
        query_terms = Counter(tokenize(query))
        scores = [0.0] * len(self.term_frequencies)
        for term, query_frequency in query_terms.items():
            idf = self.idf.get(term)
            if idf is None:
                continue
            for index, frequencies in enumerate(self.term_frequencies):
                term_frequency = frequencies.get(term, 0)
                if not term_frequency:
                    continue
                length_ratio = (
                    self.document_lengths[index] / self.average_document_length
                    if self.average_document_length
                    else 0.0
                )
                denominator = term_frequency + self.k1 * (
                    1.0 - self.b + self.b * length_ratio
                )
                scores[index] += query_frequency * idf * (
                    term_frequency * (self.k1 + 1.0) / denominator
                )
        return scores

    def search(self, query: str, *, limit: int = 3) -> list[BM25Hit]:
        if limit < 1:
            raise ValueError("limit must be positive")
        if not self.rows:
            raise ValueError("BM25 search requires rows loaded with from_rows()")
        values = self.scores(query)
        matching = [index for index, score in enumerate(values) if score > 0]
        order = sorted(
            matching,
            key=lambda index: (-values[index], str(self.rows[index]["chunk_id"])),
        )[:limit]
        return [
            BM25Hit(
                chunk_id=str(self.rows[index]["chunk_id"]),
                text=str(self.rows[index]["text"]),
                payload=self.rows[index],
                score=float(values[index]),
            )
            for index in order
        ]


class BM25Retriever:
    """Adapter implementing the retriever contract expected by AnswerService."""

    def __init__(self, index: BM25Index):
        self.index = index

    def retrieve(self, query: str, *, limit: int | None = None) -> list[BM25Hit]:
        return self.index.search(query, limit=limit or 3)
