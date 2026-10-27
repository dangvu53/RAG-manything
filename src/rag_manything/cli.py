import argparse
import sys
from pathlib import Path

from pydantic import ValidationError

from rag_manything.answer.client import QwenError
from rag_manything.answer.service import AnswerService
from rag_manything.config import Settings
from rag_manything.models import AnswerRequest


def main() -> int:
    parser = argparse.ArgumentParser(description="Answer a question using retrieved chunks")
    parser.add_argument("request", type=Path, help="UTF-8 JSON with question and chunks")
    args = parser.parse_args()
    try:
        request = AnswerRequest.model_validate_json(args.request.read_text(encoding="utf-8"))
        settings = Settings()
        with AnswerService(settings) as service:
            result = service.answer(request.question, request.chunks)
        print(result.model_dump_json(indent=2))
        return 0
    except ValidationError as exc:
        # Avoid echoing chunks or secret environment values in validation errors.
        fields = ", ".join(".".join(map(str, e["loc"])) for e in exc.errors())
        print(f"Invalid request or configuration. Check fields: {fields}", file=sys.stderr)
    except QwenError as exc:
        print(str(exc), file=sys.stderr)
    except (OSError, ValueError):
        print("Cannot read request or invalid chunk IDs (including duplicates).", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
