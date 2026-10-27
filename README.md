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

Dataset JSONL gồm **user_input**, **retrieved_contexts**, **response**, **reference** và
**latency_ms**.

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
