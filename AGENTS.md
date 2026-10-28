# AGENTS.md

## Scope

These instructions apply to the RAG-manything repository. The repository is the retrieval component of the larger workspace at `D:\AI Engineer Fresher - TPBank`.

## Environment

- Use the shared workspace environment: `D:\AI Engineer Fresher - TPBank\.venv`.
- From the workspace root, run Python as `.\.venv\Scripts\python.exe`.
- From this repository, run Python as `..\.venv\Scripts\python.exe`.
- Do not create a second `.venv` inside this repository unless the shared environment is unavailable.
- Install this package in editable mode with `python -m pip install -e .` when imports are not available.

## Project map

- `src/rag_manything/retrieval/`: retrieval contracts, query adapters, Qdrant wrapper, hybrid search, reranking, and pipeline.
- `scripts/ingest_kaggle_artifacts.py`: ingest document vectors into Qdrant.
- `scripts/search_bge_m3.py`: interactive or fixed-query BGE-M3 hybrid search.
- `scripts/evaluate_qdrant_retrieval.py`: batch retrieval and ViRE-style metrics.
- `scripts/evaluate_rerankers.py`: evaluate saved Kaggle reranker matrices on
  top-k retrieval candidates.
- `scripts/evaluate_vihermes_query_processing.py`: local BGE-M3 full-query and
  decomposition benchmark on multi-hop ViHERMES.
- `scripts/tune_vihermes_query_fusion.py`: tune full-query/decomposition fusion
  without re-encoding the dataset.
- `notebooks/retrieval_model_sweep_kaggle.ipynb`: model artifact generation on Kaggle.
- `data/benchmark_datasets/`: copied benchmark source data.
- `data/virhe4qa_subset/`: the 297-context/100-query evaluation subset.
- `data/kaggle_artifacts/`: downloaded Kaggle outputs.
- `data/retrieval_runs/`: generated experiment outputs.

## Retrieval contract

The current default baseline uses collection `virhe4qa_297` and these named vectors:

```text
bge_m3_dense       size 1024, cosine
bge_m3_sparse      Qdrant sparse vector
qwen_0_6b_dense    size 1024, cosine
qwen_4b_dense      size 2560, cosine
```

BGE-M3 hybrid retrieval is implemented by Qdrant itself:

1. Create a dense `Prefetch` using `bge_m3_dense`.
2. Create a sparse `Prefetch` using `bge_m3_sparse`.
3. Send both to Qdrant with `FusionQuery(fusion=Fusion.RRF)`.

Do not replace this with a client-side score sum unless the experiment explicitly compares a different fusion method. The runtime config also supports `dbsf`, dense-only, and sparse-only experiments.

`search_mode="hybrid"` and `fusion="rrf"` are the defaults. Keep hybrid RRF as
the default behavior; use explicit CLI/configuration overrides for comparison
runs only.

Query processing and reranking are optional injected stages. Neither is active in the current baseline. Rerankers run outside Qdrant after candidate search.

## Data and evaluation rules

- Keep `chunk_id` and `query_id` stable; Kaggle arrays and JSONL vectors are row/ID aligned with the manifests.
- `chunks_manifest.csv` has 297 rows and `queries_manifest.csv` has 100 rows.
- `gold_chunk_id` is the single positive relevance label for each prepared query.
- The current headline metrics are `P@1`, `R@10`, `MRR@10`, `nDCG@10`, and `R@20`.
- Metric values are stored in the `[0, 1]` range; report percentages only when presenting results as percentages.
- `reranker_pair_manifest.csv` lists 29,700 pairs; it is not a score file.
- `data/kaggle_artifacts/virhe4qa_model_sweep_full.zip` contains the three
  reranker score matrices and `model_timings.csv/json`; its extracted sibling
  is used for offline evaluation.
- Do not mix document vectors from one manifest/version with query vectors from another.
- The complete `data/` directory is intentionally versioned and should not be added back to `.gitignore`.
- Put new experiment outputs in a distinct directory under `data/retrieval_runs/`.

## Standard commands

From the workspace root:

```powershell
docker compose -f .\RAG-manything\docker-compose.yml up -d qdrant

.\.venv\Scripts\python.exe .\RAG-manything\scripts\ingest_kaggle_artifacts.py `
  .\RAG-manything\data\kaggle_artifacts\virhe4qa_model_sweep `
  --collection virhe4qa_297 --batch-size 32 --recreate

.\.venv\Scripts\python.exe .\RAG-manything\scripts\search_bge_m3.py `
  --query-id query_001 --collection virhe4qa_297 --limit 8

.\.venv\Scripts\python.exe .\RAG-manything\scripts\evaluate_qdrant_retrieval.py `
  --collection virhe4qa_297 --mode hybrid --fusion rrf `
  --ks 1,3,5,10,20,50,100 --prefetch-limit 100 `
  --run-name bge_m3_hybrid_rrf_100
```

`--recreate` is destructive for the named collection only. Confirm the target collection before using it. The Qdrant dashboard is at `http://localhost:6333/dashboard`.

## Planned work

The current baseline is intentionally limited to BGE-M3 hybrid RRF. Completed
follow-up runs include Qwen/BM25 comparisons, all three saved rerankers, and a
ViHERMES query-processing benchmark. Further experiments may add TF-IDF or
other full-text search, alternative Qdrant fusion/search modes, and the
external query processor. Keep those switches explicit and preserve the
baseline run for comparison.

## Validation

Run the unit tests and syntax checks before handing off changes:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s .\RAG-manything\tests -v
.\.venv\Scripts\python.exe -m compileall -q .\RAG-manything\src .\RAG-manything\scripts
```

For retrieval changes, also run a Qdrant smoke query and verify the target collection point count. Do not delete existing Qdrant collections or source datasets as part of a test.

## Change guidelines

- Preserve existing user data and unrelated worktree changes.
- Use `apply_patch` for source and documentation edits.
- Keep model downloads and generated artifacts out of source code.
- Prefer named-vector schema changes with a new collection or an explicit migration; do not silently reinterpret an existing vector name.
- Update `README.md` when commands, data paths, schema, baseline behavior, or reported metrics change.
- Update the relevant `data/README.md` or `data/retrieval_runs/README.md` when tracked artifacts or experiment outputs change.
- Keep comments short and explain only non-obvious behavior.
