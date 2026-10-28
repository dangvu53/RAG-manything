"""Analyze token and question-template frequencies for the prepared queries."""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARTIFACTS = PROJECT_ROOT / "data/kaggle_artifacts/virhe4qa_model_sweep"
DEFAULT_OUTPUT = PROJECT_ROOT / "data/retrieval_runs/query_processing"
TOKEN_PATTERN = re.compile(r"[^\W_]+", flags=re.UNICODE)
DECODE_TRANSLATION = str.maketrans({chr(273): "d", chr(272): "D"})


def decode_words(raw: str) -> set[str]:
    return {bytes(value, "ascii").decode("unicode_escape") for value in raw.split()}


HIGH_CONFIDENCE_STOPWORDS = decode_words(
    r"""c\u00e1c c\u1ee7a v\u00e0 v\u1edbi cho trong t\u1eeb v\u1ec1 theo th\u00ec l\u00e0 nh\u1eefng m\u1ed9t m\u1ed7i \u0111\u00e3 \u0111ang \u0111\u1ec3 \u0111\u1ebfn ra sau s\u1ebd t\u1ea1i v\u00e0o khi qua r\u1ea5t l\u1ea1i c\u0169ng c\u00f9ng n\u00ean nh\u01b0 n\u1ebfu"""
)
FUNCTION_CANDIDATES = HIGH_CONFIDENCE_STOPWORDS | decode_words(
    r"""ai bao ch\u1ec9 c\u00f3 g\u00ec kh\u00f4ng \u0111\u01b0\u1ee3c b\u1ecb n\u00e0o n\u00e0y m\u00e0"""
)


def tokenize(text: str) -> list[str]:
    return TOKEN_PATTERN.findall(unicodedata.normalize("NFC", text).lower())


def normalized(text: str) -> str:
    text = text.translate(DECODE_TRANSLATION)
    return "".join(
        character
        for character in unicodedata.normalize("NFD", text)
        if unicodedata.category(character) != "Mn"
    ).lower()


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifacts-dir", type=Path, default=DEFAULT_ARTIFACTS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    query_path = args.artifacts_dir.resolve() / "queries_manifest.csv"
    with query_path.open("r", encoding="utf-8-sig", newline="") as stream:
        queries = list(csv.DictReader(stream))
    if not queries:
        raise ValueError(f"No queries found in {query_path}")

    token_frequency: Counter[str] = Counter()
    query_frequency: Counter[str] = Counter()
    high_stop_frequency: Counter[str] = Counter()
    candidate_frequency: Counter[str] = Counter()
    query_stats: list[dict[str, object]] = []
    cleaned_queries: list[dict[str, str]] = []

    for query in queries:
        tokens = tokenize(query["question"])
        token_frequency.update(tokens)
        query_frequency.update(set(tokens))
        high_stops = [token for token in tokens if token in HIGH_CONFIDENCE_STOPWORDS]
        candidates = [token for token in tokens if token in FUNCTION_CANDIDATES]
        high_stop_frequency.update(high_stops)
        candidate_frequency.update(candidates)
        cleaned_queries.append(
            {
                "query_id": query["query_id"],
                "question": query["question"],
                "cleaned_question": " ".join(
                    token for token in tokens if token not in HIGH_CONFIDENCE_STOPWORDS
                ),
            }
        )
        query_stats.append(
            {
                "query_id": query["query_id"],
                "question": query["question"],
                "total_tokens": len(tokens),
                "high_confidence_stop_tokens": len(high_stops),
                "function_candidate_tokens": len(candidates),
                "high_confidence_stop_ratio": len(high_stops) / len(tokens),
                "function_candidate_ratio": len(candidates) / len(tokens),
            }
        )

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(
        output_dir / "query_token_frequencies.csv",
        ["token", "term_frequency", "query_frequency", "category"],
        [
            {
                "token": token,
                "term_frequency": count,
                "query_frequency": query_frequency[token],
                "category": (
                    "high_confidence_stopword"
                    if token in HIGH_CONFIDENCE_STOPWORDS
                    else "function_or_question_candidate"
                    if token in FUNCTION_CANDIDATES
                    else "content_or_domain_token"
                ),
            }
            for token, count in sorted(
                token_frequency.items(), key=lambda item: (-item[1], item[0])
            )
        ],
    )
    write_csv(
        output_dir / "query_token_stats.csv",
        [
            "query_id",
            "question",
            "total_tokens",
            "high_confidence_stop_tokens",
            "function_candidate_tokens",
            "high_confidence_stop_ratio",
            "function_candidate_ratio",
        ],
        query_stats,
    )
    write_csv(
        output_dir / "cleaned_queries.csv",
        ["query_id", "question", "cleaned_question"],
        cleaned_queries,
    )

    total_tokens = sum(token_frequency.values())
    total_high_stops = sum(high_stop_frequency.values())
    total_candidates = sum(candidate_frequency.values())
    phrase_patterns = {
        "co_any_khong": r"\bco\b.*\bkhong\b",
        "co_the_khong": r"co the.*khong",
        "co_kha_nang_khong": r"co kha nang khong",
        "nhu_the_nao": r"nhu the nao\s*\??$",
        "la_gi": r"la gi\s*\??$",
        "bao_nhieu": r"bao nhieu",
        "o_dau": r" o dau\s*\??$",
        "ai_at_start": r"^ai\b",
        "neu_at_start": r"^neu\b",
        "doi_voi": r"doi voi",
        "truong_hop": r"truong hop",
        "noi_dung": r"noi dung",
        "dieu_number": r"dieu\s+\d+",
    }
    normalized_questions = [normalized(query["question"]) for query in queries]

    lines = [
        "# Query Token Statistics",
        "",
        f"Source: `{query_path}`",
        "",
        "## Summary",
        "",
        f"- Queries: **{len(queries)}**",
        f"- Total tokens: **{total_tokens}**",
        f"- Unique tokens: **{len(token_frequency)}**",
        f"- Average query length: **{total_tokens / len(queries):.2f} tokens**",
        f"- High-confidence removable stopword candidates: **{total_high_stops} ({total_high_stops / total_tokens:.2%})**",
        f"- Broad function/question candidates: **{total_candidates} ({total_candidates / total_tokens:.2%})**",
        "",
        "The broad group includes words such as `có`, `không`, `được`, `ai` and `gì`; these should not be deleted blindly because they carry modality, polarity or question intent.",
        "",
        "## Frequent Tokens",
        "",
        "| Token | Term frequency | Query frequency | Category |",
        "|---|---:|---:|---|",
    ]
    for token, count in token_frequency.most_common(50):
        category = (
            "high-confidence stopword"
            if token in HIGH_CONFIDENCE_STOPWORDS
            else "function/question candidate"
            if token in FUNCTION_CANDIDATES
            else "content/domain"
        )
        lines.append(f"| `{token}` | {count} | {query_frequency[token]} | {category} |")

    lines.extend(
        [
            "",
            "## Question Templates",
            "",
            "| Pattern | Query count |",
            "|---|---:|",
        ]
    )
    for name, pattern in phrase_patterns.items():
        count = sum(bool(re.search(pattern, question)) for question in normalized_questions)
        lines.append(f"| `{name}` | {count} |")

    lines.extend(["", "## Highest Stopword Ratios", "", "| Query | Ratio | Question |", "|---|---:|---|"])
    for item in sorted(
        query_stats,
        key=lambda row: (float(row["high_confidence_stop_ratio"]), str(row["query_id"])),
        reverse=True,
    )[:20]:
        question = str(item["question"]).replace("|", "\\|")
        lines.append(
            f"| `{item['query_id']}` | {float(item['high_confidence_stop_ratio']):.2%} | {question} |"
        )

    example = next(
        (query for query in queries if query["query_id"] == "query_044"),
        None,
    )
    if example:
        example_tokens = tokenize(example["question"])
        cleaned = [token for token in example_tokens if token not in HIGH_CONFIDENCE_STOPWORDS]
        lines.extend(
            [
                "",
                "## Example: `query_044`",
                "",
                f"Original: `{example['question']}`",
                "",
                "High-confidence word filtering:",
                "",
                f"`{' '.join(cleaned)}`",
                "",
                "A phrase-level rule can additionally remove the interrogative shell `có khả năng không`, leaving the topic-bearing phrase about members discussing the thesis topic.",
            ]
        )

    report_path = output_dir / "query_token_statistics.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {report_path}")
    print(f"Wrote {output_dir / 'query_token_frequencies.csv'}")
    print(f"Wrote {output_dir / 'query_token_stats.csv'}")
    print(f"Wrote {output_dir / 'cleaned_queries.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
