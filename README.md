# RAG-manything

Hệ thống Retrieval-Augmented Generation (RAG) cho tiếng Việt, gồm hai khối:

- Retrieval: BGE-M3 dense + sparse search trên Qdrant, hợp nhất bằng RRF và hỗ trợ reranking tùy chọn.
- Prompt/Answer: kiểm tra và viết lại câu hỏi, tạo câu trả lời có citation, kiểm tra output và đánh giá bằng RAGAS.

## Luồng xử lý

~~~text
User question
→ GPT-4o mini: input guardrail + query rewrite
→ BGE-M3 hybrid retrieval trên Qdrant
→ Optional reranking
→ Prompt builder
→ Qwen3-4B: answer generation
→ GPT-5 mini: output guardrail
→ Answer + citations + latency
~~~

Nếu input guardrail phát hiện prompt injection, yêu cầu lấy bí mật hoặc nội dung không hợp lệ,
pipeline dừng trước retrieval và trả: **Câu hỏi của bạn không hợp lệ.**

Hai guardrail có thể bật/tắt độc lập. Khi input guardrail tắt, câu hỏi gốc được dùng cho
retrieval. Khi output guardrail tắt, kiểm tra cấu trúc cục bộ vẫn chặn answer rỗng,
thẻ think và citation không tồn tại.

## Thành phần chính

| Thành phần | Công nghệ | Trạng thái |
| --- | --- | --- |
| Input validation và query rewrite | GPT-4o mini | Đã triển khai |
| Retrieval | BGE-M3 dense + sparse, Qdrant RRF | Đã triển khai |
| Reranking | Adapter BGE/precomputed | Tùy chọn, mặc định tắt |
| Answer generation | Qwen3-4B trên Kaggle | Đã triển khai |
| Output guardrail | GPT-5 mini | Đã triển khai |
| Observability | LangSmith metadata tracing | Tùy chọn |
| Answer evaluation | RAGAS, 4 metric + latency | Đã triển khai |

## Cài đặt

Yêu cầu:

- Python 3.11 trở lên.
- Docker nếu chạy Qdrant local.
- Kaggle GPU và ngrok nếu chạy Qwen3-4B bằng notebook của dự án.
- OpenAI API key khi bật guardrail hoặc chạy RAGAS.

Dự án ưu tiên dùng virtual environment chung của workspace. Sau khi kích hoạt environment,
chạy từ thư mục repository:

~~~powershell
python -m pip install -r requirements.txt
Copy-Item .env.example .env
~~~

## Dữ liệu và artifacts retrieval

- `data/benchmark_datasets/`: benchmark datasets from the ViRE repository, excluding `mock`.
- `data/virhe4qa_subset/`: prepared ViRHE4QA data with 297 unique contexts and 100 queries.
- `data/kaggle_artifacts/virhe4qa_model_sweep/`: embedding output used for Qdrant ingestion.
- `data/kaggle_artifacts/virhe4qa_model_sweep_full.zip`: complete Kaggle output,
  including reranker scores and timing logs.
- `data/retrieval_runs/`: generated retrieval rankings and metric reports.

The current Kaggle directory contains document/query vectors for BGE-M3,
Qwen3-Embedding-0.6B, and Qwen3-Embedding-4B. It also contains the 29,700-pair
reranker manifest. The complete zip also contains BGE-Reranker-v2-M3,
Qwen3-Reranker-0.6B, and Qwen3-Reranker-4B score matrices for all 29,700 pairs,
plus `model_timings.csv/json`.

The complete `data/` directory is intentionally versioned and can be pushed
with this repository. It contains benchmark source copies and the generated
subset/Kaggle/retrieval outputs needed to reproduce the current baseline. The
current snapshot is about 930 MB across 210 files, including generated
retrieval rankings. If a future model artifact exceeds the hosting provider's
per-file limit, store that file with Git LFS instead of ignoring the whole data
directory.

Cài thêm dependencies cho RAGAS:

~~~powershell
python -m pip install -e ".[evaluation]"
~~~

## Cấu hình

Các biến quan trọng trong **.env**:

| Biến | Mặc định/ý nghĩa |
| --- | --- |
| QDRANT_URL | http://localhost:6333 |
| QDRANT_COLLECTION | Collection dùng khi ingestion |
| EMBEDDING_MODEL | BAAI/bge-m3 |
| QWEN_API_URL | HTTPS URL của endpoint /generate |
| QWEN_API_TOKEN | Bearer token của Qwen API |
| QWEN_MODEL | Qwen/Qwen3-4B |
| OPENAI_API_KEY | Bắt buộc khi một guardrail được bật |
| OPENAI_INPUT_GUARDRAIL_MODEL | gpt-4o-mini |
| OPENAI_OUTPUT_GUARDRAIL_MODEL | gpt-5-mini |
| OPENAI_EVAL_MODEL | Model chấm RAGAS |
| INPUT_GUARDRAIL_ENABLED | Bật/tắt kiểm tra input và query rewrite |
| OUTPUT_GUARDRAIL_ENABLED | Bật/tắt kiểm tra output bằng GPT |
| LANGSMITH_TRACING | Mặc định false |

Không commit **.env**, API key hoặc token. Remote Qwen URL phải dùng HTTPS; HTTP chỉ được
chấp nhận cho localhost.

## Khởi động retrieval

Khởi động Qdrant:

~~~powershell
docker compose up -d qdrant
~~~

Dashboard local: http://localhost:6333/dashboard

Nạp các vector đã xuất từ Kaggle:

~~~powershell
python scripts/ingest_kaggle_artifacts.py data/kaggle_artifacts/virhe4qa_model_sweep --collection virhe4qa_297
~~~

Hoặc tạo embedding và ingest một file JSONL/CSV mới:

~~~powershell
python scripts/ingest_chunks.py path/to/chunks.jsonl --collection rag_chunks
~~~

Mỗi chunk cần **chunk_id**, **document_id** và **text**. Metadata như **title**,
**source_url**, **page_start** và **page_end** được lưu trong payload để tạo citation.

## Chạy Qwen3-4B trên Kaggle

Mở [notebook Qwen](notebooks/qwen3_4b_api_kaggle.ipynb), bật GPU và Internet, sau đó
tạo hai Kaggle Secrets:

- QWEN_API_TOKEN: token ngẫu nhiên dài ít nhất 32 ký tự.
- NGROK_AUTHTOKEN: token của tài khoản ngrok.

Notebook thực hiện:

1. Load Qwen/Qwen3-4B và tắt thinking.
2. Tạo FastAPI với GET /health và POST /generate.
3. Bảo vệ cả hai endpoint bằng bearer token.
4. Giới hạn một generation tại một thời điểm.
5. Mở HTTPS tunnel và in QWEN_API_URL.

Kaggle session và ngrok URL chỉ mang tính tạm thời. Khi session dừng, cần chạy lại notebook
và cập nhật QWEN_API_URL.

## Sử dụng end-to-end

**AnswerService.answer_with_retrieval()** nhận trực tiếp một **RetrievalPipeline**. Phần
Prompt/Answer chỉ dùng contract **retrieve()**, không thay đổi thuật toán retrieval.

~~~python
from FlagEmbedding import BGEM3FlagModel

from rag_manything.answer.service import AnswerService
from rag_manything.config import Settings
from rag_manything.retrieval import (
    BgeM3QueryEncoder,
    HybridSearcher,
    QdrantStore,
    RetrievalConfig,
    RetrievalPipeline,
)

retrieval_config = RetrievalConfig(
    collection_name="virhe4qa_297",
    search_mode="hybrid",
    fusion="rrf",
    enable_reranking=False,
    final_limit=8,
)
store = QdrantStore.from_url(collection_name=retrieval_config.collection_name)
encoder = BgeM3QueryEncoder(BGEM3FlagModel("BAAI/bge-m3", use_fp16=False))
retrieval_pipeline = RetrievalPipeline(
    searcher=HybridSearcher(store, retrieval_config),
    query_encoder=encoder,
    config=retrieval_config,
)

with AnswerService(Settings()) as service:
    result = service.answer_with_retrieval(
        "Thư viện mở cửa lúc mấy giờ?",
        retrieval_pipeline,
    )

print(result.model_dump())
~~~

Hybrid RRF là cấu hình mặc định. Để bật reranking, đặt
**RetrievalConfig(enable_reranking=True, rerank_limit=20)** và truyền một reranker vào
**RetrievalPipeline**. Candidate pool được rerank trước khi lấy **final_limit**.

Kết quả trả về:

For the saved Kaggle reranker scores, use `PrecomputedReranker.from_artifacts(scores_csv, queries_manifest)`; it resolves the 100 exact questions to their `query_id` values without running a model locally.

## Quick hybrid search

Search immediately with one of the 100 BGE-M3 query vectors exported by Kaggle:

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\search_bge_m3.py --query-id query_001 --limit 8
```

For a new question, BGE-M3 must be available locally or be downloaded to the model cache:

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\search_bge_m3.py "Ai chịu trách nhiệm thực hiện kiểm tra và thanh tra nội bộ?" --limit 8
```

## Evaluate the 100-query run

Run the same 100 prepared queries and calculate the ViRE-style metrics:

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\evaluate_qdrant_retrieval.py `
  --collection virhe4qa_297 `
  --mode hybrid `
  --fusion rrf `
  --ks 1,3,5,10,20,50,100 `
  --prefetch-limit 100 `
  --run-name bge_m3_hybrid_rrf_100
```

Results are written under `data\retrieval_runs\<run-name>`, including `metrics.json`, `metrics.csv`, `ranks.csv`, full retrieved results, and `errors\fail@20.csv`. Use `--mode dense` or `--mode sparse` with a different `--run-name` for standalone baselines.

## Baseline result

The current run is BGE-M3 dense + sparse with Qdrant RRF, using 297 chunks and
100 queries. Query processing and reranking were disabled. The five headline
metrics used by the original ViRE report are:

| Metric | Raw value | Percent |
| --- | ---: | ---: |
| P@1 | 0.6200 | 62.00 |
| R@10 | 0.9100 | 91.00 |
| MRR@10 | 0.7258 | 72.58 |
| nDCG@10 | 0.7712 | 77.12 |
| R@20 | 0.9500 | 95.00 |

Additional results: `Recall@100 = 1.00`, mean first-gold rank `3.74`, median
first-gold rank `1`, and 5 queries failed to retrieve the gold chunk in the
top 20. The run took about 208.8 seconds. These formulas match ViRE, but this
is the prepared 297/100 subset rather than the complete paper benchmark.

## Reranking and query processing experiments

The complete Kaggle reranker scores were evaluated offline on the top 100
candidates from the BGE-M3 hybrid baseline and the BM25+Qwen-4B candidate
pipeline. The Qwen3-Reranker-4B was strongest: `P@1 = 86%`, `R@3 = 99%`,
`R@10 = 100%`, and `MRR@10 = 92.27%`. The full comparison and six saved runs
are in `data/retrieval_runs/reranking/`.

The Kaggle timing log measured 29,700 reranker pairs. The measured score times
were 1,654.35 s for BGE-Reranker-v2-M3, 4,008.59 s for Qwen3-Reranker-0.6B,
and 11,658.57 s for Qwen3-Reranker-4B. The run configs include a linear
estimate for 10,000 pairs (100 queries x top 100 candidates); it is an estimate,
not a new inference run.

Stopword cleaning was tested on the original 100 queries and reduced the BGE
dense, sparse, and hybrid metrics, so it is not enabled by default. To test a
dataset where query processing is more relevant, the repository now includes a
local BGE-M3 ViHERMES experiment: 998 contexts, 1,561 questions, and hop levels
1-5. Naive decomposition alone reduced quality, but a soft fusion
`full_query_dense + max(decomposed_query_dense)` improved `HitRate@1` from
66.11% to 68.42%, `Recall@10` from 69.81% to 71.91%, and `Recall@20` from
78.46% to 80.89%. Results are under
`data/retrieval_runs/query_processing/vihermes_bge_m3*`. A deterministic 80/20
check selected `alpha=1.0` on the training portion and retained the gain on
the 313-query holdout (`Recall@10`: 67.48% -> 70.91%).

## Planned extensions

The current result is deliberately a clean retrieval baseline. The next
experiments are kept separate from it:

- Compare the stored Qwen embedding branches and additional embedding models.
- Add TF-IDF/BM25 and other full-text or sparse retrieval baselines.
- Compare Qdrant fusion choices and standalone dense/sparse search.
- Connect the external query-processing pipeline while keeping it switchable.
- Tune decomposition/rewrite fusion on held-out multi-hop queries.
- Evaluate rerankers at smaller candidate limits and measure fresh online latency.

The reported baseline remains BGE-M3 hybrid RRF without query processing or
reranking; the experiment results above are kept separate from that baseline.

## Qdrant point shape

Qdrant stores each item as a point with an ID, named vectors, and a JSON payload. The script stores embeddings as vectors, not duplicated in the payload:

```text
Point {
  id: UUID derived stably from document_id + chunk_id,
  vector: {
    bge_m3_dense: float[1024],
    bge_m3_sparse: { indices: int[], values: float[] },
    qwen_0_6b_dense: float[1024],
    qwen_4b_dense: float[2560]
  },
  payload: {
    chunk_id: "doc-a-0001",
    document_id: "doc-a",
    chunk_index: 0,
    text: "Chunk content...",
    title: "Document title",
    page_start: 1,
    page_end: 1,
    source_url: "https://example.org/document.pdf"
  }
}
```

Các vector embedding được lưu trong named vectors; payload giữ text và metadata cần cho
filter/citation. Các trường nên giữ gồm `chunk_id`, `document_id`, `chunk_index`, `text`,
`title`, `page_start`, `page_end`, `source_url` và metadata nghiệp vụ.

## Kết quả Answer

~~~json
{
  "answer": "Thư viện mở cửa lúc 08:00 [doc-01].",
  "citations": [{"chunk_id": "doc-01", "source": "library.md"}],
  "status": "answered",
  "reason": null,
  "prompt_version": "answer-v1",
  "model": "Qwen/Qwen3-4B",
  "rewritten_question": "Thư viện mở cửa lúc mấy giờ?",
  "latency_ms": 1240.35
}
~~~

**status** có thể là:

- **answered**: tạo và kiểm tra answer thành công.
- **blocked**: input hoặc output bị guardrail chặn.
- **insufficient_context**: retrieval không trả context hữu ích.

## Chạy riêng Prompt/Answer

CLI nhận câu hỏi và các chunk đã retrieval/rerank từ file JSON:

~~~powershell
rag-answer examples/request.json
~~~

Đây là đường chạy dành cho phát triển, test và đánh giá answer; nó không gọi Qdrant.
**AnswerService.answer(question, chunks)** cung cấp contract tương đương cho Python.

## Run one Qwen RAG query

Set `RAG_API_URL`, `RAG_API_KEY`, and `QWEN_QDRANT_COLLECTION` in `.env`, start Qdrant and the Kaggle API notebook, then run this command from the workspace root:

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\run_qwen_rag.py "Câu hỏi cần tìm" --top-k 3
```

This calls the Qwen embedding API, runs dense cosine search in Qdrant, then sends the retrieved payload `text` fields to the answer API. It returns the answer, retrieved payloads, and per-stage timings. The current Qwen collection is dense-only; BM25 is not part of this command because the local Qdrant 1.15.5 instance rejected native BM25 text queries during the trial. Use `--output data/retrieval_runs/one_query.json` to save the full result.

## Run a 30-query governed-answer sample

The batch runner uses Qwen3-Embedding-4B dense retrieval from Qdrant and local
BM25, fuses the top 100 candidates from each branch with equal-weight RRF
(`k=2`), then sends the final chunks through the local `PromptBuilder` policy
and Kaggle `/v1/generate` route. It runs sequentially and writes a checkpoint
after every query:

```powershell
.\.venv\Scripts\python.exe .\RAG-manything\scripts\run_qwen_rag_batch.py `
  --limit 30 `
  --top-k 3 `
  --dense-candidates 100 `
  --bm25-candidates 100 `
  --rrf-k 2
```

Each run creates a timestamped directory under `data/retrieval_runs/` containing
`checkpoint.json`, `per_query.json`, and `summary.json`. Both result files are
formatted JSON arrays for direct inspection in an editor.

## Guardrail và citation

- GPT-4o mini trả structured output gồm **allowed**, **reason** và **rewritten_question**.
- Câu hỏi viết lại phải độc lập, giữ nguyên ngôn ngữ, ý định, tên riêng, số liệu và ràng buộc.
- Context được serialize như dữ liệu không đáng tin cậy để giảm prompt injection.
- GPT-5 mini kiểm tra toàn bộ answer, grounding, nội dung nhạy cảm và citation.
- Citation chỉ hợp lệ nếu **chunk_id** thực sự xuất hiện trong prompt sau khi cắt context.
- Lỗi/refusal/schema sai của guardrail được xử lý fail-closed.
- Qwen timeout hoặc lỗi tạm thời được retry tối đa hai lần; lỗi xác thực và payload sai
  không được retry.

## Observability

Khi **LANGSMITH_TRACING=true**, mỗi request có các span:

~~~text
answer_request
├── input_guardrail
├── retrieval
├── build_prompt
├── qwen_generate
└── output_guardrail
~~~

Trace chỉ ghi metadata như latency, model, prompt version, số chunk và trạng thái. Câu hỏi,
context, prompt, answer và credentials không được gửi vào trace.

## Đánh giá câu trả lời

RAGAS chỉ chấm phần answer, không chấm chất lượng retrieval trong runner này.

| Metric | Ý nghĩa |
| --- | --- |
| Faithfulness | Answer có được hỗ trợ bởi context hay không |
| Response Relevancy | Answer có trả lời đúng trọng tâm câu hỏi hay không |
| Factual Correctness | Các phát biểu có khớp reference hay không |
| Semantic Similarity | Answer có tương đồng ngữ nghĩa với reference hay không |

Dataset JSON array hoặc JSONL gồm **user_input**, **retrieved_contexts**, **response**,
**reference** và **latency_ms**.

Sinh answer thật và ghi latency:

~~~powershell
rag-evaluate examples/evaluation_seed.jsonl --generate --output reports/answers.jsonl
~~~

Chấm bốn metric:

~~~powershell
rag-evaluate reports/answers.jsonl --output reports/baseline.json
~~~

Report gồm điểm từng mẫu, điểm trung bình và latency **mean**, **p50**, **p95**, **min**,
**max**. Evaluation gửi nội dung dataset tới OpenAI nhưng tắt LangSmith tracing.

## Retrieval baseline

Baseline hiện tại:

- Collection: virhe4qa_297.
- Corpus: 297 context chunks.
- Evaluation set: 100 query/gold-chunk pairs.
- Search: BGE-M3 dense + sparse, Qdrant RRF.
- Query processing và reranking: tắt.

| Metric | Kết quả |
| --- | ---: |
| P@1 | 0.6200 |
| R@10 | 0.9100 |
| MRR@10 | 0.7258 |
| nDCG@10 | 0.7712 |
| R@20 | 0.9500 |

Kết quả và ranking đầy đủ nằm trong
**data/retrieval_runs/bge_m3_hybrid_rrf_100/**.

## Kiểm thử

~~~powershell
python -m pytest -q
python -m unittest discover -s tests -v
python -m compileall -q src scripts tests
~~~

Test chạy offline bằng mock transport, không gọi OpenAI, Kaggle hoặc Qdrant thật.

## Cấu trúc repository

~~~text
src/rag_manything/
  answer/
    client.py          Qwen HTTP client
    guardrails.py      GPT input/output guardrails
    service.py         end-to-end answer orchestration
  prompt/
    builder.py         grounded prompt và context budget
  retrieval/
    hybrid.py          dense/sparse/hybrid search
    pipeline.py        query processing và optional reranking
    qdrant_store.py    Qdrant wrapper
    query.py           query encoders
    reranking.py       reranker adapters
  evaluation/
    ragas_eval.py      answer metrics và latency report
  config.py            environment settings
  models.py            request/response contracts
  observability.py     LangSmith metadata tracing

notebooks/
scripts/
data/
tests/
~~~

## Giới hạn hiện tại

- Qwen endpoint trên Kaggle/ngrok phù hợp development và demo, không phải production.
- Generation chưa hỗ trợ streaming.
- Notebook chỉ xử lý một generation tại một thời điểm.
- Baseline RAGAS live chưa được tạo vì cần Qwen endpoint và OpenAI credentials thật.
- RAGAS đang được pin ở nhánh 0.4.x; các API wrapper hiện tại có cảnh báo deprecation
  trước khi nâng lên 1.x.

Chi tiết thiết kế Prompt/Answer nằm trong [plan.md](plan.md). Hướng dẫn dữ liệu nằm trong
[data/README.md](data/README.md) và
[data/retrieval_runs/README.md](data/retrieval_runs/README.md).
