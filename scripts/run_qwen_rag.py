"""Run one Qwen dense retrieval and answer request through the Kaggle API."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


def post_json(
    url: str,
    payload: dict[str, Any],
    *,
    headers: dict[str, str] | None = None,
    timeout: float,
) -> dict[str, Any]:
    request_headers = {"Content-Type": "application/json"}
    if headers:
        request_headers.update(headers)
    request = Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=request_headers,
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"POST {url} returned HTTP {exc.code}: {detail[:800]}") from exc
    except URLError as exc:
        raise RuntimeError(f"Could not reach {url}: {exc.reason}") from exc


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    default_collection = os.getenv(
        "QWEN_QDRANT_COLLECTION", "virhe4qa_qwen_api_30_fdd19f"
    )
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question", help="Question to retrieve context for and answer")
    parser.add_argument("--collection", default=default_collection)
    parser.add_argument("--qdrant-url", default=os.getenv("QDRANT_URL", "http://localhost:6333"))
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--max-new-tokens", type=int, default=512)
    parser.add_argument("--timeout", type=float, default=600)
    parser.add_argument("--output", type=Path, help="Optional path to save the full JSON result")
    args = parser.parse_args()
    if args.top_k < 1 or args.max_new_tokens < 1 or args.timeout <= 0:
        parser.error("top-k, max-new-tokens, and timeout must be positive")

    api_url = os.getenv("RAG_API_URL", "").rstrip("/")
    api_key = os.getenv("RAG_API_KEY", "")
    if not api_url or not api_key:
        parser.error("Set RAG_API_URL and RAG_API_KEY in RAG-manything/.env")

    auth_headers = {"Authorization": f"Bearer {api_key}"}
    qdrant_headers = {}
    qdrant_key = os.getenv("QDRANT_API_KEY", "")
    if qdrant_key:
        qdrant_headers["api-key"] = qdrant_key

    total_started = time.perf_counter()

    started = time.perf_counter()
    embedding_result = post_json(
        f"{api_url}/v1/embeddings",
        {"texts": [args.question], "is_query": True},
        headers=auth_headers,
        timeout=args.timeout,
    )
    embedding_s = time.perf_counter() - started
    vectors = embedding_result.get("embeddings", [])
    if len(vectors) != 1:
        raise RuntimeError("Embedding API did not return exactly one query vector")
    query_vector = vectors[0]

    collection_url = f"{args.qdrant_url.rstrip('/')}/collections/{quote(args.collection, safe='')}/points/query"
    started = time.perf_counter()
    search_result = post_json(
        collection_url,
        {"query": query_vector, "limit": args.top_k, "with_payload": True},
        headers=qdrant_headers,
        timeout=args.timeout,
    )
    search_s = time.perf_counter() - started
    points = search_result.get("result", {}).get("points", [])
    if not points:
        raise RuntimeError(f"Qdrant returned no hits from collection {args.collection!r}")

    contexts = [str(point.get("payload", {}).get("text", "")) for point in points]
    if any(not context.strip() for context in contexts):
        raise RuntimeError("A retrieved Qdrant point has no non-empty payload.text")

    started = time.perf_counter()
    answer_result = post_json(
        f"{api_url}/v1/answer",
        {
            "question": args.question,
            "contexts": contexts,
            "max_new_tokens": args.max_new_tokens,
        },
        headers=auth_headers,
        timeout=args.timeout,
    )
    answer_s = time.perf_counter() - started

    result = {
        "question": args.question,
        "collection": args.collection,
        "retrieval_mode": "Qwen dense cosine",
        "top_k": args.top_k,
        "hits": [
            {
                "rank": rank,
                "point_id": point.get("id"),
                "score": point.get("score"),
                "payload": point.get("payload", {}),
            }
            for rank, point in enumerate(points, start=1)
        ],
        "answer": answer_result.get("answer", ""),
        "timings_s": {
            "query_embedding_api": round(embedding_s, 4),
            "qdrant_search": round(search_s, 4),
            "answer_api": round(answer_s, 4),
            "end_to_end": round(time.perf_counter() - total_started, 4),
        },
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        output_path = args.output if args.output.is_absolute() else Path.cwd() / args.output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered + "\n", encoding="utf-8")
        print(f"Saved result: {output_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
