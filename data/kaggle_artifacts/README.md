# Kaggle artifacts

The original model sweep is under `virhe4qa_model_sweep/`. The complete
download is available as `virhe4qa_model_sweep_full.zip` and is also extracted
under `virhe4qa_model_sweep_full/` for offline evaluation.

The complete artifact contains:

- BGE-M3 dense and sparse document/query vectors.
- Qwen3-Embedding-0.6B and Qwen3-Embedding-4B dense document/query vectors.
- BGE-Reranker-v2-M3, Qwen3-Reranker-0.6B, and Qwen3-Reranker-4B score matrices
  for all `100 x 297 = 29,700` query/chunk pairs.
- `reranker_pair_manifest.csv`, which defines the score-matrix row/column
  order.
- `model_timings.csv` and `model_timings.json`, including model load time,
  embedding time, reranker pair-scoring time, throughput, and total measured
  time.

The Kaggle timing log reports the following full-matrix reranker workloads:

| Model | Pairs | Score time | Pairs/sec | Total measured time |
| --- | ---: | ---: | ---: | ---: |
| BGE-Reranker-v2-M3 | 29,700 | 1,654.35 s | 17.95 | 1,671.90 s |
| Qwen3-Reranker-0.6B | 29,700 | 4,008.59 s | 7.41 | 4,020.01 s |
| Qwen3-Reranker-4B | 29,700 | 11,658.57 s | 2.55 | 11,730.85 s |

For ingestion, use the artifact directory containing `chunks_manifest.csv`,
dense `.npy` files, and `bge_m3_sparse.jsonl`. Query vectors and reranker
scores remain offline evaluation artifacts.
