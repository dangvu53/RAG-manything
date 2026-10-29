"""Runtime and evaluation metrics exposed to Prometheus."""

from prometheus_client import Counter, Gauge, Histogram


HTTP_REQUESTS = Counter(
    "rag_http_requests_total",
    "HTTP requests received by the RAG API",
    ["endpoint", "status"],
)
HTTP_DURATION = Histogram(
    "rag_http_request_duration_seconds",
    "End-to-end API request duration in seconds",
    ["endpoint"],
    buckets=(0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20, 40, 90, 180),
)
ANSWER_RESULTS = Counter(
    "rag_answers_total",
    "Answer outcomes returned by the RAG pipeline",
    ["status"],
)
STAGE_DURATION = Histogram(
    "rag_stage_duration_seconds",
    "Duration of a named RAG pipeline stage",
    ["stage"],
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 30, 90, 180),
)
RETRIEVED_CHUNKS = Histogram(
    "rag_retrieved_chunks",
    "Number of chunks returned by BM25 per query",
    buckets=(0, 1, 2, 3, 5, 8, 10, 20),
)
EMPTY_RETRIEVALS = Counter(
    "rag_empty_retrievals_total",
    "Queries for which BM25 returned no matching chunks",
)

EVALUATION_SCORE = Gauge(
    "rag_evaluation_score",
    "Latest offline retrieval or answer quality score",
    ["dataset", "retrieval", "suite", "metric", "cutoff"],
)
EVALUATION_QUERIES = Gauge(
    "rag_evaluation_queries",
    "Number of queries in the latest offline evaluation",
    ["dataset", "retrieval", "suite"],
)
EVALUATION_LATENCY = Gauge(
    "rag_evaluation_latency_seconds",
    "Latency statistics from the latest saved answer evaluation",
    ["dataset", "retrieval", "statistic"],
)
