"""Unit tests for the configurable retrieval pipeline."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

from qdrant_client import models

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from rag_manything.retrieval import (  # noqa: E402
    CallableQueryEncoder,
    CallableQueryProcessor,
    HybridSearcher,
    ProcessedQuery,
    QueryRepresentation,
    RetrievalConfig,
    RetrievalPipeline,
)
from rag_manything.retrieval.reranking import PairReranker  # noqa: E402
from rag_manything.retrieval.reranking import PrecomputedReranker  # noqa: E402


class FakeStore:
    def __init__(self) -> None:
        self.calls: list[tuple[str, int, object]] = []

    def hybrid_search(self, **kwargs):
        self.calls.append(("hybrid", kwargs["limit"], kwargs["query_filter"]))
        return [
            SimpleNamespace(
                id="point-1",
                score=0.7,
                payload={"chunk_id": "chunk-1", "text": "first"},
            ),
            SimpleNamespace(
                id="point-2",
                score=0.6,
                payload={"chunk_id": "chunk-2", "text": "second"},
            ),
        ]


class RetrievalPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = FakeStore()
        self.encoder = CallableQueryEncoder(
            lambda query: QueryRepresentation(query_text=query, dense=[1.0, 0.0], sparse=models.SparseVector(indices=[1], values=[1.0]))
        )

    def test_hybrid_rrf_is_the_default_configuration(self) -> None:
        config = RetrievalConfig()
        self.assertEqual(config.search_mode, "hybrid")
        self.assertEqual(config.fusion, "rrf")

    def test_disabled_hooks_use_original_query_and_final_limit(self) -> None:
        config = RetrievalConfig(final_limit=1)
        pipeline = RetrievalPipeline(
            searcher=HybridSearcher(self.store, config),
            query_encoder=self.encoder,
            config=config,
        )
        results = pipeline.retrieve("original")
        self.assertEqual([item.chunk_id for item in results], ["chunk-1"])
        self.assertEqual(self.store.calls, [("hybrid", 1, None)])

    def test_query_processor_and_reranker_are_independent_hooks(self) -> None:
        query_filter = models.Filter(
            must=[models.FieldCondition(key="split", match=models.MatchValue(value="train"))]
        )
        config = RetrievalConfig(
            enable_query_processing=True,
            enable_reranking=True,
            final_limit=1,
            rerank_limit=2,
        )
        reranker = PairReranker(lambda pairs: [0.1, 0.9])
        pipeline = RetrievalPipeline(
            searcher=HybridSearcher(self.store, config),
            query_encoder=self.encoder,
            config=config,
            query_processor=CallableQueryProcessor(
                lambda _: ProcessedQuery("rewritten", query_id="q-1", qdrant_filter=query_filter)
            ),
            reranker=reranker,
        )
        results = pipeline.retrieve("original")
        self.assertEqual(results[0].chunk_id, "chunk-2")
        self.assertEqual(results[0].rerank_score, 0.9)
        self.assertEqual(self.store.calls, [("hybrid", 2, query_filter)])

    def test_precomputed_reranker_can_resolve_query_id_by_text(self) -> None:
        reranker = PrecomputedReranker(
            {("query_001", "chunk-1"): 0.8},
            query_id_by_text={"question": "query_001"},
        )
        candidate = SimpleNamespace(
            point_id="point-1",
            chunk_id="chunk-1",
            text="first",
            payload={},
            retrieval_score=0.5,
            rerank_score=None,
        )
        self.assertEqual(reranker.score("question", [candidate]), [0.8])


if __name__ == "__main__":
    unittest.main()

