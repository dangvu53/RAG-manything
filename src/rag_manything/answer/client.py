"""Bearer-authenticated Kaggle /generate client with bounded transient retries."""

import time

import httpx
from pydantic import BaseModel, Field

from rag_manything.config import Settings


class QwenError(RuntimeError):
    """Public error excludes URLs, response bodies and credentials."""


class GenerateResponse(BaseModel):
    text: str = Field(min_length=1)
    model: str = Field(min_length=1)


class QwenClient:
    def __init__(self, settings: Settings, client: httpx.Client | None = None):
        self.settings = settings
        self._client = client or httpx.Client(follow_redirects=False, trust_env=False)
        self._owns_client = client is None

    def generate(self, prompt: str) -> str:
        for attempt in range(self.settings.qwen_max_retries + 1):
            failure = "Qwen request failed"
            retry = False
            try:
                response = self._client.post(
                    str(self.settings.qwen_api_url),
                    headers={
                        "Authorization": f"Bearer {self.settings.qwen_api_token.get_secret_value()}"
                    },
                    json={
                        "prompt": prompt,
                        "max_new_tokens": self.settings.qwen_max_new_tokens,
                        "temperature": self.settings.qwen_temperature,
                    },
                    timeout=self.settings.qwen_timeout_seconds,
                )
                if response.status_code == 429 or response.status_code in {500, 502, 503, 504}:
                    failure, retry = "Qwen temporarily unavailable", True
                elif not 200 <= response.status_code < 300:
                    failure = f"Qwen rejected request (HTTP {response.status_code})"
                else:
                    parsed = GenerateResponse.model_validate(response.json())
                    if not parsed.text.strip() or parsed.model != self.settings.qwen_model:
                        raise ValueError("Unexpected generation response")
                    return parsed.text.strip()
            except (httpx.TimeoutException, httpx.NetworkError):
                failure, retry = "Qwen connection timed out or failed", True
            except ValueError:
                failure = "Qwen returned an invalid response"
            except httpx.HTTPError:
                failure = "Qwen transport failed"
            if not retry or attempt == self.settings.qwen_max_retries:
                # Outside except: traceback chains cannot reveal request data.
                raise QwenError(failure)
            time.sleep(min(0.5 * 2**attempt, 2))
        raise QwenError("Qwen request failed")

    def close(self) -> None:
        if self._owns_client:
            self._client.close()
