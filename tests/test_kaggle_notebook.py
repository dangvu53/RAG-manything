import ast
import json
from pathlib import Path

from fastapi.testclient import TestClient


def notebook_cells():
    return json.loads(
        Path("notebooks/qwen3_4b_api_kaggle.ipynb").read_text(encoding="utf-8")
    )["cells"]


def test_notebook_python_cells_compile():
    for cell in notebook_cells():
        if cell["cell_type"] == "code" and "install" not in cell["metadata"].get("tags", []):
            ast.parse("".join(cell["source"]))


def api_factory():
    namespace = {"__name__": "kaggle_api_test"}
    cell = next(c for c in notebook_cells() if "api" in c["metadata"].get("tags", []))
    exec(compile("".join(cell["source"]), "kaggle_api", "exec"), namespace)
    return namespace["create_app"]


def test_api_authentication_and_generate_contract():
    calls = []

    def generator(prompt, max_new_tokens, temperature):
        calls.append((prompt, max_new_tokens, temperature))
        return "Answer [doc-01]"

    with TestClient(api_factory()(generator, "test-token")) as client:
        assert client.get("/health").status_code == 401
        assert client.post("/generate", json={"prompt": "secret"}).status_code == 401
        headers = {"Authorization": "Bearer wrong-token"}
        assert client.get("/health", headers=headers).status_code == 401
        assert not calls
        headers = {"Authorization": "Bearer test-token"}
        assert client.get("/health", headers=headers).json()["status"] == "ok"
        response = client.post("/generate", headers=headers, json={"prompt": "prompt"})
        assert response.json() == {"text": "Answer [doc-01]", "model": "Qwen/Qwen3-4B"}
        assert calls == [("prompt", 1024, 0.1)]
        assert client.post("/generate", headers=headers, json={"prompt": ""}).status_code == 422
        assert client.post("/generate", headers=headers, json={
            "prompt": "prompt", "max_new_tokens": 99999,
        }).status_code == 422


def test_generation_failure_does_not_leak_content_and_releases_lock():
    def generator(*_):
        raise RuntimeError("secret input or API token")

    with TestClient(api_factory()(generator, "test-token")) as client:
        for _ in range(2):
            response = client.post("/generate", headers={"Authorization": "Bearer test-token"},
                                   json={"prompt": "q"})
            assert response.status_code == 503
            assert "secret" not in response.text
