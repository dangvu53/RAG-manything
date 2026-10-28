# Query Token Statistics

Source: `D:\AI Engineer Fresher - TPBank\RAG-manything\data\kaggle_artifacts\virhe4qa_model_sweep\queries_manifest.csv`

## Summary

- Queries: **100**
- Total tokens: **1752**
- Unique tokens: **419**
- Average query length: **17.52 tokens**
- High-confidence removable stopword candidates: **231 (13.18%)**
- Broad function/question candidates: **430 (24.54%)**

The broad group includes words such as `có`, `không`, `được`, `ai` and `gì`; these should not be deleted blindly because they carry modality, polarity or question intent.

## Frequent Tokens

| Token | Term frequency | Query frequency | Category |
|---|---:|---:|---|
| `có` | 55 | 52 | function/question candidate |
| `học` | 47 | 37 | content/domain |
| `không` | 38 | 37 | function/question candidate |
| `trình` | 37 | 32 | content/domain |
| `được` | 34 | 32 | function/question candidate |
| `của` | 31 | 26 | high-confidence stopword |
| `viên` | 27 | 22 | content/domain |
| `các` | 25 | 23 | high-confidence stopword |
| `quy` | 24 | 20 | content/domain |
| `sinh` | 24 | 19 | content/domain |
| `định` | 23 | 21 | content/domain |
| `chương` | 23 | 19 | content/domain |
| `nào` | 22 | 22 | function/question candidate |
| `trường` | 21 | 19 | content/domain |
| `đào` | 20 | 16 | content/domain |
| `tạo` | 20 | 16 | content/domain |
| `gì` | 20 | 20 | function/question candidate |
| `trong` | 16 | 16 | high-confidence stopword |
| `môn` | 16 | 13 | content/domain |
| `và` | 14 | 12 | high-confidence stopword |
| `đại` | 14 | 11 | content/domain |
| `thi` | 13 | 10 | content/domain |
| `là` | 13 | 13 | high-confidence stopword |
| `với` | 13 | 12 | high-confidence stopword |
| `trách` | 12 | 11 | content/domain |
| `cho` | 12 | 12 | high-confidence stopword |
| `công` | 11 | 10 | content/domain |
| `đơn` | 11 | 10 | content/domain |
| `đối` | 11 | 10 | content/domain |
| `thì` | 11 | 11 | high-confidence stopword |
| `như` | 11 | 11 | high-confidence stopword |
| `bằng` | 11 | 10 | content/domain |
| `điểm` | 11 | 7 | content/domain |
| `nhiệm` | 10 | 10 | content/domain |
| `tra` | 10 | 7 | content/domain |
| `tổ` | 10 | 10 | content/domain |
| `ngành` | 10 | 9 | content/domain |
| `về` | 10 | 9 | high-confidence stopword |
| `chỉ` | 10 | 9 | function/question candidate |
| `giảng` | 10 | 7 | content/domain |
| `theo` | 10 | 9 | high-confidence stopword |
| `vị` | 10 | 9 | content/domain |
| `chức` | 9 | 9 | content/domain |
| `thể` | 9 | 9 | content/domain |
| `ai` | 8 | 8 | function/question candidate |
| `thực` | 8 | 8 | content/domain |
| `hiện` | 8 | 8 | content/domain |
| `mở` | 8 | 7 | content/domain |
| `việc` | 8 | 8 | content/domain |
| `dạy` | 8 | 8 | content/domain |

## Question Templates

| Pattern | Query count |
|---|---:|
| `co_any_khong` | 35 |
| `co_the_khong` | 7 |
| `co_kha_nang_khong` | 1 |
| `nhu_the_nao` | 6 |
| `la_gi` | 5 |
| `bao_nhieu` | 8 |
| `o_dau` | 4 |
| `ai_at_start` | 6 |
| `neu_at_start` | 4 |
| `doi_voi` | 9 |
| `truong_hop` | 3 |
| `noi_dung` | 6 |
| `dieu_number` | 1 |

## Highest Stopword Ratios

| Query | Ratio | Question |
|---|---:|---|
| `query_059` | 33.33% | SHD là viết tắt của gì? |
| `query_011` | 30.77% | Các giáo trình sẽ được gửi đi đâu sau khi được thẩm định? |
| `query_048` | 29.41% | P.ĐTĐH làm gì sau khi nhận các phản ánh từ các đơn vị có liên quan? |
| `query_067` | 27.78% | Số lượng sinh viên tối thiểu của một lớp học cho các môn đại cương là bao nhiêu? |
| `query_046` | 27.78% | Nếu một môn học được Việt hóa thì sau khi cập nhật loại II có thay đổi không? |
| `query_093` | 25.00% | Điểm 4 sẽ được xếp vào loại gì? |
| `query_088` | 25.00% | Yêu cầu đổi với điểm KLTN và ĐTBTL và điểm rèn luyện như thế nào để được cấp bằng CTTN? |
| `query_070` | 25.00% | Trong Chương trình chuẩn thì có sự tham khảo của các chương trình của trường đại học khác hay không? |
| `query_049` | 25.00% | P.ĐTĐH/VPĐB căn cứ vào đâu để xếp lịch thi và thông báo lịch thi đến SV và các đơn vị liên quan? |
| `query_016` | 25.00% | Có phải số hiệu của phôi được ghi theo thứ tự từ bé đến lớn không? |
| `query_071` | 24.24% | Trong cùng một ngành đào tạo, nội dung của chương trình đào tạo theo phương thức ĐTTX của Trường có như chương trình đào tạo theo hình thức giáo dục chính quy không? |
| `query_087` | 23.08% | Yêu cầu về mặt pháp lý của tài liệu tham khảo là gì? |
| `query_085` | 22.22% | Với các điểm quá trình, thực hành của môn học, thì hạn nhập điểm có giống với hạn nhập điểm cuối kỳ của môn học đó không? |
| `query_074` | 22.22% | Trường có những phương thức dạy và học nào? |
| `query_054` | 22.22% | Quy trình phúc khảo diễn ra như thế nào? |
| `query_044` | 22.22% | Nếu các thành viên muốn xem xét, trao đổi thêm về đề tài thì có khả năng không? |
| `query_041` | 22.22% | Những quy định về khoá luận tốt nghiệp cho hệ chính quy áp dụng vào đối tượng nào? |
| `query_028` | 21.43% | Học liệu điện tử sử dụng trong DHTT và DHKH phải như thế nào? |
| `query_004` | 21.43% | Ai là người ra quyết định về việc giao nhiệm vụ hướng dẫn KLTN? |
| `query_055` | 21.05% | Quy định dạy học theo phương thức trực tuyên và kết hợp áp dụng cho các đối tượng nào? |

## Example: `query_044`

Original: `Nếu các thành viên muốn xem xét, trao đổi thêm về đề tài thì có khả năng không?`

High-confidence word filtering:

`thành viên muốn xem xét trao đổi thêm đề tài có khả năng không`

A phrase-level rule can additionally remove the interrogative shell `có khả năng không`, leaving the topic-bearing phrase about members discussing the thesis topic.
