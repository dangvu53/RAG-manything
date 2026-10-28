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

## Reranker evaluation

The `reranking/` directory evaluates the three precomputed Kaggle rerankers
on the top 100 candidates from both the BGE-M3 hybrid baseline and the best
BM25+Qwen-4B candidate pipeline. All six runs contain the full per-query
rankings, metrics, and `run_config.json`.

| Candidate set | Reranker | P@1 | R@3 | R@10 | MRR@10 |
| --- | --- | ---: | ---: | ---: | ---: |
| BGE-M3 hybrid RRF | BGE-Reranker-v2-M3 | 85% | 93% | 98% | 89.51% |
| BGE-M3 hybrid RRF | Qwen3-Reranker-0.6B | 80% | 94% | 98% | 87.34% |
| BGE-M3 hybrid RRF | Qwen3-Reranker-4B | **86%** | **99%** | **100%** | **92.27%** |
| BM25+Qwen-4B RRF | BGE-Reranker-v2-M3 | 85% | 93% | 99% | 89.61% |
| BM25+Qwen-4B RRF | Qwen3-Reranker-0.6B | 80% | 94% | 98% | 87.34% |
| BM25+Qwen-4B RRF | Qwen3-Reranker-4B | **86%** | **99%** | **100%** | **92.27%** |

The reranker score itself was generated on Kaggle for all 29,700 pairs. The
run configs also estimate the model time for 10,000 pairs (100 queries x top
100 candidates) by linear scaling; this estimate is not a new inference run.
Approximate load-plus-score times are BGE `574.6 s`, Qwen-0.6B `1,361.1 s`,
and Qwen-4B `3,997.7 s`.

## Query processing experiments

`query_processing/` contains the stopword-cleaning experiment on the original
100-query set and a separate BGE-M3 experiment on ViHERMES, whose 1,561
questions have hop levels 1-5 and 998 contexts.

On the original 100 queries, removing high-confidence stopwords reduced the
BGE dense/sparse/hybrid results, so cleaning is not the default. On ViHERMES,
naive decomposition alone also reduced ranking quality because the generated
subqueries introduced noise. A soft fusion anchored by the original query,
`full_dense + max(subquery_dense)`, improved multi-hop retrieval:

| Strategy | HitRate@1 | Recall@3 | Recall@10 | Recall@20 | MRR@10 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Full query BGE-M3 | 66.11% | 50.19% | 69.81% | 78.46% | 75.80% |
| Full + decomposed max | **68.42%** | **51.36%** | **71.91%** | **80.89%** | **77.40%** |
| Decomposed RRF only | 40.23% | 34.86% | 53.01% | 65.78% | 52.89% |

The ViHERMES encoder output and rankings are stored under
`query_processing/vihermes_bge_m3/`; the fused run is under
`query_processing/vihermes_bge_m3_full_plus_decomposition/`. The experiment
uses BGE-M3 dense embeddings for both contexts and queries and keeps the
decomposition heuristic explicit, so it is a comparison rather than a change
to the 100-query baseline. A deterministic 80/20 check selected `alpha=1.0`
on the training portion; on the 313-query holdout, full-query fusion improved
`Recall@10` from 67.48% to 70.91% and `Recall@20` from 77.26% to 80.19%.

Future dense, sparse, TF-IDF/BM25, fusion, query-processing, or reranking
experiments should use distinct run names and retain their outputs here.
