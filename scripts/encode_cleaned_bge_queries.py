"""Encode stopword-cleaned queries with BGE-M3 dense and sparse outputs."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))
if str(PROJECT_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from analyze_query_tokens import HIGH_CONFIDENCE_STOPWORDS, tokenize  # noqa: E402


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = [dict(row) for row in csv.DictReader(stream)]
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def clean_query(query: str) -> str:
    cleaned = [token for token in tokenize(query) if token not in HIGH_CONFIDENCE_STOPWORDS]
    if not cleaned:
        raise ValueError(f"Stopword cleaning removed the complete query: {query!r}")
    return " ".join(cleaned)


def sparse_rows(values: Any) -> list[dict[str, list[float] | list[int]]]:
    rows = []
    for value in values:
        mapping = dict(value)
        rows.append(
            {
                "indices": [int(key) for key in mapping],
                "values": [float(weight) for weight in mapping.values()],
            }
        )
    return rows


def encode_with_onnx(
    texts: list[str],
    model_dir: Path,
    tokenizer_dir: Path,
    batch_size: int,
    max_length: int,
) -> tuple[np.ndarray, list[dict[str, list[float] | list[int]]], float, float]:
    """Encode BGE-M3 queries without downloading the larger PyTorch checkpoint."""
    import onnxruntime as ort  # noqa: PLC0415
    import torch  # noqa: PLC0415
    from transformers import AutoTokenizer  # noqa: PLC0415

    model_started = time.perf_counter()
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_dir, local_files_only=True)
    session = ort.InferenceSession(
        str(model_dir / "model.onnx"),
        providers=["CPUExecutionProvider"],
    )
    sparse_state = torch.load(
        tokenizer_dir / "sparse_linear.pt", map_location="cpu", weights_only=False
    )
    sparse_weight = sparse_state["weight"].numpy().T
    sparse_bias = sparse_state["bias"].numpy()
    special_ids = {
        int(tokenizer.convert_tokens_to_ids(tokenizer.special_tokens_map[name]))
        for name in ("cls_token", "eos_token", "pad_token", "unk_token")
        if name in tokenizer.special_tokens_map
    }
    model_load_seconds = time.perf_counter() - model_started

    dense_batches: list[np.ndarray] = []
    sparse: list[dict[str, list[float] | list[int]]] = []
    encode_started = time.perf_counter()
    for start in range(0, len(texts), batch_size):
        encoded = tokenizer(
            texts[start : start + batch_size],
            truncation=True,
            max_length=max_length,
            padding=True,
            return_tensors="np",
        )
        token_embeddings, sentence_embeddings = session.run(
            ["token_embeddings", "sentence_embedding"],
            {
                "input_ids": encoded["input_ids"].astype(np.int64),
                "attention_mask": encoded["attention_mask"].astype(np.int64),
            },
        )
        dense_batches.append(np.asarray(sentence_embeddings, dtype=np.float32))
        token_weights = np.maximum(
            np.matmul(token_embeddings, sparse_weight) + sparse_bias, 0
        ).squeeze(-1)
        for weights, token_ids, mask in zip(
            token_weights, encoded["input_ids"], encoded["attention_mask"], strict=True
        ):
            row: dict[int, float] = {}
            for weight, token_id, active in zip(weights, token_ids, mask, strict=True):
                token_id = int(token_id)
                if not active or token_id in special_ids or weight <= 0:
                    continue
                row[token_id] = max(row.get(token_id, 0.0), float(weight))
            sparse.append(
                {
                    "indices": list(row),
                    "values": list(row.values()),
                }
            )
    encode_seconds = time.perf_counter() - encode_started
    return np.concatenate(dense_batches, axis=0), sparse, model_load_seconds, encode_seconds


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--artifacts-dir",
        type=Path,
        default=PROJECT_ROOT / "data/kaggle_artifacts/virhe4qa_model_sweep",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "data/retrieval_runs/query_processing/bge_m3_cleaned_stopwords",
    )
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument(
        "--onnx-model-dir",
        type=Path,
        help="Use a local BGE-M3 ONNX model directory instead of FlagEmbedding.",
    )
    parser.add_argument(
        "--tokenizer-dir",
        type=Path,
        help="Local BGE-M3 snapshot containing tokenizer files and sparse_linear.pt.",
    )
    args = parser.parse_args()

    if args.batch_size < 1 or args.max_length < 1:
        parser.error("batch-size and max-length must be positive")

    artifacts_dir = args.artifacts_dir.resolve()
    query_rows = read_rows(artifacts_dir / "queries_manifest.csv")
    cleaned_rows: list[dict[str, str]] = []
    for row in query_rows:
        item = dict(row)
        item["processed_question"] = clean_query(row["question"])
        cleaned_rows.append(item)

    if bool(args.onnx_model_dir) != bool(args.tokenizer_dir):
        parser.error("onnx-model-dir and tokenizer-dir must be supplied together")
    if args.onnx_model_dir:
        dense, sparse, model_load_seconds, encode_seconds = encode_with_onnx(
            [row["processed_question"] for row in cleaned_rows],
            args.onnx_model_dir.resolve(),
            args.tokenizer_dir.resolve(),
            args.batch_size,
            args.max_length,
        )
    else:
        from FlagEmbedding import BGEM3FlagModel  # noqa: PLC0415

        model_started = time.perf_counter()
        model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=args.fp16)
        model_load_seconds = time.perf_counter() - model_started
        encode_started = time.perf_counter()
        encoded = model.encode(
            [row["processed_question"] for row in cleaned_rows],
            batch_size=args.batch_size,
            max_length=args.max_length,
            return_dense=True,
            return_sparse=True,
            return_colbert_vecs=False,
        )
        dense = np.asarray(encoded["dense_vecs"], dtype=np.float32)
        sparse = sparse_rows(encoded["lexical_weights"])
        encode_seconds = time.perf_counter() - encode_started
    if dense.shape[0] != len(cleaned_rows) or len(sparse) != len(cleaned_rows):
        raise ValueError("Encoded query count does not match query manifest")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    np.save(output_dir / "bge_m3_query_dense.npy", dense)
    with (output_dir / "bge_m3_query_sparse.jsonl").open("w", encoding="utf-8") as stream:
        for row, vector in zip(cleaned_rows, sparse, strict=True):
            stream.write(
                json.dumps(
                    {
                        "id": row["query_id"],
                        "indices": vector["indices"],
                        "values": vector["values"],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
    with (output_dir / "queries_manifest.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as stream:
        writer = csv.DictWriter(stream, fieldnames=list(cleaned_rows[0]))
        writer.writeheader()
        writer.writerows(cleaned_rows)
    with (output_dir / "cleaned_queries.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=["query_id", "question", "processed_question"],
        )
        writer.writeheader()
        writer.writerows(
            {
                "query_id": row["query_id"],
                "question": row["question"],
                "processed_question": row["processed_question"],
            }
            for row in cleaned_rows
        )
    (output_dir / "encoding_config.json").write_text(
        json.dumps(
            {
                "model": "BAAI/bge-m3",
                "cleaning": "remove_high_confidence_stopwords",
                "stopword_count": len(HIGH_CONFIDENCE_STOPWORDS),
                "query_count": len(cleaned_rows),
                "dense_shape": list(dense.shape),
                "batch_size": args.batch_size,
                "max_length": args.max_length,
                "fp16": args.fp16,
                "backend": "onnxruntime" if args.onnx_model_dir else "FlagEmbedding",
                "onnx_model_dir": str(args.onnx_model_dir.resolve())
                if args.onnx_model_dir
                else None,
                "model_load_seconds": model_load_seconds,
                "encode_seconds": encode_seconds,
                "average_query_encode_seconds": encode_seconds / len(cleaned_rows),
                "source_artifacts_dir": str(artifacts_dir),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote cleaned query artifacts to {output_dir}")
    print(f"Model load: {model_load_seconds:.3f}s")
    print(f"Encoding: {encode_seconds:.3f}s ({encode_seconds / len(cleaned_rows):.4f}s/query)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
