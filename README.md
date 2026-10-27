# RAG-manything

Retrieval component for the RAG-manything project. The current implementation
covers Qdrant storage, BGE-M3 hybrid retrieval, optional query processing,
optional reranking, and ViRE-style offline evaluation.

## Structure

```text
src/rag_manything/
  retrieval/   retrieval component
  prompt/      prompt construction component
  answer/      answer generation component
```

The retrieval component is implemented. Prompt and answer components remain
placeholders.

## Current baseline status

- Corpus: 297 unique ViRHE4QA context chunks.
- Queries: 100 prepared query-to-gold-chunk pairs.
- Qdrant collection: `virhe4qa_297`.
- Default search: BGE-M3 dense + BGE-M3 sparse, fused with Qdrant RRF.
- Query processing: disabled; the external query pipeline is injected but not hard-coded.
- Reranking: disabled in the current baseline; adapters are ready for later scores or models.
- Alternate vectors already stored: Qwen3-Embedding-0.6B and Qwen3-Embedding-4B.

## Local setup

The project uses the shared workspace environment at
`D:\AI Engineer Fresher - TPBank\.venv`. From the workspace root:

```powershell
.\.venv\Scripts\python.exe -m pip install -r .\RAG-manything\requirements.txt
.\.venv\Scripts\python.exe -m pip install -e .\RAG-manything
Copy-Item .\RAG-manything\.env.example .\RAG-manything\.env
```

Do not create a second environment inside `RAG-manything` unless the shared
environment is unavailable.

Update `.env` to match the local model server when one is configured.

## Data used

The source data was copied from `ViRE/data` into `data/`:

- `data/benchmark_datasets/`: benchmark datasets from the ViRE repository, excluding `mock`.
- `data/virhe4qa_subset/`: prepared ViRHE4QA data with 297 unique contexts and 100 queries.
- `data/kaggle_artifacts/virhe4qa_model_sweep/`: current Kaggle model output.
- `data/retrieval_runs/`: generated retrieval rankings and metric reports.

The current Kaggle directory contains document/query vectors for BGE-M3,
Qwen3-Embedding-0.6B, and Qwen3-Embedding-4B. It also contains the 29,700-pair
reranker manifest, but no reranker score or timing files yet.

The complete `data/` directory is intentionally versioned and can be pushed
with this repository. It contains benchmark source copies and the generated
subset/Kaggle/retrieval outputs needed to reproduce the current baseline. The
current snapshot is about 252 MB across 47 files; if a future model artifact
exceeds the hosting provider's per-file limit, store that file with Git LFS
instead of ignoring the whole data directory.

## Start Qdrant

From the workspace root:

```powershell
docker compose -f .\RAG-manything\docker-compose.yml up -d qdrant
```

The current server is Qdrant `v1.15.5` at `http://localhost:6333`. Its local
dashboard is available at `http://localhost:6333/dashboard`. The installed
client may be newer than the server; `QdrantStore.from_url()` disables the
compatibility warning for this local setup. Align versions before deployment.

## Ingest parsed chunks

Then ingest one JSONL file. Each line represents one chunk. The file may contain flat metadata fields (such as `title`, `page_start`, `source_url`, `product`) or a nested `metadata` object. `chunk_id`, `document_id`, and non-empty `text` are required.

Example input line:

```json
{"chunk_id":"doc-a-0001","document_id":"doc-a","chunk_index":0,"text":"Chunk content...","metadata":{"title":"Document title","page_start":1,"page_end":1,"source_url":"https://example.org/document.pdf","product":"account"}}
```

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\ingest_chunks.py path\to\document_chunks.jsonl
```

The script creates the collection if it does not exist, generates BGE-M3 dense and sparse vectors in batches, and upserts points. Re-running it with the same chunk IDs updates those points. It does not delete chunks that were removed from a later version of the input file. BGE vectors use the named-vector keys `bge_m3_dense` and `bge_m3_sparse`.

The 100-row ViRHE4QA mock CSV can be ingested directly. The script uses each `context` as chunk text, creates a stable document ID from its content, and stores only source split/index/label as metadata. The question and answer fields are not embedded or stored in Qdrant.

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\ingest_chunks.py .\RAG-manything\data\virhe4qa_subset\ViRHE4QA_v2_sample_100\ViRHE4QA_v2_sample_100.csv --collection virhe4qa_sample_100 --batch-size 8
```

## Load Kaggle artifacts

When the Kaggle notebook has finished, download its output directory. It should contain at least `chunks_manifest.csv`, `bge_m3_dense.npy`, and `bge_m3_sparse.jsonl`. The Qwen dense `.npy` files are optional; the ingestion script discovers them automatically.

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\ingest_kaggle_artifacts.py path\to\retrieval_artifacts --collection virhe4qa_297 --recreate
```

This stores only document vectors in Qdrant. Query vectors, the reranker pair
manifest, and future reranker scores remain offline evaluation artifacts. For
interactive retrieval, the query encoder must be available locally or behind a
service; Qdrant does not generate embeddings.

## Retrieval pipeline

Qdrant performs dense search, sparse search, or dense+sparse RRF fusion. Cross-encoder rerankers run after Qdrant returns candidates, so they are injected as a Python adapter.

The active hybrid branch is Qdrant-native, not a Python-side weighted score sum:

1. Qdrant receives a dense `Prefetch` using `bge_m3_dense`.
2. Qdrant receives a sparse `Prefetch` using `bge_m3_sparse`.
3. Qdrant applies `FusionQuery(fusion=Fusion.RRF)` and returns the fused candidates.

The corresponding configuration is `search_mode="hybrid"` and `fusion="rrf"`.
These are also the defaults of `RetrievalConfig`, `search_bge_m3.py`, and the
batch evaluator, so a caller gets hybrid RRF unless it explicitly selects
`dense`, `sparse`, or another fusion method.

```python
from FlagEmbedding import BGEM3FlagModel, FlagReranker

from rag_manything.retrieval import (
    BgeM3QueryEncoder,
    FlagEmbeddingReranker,
    HybridSearcher,
    QdrantStore,
    RetrievalConfig,
    RetrievalPipeline,
)

config = RetrievalConfig(
    collection_name="virhe4qa_297",
    search_mode="hybrid",
    fusion="rrf",
    enable_query_processing=False,
    enable_reranking=False,
    final_limit=8,
)
store = QdrantStore.from_url(collection_name=config.collection_name)
encoder = BgeM3QueryEncoder(BGEM3FlagModel("BAAI/bge-m3", use_fp16=False))
pipeline = RetrievalPipeline(
    searcher=HybridSearcher(store, config),
    query_encoder=encoder,
    config=config,
)

results = pipeline.retrieve("Câu hỏi cần tìm")
for result in results:
    print(result.score, result.chunk_id, result.text[:160])
```

To enable reranking, increase the candidate pool and inject a reranker:

```python
config = RetrievalConfig(
    collection_name="virhe4qa_297",
    enable_reranking=True,
    rerank_limit=20,
    final_limit=8,
)
reranker = FlagEmbeddingReranker(
    FlagReranker("BAAI/bge-reranker-v2-m3", use_fp16=False)
)
pipeline = RetrievalPipeline(
    searcher=HybridSearcher(store, config),
    query_encoder=encoder,
    config=config,
    reranker=reranker,
)
```

Set `enable_query_processing=True` and pass `query_processor=...` when the external query pipeline is ready. It may return a rewritten string or `ProcessedQuery(text=..., qdrant_filter=...)`. Set `enable_reranking=False` to bypass reranking without changing the search code. To use a Qwen dense branch, choose `search_mode="dense"` and set `dense_vector_name` to `qwen_0_6b_dense` or `qwen_4b_dense`, then inject a matching `CallableQueryEncoder`.

For the saved Kaggle reranker scores, use `PrecomputedReranker.from_artifacts(scores_csv, queries_manifest)`; it resolves the 100 exact questions to their `query_id` values without running a model locally.

## Quick hybrid search

Search immediately with one of the 100 BGE-M3 query vectors exported by Kaggle:

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\search_bge_m3.py --query-id query_001 --limit 8
```

For a new question, BGE-M3 must be available locally or be downloaded to the model cache:

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\search_bge_m3.py "Ai chịu trách nhiệm thực hiện kiểm tra và thanh tra nội bộ?" --limit 8
```

## Evaluate the 100-query run

Run the same 100 prepared queries and calculate the ViRE-style metrics:

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\evaluate_qdrant_retrieval.py `
  --collection virhe4qa_297 `
  --mode hybrid `
  --fusion rrf `
  --ks 1,3,5,10,20,50,100 `
  --prefetch-limit 100 `
  --run-name bge_m3_hybrid_rrf_100
```

Results are written under `data\retrieval_runs\<run-name>`, including `metrics.json`, `metrics.csv`, `ranks.csv`, full retrieved results, and `errors\fail@20.csv`. Use `--mode dense` or `--mode sparse` with a different `--run-name` for standalone baselines.

## Baseline result

The current run is BGE-M3 dense + sparse with Qdrant RRF, using 297 chunks and
100 queries. Query processing and reranking were disabled. The five headline
metrics used by the original ViRE report are:

| Metric | Raw value | Percent |
| --- | ---: | ---: |
| P@1 | 0.6200 | 62.00 |
| R@10 | 0.9100 | 91.00 |
| MRR@10 | 0.7258 | 72.58 |
| nDCG@10 | 0.7712 | 77.12 |
| R@20 | 0.9500 | 95.00 |

Additional results: `Recall@100 = 1.00`, mean first-gold rank `3.74`, median
first-gold rank `1`, and 5 queries failed to retrieve the gold chunk in the
top 20. The run took about 208.8 seconds. These formulas match ViRE, but this
is the prepared 297/100 subset rather than the complete paper benchmark.

## Planned extensions

The current result is deliberately a clean retrieval baseline. The next
experiments are kept separate from it:

- Compare the stored Qwen embedding branches and additional embedding models.
- Add TF-IDF/BM25 and other full-text or sparse retrieval baselines.
- Compare Qdrant fusion choices and standalone dense/sparse search.
- Connect the external query-processing pipeline while keeping it switchable.
- Generate and evaluate BGE/Qwen cross-encoder reranking scores after candidate retrieval.

Until those experiments are run, the reported baseline remains BGE-M3 hybrid
RRF without query processing or reranking.

## Qdrant point shape

Qdrant stores each item as a point with an ID, named vectors, and a JSON payload. The script stores embeddings as vectors, not duplicated in the payload:

```text
Point {
  id: UUID derived stably from document_id + chunk_id,
  vector: {
    bge_m3_dense: float[1024],
    bge_m3_sparse: { indices: int[], values: float[] },
    qwen_0_6b_dense: float[1024],
    qwen_4b_dense: float[2560]
  },
  payload: {
    chunk_id: "doc-a-0001",
    document_id: "doc-a",
    chunk_index: 0,
    text: "Chunk content...",
    title: "Document title",
    page_start: 1,
    page_end: 1,
    source_url: "https://example.org/document.pdf"
  }
}
```

Keep fields needed to show citations or filter results in the payload. A useful starting set is `chunk_id`, `document_id`, `chunk_index`, `text`, `title`, `page_start`, `page_end`, `source_url`, and any domain filters such as `product`, `document_type`, or `version`. Extra metadata fields are accepted and flattened into the payload.

## Qdrant UI

The local Qdrant image includes a built-in dashboard. After starting the
service, open:

```text
http://localhost:6333/dashboard
```

It lets you inspect collections, payloads, vectors, and run searches. No separate UI container is needed.

