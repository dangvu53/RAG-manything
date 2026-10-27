# Retrieval runs

Each subdirectory is one reproducible retrieval experiment. The current run is
`bge_m3_hybrid_rrf_100/`.

## Current baseline

```text
297 context chunks
100 prepared queries
BGE-M3 dense + BGE-M3 sparse
Qdrant Prefetch + FusionQuery(RRF)
query processing: disabled
reranking: disabled
```

Headline metrics from the current run:

```text
P@1       62.00%
R@10      91.00%
MRR@10    72.58%
nDCG@10   77.12%
R@20      95.00%
```

Important files in a run directory:

- `metrics.json` / `metrics.csv`: aggregate metric values.
- `ranks.csv`: first gold-chunk rank per query.
- `retrieved_results.csv` / `retrieved_results.jsonl`: retrieved rankings and payload text.
- `errors/fail@20.csv`: top-20 failures.
- `run_config.json`: search mode, fusion, cutoffs, timing, and artifact paths.

Future dense, sparse, TF-IDF/BM25, fusion, query-processing, or reranking
experiments should use distinct run names and retain their outputs here.
