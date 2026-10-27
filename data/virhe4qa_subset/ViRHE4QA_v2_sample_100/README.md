# ViRHE4QA sample (100 rows)

- Source: `../../ViRHE4QA_v2.csv`.
- The CSV preserves the original seven columns and their names.
- Sampling: 100 rows with distinct contexts, fixed seed 42; one QA row selected per context.
- Source split counts in this smoke-test sample: {'test': 5, 'train': 91, 'val': 4}.
- The sample spans the original train/validation/test splits, so use it for pipeline smoke-testing only, not as a held-out benchmark result.
- For retrieval, use `question` as query and `context` as the paired candidate chunk. Use only `context` for document embeddings; keep answer fields as references.
- The source dataset is published for research use; follow the upstream terms when using or sharing it.
