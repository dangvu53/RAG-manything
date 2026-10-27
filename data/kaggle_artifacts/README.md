# Kaggle artifacts

The current output is under `virhe4qa_model_sweep/`. It contains BGE-M3 and
Qwen embedding files, manifests, and the 29,700-pair reranker manifest.

The current download does not yet contain reranker score matrices or timing
logs. The ingestion command expects `chunks_manifest.csv`, dense `.npy` files,
and `bge_m3_sparse.jsonl` in the model-sweep directory.
