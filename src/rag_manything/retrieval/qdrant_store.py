"""Small Qdrant client wrapper used by the retrieval component."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from qdrant_client import QdrantClient, models


@dataclass(frozen=True, slots=True)
class DenseVectorSpec:
    name: str
    size: int
    distance: models.Distance = models.Distance.COSINE


class QdrantStore:
    """Collection lifecycle, upsert, and vector-search operations."""

    def __init__(self, client: QdrantClient, collection_name: str):
        self.client = client
        self.collection_name = collection_name

    @classmethod
    def from_url(
        cls,
        url: str = "http://localhost:6333",
        *,
        collection_name: str = "rag_chunks",
        api_key: str | None = None,
        timeout: int = 60,
        check_compatibility: bool = False,
    ) -> "QdrantStore":
        # The project pins a Qdrant 1.15.x server while some environments have
        # a newer client. The caller can turn the check back on after aligning them.
        client = QdrantClient(
            url=url,
            api_key=api_key or None,
            timeout=timeout,
            check_compatibility=check_compatibility,
        )
        return cls(client, collection_name)

    def ensure_collection(
        self,
        dense_vectors: Mapping[str, int | DenseVectorSpec],
        sparse_vectors: Sequence[str] = (),
        *,
        recreate: bool = False,
        payload_indexes: Sequence[str] = (),
    ) -> None:
        """Create a named-vector collection or validate an existing one."""
        specs = {
            name: value
            if isinstance(value, DenseVectorSpec)
            else DenseVectorSpec(name=name, size=int(value))
            for name, value in dense_vectors.items()
        }
        if not specs:
            raise ValueError("At least one dense vector specification is required")

        if recreate and self.client.collection_exists(self.collection_name):
            self.client.delete_collection(self.collection_name)

        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config={
                    spec.name: models.VectorParams(size=spec.size, distance=spec.distance)
                    for spec in specs.values()
                },
                sparse_vectors_config={
                    name: models.SparseVectorParams() for name in sparse_vectors
                },
            )
        else:
            self._validate_vector_names(set(specs), set(sparse_vectors))

        for field_name in payload_indexes:
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name=field_name,
                field_schema=models.PayloadSchemaType.KEYWORD,
                wait=True,
            )

    def _validate_vector_names(
        self,
        expected_dense: set[str],
        expected_sparse: set[str],
    ) -> None:
        info = self.client.get_collection(self.collection_name)
        params = info.config.params
        configured_dense = params.vectors
        if isinstance(configured_dense, dict):
            dense_names = set(configured_dense)
        else:
            dense_names = {"default"}
        configured_sparse = getattr(params, "sparse_vectors", None) or {}
        sparse_names = set(configured_sparse) if isinstance(configured_sparse, dict) else set()
        missing_dense = expected_dense - dense_names
        missing_sparse = expected_sparse - sparse_names
        if missing_dense or missing_sparse:
            missing = sorted(missing_dense | missing_sparse)
            raise ValueError(
                f"Collection '{self.collection_name}' is missing named vectors {missing}. "
                "Use a new collection or rerun ingestion with --recreate."
            )

    def upsert(self, points: Sequence[models.PointStruct], *, wait: bool = True) -> None:
        self.client.upsert(collection_name=self.collection_name, points=points, wait=wait)

    def dense_search(
        self,
        query: Sequence[float],
        *,
        vector_name: str,
        limit: int,
        query_filter: models.Filter | None = None,
        with_payload: bool = True,
    ) -> list[Any]:
        response = self.client.query_points(
            collection_name=self.collection_name,
            query=[float(value) for value in query],
            using=vector_name,
            query_filter=query_filter,
            limit=limit,
            with_payload=with_payload,
        )
        return list(response.points)

    def sparse_search(
        self,
        query: models.SparseVector,
        *,
        vector_name: str,
        limit: int,
        query_filter: models.Filter | None = None,
        with_payload: bool = True,
    ) -> list[Any]:
        response = self.client.query_points(
            collection_name=self.collection_name,
            query=query,
            using=vector_name,
            query_filter=query_filter,
            limit=limit,
            with_payload=with_payload,
        )
        return list(response.points)

    def hybrid_search(
        self,
        *,
        dense_query: Sequence[float] | None,
        sparse_query: models.SparseVector | None,
        dense_vector_name: str | None,
        sparse_vector_name: str | None,
        limit: int,
        prefetch_limit: int,
        fusion: str = "rrf",
        query_filter: models.Filter | None = None,
        with_payload: bool = True,
    ) -> list[Any]:
        prefetch: list[models.Prefetch] = []
        if dense_query is not None:
            if not dense_vector_name:
                raise ValueError("dense_vector_name is required for a dense branch")
            prefetch.append(
                models.Prefetch(
                    query=[float(value) for value in dense_query],
                    using=dense_vector_name,
                    filter=query_filter,
                    limit=prefetch_limit,
                )
            )
        if sparse_query is not None:
            if not sparse_vector_name:
                raise ValueError("sparse_vector_name is required for a sparse branch")
            prefetch.append(
                models.Prefetch(
                    query=sparse_query,
                    using=sparse_vector_name,
                    filter=query_filter,
                    limit=prefetch_limit,
                )
            )
        if not prefetch:
            raise ValueError("Hybrid search needs a dense or sparse query vector")
        if len(prefetch) == 1:
            item = prefetch[0]
            response = self.client.query_points(
                collection_name=self.collection_name,
                query=item.query,
                using=item.using,
                query_filter=query_filter,
                limit=limit,
                with_payload=with_payload,
            )
            return list(response.points)

        fusion_value = {
            "rrf": models.Fusion.RRF,
            "dbsf": models.Fusion.DBSF,
        }.get(fusion.lower())
        if fusion_value is None:
            raise ValueError(f"Unsupported Qdrant fusion: {fusion}")
        response = self.client.query_points(
            collection_name=self.collection_name,
            prefetch=prefetch,
            query=models.FusionQuery(fusion=fusion_value),
            query_filter=query_filter,
            limit=limit,
            with_payload=with_payload,
        )
        return list(response.points)

