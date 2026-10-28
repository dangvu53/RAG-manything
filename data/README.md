# Local data layout

- `benchmark_datasets/`: 17 files copied from the ViRE benchmark repository, excluding `mock`.
- `virhe4qa_subset/`: the prepared ViRHE4QA subset with 297 unique contexts and 100 queries.
- `kaggle_artifacts/`: downloaded embeddings, manifests, reranker scores, and timing logs.
- `../retrieval_runs/`: generated Qdrant rankings and metric reports.

The source files under `ViRE/data` remain unchanged. Kaggle artifacts are kept
separate from source datasets so model outputs can be replaced safely.

## Why this directory is tracked

This `data/` tree is part of the reproducibility surface of the repository, not
just a local cache. It is intentionally not ignored by `.gitignore`, so the
benchmark copies, the 297-context/100-query subset, Kaggle embeddings, and
retrieval reports can be pushed together with the code. New experiments should
use a new subdirectory under `retrieval_runs/` and keep the input artifacts
that produced the report.

The current snapshot is about 930 MB across 210 files, including generated
retrieval rankings and query-processing experiments. Check individual file
limits before adding larger model artifacts; use Git LFS for files that exceed
the hosting provider's limit.
