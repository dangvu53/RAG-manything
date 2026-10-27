# ViRHE4QA all unique contexts

- Source: `../../ViRHE4QA_v2.csv`.
- Source rows: 1000; unique normalized contexts: 297.
- The CSV preserves the original seven columns and names.
- One deterministic representative QA row is retained for each normalized context.
- The representative is selected by the smallest source `index`, then `split`, then `question`.
- Representative source split counts: {'test': 15, 'train': 263, 'val': 19}.
- The `context` column is the chunk text used by the Kaggle embedding notebook.
- `queries_100.csv` contains 100 distinct question-context pairs from the existing smoke-test sample; its `question` column is used for query embeddings and its `context` column maps each query to a gold chunk.
- This is a prepared embedding input, not a held-out evaluation split.
