# Hybrid Retrieval: Queries Not Retrieved at Rank 1

Generated from `data/retrieval_runs/bge_m3_hybrid_rrf_100`.

Selection rule: `first_gold_rank != 1`; total failures: **38 / 100**.
The report is ordered from the lowest-ranked gold chunk to the closest misses.

Baseline: BGE-M3 dense + sparse, Qdrant RRF, no query processing, no reranking.

## Index

| # | Query | Hybrid rank | Dense rank | Sparse rank | Question |
|---:|---|---:|---:|---:|---|
| 1 | `query_012` | 54 | - | 28 | Các nội dung trên khóa học vi phạm các quy định của pháp luật hiện hành có bị gì không? |
| 2 | `query_026` | 35 | 17 | - | Hệ thống hỗ trợ học tập còn có tên gọi nào khác không? |
| 3 | `query_047` | 27 | 15 | 66 | Nội dung của Điều 3 của quy định đào tạo chương trình tài năng là gì? |
| 4 | `query_044` | 23 | 13 | 43 | Nếu các thành viên muốn xem xét, trao đổi thêm về đề tài thì có khả năng không? |
| 5 | `query_095` | 21 | 29 | 14 | Điểm sẽ được tính như thế nào trong trường hợp học cải thiện điểm đối với hệ đào tạo từ xa trình độ đại học của trường đại học công nghệ thông tin? |
| 6 | `query_057` | 18 | 37 | 10 | Quy định đào tạo chương trình tài năng quy định điều gì? |
| 7 | `query_082` | 13 | 7 | 29 | Vì sao UIT xây dựng và triển khai các chương trình CLC? |
| 8 | `query_098` | 13 | 37 | 8 | Đơn vị quản lý môn học có thể là cái gì? |
| 9 | `query_076` | 11 | 34 | 6 | Trường tổ chức lớp của hệ đào tạo từ xa trình độ đại học của trường đại học công nghệ thông tin như thế nào? |
| 10 | `query_021` | 8 | 10 | 5 | Giao tiếp bằng ngoại ngữ có phải một kỹ năng được kiểm tra trong các đợt kiểm tra năng lực tiếng Anh do Trung tâm Ngoại ngữ của Trường tổ chức không? |
| 11 | `query_072` | 8 | 14 | 6 | Trong một học kỳ chính Trường tổ chức bao nhiêu đợt kiểm tra? |
| 12 | `query_090` | 7 | 4 | 27 | ĐH CNTT thuộc cụm đại học nào? |
| 13 | `query_015` | 5 | 3 | 7 | Có các nội dung nào được quy định trong phần làm khóa luận tốt nghiệp dành cho sinh viên chương trình tiên tiến? |
| 14 | `query_031` | 5 | 9 | 3 | Khi sinh viên hoàn tất quá trình học tập theo quy định thì Trường có trách nhiệm gì? |
| 15 | `query_045` | 5 | 5 | 5 | Nếu không hoàn thành chương trình đào tạo thì có thể nhận chứng chỉ tốt nghiệp được không? |
| 16 | `query_017` | 4 | 6 | 3 | Có thể quy đổi số 30% tín chỉ của các môn học thạc sĩ được công nhận khi chuyển sang học thạc sĩ đối với chương trình ĐH-ThS được không? |
| 17 | `query_030` | 4 | 4 | 3 | Hồ sơ liên quan đến việc đặt trạm ĐTTX nằm ở đâu? |
| 18 | `query_100` | 4 | 6 | 3 | Đối với chương trình tiên tiến, môn Giáo dục quốc phòng - an ninh có giảng dạy bằng tiếng Anh không? |
| 19 | `query_010` | 3 | 2 | 5 | Chương trình đào tạo tối thiểu của Trường yêu cầu sinh viên tích lũy bao nhiêu tín chỉ để tốt nghiệp trong chương trình đào tạo cử nhân? |
| 20 | `query_032` | 3 | 3 | 5 | Kết quả học tập của sinh viên có được ghi vào bảng điểm không? |
| 21 | `query_033` | 3 | 4 | 4 | Kết quả đăng ký học phần được thông báo ở đâu? |
| 22 | `query_064` | 3 | 2 | 4 | Sinh viên thuộc chương trình ĐTTX chưa hoàn thành chương trình đào tạo theo quy định có thể nộp hồ sơ đề nghị xét tốt nghiệp không? |
| 23 | `query_066` | 3 | 6 | 1 | Số buổi seminar ngoại khóa của CTTN có giới hạn hay không? |
| 24 | `query_075` | 3 | 2 | 2 | Trường hợp chưa nhận chứng chỉ GDQP-AN thì có thể đăng ký xét tốt nghiệp không? |
| 25 | `query_097` | 3 | 6 | 2 | Đơn vị phụ trách thực hiện công tác chấm trắc nghiệm là đơn vị nào? |
| 26 | `query_007` | 2 | 2 | 3 | Ban giám hiệu nhà trường có trách nhiệm gì? |
| 27 | `query_020` | 2 | 1 | 5 | Cập nhật về học phí có được thông tin đến cho sinh viên hệ ĐTTX không? |
| 28 | `query_024` | 2 | 1 | 2 | Hiệu trưởng có thể cấp văn bằng tốt nghiệp bậc tiến sĩ được không? |
| 29 | `query_025` | 2 | 5 | 1 | Hằng năm phương thức tuyển sinh được công bố ở đâu? |
| 30 | `query_038` | 2 | 1 | 2 | Nghĩa vụ của Phòng Thanh tra Pháp chế và Đảm bảo Chất lượng trong quy trình tổ chức thi là gì? |
| 31 | `query_056` | 2 | 1 | 2 | Quy định về học phí về đào tạo liên thông từ trình độ đại học lên trình độ thạc sĩ hệ chính quy như thế nào? |
| 32 | `query_059` | 2 | 3 | 2 | SHD là viết tắt của gì? |
| 33 | `query_063` | 2 | 2 | 2 | Sinh viên khi đi thi có cần phải mang theo giấy tờ cá nhân như CCCD, thẻ sinh viên hay không? |
| 34 | `query_065` | 2 | 2 | 1 | Sinh viên tài năng có được tham gia xét hưởng học bổng khuyến khích tài năng như sinh viên các chương trình khác không? |
| 35 | `query_067` | 2 | 3 | 1 | Số lượng sinh viên tối thiểu của một lớp học cho các môn đại cương là bao nhiêu? |
| 36 | `query_074` | 2 | 2 | 2 | Trường có những phương thức dạy và học nào? |
| 37 | `query_084` | 2 | 2 | 2 | Văn bằng, chứng chỉ có bị hủy bỏ không? |
| 38 | `query_099` | 2 | 2 | 2 | Để Ban Giám hiệu có thể biết được toàn bộ hoạt động của chương trình thì đơn vị nào có trách nhiệm báo cáo cho Ban Giám hiệu? |

---

## 1. `query_012`

**Question:** Các nội dung trên khóa học vi phạm các quy định của pháp luật hiện hành có bị gì không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `54` |
| Dense first gold rank | `-` |
| Sparse first gold rank | `28` |
| Gold chunk | `chunk_0084` |
| Gold document | `virhe4qa_c8b08b6a6529cb3ff6b0` |
| Gold source index | `3900` |
| Hybrid top 1 | `chunk_0016` (score `0.600000`) |

### Gold context

```text
Điều  14. Trách nhiệm của đơn vị phụ trách quản lý hạ tầng công nghệ thông tin - truyền thông
1. Quản lý, vận hành và đảm bảo an ninh, an toàn: hệ thống máy chủ, cổng thông tin và hạ tầng kết nối mạng phục vụ DHTT, DHKH.
2. Cấp phát tài khoản, tạo lớp học phần, phân quyền cho người dùng trên các hệ thống; hỗ trợ kỹ thuật cho giảng viên và sinh viên trong quá trình giảng dạy và học tập; hỗ trợ bộ phận chức năng thực hiện nhiệm vụ quản lý, thanh tra, kiểm tra.
3. Tham gia giám sát quá trình DHTT, DHKH; kịp thời phát hiện, xử lý và báo cáo lãnh đạo đơn vị các hiện tượng bất thường trong quá trình DHTT, DHKH; lập các báo cáo liên quan khi được yêu cầu.
4. Tạm ngưng hoặc vô hiệu hóa các khóa học, các nội dung trên khóa học và tài khoản người dùng vi phạm các quy định của pháp luật hiện hành và các điều khoản trong quy định này.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0016` | score `0.600000` | document `virhe4qa_f396d11f4689860a9368`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng Quy định này áp dụng đối với giảng viên, sinh viên hệ chính quy đào tạo theo CTTT, thực hiện theo học chế tín chỉ, giảng dạy bằng tiếng Anh (trừ các môn lý luận chính trị, pháp luật đại cương, Giáo dục quốc phòng – an ninh, Giáo dục thể chất). Các nội dung không nêu trong quy định này được áp dụng theo Quy chế đào tạo theo học chế tín chỉ và các quy định hiện hành của Trường ĐHCNTT cho hệ đại học chính quy.
```

**Rank 2 | `chunk_0146` | score `0.562500` | document `virhe4qa_7cb107459b348ea7c9cc`**

```text
Điều 22. Xử lý cán bộ vi phạm quy định Trong thời gian thi, nếu các cán bộ thanh tra thi phát hiện thấy các trường hợp vi phạm thì lập biên bản tại chỗ và đề nghị Hiệu trưởng xử lý. Người tham gia công tác thi có hành vi vi phạm quy định (bị phát hiện trong khi làm nhiệm vụ hoặc sau kỳ thi), nếu có đủ chứng cứ, tùy theo mức độ, sẽ bị xử lý theo các hình thức sau đây. 1. Khiển trách đối với những người phạm lỗi nhẹ trong khi thi hành nhiệm vụ. 2. Cảnh cáo đối với những người vi phạm một trong các lỗi sau đây: a. CBCT bỏ coi thi mà không thông báo cho đơn vị tổ chức môn thi từ 2 lần trở lên trong một đợt thi. b. CBCT để cho SV tự do trao đổi khi làm bài, sử dụng tài liệu bị cấm sử dụng hoặc sử dụng các phương tiện thông tin liên lạc tại phòng thi. c. Cán bộ chấm thi chấm điểm hoặc cộng điểm bài thi có nhiều sai sót (trên 5% tổng số bài thi). d. Cán bộ chấm thi nộp điểm trễ so với thời hạn…
```

**Rank 3 | `chunk_0296` | score `0.395833` | document `virhe4qa_412115afa47597fc241b`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng - Văn bản này quy định việc tổ chức dạy-học ngoài giờ hành chính đối với các học phần trong chương trình đào tạo trình độ đại học hệ chính quy của Trường Đại học Công nghệ Thông tin – ĐHQG-HCM. - Quy định này được áp dụng cho các đối tượng là sinh viên chính quy, không phải là sinh viên đại học chính quy của Trường và các đơn vị, cá nhân khác có liên quan.
```

**Rank 4 | `chunk_0149` | score `0.383333` | document `virhe4qa_8a114b32e04ea94123f0`**

```text
Điều 23. Xử lý vi phạm 1. Việc xử lý các vi phạm trong tuyển sinh thực hiện theo quy chế tuyển sinh đại học hình thức ĐTTX hiện hành. 2. Việc xử lý kỷ luật đối với người học vi phạm các quy định về thi, kiểm tra được thực hiện theo quy định của quy chế đào tạo đại học chính quy hiện hành. 3. Trong quá trình tổ chức thực hiện ĐTTX, các đơn vị, cá nhân có liên quan để xảy ra sai phạm sẽ bị xử lý theo quy định của pháp luật hiện hành.
```

**Rank 5 | `chunk_0092` | score `0.366667` | document `virhe4qa_91a63da193ac6eaf253f`**

```text
Điều 15. Những hành vi nghiêm cấm trong hoạt động dạy học trực tuyến 1. Nghiêm cấm các hành vi lợi dụng DHTT, DHKH để cung cấp thông tin trên mạng nhằm mục đích: a) Chống lại Nhà nước Cộng hòa Xã hội Chủ nghĩa Việt Nam; gây phương hại đến an ninh quốc gia, trật tự an toàn xã hội; phá hoại khối đại đoàn kết dân tộc; tuyên truyền chiến tranh, khủng bố; gây hận thù, mâu thuẫn giữa các dân tộc, sắc tộc, tôn giáo. b) Tuyên truyền, kích động bạo lực, dâm ô, đồi trụy, tội ác, tệ nạn xã hội, mê tín dị đoan, phá hoại thuần phong, mỹ tục của dân tộc. c) Tiết lộ bí mật Nhà nước, bí mật quân sự, an ninh, kinh tế, đối ngoại và những bí mật khác do pháp luật quy định. d) Đưa thông tin xuyên tạc, vu khống, xúc phạm uy tín của tổ chức, danh dự và nhân phẩm của cá nhân. đ) Quảng cáo, tuyên truyền, mua bán hàng hóa, dịch vụ bị cấm; truyền bá tác phẩm báo chí, văn học, nghệ thuật, xuất bản phẩm bị cấm. e)…
```


---

## 2. `query_026`

**Question:** Hệ thống hỗ trợ học tập còn có tên gọi nào khác không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `35` |
| Dense first gold rank | `17` |
| Sparse first gold rank | `-` |
| Gold chunk | `chunk_0119` |
| Gold document | `virhe4qa_da5e1bc92b41223a8639` |
| Gold source index | `7110` |
| Hybrid top 1 | `chunk_0128` (score `1.000000`) |

### Gold context

```text
Điều  2.	Giải thích từ ngữ
Chương trình đại trà là chương trình đào tạo trình độ đại học hệ chính quy được ĐHQG-HCM cho phép triển khai đào tạo tại Trường ĐHCNTT, có mức trần học phí theo quy định hiện hành của Chính phủ.
Chương trình chất lượng cao (CT CLC) là chương trình đào tạo trình độ đại học hệ chính quy có các điều kiện đảm bảo chất lượng và chuẩn đầu ra cao hơn chương trình đại trà tương ứng của cùng một ngành hoặc chuyên ngành đào tạo.
Ngoại ngữ chính của chương trình chất lượng cao (sau đây gọi tắt là ngoại ngữ) là ngoại ngữ mà chương trình chất lượng cao đó có tổ chức giảng dạy chính.
Website môn học: Mỗi lớp học lý thuyết được cấp 01 website môn học vào đầu học kỳ tại hệ thống hỗ trợ học tập của Trường (courses.uit.edu.vn), gọi tắt là Moodle.
Chương trình đại trà tương ứng: là chương trình đại trà của cùng một ngành hoặc chuyên ngành với chương trình chất lượng cao.
Đơn vị phụ trách chuyên môn (sau đây gọi tắt là đơn vị chuyên môn): Khoa, bộ môn được giao phụ trách về mặt chuyên môn cho các CT CLC
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0128` | score `1.000000` | document `virhe4qa_92ca470accbb7e8a1116`**

```text
Điều 2. Hệ thống đào tạo từ xa 1. Hệ thống ĐTTX của Trường ĐHCNTT gồm: Chương trình ĐTTX; học liệu ĐTTX; bộ máy tổ chức và quản lý ĐTTX; hệ thống kiểm tra, đánh giá; hệ thống kỹ thuật hỗ trợ thực hiện ĐTTX; đội ngũ giảng viên, cán bộ hỗ trợ học tập, cán bộ quản lý; các văn bản quy định về ĐTTX. 2. Học liệu ĐTTX gồm: học liệu chính và các học liệu bổ trợ phục vụ cho quá trình đào tạo. Học liệu chính đảm bảo cung cấp và truyền tải đầy đủ nội dung chương trình đào tạo để người học có thể tự học phù hợp với phương thức ĐTTX. Học liệu bổ trợ cung cấp các nội dung chi tiết hỗ trợ người học hiểu biết sâu sắc, đầy đủ những nội dung trong học liệu chính, có thể là: đĩa ghi hình ảnh, âm thanh, đoạn phim ngắn; chương trình phát thanh, chương trình truyền hình; sách in, tài liệu hướng dẫn dạy và học với sự trợ giúp của máy tính; bài tập trên internet, bài seminar và các buổi trao đổi thảo luận, tru…
```

**Rank 2 | `chunk_0133` | score `0.400000` | document `virhe4qa_0c8e7f2a7b88cc78ebf1`**

```text
Điều 2. Từ ngữ sử dụng và chữ viết tắt 1. Đơn vị quản lý môn học (ĐVQLMH): Khoa, bộ môn, tổ môn học hoặc một đơn vị khác của Trường được giao nhiệm vụ quản lý về mặt chuyên môn đối với một môn học theo Danh mục các môn học đại học của Trường. 2. Giảng viên thỉnh giảng: Giảng viên hoặc trợ giảng không phải là cán bộ cơ hữu của Trường ĐHCNTT. 3. Khảo sát giảng dạy: Khảo sát lấy ý kiến phản hồi từ người học về hoạt động giảng dạy của giảng viên quy định tại Quyết định số 08/QĐ-ĐHCNTT-ĐBCL ngày 17 tháng 12 năm 2013 của Hiệu trưởng Trường ĐHCNTT. 4. Hệ thống Moodle: Hệ thống hỗ trợ học tập online của Trường tại địa chỉ courses.uit.edu.vn.
```

**Rank 3 | `chunk_0025` | score `0.364583` | document `virhe4qa_3e1602afa6a858557667`**

```text
Điều 10. Hệ thống phần mềm phục vụ DHTT và DHKH Hệ thống phần mềm phục vụ DHTT, DHKH được sử dụng kết hợp bởi các phần mềm sau đây: 1. Hệ thống UIT-Elearning (https://courses.uit.edu.vn): a) Giúp giảng viên tổ chức triển khai giảng bài, hướng dẫn, giao nhiệm vụ học tập, chuyển tải học liệu điện tử đến sinh viên; b) Giúp sinh viên tương tác, trao đổi thông tin với giảng viên và những sinh viên khác. 2. Phần mềm Microsoft Teams: a) Giúp giảng viên tổ chức triển khai giảng bài, chia sẻ màn hình máy tính, hướng dẫn, giao nhiệm vụ học tập; b) Giúp sinh viên tương tác, trao đổi thông tin với giảng viên và những sinh viên khác. 3. Hệ thống Cổng thông tin đào tạo đại học (https:/student.uit.edu.vn/ https:/daa.uit.edu.vn): a) Giúp giảng viên xem thông tin về lịch dạy, lớp học. b) Giúp sinh viên xem lịch học và cung cấp các dịch vụ sinh viên khác. 4. Hệ thống Quản lý đào tạo: Cho phép Trường quản…
```

**Rank 4 | `chunk_0207` | score `0.281250` | document `virhe4qa_b915eae2ec86674e940b`**

```text
Điều 4. Tiêu chuẩn và trách nhiệm của trợ giảng môn học (TGMH) 1. TGMH phải đáp ứng tất cả những điều kiện sau: a. Có trình độ đại học trở lên hoặc là sinh viên năm cuối khóa của Trường, b. Đáp ứng một trong các các điều kiện sau: i. Có kết quả nghiên cứu liên quan đến môn học phụ trách được thể hiện qua: luận văn tốt nghiệp trình độ đại học/thạc sĩ/tiến sĩ; bài báo khoa học đăng trên các kỷ yếu hội nghị chuyên ngành hoặc tạp chí có uy tín; sách đã xuất bản; hoặc đề tài nghiên cứu khoa học đã được nghiệm thu; ii. Đã học và thi đạt môn học tương đương trong quá trình học tập hoặc từ một khóa học có uy tín được Trường công nhận. Trường hợp TGMH chưa có trình độ đại học thì phải có kết quả học môn học đó đạt từ loại Giỏi trở lên. c. Đáp ứng một trong các điều kiện sau: i. Hoàn thành kiến tập giảng dạy được quy định tại Điều 6 của quy định này và được giảng viên hướng dẫn kiến tập nhận xét …
```

**Rank 5 | `chunk_0182` | score `0.276923` | document `virhe4qa_c436b8422fd4be91aecc`**

```text
Điều 3. Môn học 1. Học phần (hay môn học) là khối lượng kiến thức tương đối trọn vẹn, thuận tiện cho người học tích lũy trong quá trình học tập, nội dung được bố trí giảng dạy trong một học kỳ. Mỗi học phần được ký hiệu bằng một mã riêng do Trường quy định. Mỗi học phần thực hành, thí nghiệm, kiến tập,… có khối lượng từ 1 – 3 tín chỉ, mỗi học phần lý thuyết hoặc học phần có cả lý thuyết và thực hành có khối lượng từ 1 – 4 tín chỉ. Trường có hai hình thức tổ chức giảng dạy thực hành: - Thực hành Hình thức 1 (HT1): là hình thức dạy thực hành có sự hướng dẫn của giảng viên cho toàn thời lượng học thực hành. - Thực hành Hình thức 2 (HT2): là hình thức dạy thực hành có sự hướng dẫn của giảng viên với thời lượng 09 tiết/tín chỉ thực hành, không nhất thiết phải sử dụng phòng thực hành chuyên dụng. 2. Các loại học phần - Học phần tích lũy: là học phần mà sinh viên có kết quả tổng kết học phần đ…
```


---

## 3. `query_047`

**Question:** Nội dung của Điều 3 của quy định đào tạo chương trình tài năng là gì?

| Field | Value |
|---|---|
| Hybrid first gold rank | `27` |
| Dense first gold rank | `15` |
| Sparse first gold rank | `66` |
| Gold chunk | `chunk_0172` |
| Gold document | `virhe4qa_eee1040f5afc88d187a4` |
| Gold source index | `8095` |
| Hybrid top 1 | `chunk_0120` (score `0.833333`) |

### Gold context

```text
Điều  3.	Mục tiêu đào tạo
Mục tiêu đào tạo của CTTN nhằm: 
-	Tuyển chọn và tạo điều kiện phát triển cho các sinh viên ưu tú, đào tạo nguồn nhân lực chất lượng cao, cán bộ đầu ngành cho các đơn vị sản xuất, hoạt động kinh tế, cán bộ giảng dạy cho các trường đại học, cao đẳng tại TP. HCM và trong cả nước.
-	Sinh viên được phát triển toàn diện về kiến thức, kỹ năng, thái độ và ngoại ngữ.
-	Sinh viên được định hướng để phát huy năng lực sở trường, có tầm nhìn và kiến thức rộng; tăng cường hỗ trợ về hoạt động học thuật, nghiên cứu khoa học và công nghệ.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0120` | score `0.833333` | document `virhe4qa_1c466c63cf51a2b45f7a`**

```text
Điều 2. Giải thích từ ngữ Sinh viên thuộc chương trình tài năng có 02 hình thức là chính thức và dự bị, nằm trong tổng chỉ tiêu của chương trình: - Sinh viên chính thức: đảm bảo đáp ứng các tiêu chuẩn theo yêu cầu và được hưởng đầy đủ các quyền lợi của chương trình. - Sinh viên dự bị: cùng điều kiện học tập và học cùng chương trình đào tạo với sinh viên chính thức nhưng không được hưởng chính sách về học bổng tài năng. Sinh viên dự bị bao gồm các sinh viên trong lớp tài năng vi phạm điều kiện đạt sinh viên chính thức nhưng chưa bị loại ra khỏi chương trình trong các đợt xét sau mỗi học kỳ, và sinh viên mới tuyển bổ sung vào chương trình. Môn học cốt lõi: là môn học quan trọng trong CTĐT, là phần kiến thức không thể thiếu trong lĩnh vực chuyên môn liên quan tới ngành đào tạo chương trình tài năng. Danh sách môn học cốt lõi do Khoa đề nghị trong đề án mở chương trình tài năng. Seminar ngo…
```

**Rank 2 | `chunk_0264` | score `0.666667` | document `virhe4qa_ad01f6fbc0dda7c3e229`**

```text
Điều 8. Chương trình đào tạo gắn với một ngành Chương trình đào tạo gắn với một ngành được phân loại như sau: 1. Chương trình chuẩn: được xây dựng theo quy định hiện hành; đáp ứng mục tiêu và chuẩn đầu ra của bậc trình độ tương ứng; có sự tham khảo chương trình của các trường đại học có uy tín trong nước hoặc trên thế giới; có sự tham gia của các nhà khoa học chuyên môn, giảng viên, cán bộ quản lý, đại diện của các tổ chức xã hội - nghề nghiệp, nhà tuyển dụng lao động và người đã tốt nghiệP. 2. Chương trình tài năng: được xây dựng dựa trên chương trình chuẩn nhằm tuyển chọn và tạo điều kiện phát triển cho các sinh viên xuất sắc. 3. Chương trình tiên tiến: được thiết kế, xây dựng dựa trên cơ sở chương trình đang được áp dụng ở trường đại học tiên tiến trên thế giới (gọi tắt là chương trình gốc) được giảng dạy bằng ngôn ngữ của chương trình gốc. 4. Chương trình nâng cao: được xây dựng dựa…
```

**Rank 3 | `chunk_0064` | score `0.500000` | document `virhe4qa_3abd8382b4312b3ad46f`**

```text
Điều 13. Quy định về tài chính 1. Học bổng sinh viên Học bổng chương trình: học bổng được cấp cho sinh viên theo từng học kỳ – một học kỳ tính là 5.0 tháng. Mức học bổng hàng năm do Hiệu trưởng quyết định. Tất cả các sinh viên tài năng theo danh sách chính thức từng học kỳ đều được hưởng học bổng này. Học bổng khuyến khích học tập: sinh viên tài năng được tham gia xét hưởng học bổng khuyến khích học tập theo quy định của nhà nước tương tự như các sinh viên chương trình khác (xét chung theo khóa, Khoa-Ngành). 2. Khen thưởng sinh viên Căn cứ vào tình hình kinh phí và hoạt động của các lớp CTTN, Hiệu trưởng quyết định thêm các hình thức khen thưởng sau: - Sinh viên đạt thành tích xuất sắc trong các cuộc thi học thuật. - Tuyên dương nỗ lực phấn đấu và tích cực tham gia phong trào, do tập thể lớp bình chọn. 3. Chi nghiệp vụ chuyên môn đặc biệt khác Ngoài các khoản chi thường xuyên kể trên, đ…
```

**Rank 4 | `chunk_0274` | score `0.444444` | document `virhe4qa_c31538b810cd4921a313`**

```text
Điều 9. Tuyển bổ sung và loại ra khỏi chương trình, xét chính thức và dự bị Đối tượng tham gia CTTN là những sinh viên có năng lực xuất sắc, do đó, sau mỗi học kỳ BĐH quyết định việc loại sinh viên khỏi lớp tài năng, tuyển bổ sung sinh viên từ chương trình chuẩn vào lớp tài năng, xét chuyển đổi sinh viên chính thức và dự bị. Đầu mỗi học kỳ, Khoa xét và đề nghị lên BĐH các danh sách sinh viên tuyển bổ sung, bị loại ra khỏi các lớp CTTN hoặc danh sách sinh viên chính thức và dự bị theo các tiêu chuẩn như sau: 1. Loại khỏi chương trình Tại thời điểm xem xét, sinh viên rơi vào một trong các trường hợp sau: - Chưa tốt nghiệp khi đã quá thời gian thiết kế của khóa học và không có lý do đặc biệt. - Không đăng ký học đầy đủ các môn học CTTN bắt buộc trong học kỳ. - ĐTBTL nhỏ hơn 6,5 – tính tương ứng sau học kỳ 1 và sau học kỳ hè (kết quả học tập của học kỳ hè sẽ được tính chung vào kết quả học …
```

**Rank 5 | `chunk_0171` | score `0.220833` | document `virhe4qa_43ecdac7caa6a930c0b7`**

```text
Điều 3. Mục tiêu của quy định 1. Đảm bảo thực hiện mở ngành đào tạo theo định hướng, chủ trương chung của Trường Đại học Công nghệ Thông tin (sau đây gọi là Trường) và ĐHQG-HCM về phát triển ngành, nghề đào tạo. 2. Hướng dẫn thống nhất công tác xây dựng, thẩm định đề án mở ngành đào tạo tại Trường. 3. Là cơ sở pháp lý cho việc kiểm tra, giám sát, đánh giá về mở ngành đào tạo tại Trường.
```


---

## 4. `query_044`

**Question:** Nếu các thành viên muốn xem xét, trao đổi thêm về đề tài thì có khả năng không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `23` |
| Dense first gold rank | `13` |
| Sparse first gold rank | `43` |
| Gold chunk | `chunk_0045` |
| Gold document | `virhe4qa_dac5d96e841d82cdbb08` |
| Gold source index | `9269` |
| Hybrid top 1 | `chunk_0200` (score `0.750000`) |

### Gold context

```text
Điều  11. Tổ chức bảo vệ KLTN
–	Hằng năm sẽ có 2 đợt bảo vệ khóa luận tốt nghiệp theo kế hoạch chung của Trường và được công bố vào đầu mỗi năm học. Khoa đề nghị thời gian tổ chức Hội đồng và gởi về phòng ĐTĐH chậm nhất 7 ngày sau thời hạn thực hiện KLTN đã hết.
–	Danh sách sinh viên đủ điều kiện bảo vệ KLTN trước Hội đồng do P. ĐTĐH xem xét, đề nghị và Hiệu trưởng ra quyết định.
–	Các thành viên Hội đồng phải có mặt đầy đủ khi Hội đồng họp đánh giá các KLTN.
–	Buổi bảo vệ KLTN do chủ tịch Hội đồng chủ trì. Việc bảo vệ phải được hoãn lại khi có nhiều hơn 1 thành viên hội đồng vắng mặt. Trong trường hợp có một thành viên Hội đồng vắng mặt đột xuất, nhưng không phải chủ tịch hoặc thư ký thì chủ tịch Hội đồng quyết định việc tiếp tục hay hoãn buổi bảo vệ căn cứ vào lĩnh vực chuyên môn của đề tài và tình hình thực tế có phù hợp để Hội đồng tiếp tục làm việc hay không.
–	CBHD và CBPB nếu không phải là thành viên Hội đồng phải gửi bản nhận xét bằng văn bản có chữ ký kèm ý kiến đánh giá xếp loại và điểm cụ thể dành cho KLTN cho thư ký Hội đồng trước khi Hội đồng bắt đầu làm việc.
–	Qui trình tổ chức bảo vệ KLTN gồm những bước cơ bản sau:
	Thư ký đọc quyết định thành lập hội đồng, danh sách sinh viên và tên đề tài, tên CBHD và CBPB.
	Chủ tịch hội đồng phát biểu, xác định các quy định làm việc thống nhất cho toàn hội đồng.
	Thư ký ghi biên bản đầy đủ họ tên các sinh viên tham gia thực hiện đề tài, nội dung trao đổi, thảo luận trong buổi bảo vệ.
	Sinh viên trình bày đề tài không quá 15 phút.
	CBPB (hoặc thư ký) đọc nhận xét đề tài
	Sinh viên trả lời các câu hỏi của CBPB và hội đồng.
	CBHD (hoặc thư ký) đọc nhận xét đề tài 
	Hội đồng đánh giá theo điểm cho từng SV trên phiếu chấm theo mẫu của Trường.
	Thư ký tập hợp phiếu nhận xét của CBHD, CBPB và phiếu chấm của các thành viên Hội đồng để tính điểm trung bình của đề tài.
	Chủ tịch Hội đồng có thể họp các thành viên để xem xét, trao đổi thêm về kết quả bảo vệ. Kết quả chính thức phải được công bố trước khi Hội đồng tuyên bố kết thúc buổi bảo vệ.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0200` | score `0.750000` | document `virhe4qa_0ed0a99b2e3186cca0ce`**

```text
Điều 4. Xét duyệt đề tài KLTN Khoa chịu trách nhiệm xét duyệt đề tài KLTN. Việc xét duyệt phải đảm bảo các yêu cầu sau: a. Đề tài có thể do giảng viên hay các doanh nghiệp đề xuất. b. Đề tài và đề cương nghiên cứu phải đảm bảo: - Tính khoa học, tính thực tiễn của đề tài; - Tính khả thi của đề tài (điều kiện thực hiện, thời gian, khối lượng…); - Đề tài phù hợp với mục tiêu đào tạo và chuẩn đầu ra của ngành đào tạo tương ứng; c. Các đề tài đã qua xét duyệt phải được công bố để sinh viên đăng ký. d. Mỗi đề tài KLTN được giao cho từ 1 đến 2 SV thực hiện với sự phân công trách nhiệm cụ thể cho từng SV có ghi rõ trong đề cương nghiên cứu. e. Mỗi đề tài KLTN phải do tối thiểu 1 CBHD có học vị từ thạc sĩ trở lên hướng dẫn, nếu đề tài do doanh nghiệp đề xuất thì có thể có thêm 1 đại diện của doanh nghiệp đồng hướng dẫn. f. CBHD đề tài không được là người có quan hệ ruột thịt với SV thực hiện (ch…
```

**Rank 2 | `chunk_0022` | score `0.547619` | document `virhe4qa_9697b02165a2baacbce3`**

```text
Điều 10. Thành lập hội đồng bảo vệ KLTN Mỗi đợt bảo vệ, ứng với mỗi ngành (hoặc có thể là liên ngành khi cần thiết) theo đề nghị của Trưởng Khoa phụ trách ngành, Hiệu Trưởng sẽ ra quyết định thành lập một hay nhiều hội đồng bảo vệ KLTN. Hội đồng có thành phần như sau: – Số thành viên của Hội đồng từ 3 đến 5 người. CBHD và CBPB có thể thuộc hoặc không thuộc Hội đồng. – Thành phần Hội đồng bao gồm chủ tịch hội đồng, ủy viên thư ký và các ủy viên khác. – Thành viên của Hội đồng là giảng viên có học vị từ thạc sĩ trở lên hoặc có thể mời những người có chuyên môn phù hợp ở ngoài trường. Số thành viên Hội đồng mời từ ngoài trường, nếu có, không quá 1/3 tổng số thành viên của Hội đồng. – Chủ tịch hội đồng là giảng viên có học vị từ tiến sĩ hoặc có học hàm từ giảng viên chính trở lên, có năng lực chuyên môn, kinh nghiệm giảng dạy và quản lý đào tạo, am hiểu lĩnh vực liên quan đến hướng nghiên c…
```

**Rank 3 | `chunk_0262` | score `0.375000` | document `virhe4qa_ba9a7671c41bd6474094`**

```text
Điều 8. Thẩm định đề án mở ngành đào tạo 1. Hiệu trưởng đề xuất thành lập Hội đồng thẩm định đề án mở ngành đào tạo trình ĐHQG-HCM ra quyết định thành lập Hội đồng thẩm định đề án mở ngành đào tạo bao gồm từ 5 đến 9 thành viên với cơ cấu như sau: + Chủ tịch: Hiệu trưởng/Phó hiệu trưởng Trường; + Ủy viên:  Đại diện lãnh đạo Ban Đại học/ Ban Sau đại học của ĐHQG-HCM;  Đại diện lãnh đạo Phòng Đào tạo đại học/Phòng Đào tạo sau đại học và Khoa học công nghệ và các phòng chức năng có liên quan của Trường;  Ủy viên phản biện (ít nhất 2): là đại diện các chuyên gia, các nhà khoa học có chuyên môn sâu về ngành đào tạo, các đơn vị sử dụng lao động liên quan đến ngành đào tạo, có trình độ từ thạc sĩ trở lên (đối với mở ngành đại học)/ tiến sĩ trở lên (đối với mở ngành sau đại học); + Thư ký: chuyên viên của ĐVQL. Các thành viên đã tham gia Tổ soạn thảo đề án mở ngành đào tạo thì không được là t…
```

**Rank 4 | `chunk_0120` | score `0.343643` | document `virhe4qa_1c466c63cf51a2b45f7a`**

```text
Điều 2. Giải thích từ ngữ Sinh viên thuộc chương trình tài năng có 02 hình thức là chính thức và dự bị, nằm trong tổng chỉ tiêu của chương trình: - Sinh viên chính thức: đảm bảo đáp ứng các tiêu chuẩn theo yêu cầu và được hưởng đầy đủ các quyền lợi của chương trình. - Sinh viên dự bị: cùng điều kiện học tập và học cùng chương trình đào tạo với sinh viên chính thức nhưng không được hưởng chính sách về học bổng tài năng. Sinh viên dự bị bao gồm các sinh viên trong lớp tài năng vi phạm điều kiện đạt sinh viên chính thức nhưng chưa bị loại ra khỏi chương trình trong các đợt xét sau mỗi học kỳ, và sinh viên mới tuyển bổ sung vào chương trình. Môn học cốt lõi: là môn học quan trọng trong CTĐT, là phần kiến thức không thể thiếu trong lĩnh vực chuyên môn liên quan tới ngành đào tạo chương trình tài năng. Danh sách môn học cốt lõi do Khoa đề nghị trong đề án mở chương trình tài năng. Seminar ngo…
```

**Rank 5 | `chunk_0274` | score `0.283333` | document `virhe4qa_c31538b810cd4921a313`**

```text
Điều 9. Tuyển bổ sung và loại ra khỏi chương trình, xét chính thức và dự bị Đối tượng tham gia CTTN là những sinh viên có năng lực xuất sắc, do đó, sau mỗi học kỳ BĐH quyết định việc loại sinh viên khỏi lớp tài năng, tuyển bổ sung sinh viên từ chương trình chuẩn vào lớp tài năng, xét chuyển đổi sinh viên chính thức và dự bị. Đầu mỗi học kỳ, Khoa xét và đề nghị lên BĐH các danh sách sinh viên tuyển bổ sung, bị loại ra khỏi các lớp CTTN hoặc danh sách sinh viên chính thức và dự bị theo các tiêu chuẩn như sau: 1. Loại khỏi chương trình Tại thời điểm xem xét, sinh viên rơi vào một trong các trường hợp sau: - Chưa tốt nghiệp khi đã quá thời gian thiết kế của khóa học và không có lý do đặc biệt. - Không đăng ký học đầy đủ các môn học CTTN bắt buộc trong học kỳ. - ĐTBTL nhỏ hơn 6,5 – tính tương ứng sau học kỳ 1 và sau học kỳ hè (kết quả học tập của học kỳ hè sẽ được tính chung vào kết quả học …
```


---

## 5. `query_095`

**Question:** Điểm sẽ được tính như thế nào trong trường hợp học cải thiện điểm đối với hệ đào tạo từ xa trình độ đại học của trường đại học công nghệ thông tin?

| Field | Value |
|---|---|
| Hybrid first gold rank | `21` |
| Dense first gold rank | `29` |
| Sparse first gold rank | `14` |
| Gold chunk | `chunk_0102` |
| Gold document | `virhe4qa_137ba0a57805debebb18` |
| Gold source index | `3055` |
| Hybrid top 1 | `chunk_0293` (score `0.833333`) |

### Gold context

```text
Điều  16. Đăng ký học tập, học lại và học cải thiện
1. 	Sinh viên được phép đăng ký học những môn học được Trường mở lớp trong học kỳ.
2. 	Học lại: Sinh viên phải đăng ký học lại các môn học chưa đạt (có điểm tổng kết môn học dưới 5,0) đối với những môn học có tính chất bắt buộc trong chương trình đào tạo . 
3. 	Học cải thiện: Sinh viên được đăng ký học lại môn học đã đạt để cải thiện điểm. Kết quả cao nhất trong các lần học sẽ được chọn để tính vào điểm trung bình chung tích lũy và điểm trung bình tích lũy toàn khóa.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0293` | score `0.833333` | document `virhe4qa_d447188b9c7756a04e95`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Quy chế này quy định những điều chung nhất về đào tạo đại học theo hình thức chính quy (gọi tắt là hệ đại học chính quy) của Trường Đại học Công nghệ Thông tin thuộc ĐHQG-HCM (gọi tắt là Trường). 2. Quy chế này áp dụng đối với các đơn vị, cá nhân liên quan trong đào tạo hệ đại học chính quy. 3. Quy định đào tạo đại học theo hình thức đào tạo từ xa (gọi tắt là hệ đại học từ xa) và đào tạo các chương trình đặc biệt của Trường được xây dựng, điều chỉnh phù hợp với đặc thù hệ đào tạo/chương trình dựa trên cơ sở quy chế này.
```

**Rank 2 | `chunk_0292` | score `0.833333` | document `virhe4qa_37b055fb6f41d3dfcda9`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Quy chế này quy định những điều chung nhất về tổ chức tuyển sinh và đào tạo theo hình thức đào tạo từ xa (hay đào tạo từ xa qua mạng) trình độ đại học của Trường Đại học Công nghệ Thông tin (gọi tắt là Trường) thuộc ĐHQG-HCM. 2. Quy chế này áp dụng đối với sinh viên, giảng viên, các đơn vị và cá nhân có liên quan đến đào tạo từ xa trình độ đại học của Trường.
```

**Rank 3 | `chunk_0297` | score `0.309524` | document `virhe4qa_31d7f0e5afe10c15cf33`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Văn bản này quy định về tuyển sinh, tổ chức và quản lý đào tạo đối với chương trình đào tạo liên thông từ trình độ đại học lên trình đô thạc sĩ hệ chính quy của Trường Đại học Công nghệ Thông tin – ĐHQG-HCM (sau đây gọi tắt là chương trình ĐH-ThS). 2. Quy định này áp dụng đối với tổ chức và cá nhân có liên quan đến chương trình ĐH-ThS.
```

**Rank 4 | `chunk_0085` | score `0.297619` | document `virhe4qa_37318b15d819dcedcaa6`**

```text
Điều 14. Đăng ký học tập Sinh viên được đăng ký học và thi các môn học trong chương trình đào tạo do bất kỳ một CSĐT nào thuộc ĐHQG-HCM hoặc hệ thống các trường thành viên của ASEAN University Network tổ chức giảng dạy. Việc chuyển đổi và công nhận tín chỉ được thực hiện theo quy định tại Điều 27 của Quy chế này. Nếu đăng ký học tại Trường thì đầu mỗi học kỳ, sinh viên phải tìm hiểu, nghiên cứu để nắm được chương trình giáo dục, các học phần được mở trong học kỳ và đăng ký các học phần qua hệ thống đăng ký hoặc bằng phiếu đăng ký theo quy định của Trường. Riêng sinh viên khóa tuyển mới, học kỳ đầu tiên sẽ học theo thời khóa biểu được xếp sẵn dựa trên kế hoạch giảng dạy mẫu theo chương trình đào tạo. 1. Số tín chỉ tối thiểu, tối đa Số tín chỉ tối thiểu, tối đa được tính bao gồm số các tín chỉ đăng ký tại Trường hoặc CSĐT khác. a) Trong học kỳ chính: - Số tín chỉ đăng ký học n trong mỗi h…
```

**Rank 5 | `chunk_0290` | score `0.295455` | document `virhe4qa_ad032722ed70ae0e715e`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng Đào tạo chất lượng cao trình độ đại học tại Trường Đại học Công nghệ Thông tin (ĐHCNTT) được thực hiện theo quy chế đào tạo đại học hệ chính quy theo học chế tín chỉ của Trường ĐHCNTT và các quy định cụ thể về đào tạo áp dụng cho hệ đại học hệ chính quy. Quy định này quy định một số vấn đề khác biệt hoặc quy định thêm đối với đào tạo chương trình chất lượng cao. Quy định này áp dụng cho các đơn vị quản lý chương trình Chất lượng cao (CT CLC), các đơn vị chuyên môn phụ trách chương trình đào tạo, giảng viên tham gia giảng dạy và sinh viên các CT CLC của Trường ĐHCNTT.
```


---

## 6. `query_057`

**Question:** Quy định đào tạo chương trình tài năng quy định điều gì?

| Field | Value |
|---|---|
| Hybrid first gold rank | `18` |
| Dense first gold rank | `37` |
| Sparse first gold rank | `10` |
| Gold chunk | `chunk_0012` |
| Gold document | `virhe4qa_50f39be6faf4383a68ec` |
| Gold source index | `7870` |
| Hybrid top 1 | `chunk_0064` (score `0.666667`) |

### Gold context

```text
Điều  1.	Phạm vi điều chỉnh và đối tượng áp dụng
Quy định này quy định những điều chung nhất về đào tạo Đại học chính quy CTTN của Trường ĐHCNTT thuộc ĐHQG-HCM và nằm trong khuôn khổ quy chế đào tạo theo học chế tín chỉ cho hệ đại học chính quy của Trường ĐHCNTT.
Quy định này áp dụng đối với thành viên BĐH, các Khoa có đào tạo CTTN, sinh viên hệ chính quy CTTN ở trình độ đại học của Trường ĐHCNTT.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0064` | score `0.666667` | document `virhe4qa_3abd8382b4312b3ad46f`**

```text
Điều 13. Quy định về tài chính 1. Học bổng sinh viên Học bổng chương trình: học bổng được cấp cho sinh viên theo từng học kỳ – một học kỳ tính là 5.0 tháng. Mức học bổng hàng năm do Hiệu trưởng quyết định. Tất cả các sinh viên tài năng theo danh sách chính thức từng học kỳ đều được hưởng học bổng này. Học bổng khuyến khích học tập: sinh viên tài năng được tham gia xét hưởng học bổng khuyến khích học tập theo quy định của nhà nước tương tự như các sinh viên chương trình khác (xét chung theo khóa, Khoa-Ngành). 2. Khen thưởng sinh viên Căn cứ vào tình hình kinh phí và hoạt động của các lớp CTTN, Hiệu trưởng quyết định thêm các hình thức khen thưởng sau: - Sinh viên đạt thành tích xuất sắc trong các cuộc thi học thuật. - Tuyên dương nỗ lực phấn đấu và tích cực tham gia phong trào, do tập thể lớp bình chọn. 3. Chi nghiệp vụ chuyên môn đặc biệt khác Ngoài các khoản chi thường xuyên kể trên, đ…
```

**Rank 2 | `chunk_0120` | score `0.642857` | document `virhe4qa_1c466c63cf51a2b45f7a`**

```text
Điều 2. Giải thích từ ngữ Sinh viên thuộc chương trình tài năng có 02 hình thức là chính thức và dự bị, nằm trong tổng chỉ tiêu của chương trình: - Sinh viên chính thức: đảm bảo đáp ứng các tiêu chuẩn theo yêu cầu và được hưởng đầy đủ các quyền lợi của chương trình. - Sinh viên dự bị: cùng điều kiện học tập và học cùng chương trình đào tạo với sinh viên chính thức nhưng không được hưởng chính sách về học bổng tài năng. Sinh viên dự bị bao gồm các sinh viên trong lớp tài năng vi phạm điều kiện đạt sinh viên chính thức nhưng chưa bị loại ra khỏi chương trình trong các đợt xét sau mỗi học kỳ, và sinh viên mới tuyển bổ sung vào chương trình. Môn học cốt lõi: là môn học quan trọng trong CTĐT, là phần kiến thức không thể thiếu trong lĩnh vực chuyên môn liên quan tới ngành đào tạo chương trình tài năng. Danh sách môn học cốt lõi do Khoa đề nghị trong đề án mở chương trình tài năng. Seminar ngo…
```

**Rank 3 | `chunk_0264` | score `0.583333` | document `virhe4qa_ad01f6fbc0dda7c3e229`**

```text
Điều 8. Chương trình đào tạo gắn với một ngành Chương trình đào tạo gắn với một ngành được phân loại như sau: 1. Chương trình chuẩn: được xây dựng theo quy định hiện hành; đáp ứng mục tiêu và chuẩn đầu ra của bậc trình độ tương ứng; có sự tham khảo chương trình của các trường đại học có uy tín trong nước hoặc trên thế giới; có sự tham gia của các nhà khoa học chuyên môn, giảng viên, cán bộ quản lý, đại diện của các tổ chức xã hội - nghề nghiệp, nhà tuyển dụng lao động và người đã tốt nghiệP. 2. Chương trình tài năng: được xây dựng dựa trên chương trình chuẩn nhằm tuyển chọn và tạo điều kiện phát triển cho các sinh viên xuất sắc. 3. Chương trình tiên tiến: được thiết kế, xây dựng dựa trên cơ sở chương trình đang được áp dụng ở trường đại học tiên tiến trên thế giới (gọi tắt là chương trình gốc) được giảng dạy bằng ngôn ngữ của chương trình gốc. 4. Chương trình nâng cao: được xây dựng dựa…
```

**Rank 4 | `chunk_0274` | score `0.380952` | document `virhe4qa_c31538b810cd4921a313`**

```text
Điều 9. Tuyển bổ sung và loại ra khỏi chương trình, xét chính thức và dự bị Đối tượng tham gia CTTN là những sinh viên có năng lực xuất sắc, do đó, sau mỗi học kỳ BĐH quyết định việc loại sinh viên khỏi lớp tài năng, tuyển bổ sung sinh viên từ chương trình chuẩn vào lớp tài năng, xét chuyển đổi sinh viên chính thức và dự bị. Đầu mỗi học kỳ, Khoa xét và đề nghị lên BĐH các danh sách sinh viên tuyển bổ sung, bị loại ra khỏi các lớp CTTN hoặc danh sách sinh viên chính thức và dự bị theo các tiêu chuẩn như sau: 1. Loại khỏi chương trình Tại thời điểm xem xét, sinh viên rơi vào một trong các trường hợp sau: - Chưa tốt nghiệp khi đã quá thời gian thiết kế của khóa học và không có lý do đặc biệt. - Không đăng ký học đầy đủ các môn học CTTN bắt buộc trong học kỳ. - ĐTBTL nhỏ hơn 6,5 – tính tương ứng sau học kỳ 1 và sau học kỳ hè (kết quả học tập của học kỳ hè sẽ được tính chung vào kết quả học …
```

**Rank 5 | `chunk_0011` | score `0.361111` | document `virhe4qa_b2fe2a70f6d2f5913fdb`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Văn bản này quy định về đào tạo ngoại ngữ đối với các chương trình đào tạo hệ đại học chính quy của Trường Đại học Công nghệ Thông tin (gọi tắt là Trường) bao gồm: chương trình giảng dạy, kiểm tra xếp lớp đầu khóa, xét miễn học các môn học ngoại ngữ, chuẩn ngoại ngữ xét tốt nghiệp và tổ chức giảng dạy các môn học chuyên ngành bằng ngoại ngữ. 2. Quy định này áp dụng với sinh viên các loại chương trình đại học chính quy, bao gồm: chương trình chuẩn (CTC) (trước đây gọi là chương trình đại trà), chương trình chất lượng cao (CLC), chương trình tài năng (CTTN), chương trình tiên tiến (CTTT), chương trình văn bằng hai (VB2), chương trình liên thông từ cao đẳng lên đại học (LT). 3. Quy định này áp dụng bắt buộc cho các khóa tuyển sinh từ năm 2022. Các khóa tuyển sinh trước năm 2022 có thể lựa chọn áp dụng quy định này hoặc quy định được ban hà…
```


---

## 7. `query_082`

**Question:** Vì sao UIT xây dựng và triển khai các chương trình CLC?

| Field | Value |
|---|---|
| Hybrid first gold rank | `13` |
| Dense first gold rank | `7` |
| Sparse first gold rank | `29` |
| Gold chunk | `chunk_0176` |
| Gold document | `virhe4qa_58eca8d65dc1fc4283f7` |
| Gold source index | `7115` |
| Hybrid top 1 | `chunk_0119` (score `0.750000`) |

### Gold context

```text
Điều  3.        Mục tiêu đào tạo
Nhằm thực hiện tầm nhìn, sứ mạng của Trường ĐHCNTT, Trường xây dựng và triển khai các chương trình chất lượng cao nhằm cung cấp những chương trình đào tạo có chất lượng tốt và có tính cạnh tranh cao trên thị trường lao động trong thời kỳ hội nhập kinh tế khu vực và thế giới.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0119` | score `0.750000` | document `virhe4qa_da5e1bc92b41223a8639`**

```text
Điều 2. Giải thích từ ngữ Chương trình đại trà là chương trình đào tạo trình độ đại học hệ chính quy được ĐHQG-HCM cho phép triển khai đào tạo tại Trường ĐHCNTT, có mức trần học phí theo quy định hiện hành của Chính phủ. Chương trình chất lượng cao (CT CLC) là chương trình đào tạo trình độ đại học hệ chính quy có các điều kiện đảm bảo chất lượng và chuẩn đầu ra cao hơn chương trình đại trà tương ứng của cùng một ngành hoặc chuyên ngành đào tạo. Ngoại ngữ chính của chương trình chất lượng cao (sau đây gọi tắt là ngoại ngữ) là ngoại ngữ mà chương trình chất lượng cao đó có tổ chức giảng dạy chính. Website môn học: Mỗi lớp học lý thuyết được cấp 01 website môn học vào đầu học kỳ tại hệ thống hỗ trợ học tập của Trường (courses.uit.edu.vn), gọi tắt là Moodle. Chương trình đại trà tương ứng: là chương trình đại trà của cùng một ngành hoặc chuyên ngành với chương trình chất lượng cao. Đơn vị p…
```

**Rank 2 | `chunk_0216` | score `0.666667` | document `virhe4qa_ae295b2fe64356a35465`**

```text
Điều 5. Chương trình đào tạo CT CLC được xây dựng trên nền chương trình đào tạo đại trà tương ứng và theo quy định xây dựng chương trình đào tạo của Trường ĐHCNTT. CT CLC có sự khác biệt so với chương trình đại trà ở những điểm dưới đây: - Chuẩn đầu ra của CT CLC phải cao hơn chuẩn đầu ra của chương trình đại trà tương ứng về năng lực chuyên môn; năng lực ngoại ngữ; năng lực làm việc nhóm; khả năng thích nghi với môi trường công tác. - Chuẩn đầu ra ngoại ngữ: để được xét tốt nghiệp, sinh viên phải hoàn tất chương trình ngoại ngữ bắt buộc trong chương trình đào tạo và có một trong các chứng chỉ ngoại ngữ đạt trình độ tối thiểu: • Tiếng Anh: bậc 4/6 theo khung năng lực ngoại ngữ 6 bậc dùng cho Việt Nam. Cụ thể mức quy đổi sang các chứng chỉ quốc tế được quy định trong Quy định đào tạo ngoại ngữ hiện hành của Trường. • Tiếng Nhật: tương đương JLPT N3. - Để đảm bảo tính liên thông giữa CT C…
```

**Rank 3 | `chunk_0198` | score `0.538462` | document `virhe4qa_06d792ed3048eb2fed78`**

```text
Điều 4. Tổ chức và điều hành CT CLC Ban Giám hiệu giao nhiệm vụ cho đơn vị quản lý triển khai chương trình, phối hợp chặt chẽ với đơn vị chuyên môn phụ trách ngành đào tạo. Đơn vị quản lý triển khai chịu trách nhiệm vận hành chương trình và báo cáo định kỳ cho Ban Giám hiệu.
```

**Rank 4 | `chunk_0229` | score `0.450000` | document `virhe4qa_d6c52a4856e2361059a3`**

```text
Điều 6. Tổ chức chương trình - Các lớp CT CLC được ưu tiên về cơ sở vật chất cho việc học tập và nghiên cứu, được trang bị phòng học riêng có các thiết bị hỗ trợ giảng dạy và học tập hiện đại; có đủ giáo trình, tài liệu tham khảo trong, ngoài nước và được cập nhật thường xuyên; có thư viện và thư viện điện tử cho giảng viên, sinh viên tra cứu, sử dụng trong giảng dạy, học tập và nghiên cứu khoa học. - Về chất lượng quản lý và giảng dạy: Các lớp CT CLC được quản lý và giảng dạy bởi các cán bộ có chuyên môn giỏi và có kinh nghiệm trong công tác, đảm bảo chất lượng đào tạo và dịch vụ hỗ trợ chất lượng cao cho sinh viên.
```

**Rank 5 | `chunk_0127` | score `0.226316` | document `virhe4qa_2f97aab7d2d506cf57a9`**

```text
Điều 2. Giải thích từ ngữ Chương trình đào tạo khác là chương trình đào tạo trình độ đại học hệ chính quy được ĐHQG-HCM cho phép triển khai đào tạo tại Trường ĐHCNTT. Chương trình Tiên tiến (CTTT) là chương trình đào tạo kết hợp sử dụng chương trình đào tạo nước ngoài. Website môn học: Mỗi lớp học lý thuyết được cấp 01 website môn học vào đầu học kỳ tại hệ thống hỗ trợ học tập của Trường (courses.uit.edu.vn). Đơn vị phụ trách chuyên môn (sau đây gọi tắt là đơn vị chuyên môn): Khoa được giao phụ trách về mặt chuyên môn cho CTTT. Đại học đối tác nước ngoài (ĐHNN): là đơn vị có ký kết hợp tác (MOU) với Trường đào tạo trình độ đại học gồm cung cấp chương trình đào tạo, đề cương môn học, hỗ trợ giảng viên tham gia giảng dạy và công nhận kết quả đào tạo tại Trường nếu sinh viên học chuyển tiếp.
```


---

## 8. `query_098`

**Question:** Đơn vị quản lý môn học có thể là cái gì?

| Field | Value |
|---|---|
| Hybrid first gold rank | `13` |
| Dense first gold rank | `37` |
| Sparse first gold rank | `8` |
| Gold chunk | `chunk_0126` |
| Gold document | `virhe4qa_53038edd68d0bf0e03c6` |
| Gold source index | `4019` |
| Hybrid top 1 | `chunk_0222` (score `0.833333`) |

### Gold context

```text
Điều  2. Giải thích từ ngữ
1. Học liệu điện tử: là các tài liệu học tập được số hóa theo các định dạng đa phương tiện trên máy tính (văn bản, âm thanh, hình ảnh, video, đồ họa, …), được cấu trúc theo kịch bản dạy và học nhất định, có nội dung đáp ứng chuẩn đầu ra của một môn học. Video bài giảng là thành phần bắt buộc phải có của học liệu điện tử.
2. Phương thức dạy học trực tiếp: là phương thức dạy và học có sự gặp mặt trực tiếp giữa giảng viên và sinh viên.
3. Phương thức dạy học trực tuyến (DHTT): là phương thức dạy và học thông qua phần mềm ứng dụng trên môi trường mạng để thực hiện việc giảng dạy và học tập, qua đó sinh viên có thể tự học mọi lúc mọi nơi với các học liệu điện tử; sinh viên có thể trao đổi với nhau và với giảng viên thông qua các phần mềm ứng dụng trên môi trường mạng.
4. Phương thức dạy học kết hợp (DHKH): là phương thức dạy và học có sự phối hợp một cách hợp lý, có chủ đích giữa phương thức dạy học trực tuyến với phương thức dạy học trực tiếp.
5. Đơn vị quản lý môn học (ĐVQLMH): Đơn vị được Trường giao quản lý chuyên môn cho môn học, có thể là Khoa, Bộ môn, Trung tâm hoặc Tổ phụ trách môn học.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0222` | score `0.833333` | document `virhe4qa_954fe80222865e12bc56`**

```text
Điều 5. Trách nhiệm chuẩn bị và tổ chức thi P.ĐTĐH, Văn phòng các Chương trình đặc biệt (VPĐB) và các khoa, bộ môn, trung tâm (gọi tắt là Đơn vị quản lý môn học - ĐVQLMH) có trách nhiệm chuẩn bị và tổ chức thi cho những môn học do mình quản lý. Đơn vị có trách nhiệm chuẩn bị và tổ chức thi cho môn học được gọi tắt là Đơn vị tổ chức thi.
```

**Rank 2 | `chunk_0158` | score `0.833333` | document `virhe4qa_a8b40da54ab8837d2028`**

```text
Điều 25. Trách nhiệm của Đơn vị quản lý môn học 1. Chuẩn bị thi, tổ chức thi, tổ chức chấm thi và chấm phúc khảo cho những môn học do đơn vị đó quản lý; 2. Bàn giao bài thi và hồ sơ thi cho P.ĐTĐH sau khi hoàn tất công tác chấm phúc khảo; 3. Lưu trữ hồ sơ thi.
```

**Rank 3 | `chunk_0043` | score `0.450000` | document `virhe4qa_6fc43784a4bf56ae42c2`**

```text
Điều 11. Quyền hạn và trách nhiệm của đơn vị quản lý chuyên môn đối với môn học 1. Xác định phương thức giảng dạy cho từng môn học theo từng học kỳ, tổ chức giảng dạy và kiểm soát chất lượng giảng dạy. 2. Tập huấn kỹ năng cần thiết cho giảng viên và sinh viên để triển khai DHTT, DHKH hiệu quả.
```

**Rank 4 | `chunk_0133` | score `0.416667` | document `virhe4qa_0c8e7f2a7b88cc78ebf1`**

```text
Điều 2. Từ ngữ sử dụng và chữ viết tắt 1. Đơn vị quản lý môn học (ĐVQLMH): Khoa, bộ môn, tổ môn học hoặc một đơn vị khác của Trường được giao nhiệm vụ quản lý về mặt chuyên môn đối với một môn học theo Danh mục các môn học đại học của Trường. 2. Giảng viên thỉnh giảng: Giảng viên hoặc trợ giảng không phải là cán bộ cơ hữu của Trường ĐHCNTT. 3. Khảo sát giảng dạy: Khảo sát lấy ý kiến phản hồi từ người học về hoạt động giảng dạy của giảng viên quy định tại Quyết định số 08/QĐ-ĐHCNTT-ĐBCL ngày 17 tháng 12 năm 2013 của Hiệu trưởng Trường ĐHCNTT. 4. Hệ thống Moodle: Hệ thống hỗ trợ học tập online của Trường tại địa chỉ courses.uit.edu.vn.
```

**Rank 5 | `chunk_0225` | score `0.276923` | document `virhe4qa_a4f98999335b259b255a`**

```text
Điều 5. Tổ chức thực hiện - Phòng Đào tạo Đại học có trách nhiệm quản lý toàn bộ quá trình giảng dạy - học tập. - Phòng Thanh tra Pháp chế và Đảm bảo Chất lượng có nhiệm vụ thanh tra, giám sát, đảm bảo quá trình giảng dạy - học tập tuân thủ các quy định của Trường. - Các Khoa, Bộ môn, Trung tâm Ngoại ngữ, Văn phòng các chương trình đặc biệt và các đơn vị phụ trách chuyên môn cho môn học có trách nhiệm phối hợp mở lớp, phân công cán bộ giảng dạy và quản lý chất lượng giảng dạy. - Các cán bộ giảng dạy có trách nhiệm thực hiện nhiệm vụ được phân công và đảm bảo chất lượng giảng dạy theo các quy định của Trường.
```


---

## 9. `query_076`

**Question:** Trường tổ chức lớp của hệ đào tạo từ xa trình độ đại học của trường đại học công nghệ thông tin như thế nào?

| Field | Value |
|---|---|
| Hybrid first gold rank | `11` |
| Dense first gold rank | `34` |
| Sparse first gold rank | `6` |
| Gold chunk | `chunk_0069` |
| Gold document | `virhe4qa_413730d3490a5b999f83` |
| Gold source index | `2977` |
| Hybrid top 1 | `chunk_0292` (score `1.000000`) |

### Gold context

```text
Điều  13. Lớp học
Trường tổ chức lớp theo khóa học, theo môn học cho sinh viên theo học hệ ĐTTX tùy theo tình hình và điều kiện cụ thể
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0292` | score `1.000000` | document `virhe4qa_37b055fb6f41d3dfcda9`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Quy chế này quy định những điều chung nhất về tổ chức tuyển sinh và đào tạo theo hình thức đào tạo từ xa (hay đào tạo từ xa qua mạng) trình độ đại học của Trường Đại học Công nghệ Thông tin (gọi tắt là Trường) thuộc ĐHQG-HCM. 2. Quy chế này áp dụng đối với sinh viên, giảng viên, các đơn vị và cá nhân có liên quan đến đào tạo từ xa trình độ đại học của Trường.
```

**Rank 2 | `chunk_0293` | score `0.666667` | document `virhe4qa_d447188b9c7756a04e95`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Quy chế này quy định những điều chung nhất về đào tạo đại học theo hình thức chính quy (gọi tắt là hệ đại học chính quy) của Trường Đại học Công nghệ Thông tin thuộc ĐHQG-HCM (gọi tắt là Trường). 2. Quy chế này áp dụng đối với các đơn vị, cá nhân liên quan trong đào tạo hệ đại học chính quy. 3. Quy định đào tạo đại học theo hình thức đào tạo từ xa (gọi tắt là hệ đại học từ xa) và đào tạo các chương trình đặc biệt của Trường được xây dựng, điều chỉnh phù hợp với đặc thù hệ đào tạo/chương trình dựa trên cơ sở quy chế này.
```

**Rank 3 | `chunk_0297` | score `0.392857` | document `virhe4qa_31d7f0e5afe10c15cf33`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Văn bản này quy định về tuyển sinh, tổ chức và quản lý đào tạo đối với chương trình đào tạo liên thông từ trình độ đại học lên trình đô thạc sĩ hệ chính quy của Trường Đại học Công nghệ Thông tin – ĐHQG-HCM (sau đây gọi tắt là chương trình ĐH-ThS). 2. Quy định này áp dụng đối với tổ chức và cá nhân có liên quan đến chương trình ĐH-ThS.
```

**Rank 4 | `chunk_0168` | score `0.333333` | document `virhe4qa_d8046edbe4df65be275c`**

```text
Điều 28. Ứng dụng công nghệ thông tin trong tổ chức đào tạo 1. Ứng dụng công nghệ thông tin trong tổ chức đào tạo qua mạng là việc sử dụng các trang thiết bị điện tử, phần mềm, học liệu điện tử và mạng viễn thông (chủ yếu là mạng Internet) cho các hoạt động giảng dạy và học tập nhằm đổi mới phương pháp dạy - học, nâng cao hiệu quả công tác đào tạo. 2. Môn học đào tạo qua mạng có thể được tổ chức đào tạo theo phương thức qua mạng hoàn toàn (bao gồm cả phương thức trực tuyến) hoặc phương thức kết hợp đào tạo qua mạng (chỉ triển khai một phần nội dung môn học qua mạng). Đơn vị quản lý chuyên môn đối với môn học đào tạo qua mạng có trách nhiệm đảm bảo chất lượng giảng dạy và đánh giá môn học không thấp hơn chất lượng lớp học theo phương thức trực tiếP. 3. Đối với đào tạo theo hình thức chính quy, tối đa 30% tổng khối lượng của chương trình đào tạo được thực hiện bằng phương thức qua mạng. T…
```

**Rank 5 | `chunk_0294` | score `0.326923` | document `virhe4qa_43ff1f111c35b3d2dce1`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Mỗi học kỳ, Trường Đại học Công nghệ Thông tin thuộc Đại học Quốc gia thành phố Hồ Chí Minh (Trường) tổ chức 01 lần thi lý thuyết giữa kỳ và 01 lần thi lý thuyết cuối kỳ tập trung trực tiếp hoặc trực tuyến (gọi chung là thi) cho các môn học được mở trong học kỳ đó. Thời gian tổ chức thi được qui định trên biểu đồ giảng dạy năm học. Quy định này quy định chung về việc tổ chức các đợt thi bao gồm các công tác: chuẩn bị thi, tổ chức thi, chấm thi, công bố điểm, phúc khảo, chế độ lưu trữ và xử lý vi phạm. Quy định này áp dụng đối với hệ đại học chính quy. Các chương trình đặc biệt có thể có kế hoạch thi riêng tùy theo đặc thù của chương trình. 2. Các hình thức thi bao gồm: Tự luận (hoặc tự luận kết hợp với trắc nghiệm) Trắc nghiệm Vấn đáp Đồ án 3. Việc tổ chức thi theo hình thức trực tuyến thực hiện theo quy định riêng.
```


---

## 10. `query_021`

**Question:** Giao tiếp bằng ngoại ngữ có phải một kỹ năng được kiểm tra trong các đợt kiểm tra năng lực tiếng Anh do Trung tâm Ngoại ngữ của Trường tổ chức không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `8` |
| Dense first gold rank | `10` |
| Sparse first gold rank | `5` |
| Gold chunk | `chunk_0217` |
| Gold document | `virhe4qa_97cc3a44cfea82133821` |
| Gold source index | `8689` |
| Hybrid top 1 | `chunk_0124` (score `0.833333`) |

### Gold context

```text
Điều  5.        Xét miễn các môn học tiếng Anh 
1.        Sinh viên được xét miễn học các môn tiếng Anh tương ứng nếu có một trong các chứng chỉ/chứng nhận đạt trình độ tối thiểu theo quy định tại Bảng 3. Sinh viên được miễn môn học nào thì đồng thời được miễn những môn học ở cấp độ thấp hơn mà sinh viên chưa học hoặc chưa đạt.
Dưới đây là các mức điểm của  chứng chỉ/chứng nhận và môn học được miễn theo các điểm số tương ứng:

TOEIC Nghe-Đọc đạt từ  350 - dưới 400, TOEIC Nói-Viết đạt từ 100 – dưới 120, TOEFL iBT đạt từ 32 – dưới 35, IELTS đạt 3.5, VNU-EPT đạt từ 152 - dưới 165, chứng chỉ Cambridge English KET (Merit) hay A2 Key  (Grade C) sẽ được miễn Anh văn 1 (mã môn ENG01) đối với cả chương trình CTC/ CTTN và CTTT.

TOEIC Nghe-Đọc đạt từ  400 - dưới 450, TOEIC Nói-Viết đạt từ 120 – dưới 140, TOEFL iBT đạt từ 32 – dưới 35, IELTS đạt 3.5, VNU-EPT đạt từ 152 - dưới 165, chứng chỉ Cambridge English KET (Merit) hay A2 Key  (Grade C) sẽ được miễn Anh văn 2 (mã môn ENG02) đối với cả chương trình CTC/ CTTN và CTTT.

TOEIC Nghe-Đọc đạt từ  450 - dưới 500, TOEIC Nói-Viết đạt từ 140 – dưới 160, TOEFL iBT đạt từ 45 – dưới 50, IELTS đạt 4.5, VNU-EPT đạt từ 176 - dưới 201, chứng chỉ Cambridge English A2 Key (Grade A) hoặc  B1 Preliminary (Grade C) hoặc B1 Business Preliminary (Pass) sẽ được miễn Anh văn 3 (mã môn ENG03) đối với cả chương trình CTC/ CTTN và CTTT.

TOEIC Nghe-Đọc đạt từ  550 - dưới 555, TOEIC Nói-Viết đạt từ 160 – dưới 180, TOEFL iBT đạt từ 50 – dưới 60, IELTS đạt 5.0, VNU-EPT đạt từ 201 - dưới 251, chứng chỉ Cambridge English KET B1 Preliminary (Grade B) hoặc B1 Business Preliminary (Merit) sẽ được miễn Anh văn 4 (mã môn ENG04) đối với chương trình CTTT.

TOEIC Nghe-Đọc đạt từ  555 trở lên, TOEIC Nói-Viết đạt từ 180 trở lên, TOEFL iBT đạt từ 60 trở lên, IELTS đạt 5.5 trở lên, VNU-EPT đạt từ 251 trở lên, chứng chỉ Cambridge English B1 Preliminary (Grade A) hoặc B2 First (Grade C) hoặc B1 Business Preliminary (Distinction) hoặc B2 Business Vantage (Grade C) sẽ được miễn Anh văn 5 (mã môn ENG05) đối với chương trình CTTT.
2.        Hàng năm, Trung tâm Ngoại ngữ của Trường tổ chức 04 đợt kiểm tra năng lực tiếng Anh với 04 kỹ năng nghe – đọc – nói – viết và cấp chứng nhận nội bộ. Sinh viên có thể dùng chứng nhận nội bộ này tương đương với chứng chỉ TOEIC để nộp xét miễn các môn tiếng Anh như trong khoảng 1 điều 5.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0124` | score `0.833333` | document `virhe4qa_ffb03558a4ad0f1f974d`**

```text
Điều 2. Mục đích đào tạo ngoại ngữ 1 . Chương trình giảng dạy tiếng Anh nhằm mục đích giúp sinh viên: a . Phát triển toàn diện 4 kỹ năng sử dụng tiếng Anh tổng quát: nghe, nói, đọc, viết; phát triển kỹ năng sử dụng tiếng Anh chuyên ngành ở mức độ phù hợp với trình độ đào tạo, ngành đào tạo và loại chương trình đào tạo. b . Đáp ứng được chuẩn ngoại ngữ tiếng Anh đầu ra theo quy định của ĐHQG-HCM. 2 . Các ngoại ngữ khác tiếng Anh được đưa vào nhằm khuyến khích sinh viên học để đáp ứng nhu cầu đa dạng của thị trường lao động. 3 . Sinh viên chương trình chuẩn, chương trình tài năng, chương trình văn bằng hai và chương trình liên thông được chọn một trong các chứng chỉ ngoại ngữ: tiếng Anh, tiếng Nhật hoặc tiếng Pháp để xét tốt nghiệp, tuy nhiên sinh viên vẫn phải hoàn thành chương trình ngoại ngữ quy định tại Điều 3 (ngoại trừ chương trình định hướng Nhật Bản). Các chuẩn quá trình được xây …
```

**Rank 2 | `chunk_0201` | score `0.611111` | document `virhe4qa_37a54d5cd4cb142fc4be`**

```text
Điều 4. Kiểm tra xếp lớp đầu khóa cho sinh viên thuộc CTC, CTTN, CTTT 1. Vào đầu khóa học, Trường tổ chức kiểm tra tiếng Anh để xếp lớp cho tất cả sinh viên khóa tuyển mới. Đề kiểm tra xếp lớp đầu khóa có dạng thức như đề thi TOEIC 2 kỹ năng (nghe và đọc). Căn cứ vào kết quả kiểm tra tiếng Anh, sinh viên được xếp vào lớp tiếng Anh phù hợp với trình độ của sinh viên theo thông tin xếp lớp đầu khoá. Tùy theo tình hình thực tế, các mức điểm có thể được Hiệu trưởng quyết định điều chỉnh theo đề xuất hợp lý của bộ phận chuyên môn. 2. Xếp lớp đầu khóa Điểm kiểm tra(dạng thức TOEIC nghe và đọc) Dưới 300 điểm sẽ không được học Anh văn 1 (mã môn ENG01), được đăng ký học Anh văn sơ cấp ngoài CTĐT chính quy do Trung tâm Ngoại ngữ phụ trách (không bắt buộc). Từ 300 – 345 điểm sẽ Học Anh Văn 1 (Mã môn ENG01) Từ 350 – 395 điểm sẽ Miễn Anh văn 1 (mã môn ENG01) và Học Anh văn 2 (mã môn ENG02). Từ 400-4…
```

**Rank 3 | `chunk_0032` | score `0.533333` | document `virhe4qa_d129482c2382716cf531`**

```text
Điều 11. Đào tạo ngoại ngữ - Vào đầu khóa học, sinh viên CT CLC phải tham dự kiểm tra ngoại ngữ đầu vào để phân loại trình độ theo quy định chung của Trường. - Trong quá trình học, sinh viên phải đạt các chuẩn quá trình và chuẩn đầu ra theo quy định về đào tạo ngoại ngữ hiện hành của Trường. - Nhằm tăng cường kỹ năng ngoại ngữ song song với việc trang bị kiến thức chuyên ngành cho sinh viên, những môn học giảng dạy bằng ngoại ngữ được triển khai giảng dạy theo lộ trình được thiết kế trong chương trình đào tạo. - Tùy theo tình hình cụ thể, Trường có thể mở các chương trình ngoại ngữ tăng cường nhằm giúp sinh viên đạt được chuẩn đầu ra theo quy định.
```

**Rank 4 | `chunk_0183` | score `0.500000` | document `virhe4qa_a41467c90904194f8a7b`**

```text
Điều 3. Mục tiêu đào tạo CTTT nhằm phát hiện và đào tạo những sinh viên xuất sắc, có kiến thức chuyên môn sâu về một chuyên ngành đào tạo, có kỹ năng và ngoại ngữ tốt thông qua việc ưu tiên đầu tư cơ sở vật chất trang thiết bị, đội ngũ giảng viên giỏi và áp dụng phương pháp dạy và học hiện đại theo định hướng tiêu chuẩn của các đại học tiên tiến trong khu vực và quốc tế. Sinh viên tốt nghiệp đáp ứng các yêu cầu: - Có kiến thức chuyên môn vững vàng, năng lực sáng tạo cao. - Có trình độ tiếng Anh thành thạo về cả 04 kỹ năng: nghe, nói, đọc, viết đáp ứng được yêu cầu giao tiếp trong môi trường làm việc quốc tế.
```

**Rank 5 | `chunk_0011` | score `0.325000` | document `virhe4qa_b2fe2a70f6d2f5913fdb`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Văn bản này quy định về đào tạo ngoại ngữ đối với các chương trình đào tạo hệ đại học chính quy của Trường Đại học Công nghệ Thông tin (gọi tắt là Trường) bao gồm: chương trình giảng dạy, kiểm tra xếp lớp đầu khóa, xét miễn học các môn học ngoại ngữ, chuẩn ngoại ngữ xét tốt nghiệp và tổ chức giảng dạy các môn học chuyên ngành bằng ngoại ngữ. 2. Quy định này áp dụng với sinh viên các loại chương trình đại học chính quy, bao gồm: chương trình chuẩn (CTC) (trước đây gọi là chương trình đại trà), chương trình chất lượng cao (CLC), chương trình tài năng (CTTN), chương trình tiên tiến (CTTT), chương trình văn bằng hai (VB2), chương trình liên thông từ cao đẳng lên đại học (LT). 3. Quy định này áp dụng bắt buộc cho các khóa tuyển sinh từ năm 2022. Các khóa tuyển sinh trước năm 2022 có thể lựa chọn áp dụng quy định này hoặc quy định được ban hà…
```


---

## 11. `query_072`

**Question:** Trong một học kỳ chính Trường tổ chức bao nhiêu đợt kiểm tra?

| Field | Value |
|---|---|
| Hybrid first gold rank | `8` |
| Dense first gold rank | `14` |
| Sparse first gold rank | `6` |
| Gold chunk | `chunk_0137` |
| Gold document | `virhe4qa_5d5e8dbec5b7d71b3d74` |
| Gold source index | `2025` |
| Hybrid top 1 | `chunk_0220` (score `1.000000`) |

### Gold context

```text
Điều  20. Tổ chức đánh giá môn học
1.	Điều kiện dự thi kết thúc học phần
Sinh viên được dự thi kết thúc học phần khi có mặt từ 80% trở lên số buổi học theo thời khóa biểu của học phần đó, trừ những sinh viên được Hiệu trưởng cho phép học chương trình song ngành.
Giảng viên có thể để nghị P.ĐTĐH không cho sinh viên dự thi kết thúc học phần theo quy định riêng của môn học đã công bố cho sinh viên.
2.	Tổ chức các đợt thi tập trung
Mỗi học kỳ chính Trường tổ chức một kỳ kiểm tra giữa kỳ và một kỳ thi kết thúc học kỳ. Hai đợt thi được tổ chức tập trung theo kế hoạch giảng dạy và học tập của Trường. Khoa, bộ môn, giảng viên không tổ chức thi ngoài các đợt đã thông báo. Hiệu trưởng quy định thời gian học, ôn thi và thi cho từng học kỳ.
3.	Tổ chức đánh giá môn học
Việc tổ chức đánh giá học phần được thực hiện theo đề cương chi tiết đã phê duyệt. Quy định cụ thể việc tổ chức thi kết thúc học phần, ra đề thi, chấm thi, chấm phúc khảo và xử lý điểm sau chấm phúc khảo; thông báo kết quả, công tác bảo quản, lưu trữ được áp dụng theo Quy định tổ chức đánh giá các môn học hệ đại học chính quy của Trường ĐHCNTT.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0220` | score `1.000000` | document `virhe4qa_59e0dda780d18b8d7f20`**

```text
Điều 5. Học kỳ, năm học 1. Học kỳ là thời gian để sinh viên hoàn thành một số học phần của chương trình đào tạo. Một học kỳ chính có 15 tuần thực học và 2 đến 3 tuần dành cho đánh giá hoạt động đào tạo (thi cuối kỳ, thi giữa kỳ, kiểm tra,…). Một học kỳ hè có tối thiểu 5 tuần thực học và 1 tuần thi. Căn cứ vào tình hình thực tế mỗi năm, kế hoạch giảng dạy của học kỳ có thể được điều chỉnh theo quyết định của Hiệu trưởng. 2. Một năm học có 2 học kỳ chính. Tùy theo điều kiện, Trường có thể tổ chức thêm học kỳ hè. Việc đăng ký học phần học kỳ hè được quy định tại Điều 14 của quy chế này. Kế hoạch học tập của mỗi học kỳ và năm học bao gồm thời gian biểu tiến hành các hoạt động giảng dạy, học tập và đánh giá hoạt động đào tạo. Kế hoạch học tập được công bố rộng rãi trên trang thông tin điện tử của Trường.
```

**Rank 2 | `chunk_0294` | score `0.500000` | document `virhe4qa_43ff1f111c35b3d2dce1`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Mỗi học kỳ, Trường Đại học Công nghệ Thông tin thuộc Đại học Quốc gia thành phố Hồ Chí Minh (Trường) tổ chức 01 lần thi lý thuyết giữa kỳ và 01 lần thi lý thuyết cuối kỳ tập trung trực tiếp hoặc trực tuyến (gọi chung là thi) cho các môn học được mở trong học kỳ đó. Thời gian tổ chức thi được qui định trên biểu đồ giảng dạy năm học. Quy định này quy định chung về việc tổ chức các đợt thi bao gồm các công tác: chuẩn bị thi, tổ chức thi, chấm thi, công bố điểm, phúc khảo, chế độ lưu trữ và xử lý vi phạm. Quy định này áp dụng đối với hệ đại học chính quy. Các chương trình đặc biệt có thể có kế hoạch thi riêng tùy theo đặc thù của chương trình. 2. Các hình thức thi bao gồm: Tự luận (hoặc tự luận kết hợp với trắc nghiệm) Trắc nghiệm Vấn đáp Đồ án 3. Việc tổ chức thi theo hình thức trực tuyến thực hiện theo quy định riêng.
```

**Rank 3 | `chunk_0108` | score `0.450000` | document `virhe4qa_f4704ead38c4dfcd81ba`**

```text
Điều 17. Xử lý học vụ Hằng năm, Trường tiến hành xử lý học vụ 01 đợt vào tháng 12. 1. Cảnh báo học vụ: Sinh viên bị cảnh báo học tập nếu thuộc một trong những trường hợp sau: - Không đóng học phí theo quy định; - Không dự kiểm tra/thi kết thúc môn học quá 30% số môn học đăng ký trong năm học; 2. Đình chỉ học tập: - Sinh viên bị đình chỉ học tập 1 năm học nếu vi phạm lần đầu trong việc đi thi hộ hoặc nhờ người thi hộ. - Đình chỉ học tập có thời hạn: áp dụng đối với những sinh viên đang trong thời gian bị cảnh báo mà vẫn vi phạm kỷ luật hoặc vi phạm nghiêm trọng các hành vi sinh viên không được làm; sinh viên vi phạm pháp luật bị xử phạt tù nhưng cho hưởng án treo. 3. Buộc thôi học: Sinh viên bị buộc thôi học và xóa tên khỏi danh sách sinh viên nếu rơi vào một trong những trường hợp sau đây: - Đã bị cảnh báo học vụ 2 lần liên tiếp nhưng tiếp tục vi phạm mức cảnh báo học vụ; - Bị đình chỉ …
```

**Rank 4 | `chunk_0138` | score `0.433333` | document `virhe4qa_a97cab2fc20aeb80269e`**

```text
Điều 20. Đánh giá kết quả học tập 1. Giảng viên giảng dạy môn học có trách nhiệm phổ biến quy trình kiểm tra, đánh giá môn học vào đầu học kỳ để đảm bảo người học hiểu được các yêu cầu cho việc hoàn thành môn học. 2. Việc kiểm tra, đánh giá môn học được thực hiện trên cơ sở quy định của hình thức giáo dục chính quy. Giảng viên giảng dạy môn học có thể chủ động thay đổi hình thức đánh giá phù hợp với hình thức ĐTTX. Thành phần và hình thức đánh giá đối với ĐTTX được thể hiện trong đề cương môn học có sự phê duyệt của đơn vị quản lý chuyên môn đối với môn học. 3. Việc tổ chức thi kết thúc môn học (cuối kỳ) phải được thực hiện tập trung tại Trường hoặc tại Trạm ĐTTX, được giám sát bởi cán bộ của Trường. Đề thi kết thúc môn học phải lấy trong ngân hàng đề thi chung với hệ chính quy (nếu có).
```

**Rank 5 | `chunk_0026` | score `0.333333` | document `virhe4qa_7f37ffd42956999da52e`**

```text
Điều 10. Kiểm tra, thanh tra Phòng Thanh tra pháp chế - Đảm bảo chất lượng có trách nhiệm tổ chức kiểm tra, thanh tra nội bộ việc tổ chức thực hiện các quy định về đánh giá, cập nhật CTĐT của Trường theo quy định này.
```


---

## 12. `query_090`

**Question:** ĐH CNTT thuộc cụm đại học nào?

| Field | Value |
|---|---|
| Hybrid first gold rank | `7` |
| Dense first gold rank | `4` |
| Sparse first gold rank | `27` |
| Gold chunk | `chunk_0014` |
| Gold document | `virhe4qa_c59442843db605eb1cd0` |
| Gold source index | `8913` |
| Hybrid top 1 | `chunk_0290` (score `0.666667`) |

### Gold context

```text
Điều  1. Phạm vi điều chỉnh
Văn bản này quy định về quy trình đánh giá, cập nhật chương trình đào tạo trình độ Đại học/Sau Đại học của Trường Đại học Công nghệ Thông tin – ĐHQG-HCM (Trường ĐH CNTT).
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0290` | score `0.666667` | document `virhe4qa_ad032722ed70ae0e715e`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng Đào tạo chất lượng cao trình độ đại học tại Trường Đại học Công nghệ Thông tin (ĐHCNTT) được thực hiện theo quy chế đào tạo đại học hệ chính quy theo học chế tín chỉ của Trường ĐHCNTT và các quy định cụ thể về đào tạo áp dụng cho hệ đại học hệ chính quy. Quy định này quy định một số vấn đề khác biệt hoặc quy định thêm đối với đào tạo chương trình chất lượng cao. Quy định này áp dụng cho các đơn vị quản lý chương trình Chất lượng cao (CT CLC), các đơn vị chuyên môn phụ trách chương trình đào tạo, giảng viên tham gia giảng dạy và sinh viên các CT CLC của Trường ĐHCNTT.
```

**Rank 2 | `chunk_0012` | score `0.625000` | document `virhe4qa_50f39be6faf4383a68ec`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng Quy định này quy định những điều chung nhất về đào tạo Đại học chính quy CTTN của Trường ĐHCNTT thuộc ĐHQG-HCM và nằm trong khuôn khổ quy chế đào tạo theo học chế tín chỉ cho hệ đại học chính quy của Trường ĐHCNTT. Quy định này áp dụng đối với thành viên BĐH, các Khoa có đào tạo CTTN, sinh viên hệ chính quy CTTN ở trình độ đại học của Trường ĐHCNTT.
```

**Rank 3 | `chunk_0083` | score `0.525641` | document `virhe4qa_024864f27ed0da9e11a9`**

```text
Điều 14. Thời hạn cấp văn bằng, chứng chỉ 1. Hiệu trưởng Trường ĐHCNTT có trách nhiệm cấp văn bằng cho người học trong thời hạn: a) 30 ngày kể từ ngày có quyết định công nhận tốt nghiệp đại học. b) 30 ngày kể từ ngày có quyết định công nhận tốt nghiệp và cấp bằng thạc sĩ. c) 30 ngày kể từ ngày có quyết định công nhận học vị tiến sĩ và cấp bằng tiến sĩ. 2. Hiệu trưởng hoặc thủ trưởng đơn vị trực thuộc được ủy quyền có trách nhiệm cấp chứng chỉ cho người học chậm nhất là 30 ngày kể từ ngày kết thúc khóa đào tạo, bồi dưỡng nâng cao trình độ học vấn, nghề nghiệp. 3. Trong thời gian chờ cấp văn bằng, người học đã tốt nghiệp được Hiệu trưởng Trường ĐHCNTT cấp giấy chứng nhận tốt nghiệp tạm thời (theo mẫu Phụ lục 7, 8 kèm theo Quy chế này).
```

**Rank 4 | `chunk_0119` | score `0.416667` | document `virhe4qa_da5e1bc92b41223a8639`**

```text
Điều 2. Giải thích từ ngữ Chương trình đại trà là chương trình đào tạo trình độ đại học hệ chính quy được ĐHQG-HCM cho phép triển khai đào tạo tại Trường ĐHCNTT, có mức trần học phí theo quy định hiện hành của Chính phủ. Chương trình chất lượng cao (CT CLC) là chương trình đào tạo trình độ đại học hệ chính quy có các điều kiện đảm bảo chất lượng và chuẩn đầu ra cao hơn chương trình đại trà tương ứng của cùng một ngành hoặc chuyên ngành đào tạo. Ngoại ngữ chính của chương trình chất lượng cao (sau đây gọi tắt là ngoại ngữ) là ngoại ngữ mà chương trình chất lượng cao đó có tổ chức giảng dạy chính. Website môn học: Mỗi lớp học lý thuyết được cấp 01 website môn học vào đầu học kỳ tại hệ thống hỗ trợ học tập của Trường (courses.uit.edu.vn), gọi tắt là Moodle. Chương trình đại trà tương ứng: là chương trình đại trà của cùng một ngành hoặc chuyên ngành với chương trình chất lượng cao. Đơn vị p…
```

**Rank 5 | `chunk_0007` | score `0.366667` | document `virhe4qa_cd985b886f0dad0b5712`**

```text
Thông báo Thời điểm và mức thu học phí gia hạn đối với sinh viên hệ đại học chính quy Căn cứ quyết định số 546/QĐ-ĐHCNTT, ngày 30/08/2019 của Hiệu trưởng Trường Đại học Công nghệ Thông tin (ĐHCNTT) về việc ban hành quy chế đào taoụ theo học chế tín chỉ cho hệ đại học chính quy; Căn cứ thông báo số 02/TB-ĐTĐH, ngày 9/6/2020 của Trưởng phòng Đào tạo Đại học – Trường ĐHCNTT về việc thu học phí đối với sinh viên (SV) hệ đại học chính quy từ học kỳ 1 năm học 2020 – 2021; Phòng Kế hoạch Tài chính thông báo về việc áp dụng mức thu học phí gia hạn (HPGH) theo Điều 4, Quyết định số 546/QĐ-ĐHCNTT như sau: 1. Đối tượng áp dụng: SV đã quá thời gian học theo thiết kế chương trình đào tạo (CTĐT). 2. Mức thu HPGH = t * học phí học kỳ của học kỳ cuối cùng theo thiết kế CTĐT, hệ số t: được xác định theo bảng sau đây: - Học kỳ thứ 1 + học kỳ thứ 2. Hệ số t = 10%. - Học kỳ thứ 3 + học kỳ thứ 4. Hệ số t = …
```


---

## 13. `query_015`

**Question:** Có các nội dung nào được quy định trong phần làm khóa luận tốt nghiệp dành cho sinh viên chương trình tiên tiến?

| Field | Value |
|---|---|
| Hybrid first gold rank | `5` |
| Dense first gold rank | `3` |
| Sparse first gold rank | `7` |
| Gold chunk | `chunk_0058` |
| Gold document | `virhe4qa_11e7fc1b5ac6e5cce540` |
| Gold source index | `7483` |
| Hybrid top 1 | `chunk_0203` (score `1.000000`) |

### Gold context

```text
Điều  12. Thực tập doanh nghiệp và làm khóa luận tốt nghiệp
12.1. Thực tập doanh nghiệp
Giảng viên hướng dẫn sinh viên thực tập phải đáp ứng điều kiện của giảng viên giảng dạy lý thuyết cho chương trình.
Sau khi kết thúc thời gian thực tập tại doanh nghiệp, sinh viên viết báo cáo cá nhân theo biểu mẫu do đơn vị chuyên môn quy định và báo cáo trước Hội đồng bằng tiếng Anh.
12.2. Làm khóa luận tốt nghiệp
Giảng viên hướng dẫn sinh viên làm khóa luận tốt nghiệp phải đáp ứng điều kiện của giảng viên giảng dạy lý thuyết cho chương trình.
Sinh viên thực hiện khóa luận tốt nghiệp/đồ án để được tốt nghiệp theo quy định cụ thể của chương trình đào tạo.
Sinh viên đăng ký làm khóa luận tốt nghiệp vào đầu mỗi học kỳ và được xét duyệt khi thỏa các điều kiện sau:
- Không được phép nợ quá 08 tín chỉ theo chương trình đào tạo. 
- Đã hoàn thành chương trình đào tạo tiếng Anh của CTTT theo quy định đào tạo ngoại ngữ hiện hành của Trường.
Sinh viên viết báo cáo và bảo vệ khóa luận hoàn toàn bằng tiếng Anh.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0203` | score `1.000000` | document `virhe4qa_19f2421dfa11608348be`**

```text
Điều 4. Chương trình đào tạo Chương trình gồm các học phần thuộc 02 khối kiến thức: giáo dục đại cương và giáo dục chuyên nghiệp, được xây dựng theo đúng quy định hiện hành của Bộ Giáo dục và Đào tạo kết hợp với chương trình đào tạo của ĐHNN và được giảng dạy hoàn toàn bằng tiếng Anh (trừ các môn lý luận chính trị, pháp luật, giáo dục thể chất, giáo dục quốc phòng) Chương trình đào tạo Tiên tiến được thiết kế riêng với yêu cầu về trình độ và nội dung sâu rộng hơn theo hướng cử nhân chuẩn quốc tế; đề cao tư duy sáng tạo, khả năng tự học; tăng cường kỹ năng thực hành, kiến thức thực tế, khả năng sử dụng tin học, ngoại ngữ và các kỹ năng mềm cần thiết. Sau giai đoạn đại cương, những sinh viên đạt các điều kiện yêu cầu về tiếng Anh, số tín chỉ tích lũy và điểm trung bình tích lũy theo quy định của ĐHNN và có nguyện vọng sẽ được chuyển tiếp sang ĐHNN. Sinh viên thực hiện khóa luận/đồ án tốt …
```

**Rank 2 | `chunk_0190` | score `0.500000` | document `virhe4qa_bcff59f2879248216139`**

```text
Điều 31. Thực tập, khóa luận tốt nghiệp và chuyên đề tốt nghiệp 1. Thực tập - Học phần Thực tập doanh nghiệp là học phần đặc biệt trong một số chương trình đào tạo của Trường. Theo đó, sinh viên đến thực tập tại doanh nghiệp dưới sự hướng dẫn của một giảng viên do khoa/bộ môn quản lý ngành đào tạo phân công. - Khoa/bộ môn quản lý ngành đào tạo tổ chức báo cáo kết quả thực tập doanh nghiệp cuối mỗi học kỳ có mở học phần Thực tập doanh nghiệP. - Sinh viên đăng ký học phần Thực tập doanh nghiệp trong học kỳ nào thì báo cáo kết quả thực tập vào cuối học kỳ đó theo kế hoạch của khoa/bộ môn quản lý ngành đào tạo. Nếu sinh viên không báo cáo vào đúng đợt báo cáo của học kỳ đã đăng ký thì xem như không đạt học phần này và nhận điểm không (0). Sinh viên phải đăng ký học lại vào các học kỳ tiếp theo. 2. Để hoàn tất chương trình giáo dục bậc đại học, sinh viên phải thực hiện khóa luận tốt nghiệp h…
```

**Rank 3 | `chunk_0013` | score `0.400000` | document `virhe4qa_74a8d2ead926cfa85b84`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng Quy định này quy định những yêu cầu, hình thức thực hiện và bảo vệ khoá luận tốt nghiệp, áp dụng đối với sinh viên bậc đại học hệ chính quy của Trường Đại học Công nghệ Thông tin – Đại học Quốc gia TP.HCM. Đối với các chương trình đặc biệt của Trường (chương trình tiên tiến, chương trình tài năng, chương trình chất lượng cao), quy định này sẽ được điều chỉnh cho phù hợp với đặc thù của từng chương trình.
```

**Rank 4 | `chunk_0182` | score `0.385965` | document `virhe4qa_c436b8422fd4be91aecc`**

```text
Điều 3. Môn học 1. Học phần (hay môn học) là khối lượng kiến thức tương đối trọn vẹn, thuận tiện cho người học tích lũy trong quá trình học tập, nội dung được bố trí giảng dạy trong một học kỳ. Mỗi học phần được ký hiệu bằng một mã riêng do Trường quy định. Mỗi học phần thực hành, thí nghiệm, kiến tập,… có khối lượng từ 1 – 3 tín chỉ, mỗi học phần lý thuyết hoặc học phần có cả lý thuyết và thực hành có khối lượng từ 1 – 4 tín chỉ. Trường có hai hình thức tổ chức giảng dạy thực hành: - Thực hành Hình thức 1 (HT1): là hình thức dạy thực hành có sự hướng dẫn của giảng viên cho toàn thời lượng học thực hành. - Thực hành Hình thức 2 (HT2): là hình thức dạy thực hành có sự hướng dẫn của giảng viên với thời lượng 09 tiết/tín chỉ thực hành, không nhất thiết phải sử dụng phòng thực hành chuyên dụng. 2. Các loại học phần - Học phần tích lũy: là học phần mà sinh viên có kết quả tổng kết học phần đ…
```

**Rank 5 | `chunk_0058` | score `0.375000` | document `virhe4qa_11e7fc1b5ac6e5cce540`**

```text
Điều 12. Thực tập doanh nghiệp và làm khóa luận tốt nghiệp 12.1. Thực tập doanh nghiệp Giảng viên hướng dẫn sinh viên thực tập phải đáp ứng điều kiện của giảng viên giảng dạy lý thuyết cho chương trình. Sau khi kết thúc thời gian thực tập tại doanh nghiệp, sinh viên viết báo cáo cá nhân theo biểu mẫu do đơn vị chuyên môn quy định và báo cáo trước Hội đồng bằng tiếng Anh. 12.2. Làm khóa luận tốt nghiệp Giảng viên hướng dẫn sinh viên làm khóa luận tốt nghiệp phải đáp ứng điều kiện của giảng viên giảng dạy lý thuyết cho chương trình. Sinh viên thực hiện khóa luận tốt nghiệp/đồ án để được tốt nghiệp theo quy định cụ thể của chương trình đào tạo. Sinh viên đăng ký làm khóa luận tốt nghiệp vào đầu mỗi học kỳ và được xét duyệt khi thỏa các điều kiện sau: - Không được phép nợ quá 08 tín chỉ theo chương trình đào tạo. - Đã hoàn thành chương trình đào tạo tiếng Anh của CTTT theo quy định đào tạo …
```


---

## 14. `query_031`

**Question:** Khi sinh viên hoàn tất quá trình học tập theo quy định thì Trường có trách nhiệm gì?

| Field | Value |
|---|---|
| Hybrid first gold rank | `5` |
| Dense first gold rank | `9` |
| Sparse first gold rank | `3` |
| Gold chunk | `chunk_0159` |
| Gold document | `virhe4qa_657b2d2bac3765aa27a7` |
| Gold source index | `2251` |
| Hybrid top 1 | `chunk_0094` (score `0.833333`) |

### Gold context

```text
Điều  26. Công nhận và chuyển đổi tín chỉ
1.  Trường có trách nhiệm cấp giấy chứng nhận kết quả môn học của sinh viên khi hoàn tất quá trình học tập theo quy định.
2. Việc công nhận và chuyển đổi tín chỉ đối với đào tạo từ xa, văn bằng 2 và liên thông được thực hiện theo nguyên tắc sau:
a) Sinh viên được công nhận và chuyển đổi tín chỉ đối với những môn học đã tích lũy có từ 80% trở lên nội dung tương đương với nội dung môn học trong chương trình đào tạo; 
b) Căn cứ chương trình môn học và kết quả trên bảng điểm học tập của sinh viên, Hiệu trưởng quyết định việc công nhận kết quả học tập, khối lượng kiến thức và các môn học cần phải bổ sung.
3.  Việc công nhận và chuyển đổi tín chỉ của Trường đảm bảo các nguyên tắc sau:
a)	Kết quả đối sánh chuẩn đầu ra, chương trình đào tạo và nội dung môn học là cơ sở cốt lõi cho việc công nhận và chuyển đổi tín chỉ;
b)	Thông qua ý kiến của đơn vị phụ trách chuyên môn các học phần có liên quan về việc công nhận và chuyển đổi tín chỉ.  
4.  Công nhận và chuyển đổi tín chỉ theo các quy định và ký kết khác giữa ĐHQG-HCM và các đơn vị đối tác.
5.  Tổng số tín chỉ chương trình đào tạo chính quy của các cơ sở đào tạo ngoài trường được công nhận và chuyển đổi không vượt quá 50% tổng số tín chỉ chương trình đào tạo của trường.
6.  Khi sinh viên được chuyển từ chương trình chính quy của Trường sang chương trình đào tạo từ xa của Trường thì được công nhận chuyển đổi tối đa số tín chỉ theo nguyên tắc tại Khoản 3 của điều này.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0094` | score `0.833333` | document `virhe4qa_e7dc822dea4ebc591dd7`**

```text
Điều 15. Trách nhiệm của sinh viên và cố vấn học tập 1. Sinh viên có trách nhiệm theo dõi kết quả đăng ký học phần trên Cổng thông tin đào tạo của Trường. Kết quả đăng ký học phần thể hiện: tên học phần, mã học phần, số tín chỉ của mỗi học phần, lịch học của các học phần. 2. Sinh viên có trách nhiệm thực hiện đầy đủ các yêu cầu của môn học như lên lớp, làm bài tập, thực hành, thí nghiệm, tham gia thảo luận, dự kiểm tra thường kỳ và thi kết thúc học phần. 3. Mỗi lớp sinh viên có một Cố vấn học tập. Cố vấn học tập do Trưởng khoa/Trưởng bộ môn quản lý ngành đào tạo đề nghị và Hiệu trưởng ra quyết định bổ nhiệm. Nhiệm vụ cụ thể của Cố vấn học tập có quy định riêng.
```

**Rank 2 | `chunk_0070` | score `0.700000` | document `virhe4qa_768266153037d82fad02`**

```text
Điều 13. Quyền và trách nhiệm của sinh viên Ngoài những quyền và trách nhiệm của sinh viên theo các quy định hiện hành của Trường, sinh viên có thêm những quyền và trách nhiệm sau đây: 1. Sinh viên được cung cấp, tiếp cận các nguồn học liệu điện tử của môn học, được giải đáp thắc mắc trong quá trình học tập một cách nhanh chóng. 2. Sinh viên có quyền bổ sung các thông tin khác như hình ảnh đại diện, chữ ký vào hồ sơ cá nhân trên các hệ thống phần mềm học tập trực tuyến của trường. Hình ảnh đại diện phải nghiêm túc, có văn hóa. Nghiêm cấm sử dụng hình ảnh không phù hợp với thuần phong mỹ tục của Việt Nam. 3. Sinh viên có trách nhiệm bảo vệ tài khoản của mình, chịu trách nhiệm về việc để người khác sử dụng tài khoản của mình sai mục đích, không đúng với quy định; chịu trách nhiệm về các thông tin đưa lên hệ thống từ tài khoản của mình. 4. Sinh viên phải hoàn thành các nhiệm vụ do giảng vi…
```

**Rank 3 | `chunk_0144` | score `0.416667` | document `virhe4qa_0d970ef217e73b381ec2`**

```text
Điều 22. Quyền và trách nhiệm của người học 1. Được cung cấp đầy đủ thông tin về tuyển sinh, thời hạn đăng ký nộp hồ sơ, chương trình ĐTTX, điều kiện công nhận giá trị chuyển đổi kết quả học tập, kế hoạch đào tạo, quy định về ĐTTX, yêu cầu về bằng cấp và các chính sách ĐTTX của Trường. 2. Được quyền tham gia học tập các tín chỉ cùng với hệ đào tạo chính quy, hệ vừa làm vừa học theo quy định của Trường. 3. Được cung cấp đầy đủ các thông tin về đánh giá công nhận chuyển đổi kết quả học tập và có thể đề nghị xem xét lại việc đánh giá công nhận kết quả học tập. 4. Nộp hồ sơ đầy đủ và đúng thời gian đã được Trường công bố; nộp lệ phí và học phí theo quy định của Trường. 5. Lập kế hoạch học tập cụ thể theo các yêu cầu về bằng cấp của Trường về chương trình ĐTTX đã được công bố để có thể được cấp bằng tốt nghiệp. 6. Chấp hành Quy chế này và quy định liên quan về ĐTTX của Trường. 7. Chủ động li…
```

**Rank 4 | `chunk_0101` | score `0.383333` | document `virhe4qa_b7ceba62cb5294c0a8e6`**

```text
Điều 16. Xử lý học vụ Xử lý học vụ nhằm giúp cho sinh viên lưu ý, điều chỉnh kế hoạch học tập và thái độ học tập để có thể tốt nghiệp đúng thời hạn quy định. Hằng năm, Trường tiến hành xử lý học vụ theo 2 đợt: sau học kỳ 1 và sau học kỳ hè. Kết quả học tập của học kỳ hè được tính chung vào kết quả học tập học kỳ 2 của năm học tương ứng để xem xét xử lý học vụ. 1. Cảnh báo học vụ Sinh viên bị cảnh báo học vụ nếu vi phạm một trong những trường hợp sau đây: - Không hoàn thành nghĩa vụ học phí đúng quy định. - Có ĐTBHK dưới 3,0 hoặc điểm trung bình của liên tiếp 2 học kỳ gần nhất đều dưới 4,0. Thời hạn cảnh báo học vụ kéo dài trong một học kỳ chính tiếp theo. Sinh viên sẽ được tự động xóa hình thức xử lý khi kết thúc thời hạn. 2. Đình chỉ học tập - Sinh viên bị đình chỉ học tập 1 học kỳ chính nếu vi phạm lần đầu trong việc đi thi hộ hoặc nhờ người thi hộ. - Đình chỉ học tập có thời hạn: áp …
```

**Rank 5 | `chunk_0159` | score `0.350000` | document `virhe4qa_657b2d2bac3765aa27a7`**

```text
Điều 26. Công nhận và chuyển đổi tín chỉ 1. Trường có trách nhiệm cấp giấy chứng nhận kết quả môn học của sinh viên khi hoàn tất quá trình học tập theo quy định. 2. Việc công nhận và chuyển đổi tín chỉ đối với đào tạo từ xa, văn bằng 2 và liên thông được thực hiện theo nguyên tắc sau: a) Sinh viên được công nhận và chuyển đổi tín chỉ đối với những môn học đã tích lũy có từ 80% trở lên nội dung tương đương với nội dung môn học trong chương trình đào tạo; b) Căn cứ chương trình môn học và kết quả trên bảng điểm học tập của sinh viên, Hiệu trưởng quyết định việc công nhận kết quả học tập, khối lượng kiến thức và các môn học cần phải bổ sung. 3. Việc công nhận và chuyển đổi tín chỉ của Trường đảm bảo các nguyên tắc sau: a) Kết quả đối sánh chuẩn đầu ra, chương trình đào tạo và nội dung môn học là cơ sở cốt lõi cho việc công nhận và chuyển đổi tín chỉ; b) Thông qua ý kiến của đơn vị phụ trác…
```


---

## 15. `query_045`

**Question:** Nếu không hoàn thành chương trình đào tạo thì có thể nhận chứng chỉ tốt nghiệp được không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `5` |
| Dense first gold rank | `5` |
| Sparse first gold rank | `5` |
| Gold chunk | `chunk_0075` |
| Gold document | `virhe4qa_09a10fba0ad38ed3d729` |
| Gold source index | `750` |
| Hybrid top 1 | `chunk_0275` (score `0.600000`) |

### Gold context

```text
Điều  13. Điều kiện cấp văn bằng, chứng chỉ 
Người học được cấp văn bằng, chứng chỉ khi đảm bảo các điều kiện sau:
1. Văn bằng được cấp sau khi người học hoàn thành chương trình giáo dục, chương trình đào tạo theo cấp học, trình độ đào tạo và đạt các điều kiện khác theo quy định của quy chế đào tạo đại học, thạc sĩ, tiến sĩ.
2. Chứng chỉ:
a) Được cấp sau khi người học hoàn thành chương trình đào tạo hoặc bồi dưỡng nâng cao trình độ học vấn, nghề nghiệp theo chương trình do Bộ GD&ĐT quy định hoặc ban hành. 
b) Được cấp cho cá nhân có nhu cầu được đánh giá năng lực sử dụng CNTT hoặc có nhu cầu được cấp chứng chỉ ứng dụng CNTT theo quy định của Bộ GD&ĐT.
3. Không đang trong thời gian bị truy cứu trách nhiệm hình sự.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0275` | score `0.600000` | document `virhe4qa_9ee423b212481d1ec26d`**

```text
Điều 9. Văn bằng, chứng chỉ/chứng nhận được sử dụng để công nhận đạt chuẩn xét tốt nghiệp Để được xét tốt nghiệp sinh viên phải hoàn tất các môn học tiếng Anh trong chương trình giảng dạy tiếng Anh tại Điều 3 và có một trong các văn bằng, chứng chỉ/chứng nhận được quy định như sau: 1. Văn bằng tốt nghiệp đại học/trên đại học trong nước, nước ngoài mà ngành học hoặc ngôn ngữ sử dụng toàn phần trong đào tạo (không thông qua phiên dịch) là một trong ba ngoại ngữ: tiếng Anh, tiếng Pháp, tiếng Nhật. 2. Chứng chỉ/chứng nhận ngoại ngữ: Sinh viên có một trong các loại chứng chỉ/chứng nhận tiếng Anh, có chứng chỉ/chứng nhận tiếng Pháp, hoặc tiếng Nhật tối thiểu như sau Đối với chương trình văn bằng 2, liên thông, chương trình chuẩn phải đạt chứng chỉ tiếng Anh TOEIC Nghe-Đọc đạt từ 450 trở lên và TOEIC Nói-Viết đạt từ 185 trở lên hoặc TOEFL iBT đạt từ 45 trở lên hoặc IELTS đạt 4.5, chứng chỉ Cam…
```

**Rank 2 | `chunk_0050` | score `0.555556` | document `virhe4qa_8d5eeb2986483f0c0504`**

```text
Điều 12. Tốt nghiệp Chương trình Tài năng Sinh viên sẽ được cấp bằng "Cử nhân/Kỹ sư Tài năng" (Honor Program) của Trường ĐHCNTT – ĐHQG HCM nếu hội đủ các điều kiện sau: - Đang là sinh viên của CTTN. - Hoàn tất chương trình đúng hạn – đủ điều kiện để được cấp bằng theo đúng ngành học của lớp CTTN tương ứng. Nếu sinh viên đã bảo vệ KLTN đúng hạn nhưng chưa đủ điều kiện tốt nghiệp, Khoa có thể xem xét hoàn cảnh cụ thể để đề nghị BĐH và trình BGH phê duyệt cho phép gia hạn tối đa 1 học kỳ để hoàn tất CTĐT và được cấp bằng CTTN. - Có điểm KLTN  7.0, ĐTBTL  7.0 và điểm rèn luyện từ loại Khá trở lên. - Có trình độ Anh văn đạt chuẩn đầu ra của CTTN do Trường quy định. Các sinh viên không đạt một trong các điều kiện nêu trên sẽ nhận bằng tốt nghiệp như sinh viên chương trình chuẩn khi đã đạt đủ các điều kiện được quy định trong quy chế đào tạo theo học chế tín chỉ của Trường; đồng thời sinh vi…
```

**Rank 3 | `chunk_0287` | score `0.380952` | document `virhe4qa_772f8cc6d22836eae64f`**

```text
Điều 9: Xét tốt nghiệp và cấp bằng 1. Người học sau khi hoàn thành chương trình đào tạo phần trình độ đại học theo Điều 5 và thỏa điều kiện cấp bằng theo quy chế đào tạo trình độ đại học hiện hành của Trường thì được cấp bằng tốt nghiệp đại học theo ngành ĐH-ThS. 2. Người học sau khi hoàn thành phần trình độ thạc sĩ theo Điều 5 và thỏa điều kiện cấp bằng theo quy chế đào tạo trình độ thạc sĩ hiện hành của Trường thì được cấp bằng tốt nghiệp thạc sĩ theo ngành ĐH-ThS.
```

**Rank 4 | `chunk_0216` | score `0.363636` | document `virhe4qa_ae295b2fe64356a35465`**

```text
Điều 5. Chương trình đào tạo CT CLC được xây dựng trên nền chương trình đào tạo đại trà tương ứng và theo quy định xây dựng chương trình đào tạo của Trường ĐHCNTT. CT CLC có sự khác biệt so với chương trình đại trà ở những điểm dưới đây: - Chuẩn đầu ra của CT CLC phải cao hơn chuẩn đầu ra của chương trình đại trà tương ứng về năng lực chuyên môn; năng lực ngoại ngữ; năng lực làm việc nhóm; khả năng thích nghi với môi trường công tác. - Chuẩn đầu ra ngoại ngữ: để được xét tốt nghiệp, sinh viên phải hoàn tất chương trình ngoại ngữ bắt buộc trong chương trình đào tạo và có một trong các chứng chỉ ngoại ngữ đạt trình độ tối thiểu: • Tiếng Anh: bậc 4/6 theo khung năng lực ngoại ngữ 6 bậc dùng cho Việt Nam. Cụ thể mức quy đổi sang các chứng chỉ quốc tế được quy định trong Quy định đào tạo ngoại ngữ hiện hành của Trường. • Tiếng Nhật: tương đương JLPT N3. - Để đảm bảo tính liên thông giữa CT C…
```

**Rank 5 | `chunk_0075` | score `0.333333` | document `virhe4qa_09a10fba0ad38ed3d729`**

```text
Điều 13. Điều kiện cấp văn bằng, chứng chỉ Người học được cấp văn bằng, chứng chỉ khi đảm bảo các điều kiện sau: 1. Văn bằng được cấp sau khi người học hoàn thành chương trình giáo dục, chương trình đào tạo theo cấp học, trình độ đào tạo và đạt các điều kiện khác theo quy định của quy chế đào tạo đại học, thạc sĩ, tiến sĩ. 2. Chứng chỉ: a) Được cấp sau khi người học hoàn thành chương trình đào tạo hoặc bồi dưỡng nâng cao trình độ học vấn, nghề nghiệp theo chương trình do Bộ GD&ĐT quy định hoặc ban hành. b) Được cấp cho cá nhân có nhu cầu được đánh giá năng lực sử dụng CNTT hoặc có nhu cầu được cấp chứng chỉ ứng dụng CNTT theo quy định của Bộ GD&ĐT. 3. Không đang trong thời gian bị truy cứu trách nhiệm hình sự.
```


---

## 16. `query_017`

**Question:** Có thể quy đổi số 30% tín chỉ của các môn học thạc sĩ được công nhận khi chuyển sang học thạc sĩ đối với chương trình ĐH-ThS được không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `4` |
| Dense first gold rank | `6` |
| Sparse first gold rank | `3` |
| Gold chunk | `chunk_0221` |
| Gold document | `virhe4qa_4fa57a44b85abe84ec35` |
| Gold source index | `4406` |
| Hybrid top 1 | `chunk_0160` (score `0.833333`) |

### Gold context

```text
Điều  5. Thiết kế chương trình đào tạo
1. Thời gian thiết kế chương trình ĐH-ThS từ 4.5 – 5.5 năm.
2. Cấu trúc khung chương trình đào tạo gồm hai phần: phần trình độ đại học và phần trình độ thạc sĩ. Khung chương trình đào tạo được thiết kế theo quy định hiện hành về thiết kế chương trình đào tạo trình độ đại học và thạc sĩ.
3. Chương trình đào tạo quy định rõ các học phần của chương trình đào tạo trình độ thạc sĩ tổ chức giảng dạy trong phần trình độ đại học được xét công nhận tương đương cho các học phần ở trình độ đại học (gọi tắt là môn học thạc sĩ được công nhận).
4. Tổng số tín chỉ của các môn học thạc sĩ được công nhận không quá 50% số tín chỉ của chương trình đào tạo trình độ thạc sĩ; các môn học này phải có trong khung chương trình đào tạo thạc sĩ của ngành tương ứng. Khung chương trình ĐH-ThS phải được cập nhật định kỳ theo quy định hiện hành.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0160` | score `0.833333` | document `virhe4qa_1adc09fd3adbe3a9efe7`**

```text
Điều 26. Công nhận và chuyển đổi tín chỉ 1. Trường có trách nhiệm cấp giấy chứng nhận kết quả môn học của sinh viên khi hoàn tất quá trình học tập theo quy định. 2. Việc công nhận và chuyển đổi tín chỉ đối với đào tạo từ xa, văn bằng 2 và liên thông được thực hiện theo nguyên tắc sau: a) Sinh viên được công nhận và chuyển đổi tín chỉ đối với những môn học đã tích lũy có từ 80% trở lên nội dung tương đương với nội dung môn học trong chương trình đào tạo; b) Căn cứ chương trình môn học và kết quả trên bảng điểm học tập của sinh viên, Hiệu trưởng quyết định việc công nhận kết quả học tập, khối lượng kiến thức và các môn học cần phải bổ sung. 3. Việc công nhận và chuyển đổi tín chỉ của Trường đảm bảo các nguyên tắc sau: a) Kết quả đối sánh chuẩn đầu ra, chương trình đào tạo và nội dung môn học là cơ sở cốt lõi cho việc công nhận và chuyển đổi tín chỉ; b) Thông qua ý kiến của đơn vị phụ trác…
```

**Rank 2 | `chunk_0159` | score `0.833333` | document `virhe4qa_657b2d2bac3765aa27a7`**

```text
Điều 26. Công nhận và chuyển đổi tín chỉ 1. Trường có trách nhiệm cấp giấy chứng nhận kết quả môn học của sinh viên khi hoàn tất quá trình học tập theo quy định. 2. Việc công nhận và chuyển đổi tín chỉ đối với đào tạo từ xa, văn bằng 2 và liên thông được thực hiện theo nguyên tắc sau: a) Sinh viên được công nhận và chuyển đổi tín chỉ đối với những môn học đã tích lũy có từ 80% trở lên nội dung tương đương với nội dung môn học trong chương trình đào tạo; b) Căn cứ chương trình môn học và kết quả trên bảng điểm học tập của sinh viên, Hiệu trưởng quyết định việc công nhận kết quả học tập, khối lượng kiến thức và các môn học cần phải bổ sung. 3. Việc công nhận và chuyển đổi tín chỉ của Trường đảm bảo các nguyên tắc sau: a) Kết quả đối sánh chuẩn đầu ra, chương trình đào tạo và nội dung môn học là cơ sở cốt lõi cho việc công nhận và chuyển đổi tín chỉ; b) Thông qua ý kiến của đơn vị phụ trác…
```

**Rank 3 | `chunk_0089` | score `0.450000` | document `virhe4qa_c072ac06f88b20b3bd13`**

```text
Điều 15. Công nhận kết quả học tập Khi có nhu cầu công nhận kết quả học tập từ các chương trình đào tạo trình độ đại học khác, sinh viên nộp đơn xin công nhận kết quả học tập kèm các hồ sơ liên quan cho Phòng Đào tạo Đại học thông qua Trạm ĐTTX chính. Hội đồng khoa quản lý chương trình ĐTTX hoặc hội đồng chuyên môn được Hiệu trưởng thành lập có trách nhiệm xem xét, quyết định công nhận kết quả học tập để chuyển đổi, miễn trừ những môn học mà sinh viên đã tích lũy ở các chương trình đào tạo cấp văn bằng khác. Số tín chỉ được công nhận kết quả học tập để chuyển đổi, miễn trừ tích lũy từ các trường khác ngoài Trường ĐHCNTT không được vượt quá 50% tổng số tín chỉ của chương trình ĐTTX. Hội đồng chuyên môn được Hiệu trưởng thành lập trên cơ sở đề xuất của P.ĐTĐH bao gồm: đại diện Ban Giám hiệu, đại diện lãnh đạo các đơn vị: P.ĐTĐH, Khoa chuyên môn quản lý chương trình ĐTTX, Trạm ĐTTX liên qu…
```

**Rank 4 | `chunk_0221` | score `0.392857` | document `virhe4qa_4fa57a44b85abe84ec35`**

```text
Điều 5. Thiết kế chương trình đào tạo 1. Thời gian thiết kế chương trình ĐH-ThS từ 4.5 – 5.5 năm. 2. Cấu trúc khung chương trình đào tạo gồm hai phần: phần trình độ đại học và phần trình độ thạc sĩ. Khung chương trình đào tạo được thiết kế theo quy định hiện hành về thiết kế chương trình đào tạo trình độ đại học và thạc sĩ. 3. Chương trình đào tạo quy định rõ các học phần của chương trình đào tạo trình độ thạc sĩ tổ chức giảng dạy trong phần trình độ đại học được xét công nhận tương đương cho các học phần ở trình độ đại học (gọi tắt là môn học thạc sĩ được công nhận). 4. Tổng số tín chỉ của các môn học thạc sĩ được công nhận không quá 50% số tín chỉ của chương trình đào tạo trình độ thạc sĩ; các môn học này phải có trong khung chương trình đào tạo thạc sĩ của ngành tương ứng. Khung chương trình ĐH-ThS phải được cập nhật định kỳ theo quy định hiện hành.
```

**Rank 5 | `chunk_0279` | score `0.262500` | document `virhe4qa_c856861ab0c510bc7eab`**

```text
Điều 9. Chuyển đổi chương trình đào tạo Trong thời gian học tập, vì lý do cá nhân nếu sinh viên muốn chuyển sang học các chương trình đào tạo khác của Trường phải được sự đồng ý của Hiệu trưởng. Sinh viên được chuyển điểm những môn học tương đương giữa hai chương trình đào tạo Sinh viên được phép chuyển vào hoặc ra khỏi chương trình trong vòng 03 học kỳ đầu tiên. Ngoài việc phải thỏa các điều kiện về chuyển ngành/chương trình theo quy chế đào tạo hiện hành, sinh viên phải thỏa thêm các điều kiện: - Sinh viên từ CTTT chuyển sang chương trình đào tạo khác: + Điểm rèn luyện đạt từ loại Khá trở lên, + Có các giấy tờ xác nhận khác (của cơ quan y tế, của địa phương…) hợp lệ để Hiệu trưởng xem xét quyết định. - Sinh viên từ các chương trình đào tạo khác có nguyện vọng chuyển vào CTTT: + Điểm trung bình học kỳ gần nhất không dưới 6.5. + Các môn ngoại ngữ trong CTĐT tương ứng với tiến độ của CTT…
```


---

## 17. `query_030`

**Question:** Hồ sơ liên quan đến việc đặt trạm ĐTTX nằm ở đâu?

| Field | Value |
|---|---|
| Hybrid first gold rank | `4` |
| Dense first gold rank | `4` |
| Sparse first gold rank | `3` |
| Gold chunk | `chunk_0156` |
| Gold document | `virhe4qa_4b4732548b61f556d7fc` |
| Gold source index | `3352` |
| Hybrid top 1 | `chunk_0242` (score `0.833333`) |

### Gold context

```text
Điều  25. Quản lý và lưu trữ hồ sơ
1. 	Hồ sơ được bảo quản và lưu trữ tại P.ĐTĐH gồm có:
	a) Hồ sơ liên quan đến đặt Trạm ĐTTX;
b) Chương trình đào tạo; kế hoạch đào tạo toàn khóa; 
	c) Hồ sơ tuyển sinh, kết quả quá trình học tập, hồ sơ công nhận tốt nghiệp;
	d) Sổ cấp phát văn bằng.
2. Hồ sơ được bảo quản và lưu trữ tại Trạm ĐTTX gồm có:
	a) Hồ sơ liên quan đến đặt Trạm ĐTTX;
b) Chương trình đào tạo; kế hoạch đào tạo toàn khóa; kế hoạch đào tạo chi tiết từng học kỳ;
	c) Danh sách và kết quả học tập của người học của từng môn học;
	d) Danh sách giảng viên, cán bộ quản lý có liên quan tới khóa học, môn học.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0242` | score `0.833333` | document `virhe4qa_7ff895ead7ffbf3fed1f`**

```text
Điều 6. Đặt hoặc thôi đặt trạm đào tạo từ xa mới 1. Đặt trạm ĐTTX mới: a) Trạm ĐTTX chính gửi công văn đề nghị đặt trạm ĐTTX mới tới Hiệu trưởng thông qua phòng ĐTĐH. b) Hiệu trưởng ra quyết định thành lập Tổ kiểm tra trên cơ sở đề nghị của Phòng ĐTĐH để tổ chức kiểm tra thực tế tại Trạm ĐTTX và xác nhận các điều kiện đảm bảo chất lượng, đảm bảo đáp ứng các yêu cầu để thực hiện chương trình ĐTTX. c) Hội đồng khoa học và đào tạo xem xét hồ sơ, biên bản làm việc và đề nghị của Tổ kiểm tra và cho ý kiến. Hiệu trưởng quyết định việc đặt Trạm ĐTTX cho từng ngành đào tạo trên cơ sở ý kiến của Hội đồng khoa học và đào tạo. 2. Thôi đặt trạm ĐTTX: Hiệu trưởng ra quyết định việc thôi đặt Trạm ĐTTX trong những trường hợp sau: a) Không còn sinh viên theo học và không có khả năng tiếp tục tuyển sinh; b) Không còn đảm bảo các điều kiện về cơ sở vật chất để thực hiện chương trình ĐTTX; c) Vi phạm các …
```

**Rank 2 | `chunk_0202` | score `0.666667` | document `virhe4qa_2248b836aecbf765c1aa`**

```text
Điều 4. Bộ máy tổ chức và quản lý ĐTTX Các đơn vị chính trong bộ máy tổ chức và quản lý ĐTTX gồm: 1. Trung tâm Phát triển Công nghệ Thông tin: Là Trạm ĐTTX chính của Trường, là đầu mối quản lý tất cả sinh viên chương trình ĐTTX và tổ chức hoạt động ĐTTX của Trường đối với tất cả các ngành đào tạo mà Trường ĐHCNTT được phép ĐTTX; làm việc với các đơn vị, địa phương để thiết lập và hỗ trợ Trường quản lý các Trạm ĐTTX khác; chịu trách nhiệm chính trong việc phối hợp các đơn vị và các Trạm ĐTTX để triển khai các hoạt động tuyển sinh và tổ chức ĐTTX; đồng thời thực hiện các nhiệm vụ của một Trạm ĐTTX quy định tại Điều 5 của Quy chế này. 2. Các Khoa chuyên môn: chịu trách nhiệm quản lý chuyên môn theo ngành/chuyên ngành đào tạo được giao, chủ trì việc tổ chức xây dựng chương trình đào tạo, xây dựng học liệu ĐTTX, xây dựng ngân hàng đề thi (nếu có) cho những môn học thuộc trách nhiệm quản lý, …
```

**Rank 3 | `chunk_0223` | score `0.583333` | document `virhe4qa_56eeb136d845a53194db`**

```text
Điều 5. Trạm đào tạo từ xa của Trường ĐHCNTT 1. Trạm ĐTTX: đặt tại một trong những cơ quan, tổ chức sau đây: cơ sở giáo dục đại học, trường cao đẳng, trường trung cấp, trung tâm giáo dục thường xuyên, trường của cơ quan nhà nước, trường của tổ chức chính trị, tổ chức chính trị - xã hội, trường của lực lượng vũ trang nhân dân có đủ điều kiện đảm bảo các yêu cầu về môi trường sư phạm, cơ sở vật chất, thiết bị, thiết bị thí nghiệm, thực hành, thực tập, cán bộ quản lý để thực hiện chương trình ĐTTX. 2. Trách nhiệm của trạm ĐTTX: Phối hợp với các đơn vị của Trường trong công tác tuyển sinh, tổ chức đào tạo, học phí và những công tác liên quan khác. Cụ thể, 2.1. Quảng bá tuyển sinh, thu hồ sơ xét tuyển, phối hợp thông báo kết quả tuyển sinh đến thí sinh. 2.2. Cung cấp cho người học kiến thức, kỹ năng về phương pháp học tập từ xa trước khi tham gia chính thức khoá học. 2.3. Lên kế hoạch đào tạ…
```

**Rank 4 | `chunk_0156` | score `0.450000` | document `virhe4qa_4b4732548b61f556d7fc`**

```text
Điều 25. Quản lý và lưu trữ hồ sơ 1. Hồ sơ được bảo quản và lưu trữ tại P.ĐTĐH gồm có: a) Hồ sơ liên quan đến đặt Trạm ĐTTX; b) Chương trình đào tạo; kế hoạch đào tạo toàn khóa; c) Hồ sơ tuyển sinh, kết quả quá trình học tập, hồ sơ công nhận tốt nghiệp; d) Sổ cấp phát văn bằng. 2. Hồ sơ được bảo quản và lưu trữ tại Trạm ĐTTX gồm có: a) Hồ sơ liên quan đến đặt Trạm ĐTTX; b) Chương trình đào tạo; kế hoạch đào tạo toàn khóa; kế hoạch đào tạo chi tiết từng học kỳ; c) Danh sách và kết quả học tập của người học của từng môn học; d) Danh sách giảng viên, cán bộ quản lý có liên quan tới khóa học, môn học.
```

**Rank 5 | `chunk_0110` | score `0.325000` | document `virhe4qa_92640ad22e84af2da079`**

```text
Điều 18. Chuyển ngành, chuyển hệ đào tạo, chuyển trường, chuyển trạm ĐTTX 1. Chuyển ngành Sinh viên hệ ĐTTX được xin chuyển sang ngành đào tạo từ xa khác của Trường nếu đủ điều kiện trúng tuyển ngành đào tạo của khóa tuyển tương ứng. Sinh viên nộp đơn xin chuyển ngành cho P.ĐTĐH. Hiệu trưởng ra quyết định chuyển ngành trên cơ sở đề nghị của P.ĐTĐH. 2. Chuyển hệ đào tạo Sinh viên học hệ vừa học vừa làm, hệ đại học chính quy của Trường được chuyển sang học hệ ĐTTX. Sinh viên nộp đơn xin chuyển hệ đào tạo cho P.ĐTĐH. Hiệu trưởng ra quyết định chuyển hệ đào tạo trên cơ sở đề nghị của P.ĐTĐH. 3. Chuyển trạm ĐTTX Sinh viên hệ ĐTTX được xin chuyển từ trạm ĐTTX này sang trạm ĐTTX khác. Sinh viên nộp đơn xin chuyển trạm ĐTTX cho P.ĐTĐH. Hiệu trưởng ra quyết định chuyển trạm ĐTTX trên cơ sở đề nghị của P.ĐTĐH. 4. Chuyển trường Sinh viên được chuyển trường nếu có đủ các điều kiện sau: - Trong thời…
```


---

## 18. `query_100`

**Question:** Đối với chương trình tiên tiến, môn Giáo dục quốc phòng - an ninh có giảng dạy bằng tiếng Anh không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `4` |
| Dense first gold rank | `6` |
| Sparse first gold rank | `3` |
| Gold chunk | `chunk_0016` |
| Gold document | `virhe4qa_f396d11f4689860a9368` |
| Gold source index | `7291` |
| Hybrid top 1 | `chunk_0203` (score `1.000000`) |

### Gold context

```text
Điều  1. Phạm vi điều chỉnh và đối tượng áp dụng
Quy định này áp dụng đối với giảng viên, sinh viên hệ chính quy đào tạo theo CTTT, thực hiện theo học chế tín chỉ, giảng dạy bằng tiếng Anh (trừ các môn lý luận chính trị, pháp luật đại cương, Giáo dục quốc phòng – an ninh, Giáo dục thể chất).
Các nội dung không nêu trong quy định này được áp dụng theo Quy chế đào tạo theo học chế tín chỉ và các quy định hiện hành của Trường ĐHCNTT cho hệ đại học chính quy.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0203` | score `1.000000` | document `virhe4qa_19f2421dfa11608348be`**

```text
Điều 4. Chương trình đào tạo Chương trình gồm các học phần thuộc 02 khối kiến thức: giáo dục đại cương và giáo dục chuyên nghiệp, được xây dựng theo đúng quy định hiện hành của Bộ Giáo dục và Đào tạo kết hợp với chương trình đào tạo của ĐHNN và được giảng dạy hoàn toàn bằng tiếng Anh (trừ các môn lý luận chính trị, pháp luật, giáo dục thể chất, giáo dục quốc phòng) Chương trình đào tạo Tiên tiến được thiết kế riêng với yêu cầu về trình độ và nội dung sâu rộng hơn theo hướng cử nhân chuẩn quốc tế; đề cao tư duy sáng tạo, khả năng tự học; tăng cường kỹ năng thực hành, kiến thức thực tế, khả năng sử dụng tin học, ngoại ngữ và các kỹ năng mềm cần thiết. Sau giai đoạn đại cương, những sinh viên đạt các điều kiện yêu cầu về tiếng Anh, số tín chỉ tích lũy và điểm trung bình tích lũy theo quy định của ĐHNN và có nguyện vọng sẽ được chuyển tiếp sang ĐHNN. Sinh viên thực hiện khóa luận/đồ án tốt …
```

**Rank 2 | `chunk_0224` | score `0.533333` | document `virhe4qa_df5a8af281af7a0e162f`**

```text
Điều 5. Tổ chức chương trình Các lớp CTTT được ưu tiên về cơ sở vật chất cho việc học tập và nghiên cứu. Các lớp CTTT được trang bị phòng học riêng có các thiết bị hỗ trợ giảng dạy và học tập hiện đại; có đủ giáo trình, tài liệu tham khảo trong, ngoài nước và được cập nhật thường xuyên; có thư viện và thư viện điện tử cho giảng viên và sinh viên tra cứu và sử dụng trong giảng dạy, học tập và NCKH. Về chất lượng quản lý và giảng dạy: Các lớp CTTT được quản lý và giảng dạy bởi các cán bộ có chuyên môn giỏi và có kinh nghiệm trong công tác, đảm bảo chất lượng đào tạo và dịch vụ hỗ trợ chất lượng cao cho sinh viên. Năm học đầu tiên sinh viên CTTT phải học tập trung tiếng Anh để đáp ứng điều kiện học các môn chuyên ngành hoàn toàn bằng tiếng Anh. Các lớp tiếng Anh được tổ chức tối đa 30 sinh viên theo trình độ khác nhau, tạo điều kiện cho việc giảng dạy tiếng Anh một cách tốt nhất. Đơn vị ch…
```

**Rank 3 | `chunk_0175` | score `0.500000` | document `virhe4qa_fbc566cbccab146e8b56`**

```text
Điều 3. Chương trình giảng dạy tiếng Anh 1. Chương trình giảng dạy tiếng Anh của từng loại chương trình bao gồm những môn học được liệt kê theo cấp độ khó tăng dần như trong Bảng 1 nhằm hỗ trợ sinh viên đạt chuẩn ngoại ngữ xét tốt nghiệp theo quy định của từng chương trình. Đối với những môn học tiếng Anh nằm trong chương trình đào tạo (CTĐT) được xét miễn học theo Điều 4 và Điều 5 của Quy định này thì sinh viên được nhận điểm Miễn cho môn học đó và không tính vào điểm trung bình chung, điểm trung bình chung tích lũy, điểm trung bình học kỳ. Chương trình giảng dạy tiếng Anh áp dụng từ khóa tuyển 2022 CTC và CTTN Gồm 3 môn học: 1. Anh văn 1 (mã môn ENG01) 2. Anh văn 2 (mã môn ENG02) 3. Anh văn 3 (mã môn ENG03) CTTT Gồm 8 môn học: 1. Anh văn 1 (mã môn ENG01) 2. Anh văn 2 (mã môn ENG02) 3. Anh văn 3 (mã môn ENG03) 4. Anh văn 4 (mã môn ENG04) 5. Anh văn 5 (mã môn ENG05) 6. Tiếng Anh 1 (mã m…
```

**Rank 4 | `chunk_0016` | score `0.392857` | document `virhe4qa_f396d11f4689860a9368`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng Quy định này áp dụng đối với giảng viên, sinh viên hệ chính quy đào tạo theo CTTT, thực hiện theo học chế tín chỉ, giảng dạy bằng tiếng Anh (trừ các môn lý luận chính trị, pháp luật đại cương, Giáo dục quốc phòng – an ninh, Giáo dục thể chất). Các nội dung không nêu trong quy định này được áp dụng theo Quy chế đào tạo theo học chế tín chỉ và các quy định hiện hành của Trường ĐHCNTT cho hệ đại học chính quy.
```

**Rank 5 | `chunk_0124` | score `0.350000` | document `virhe4qa_ffb03558a4ad0f1f974d`**

```text
Điều 2. Mục đích đào tạo ngoại ngữ 1 . Chương trình giảng dạy tiếng Anh nhằm mục đích giúp sinh viên: a . Phát triển toàn diện 4 kỹ năng sử dụng tiếng Anh tổng quát: nghe, nói, đọc, viết; phát triển kỹ năng sử dụng tiếng Anh chuyên ngành ở mức độ phù hợp với trình độ đào tạo, ngành đào tạo và loại chương trình đào tạo. b . Đáp ứng được chuẩn ngoại ngữ tiếng Anh đầu ra theo quy định của ĐHQG-HCM. 2 . Các ngoại ngữ khác tiếng Anh được đưa vào nhằm khuyến khích sinh viên học để đáp ứng nhu cầu đa dạng của thị trường lao động. 3 . Sinh viên chương trình chuẩn, chương trình tài năng, chương trình văn bằng hai và chương trình liên thông được chọn một trong các chứng chỉ ngoại ngữ: tiếng Anh, tiếng Nhật hoặc tiếng Pháp để xét tốt nghiệp, tuy nhiên sinh viên vẫn phải hoàn thành chương trình ngoại ngữ quy định tại Điều 3 (ngoại trừ chương trình định hướng Nhật Bản). Các chuẩn quá trình được xây …
```


---

## 19. `query_010`

**Question:** Chương trình đào tạo tối thiểu của Trường yêu cầu sinh viên tích lũy bao nhiêu tín chỉ để tốt nghiệp trong chương trình đào tạo cử nhân?

| Field | Value |
|---|---|
| Hybrid first gold rank | `3` |
| Dense first gold rank | `2` |
| Sparse first gold rank | `5` |
| Gold chunk | `chunk_0250` |
| Gold document | `virhe4qa_720a25859206a5742dc8` |
| Gold source index | `2867` |
| Hybrid top 1 | `chunk_0085` (score `0.700000`) |

### Gold context

```text
Điều  7. Chương trình đào tạo
1. Chương trình đào tạo của mỗi ngành đào tạo do Trường xây dựng phù hợp với các quy định hiện hành của Bộ GD&ĐT và ĐHQG-HCM, được bổ sung cập nhật nội dung chương trình giáo dục tiên tiến quốc tế theo định hướng đào tạo nguồn nhân lực chất lượng cao, đáp ứng nhu cầu phát triển khoa học, công nghệ, kinh tế, xã hội đất nước và hội nhập quốc tế. Chương trình đào tạo phải đảm bảo các điều kiện sau:
a)	Đáp ứng được mục tiêu chương trình giáo dục đại học quy định tại Điều 2, Khoản 1 của quy chế này, mục tiêu cụ thể và chuẩn đầu ra của chương trình đào tạo; đảm bảo các yêu cầu theo quy định của Luật giáo dục đại học; đáp ứng Khung trình độ năng lực quốc gia; đáp ứng Bộ phẩm chất, năng lực sinh viên tốt nghiệp ĐHQG-HCM và các quy định hiện hành khác về CTĐT; phù hợp với nhu cầu sử dụng nhân lực của ngành, địa phương và xã hội.
b)	Thể hiện rõ trình độ đào tạo; điều kiện tuyển sinh và điều kiện tốt nghiệp; mục tiêu đào tạo; chuẩn kiến thức, kỹ năng, mức tự chủ và trách nhiệm của người học khi tốt nghiệp; khối lượng kiến thức lý thuyết, thực hành, thực tập; kế hoạch đào tạo theo thời gian thiết kế; phương pháp và hình thức đào tạo; cách thức đánh giá kết quả học tập; các điều kiện thực hiện chương trình đào tạo của CSĐT.
c)	Được thiết kế tích hợp thông qua phương pháp tiếp cận hệ thống đối với việc giảng dạy kỹ năng, phẩm chất cá nhân, nghề nghiệp kết hợp với kiến thức nền tảng và kiến thức chuyên môn.
d)	Xây dựng kế hoạch và thực hiện các điều kiện đảm bảo chất lượng giáo dục đối với chương trình đào tạo đang triển khai.
đ) Định kỳ sau một khóa đào tạo, thực hiện rà soát chỉnh sửa, bổ sung chương trình đào tạo phù hợp với quy định về chuẩn chương trình đào tạo và phù hợp với nhu cầu của thị trường lao động.
e) Có khả năng liên thông giữa các bậc và các ngành đào tạo khác, điều kiện nhập học và điều kiện tốt nghiệP.
Tổng số tín chỉ của các chương trình đào tạo tối thiểu là 120 và tối đa là 132 tín chỉ đối với đào tạo chương trình cử nhân; tối thiểu 150 tín chỉ đối với chương trình đào tạo chuyên sâu đặc thù trình độ đại học (không tính Giáo dục quốc phòng-An ninh và Giáo dục thể chất). Chương trình đào tạo được Hiệu trưởng phê duyệt theo đề nghị của Trưởng khoa/Trưởng bộ môn quản lý ngành đào tạo và Trưởng phòng Đào tạo Đại học (P. ĐTĐH).
2. Chương trình đào tạo bao gồm hai khối kiến thức:
a) Khối kiến thức giáo dục đại cương bao gồm các học phần thuộc các lĩnh vực: Lý luận chính trị, Khoa học xã hội và nhân văn, Khoa học tự nhiên, Toán, Ngoại ngữ, Giáo dục quốc phòng-An ninh, Giáo dục thể chất và Kỹ năng mềm, được thiết kế nhằm trang bị cho sinh viên nền học vấn rộng để tiếp thu tốt kiến thức chuyên môn, tạo nền tảng cho người học dễ dàng thích nghi với môi trường làm việc, tự cập nhật kiến thức trước tình hình phát triển nhanh của khoa học và công nghệ. Khối kiến thức này được tổ chức đào tạo chủ yếu trong 4 học kỳ đầu.
b) Khối kiến thức giáo dục chuyên nghiệp gồm các học phần cơ sở ngành và các học phần chuyên ngành nhằm cung cấp cho người học những kiến thức và kỹ năng nghề nghiệp cần thiết. Khối kiến thức giáo dục chuyên nghiệp được quy định cụ thể trong từng chương trình đào tạo. Những môn học cơ sở ngành chung của nhiều ngành khác nhau gọi là môn học cơ sở nhóm ngành.
3. Mỗi khối  kiến thức có 2 nhóm học phần như sau:
a) Nhóm học phần bắt buộc gồm những học phần chứa đựng những nội dung kiến thức chính yếu của ngành đào tạo, bắt buộc sinh viên phải đăng ký học và tích lũy.
b) Nhóm học phần tự chọn gồm những học phần chứa đựng những nội dung kiến thức cần thiết và sinh viên được tự chọn theo hướng chuyên môn, tạo sự mềm dẻo trong chương trình đào tạo. Các học phần tự chọn có thể được xếp theo từng nhóm, sinh viên phải tích lũy được một số học phần nhất định trong từng nhóm nhằm tích lũy đủ số tín chỉ tối thiểu quy định cho nhóm học phần tự chọn tương ứng. Sinh viên chọn lựa những học phần này theo hướng dẫn của cố vấn học tậP.
4. Các học phần trong chương trình đào tạo được sắp xếp theo trình tự nhất định vào từng học kỳ của khóa đào tạo. Đây là trình tự mà Trường khuyến cáo sinh viên nên tuân thủ để thuận lợi nhất cho việc tiếp thu kiến thức.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0085` | score `0.700000` | document `virhe4qa_37318b15d819dcedcaa6`**

```text
Điều 14. Đăng ký học tập Sinh viên được đăng ký học và thi các môn học trong chương trình đào tạo do bất kỳ một CSĐT nào thuộc ĐHQG-HCM hoặc hệ thống các trường thành viên của ASEAN University Network tổ chức giảng dạy. Việc chuyển đổi và công nhận tín chỉ được thực hiện theo quy định tại Điều 27 của Quy chế này. Nếu đăng ký học tại Trường thì đầu mỗi học kỳ, sinh viên phải tìm hiểu, nghiên cứu để nắm được chương trình giáo dục, các học phần được mở trong học kỳ và đăng ký các học phần qua hệ thống đăng ký hoặc bằng phiếu đăng ký theo quy định của Trường. Riêng sinh viên khóa tuyển mới, học kỳ đầu tiên sẽ học theo thời khóa biểu được xếp sẵn dựa trên kế hoạch giảng dạy mẫu theo chương trình đào tạo. 1. Số tín chỉ tối thiểu, tối đa Số tín chỉ tối thiểu, tối đa được tính bao gồm số các tín chỉ đăng ký tại Trường hoặc CSĐT khác. a) Trong học kỳ chính: - Số tín chỉ đăng ký học n trong mỗi h…
```

**Rank 2 | `chunk_0181` | score `0.552632` | document `virhe4qa_5b3d1bd990bf2d25a880`**

```text
Điều 3. Môn học 1. Học phần (hay môn học) là khối lượng kiến thức tương đối trọn vẹn, thuận tiện cho người học tích lũy trong quá trình học tập, nội dung được bố trí giảng dạy trong một học kỳ. Mỗi học phần được ký hiệu bằng một mã riêng do Trường quy định. Mỗi học phần thực hành, thí nghiệm, kiến tập,… có khối lượng từ 1 – 3 tín chỉ, mỗi học phần lý thuyết hoặc học phần có cả lý thuyết và thực hành có khối lượng từ 1 – 4 tín chỉ. Trường có hai hình thức tổ chức giảng dạy thực hành: - Thực hành Hình thức 1 (HT1): là hình thức dạy thực hành có sự hướng dẫn của giảng viên cho toàn thời lượng học thực hành. - Thực hành Hình thức 2 (HT2): là hình thức dạy thực hành có sự hướng dẫn của giảng viên với thời lượng 09 tiết/tín chỉ thực hành, không nhất thiết phải sử dụng phòng thực hành chuyên dụng. 2. Các loại học phần - Học phần tích lũy: là học phần mà sinh viên có kết quả tổng kết học phần đ…
```

**Rank 3 | `chunk_0250` | score `0.500000` | document `virhe4qa_720a25859206a5742dc8`**

```text
Điều 7. Chương trình đào tạo 1. Chương trình đào tạo của mỗi ngành đào tạo do Trường xây dựng phù hợp với các quy định hiện hành của Bộ GD&ĐT và ĐHQG-HCM, được bổ sung cập nhật nội dung chương trình giáo dục tiên tiến quốc tế theo định hướng đào tạo nguồn nhân lực chất lượng cao, đáp ứng nhu cầu phát triển khoa học, công nghệ, kinh tế, xã hội đất nước và hội nhập quốc tế. Chương trình đào tạo phải đảm bảo các điều kiện sau: a) Đáp ứng được mục tiêu chương trình giáo dục đại học quy định tại Điều 2, Khoản 1 của quy chế này, mục tiêu cụ thể và chuẩn đầu ra của chương trình đào tạo; đảm bảo các yêu cầu theo quy định của Luật giáo dục đại học; đáp ứng Khung trình độ năng lực quốc gia; đáp ứng Bộ phẩm chất, năng lực sinh viên tốt nghiệp ĐHQG-HCM và các quy định hiện hành khác về CTĐT; phù hợp với nhu cầu sử dụng nhân lực của ngành, địa phương và xã hội. b) Thể hiện rõ trình độ đào tạo; điều …
```

**Rank 4 | `chunk_0182` | score `0.388889` | document `virhe4qa_c436b8422fd4be91aecc`**

```text
Điều 3. Môn học 1. Học phần (hay môn học) là khối lượng kiến thức tương đối trọn vẹn, thuận tiện cho người học tích lũy trong quá trình học tập, nội dung được bố trí giảng dạy trong một học kỳ. Mỗi học phần được ký hiệu bằng một mã riêng do Trường quy định. Mỗi học phần thực hành, thí nghiệm, kiến tập,… có khối lượng từ 1 – 3 tín chỉ, mỗi học phần lý thuyết hoặc học phần có cả lý thuyết và thực hành có khối lượng từ 1 – 4 tín chỉ. Trường có hai hình thức tổ chức giảng dạy thực hành: - Thực hành Hình thức 1 (HT1): là hình thức dạy thực hành có sự hướng dẫn của giảng viên cho toàn thời lượng học thực hành. - Thực hành Hình thức 2 (HT2): là hình thức dạy thực hành có sự hướng dẫn của giảng viên với thời lượng 09 tiết/tín chỉ thực hành, không nhất thiết phải sử dụng phòng thực hành chuyên dụng. 2. Các loại học phần - Học phần tích lũy: là học phần mà sinh viên có kết quả tổng kết học phần đ…
```

**Rank 5 | `chunk_0216` | score `0.361111` | document `virhe4qa_ae295b2fe64356a35465`**

```text
Điều 5. Chương trình đào tạo CT CLC được xây dựng trên nền chương trình đào tạo đại trà tương ứng và theo quy định xây dựng chương trình đào tạo của Trường ĐHCNTT. CT CLC có sự khác biệt so với chương trình đại trà ở những điểm dưới đây: - Chuẩn đầu ra của CT CLC phải cao hơn chuẩn đầu ra của chương trình đại trà tương ứng về năng lực chuyên môn; năng lực ngoại ngữ; năng lực làm việc nhóm; khả năng thích nghi với môi trường công tác. - Chuẩn đầu ra ngoại ngữ: để được xét tốt nghiệp, sinh viên phải hoàn tất chương trình ngoại ngữ bắt buộc trong chương trình đào tạo và có một trong các chứng chỉ ngoại ngữ đạt trình độ tối thiểu: • Tiếng Anh: bậc 4/6 theo khung năng lực ngoại ngữ 6 bậc dùng cho Việt Nam. Cụ thể mức quy đổi sang các chứng chỉ quốc tế được quy định trong Quy định đào tạo ngoại ngữ hiện hành của Trường. • Tiếng Nhật: tương đương JLPT N3. - Để đảm bảo tính liên thông giữa CT C…
```


---

## 20. `query_032`

**Question:** Kết quả học tập của sinh viên có được ghi vào bảng điểm không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `3` |
| Dense first gold rank | `3` |
| Sparse first gold rank | `5` |
| Gold chunk | `chunk_0195` |
| Gold document | `virhe4qa_56f9722f28119591218c` |
| Gold source index | `2663` |
| Hybrid top 1 | `chunk_0164` (score `1.000000`) |

### Gold context

```text
Điều  34. Cấp bằng tốt nghiệp
1.   Bằng tốt nghiệp được cấp theo ngành đào tạo. Bằng chỉ được cấp cho sinh viên khi đã ghi đầy đủ, chính xác các nội dung trên bằng. 
2.   Xếp loại tốt nghiệp được xác định dựa trên ĐTBCTL theo bảng xếp loại quy định tại Khoản 1, Điều 21 của Quy chế này. Riêng đối với những sinh viên có kết quả học tập toàn khóa đạt "Xuất sắc", loại tốt nghiệp sẽ giảm xuống 1 bậc nếu rơi vào các trường hợp sau (nếu đồng thời rơi vào nhiều trường hợp thì cũng chỉ giảm 1 bậc): 
-	Có thời gian học tập tại Trường vượt quá 02 học kỳ so với thời gian thiết kế chương trình đào tạo.
-	Trong thời gian học, đã bị kỷ luật mức cảnh cáo trở lên.
-	Có số tín chỉ học lại vượt quá 5% tổng số tín chỉ toàn khóa.
-	Điểm rèn luyện toàn khóa học < 75 điểm.
3.  Kết quả học tập của sinh viên phải được ghi vào bảng điểm theo từng học phần. Trong bảng điểm ghi rõ chuyên ngành (nếu có) và điểm rèn luyện toàn khóa học.
4.   Những sinh viên không đủ điều kiện cấp bằng tốt nghiệp nhưng chưa hết thời gian tối đa được phép học, được bảo lưu các học phần có kết quả đạt. Trong thời gian tối đa được phép học như quy định tại Khoản 2, Điều 6 của Quy chế này, sinh viên được đăng ký học lại những học phần chưa đạt hoặc chưa học.
5. Trường hợp sinh viên được cho thôi học theo mục b Khoản 3 Điều 16 của quy chế này sinh viên được hoàn thiện các điều kiện còn thiếu và đề nghị xét công nhận tốt nghiệP.
6.   Những sinh viên đã hết thời hạn tối đa được phép học nhưng không đủ điều kiện cấp bằng tốt nghiệp hoặc đã thôi học được đề nghị Trường cấp giấy chứng nhận kết quả học tập của các học phần đã tích lũy trong quá trình học tại Trường.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0164` | score `1.000000` | document `virhe4qa_9afbce60df65f26c0375`**

```text
Điều 27. Cấp bảng điểm 1. Trong quá trình học tập, sinh viên có thể đề nghị Trường cấp bảng điểm. Sinh viên thực hiện theo hướng dẫn của P.ĐTĐH. 2. Sau khi tốt nghiệp, sinh viên được cấp một bảng điểm kèm theo bằng tốt nghiệP.
```

**Rank 2 | `chunk_0142` | score `0.666667` | document `virhe4qa_5f19f0f546a8d9c67b8b`**

```text
Điều 21. Đánh giá kết quả học tập của học phần, học kỳ, năm học, toàn khóa 1. Thang điểm đánh giá và xếp loại Các loại điểm của học phần được đánh giá theo thang điểm 10. Các thang điểm khác chỉ mang tính tham khảo, chuyển đổi khi cần thiết. Bảng xếp loại và thang điểm tương ứng : Từ 5,0 đến 10,0 được xem là đạt, trong đó : Từ 5,0 đến cận 6,0 trong thang điểm 10 là Trung bình. Từ 6,0 đến cận 7,0 trong thang điểm 10 là Trung bình khá. Từ 7,0 đến cận 8,0 trong thang điểm 10 là Khá. Từ 8,0 đến cận 9,0 trong thang điểm 10 là Giỏi. Từ 9,0 đến cận 10,0 trong thang điểm 10 là Xuất sắc. Từ 0,0 đến cận 5,0 được xem là không đạt: Từ 4,0 đến cận 5,0 trong thang điểm 10 là Yếu. Từ 0,0 đến cận 4,0 trong thang điểm 10 là Kém. 2. Điểm cuối cùng để đánh giá một học phần được gọi là điểm học phần. Điểm học phần được đánh giá dựa trên kết quả học tập toàn diện của sinh viên trong suốt học kỳ đối với học …
```

**Rank 3 | `chunk_0195` | score `0.416667` | document `virhe4qa_56f9722f28119591218c`**

```text
Điều 34. Cấp bằng tốt nghiệp 1. Bằng tốt nghiệp được cấp theo ngành đào tạo. Bằng chỉ được cấp cho sinh viên khi đã ghi đầy đủ, chính xác các nội dung trên bằng. 2. Xếp loại tốt nghiệp được xác định dựa trên ĐTBCTL theo bảng xếp loại quy định tại Khoản 1, Điều 21 của Quy chế này. Riêng đối với những sinh viên có kết quả học tập toàn khóa đạt "Xuất sắc", loại tốt nghiệp sẽ giảm xuống 1 bậc nếu rơi vào các trường hợp sau (nếu đồng thời rơi vào nhiều trường hợp thì cũng chỉ giảm 1 bậc): - Có thời gian học tập tại Trường vượt quá 02 học kỳ so với thời gian thiết kế chương trình đào tạo. - Trong thời gian học, đã bị kỷ luật mức cảnh cáo trở lên. - Có số tín chỉ học lại vượt quá 5% tổng số tín chỉ toàn khóa. - Điểm rèn luyện toàn khóa học < 75 điểm. 3. Kết quả học tập của sinh viên phải được ghi vào bảng điểm theo từng học phần. Trong bảng điểm ghi rõ chuyên ngành (nếu có) và điểm rèn luyện t…
```

**Rank 4 | `chunk_0085` | score `0.350000` | document `virhe4qa_37318b15d819dcedcaa6`**

```text
Điều 14. Đăng ký học tập Sinh viên được đăng ký học và thi các môn học trong chương trình đào tạo do bất kỳ một CSĐT nào thuộc ĐHQG-HCM hoặc hệ thống các trường thành viên của ASEAN University Network tổ chức giảng dạy. Việc chuyển đổi và công nhận tín chỉ được thực hiện theo quy định tại Điều 27 của Quy chế này. Nếu đăng ký học tại Trường thì đầu mỗi học kỳ, sinh viên phải tìm hiểu, nghiên cứu để nắm được chương trình giáo dục, các học phần được mở trong học kỳ và đăng ký các học phần qua hệ thống đăng ký hoặc bằng phiếu đăng ký theo quy định của Trường. Riêng sinh viên khóa tuyển mới, học kỳ đầu tiên sẽ học theo thời khóa biểu được xếp sẵn dựa trên kế hoạch giảng dạy mẫu theo chương trình đào tạo. 1. Số tín chỉ tối thiểu, tối đa Số tín chỉ tối thiểu, tối đa được tính bao gồm số các tín chỉ đăng ký tại Trường hoặc CSĐT khác. a) Trong học kỳ chính: - Số tín chỉ đăng ký học n trong mỗi h…
```

**Rank 5 | `chunk_0047` | score `0.300000` | document `virhe4qa_b259d297ad52c6a72ba7`**

```text
Điều 11. Đánh giá kết quả học tập của học phần Việc lựa chọn các hình thức đánh giá và trọng số của các thành phần đánh giá được quy định rõ trong đề cương chi tiết của môn học, giảng viên phải công bố cho sinh viên vào đầu mỗi học kỳ. Giảng viên ra đề thi, đề kiểm tra bằng tiếng Anh. Sinh viên thực hiện các báo cáo môn học, seminar, bài thi giữa kỳ, cuối kỳ bằng tiếng Anh. Điểm tổng hợp đánh giá môn học (gọi tắt là điểm môn học) là điểm kiểm tra xuyên suốt quá trình học tập bao gồm điểm quá trình (chuyên cần), điểm thực hành, điểm thi giữa học phần (giữa kỳ), điểm thi kết thúc học phần (cuối kỳ).
```


---

## 21. `query_033`

**Question:** Kết quả đăng ký học phần được thông báo ở đâu?

| Field | Value |
|---|---|
| Hybrid first gold rank | `3` |
| Dense first gold rank | `4` |
| Sparse first gold rank | `4` |
| Gold chunk | `chunk_0094` |
| Gold document | `virhe4qa_e7dc822dea4ebc591dd7` |
| Gold source index | `1839` |
| Hybrid top 1 | `chunk_0182` (score `0.531250`) |

### Gold context

```text
Điều  15. Trách nhiệm của sinh viên và cố vấn học tập
1.  Sinh viên có trách nhiệm theo dõi kết quả đăng ký học phần trên Cổng thông tin đào tạo của Trường. Kết quả đăng ký học phần thể hiện: tên học phần, mã học phần, số tín chỉ của mỗi học phần, lịch học của các học phần.
2.  Sinh viên có trách nhiệm thực hiện đầy đủ các yêu cầu của môn học như lên lớp, làm bài tập, thực hành, thí nghiệm, tham gia thảo luận, dự kiểm tra thường kỳ và thi kết thúc học phần.
3.  Mỗi lớp sinh viên có một Cố vấn học tập. Cố vấn học tập do Trưởng khoa/Trưởng bộ môn quản lý ngành đào tạo đề nghị và Hiệu trưởng ra quyết định bổ nhiệm. Nhiệm vụ cụ thể của Cố vấn học tập có quy định riêng.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0182` | score `0.531250` | document `virhe4qa_c436b8422fd4be91aecc`**

```text
Điều 3. Môn học 1. Học phần (hay môn học) là khối lượng kiến thức tương đối trọn vẹn, thuận tiện cho người học tích lũy trong quá trình học tập, nội dung được bố trí giảng dạy trong một học kỳ. Mỗi học phần được ký hiệu bằng một mã riêng do Trường quy định. Mỗi học phần thực hành, thí nghiệm, kiến tập,… có khối lượng từ 1 – 3 tín chỉ, mỗi học phần lý thuyết hoặc học phần có cả lý thuyết và thực hành có khối lượng từ 1 – 4 tín chỉ. Trường có hai hình thức tổ chức giảng dạy thực hành: - Thực hành Hình thức 1 (HT1): là hình thức dạy thực hành có sự hướng dẫn của giảng viên cho toàn thời lượng học thực hành. - Thực hành Hình thức 2 (HT2): là hình thức dạy thực hành có sự hướng dẫn của giảng viên với thời lượng 09 tiết/tín chỉ thực hành, không nhất thiết phải sử dụng phòng thực hành chuyên dụng. 2. Các loại học phần - Học phần tích lũy: là học phần mà sinh viên có kết quả tổng kết học phần đ…
```

**Rank 2 | `chunk_0188` | score `0.510101` | document `virhe4qa_2d0d3f56308f26e42ee5`**

```text
Điều 30. Công bố thông tin 1. Trường xây dựng trang thông tin điện tử để công bố công khai chuẩn đầu ra, nội dung chương trình đào tạo, điều kiện đảm bảo chất lượng đào tạo tương ứng với quy mô theo chỉ tiêu hàng năm, quy định học vụ và cho phép người sử dụng tra cứu thông tin cơ bản của sinh viên tốt nghiệp theo số hiệu tương ứng trên văn bằng chứng chỉ do Trường cấP. 2. Hộp thư điện tử (email) được Trường cung cấp cho từng sinh viên vào thời điểm nhập học là kênh giao tiếp chính thức giữa Trường với sinh viên.
```

**Rank 3 | `chunk_0094` | score `0.400000` | document `virhe4qa_e7dc822dea4ebc591dd7`**

```text
Điều 15. Trách nhiệm của sinh viên và cố vấn học tập 1. Sinh viên có trách nhiệm theo dõi kết quả đăng ký học phần trên Cổng thông tin đào tạo của Trường. Kết quả đăng ký học phần thể hiện: tên học phần, mã học phần, số tín chỉ của mỗi học phần, lịch học của các học phần. 2. Sinh viên có trách nhiệm thực hiện đầy đủ các yêu cầu của môn học như lên lớp, làm bài tập, thực hành, thí nghiệm, tham gia thảo luận, dự kiểm tra thường kỳ và thi kết thúc học phần. 3. Mỗi lớp sinh viên có một Cố vấn học tập. Cố vấn học tập do Trưởng khoa/Trưởng bộ môn quản lý ngành đào tạo đề nghị và Hiệu trưởng ra quyết định bổ nhiệm. Nhiệm vụ cụ thể của Cố vấn học tập có quy định riêng.
```

**Rank 4 | `chunk_0085` | score `0.375000` | document `virhe4qa_37318b15d819dcedcaa6`**

```text
Điều 14. Đăng ký học tập Sinh viên được đăng ký học và thi các môn học trong chương trình đào tạo do bất kỳ một CSĐT nào thuộc ĐHQG-HCM hoặc hệ thống các trường thành viên của ASEAN University Network tổ chức giảng dạy. Việc chuyển đổi và công nhận tín chỉ được thực hiện theo quy định tại Điều 27 của Quy chế này. Nếu đăng ký học tại Trường thì đầu mỗi học kỳ, sinh viên phải tìm hiểu, nghiên cứu để nắm được chương trình giáo dục, các học phần được mở trong học kỳ và đăng ký các học phần qua hệ thống đăng ký hoặc bằng phiếu đăng ký theo quy định của Trường. Riêng sinh viên khóa tuyển mới, học kỳ đầu tiên sẽ học theo thời khóa biểu được xếp sẵn dựa trên kế hoạch giảng dạy mẫu theo chương trình đào tạo. 1. Số tín chỉ tối thiểu, tối đa Số tín chỉ tối thiểu, tối đa được tính bao gồm số các tín chỉ đăng ký tại Trường hoặc CSĐT khác. a) Trong học kỳ chính: - Số tín chỉ đăng ký học n trong mỗi h…
```

**Rank 5 | `chunk_0181` | score `0.365591` | document `virhe4qa_5b3d1bd990bf2d25a880`**

```text
Điều 3. Môn học 1. Học phần (hay môn học) là khối lượng kiến thức tương đối trọn vẹn, thuận tiện cho người học tích lũy trong quá trình học tập, nội dung được bố trí giảng dạy trong một học kỳ. Mỗi học phần được ký hiệu bằng một mã riêng do Trường quy định. Mỗi học phần thực hành, thí nghiệm, kiến tập,… có khối lượng từ 1 – 3 tín chỉ, mỗi học phần lý thuyết hoặc học phần có cả lý thuyết và thực hành có khối lượng từ 1 – 4 tín chỉ. Trường có hai hình thức tổ chức giảng dạy thực hành: - Thực hành Hình thức 1 (HT1): là hình thức dạy thực hành có sự hướng dẫn của giảng viên cho toàn thời lượng học thực hành. - Thực hành Hình thức 2 (HT2): là hình thức dạy thực hành có sự hướng dẫn của giảng viên với thời lượng 09 tiết/tín chỉ thực hành, không nhất thiết phải sử dụng phòng thực hành chuyên dụng. 2. Các loại học phần - Học phần tích lũy: là học phần mà sinh viên có kết quả tổng kết học phần đ…
```


---

## 22. `query_064`

**Question:** Sinh viên thuộc chương trình ĐTTX chưa hoàn thành chương trình đào tạo theo quy định có thể nộp hồ sơ đề nghị xét tốt nghiệp không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `3` |
| Dense first gold rank | `2` |
| Sparse first gold rank | `4` |
| Gold chunk | `chunk_0117` |
| Gold document | `virhe4qa_f97d7f975931894918ac` |
| Gold source index | `3110` |
| Hybrid top 1 | `chunk_0144` (score `0.666667`) |

### Gold context

```text
Điều  19. Điều kiện xét tốt nghiệp và công nhận tốt nghiệp
1.  Định kỳ theo kế hoạch đã được Hiệu trưởng phê duyệt, những sinh viên có đủ các điều kiện sau đây có thể nộp hồ sơ đề nghị xét tốt nghiệp:
-	Tại thời điểm xét tốt nghiệp sinh viên không bị truy cứu trách nhiệm hình sự, không bị kỷ luật từ mức đình chỉ học tập;
-	Hoàn thành nghĩa vụ học phí;
-	Hoàn thành chương trình đào tạo theo quy định;
2.  Căn cứ biên bản và đề nghị của Hội đồng xét tốt nghiệp, Hiệu trưởng ký quyết định công nhận tốt nghiệp cho những sinh viên đủ điều kiện theo quy định.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0144` | score `0.666667` | document `virhe4qa_0d970ef217e73b381ec2`**

```text
Điều 22. Quyền và trách nhiệm của người học 1. Được cung cấp đầy đủ thông tin về tuyển sinh, thời hạn đăng ký nộp hồ sơ, chương trình ĐTTX, điều kiện công nhận giá trị chuyển đổi kết quả học tập, kế hoạch đào tạo, quy định về ĐTTX, yêu cầu về bằng cấp và các chính sách ĐTTX của Trường. 2. Được quyền tham gia học tập các tín chỉ cùng với hệ đào tạo chính quy, hệ vừa làm vừa học theo quy định của Trường. 3. Được cung cấp đầy đủ các thông tin về đánh giá công nhận chuyển đổi kết quả học tập và có thể đề nghị xem xét lại việc đánh giá công nhận kết quả học tập. 4. Nộp hồ sơ đầy đủ và đúng thời gian đã được Trường công bố; nộp lệ phí và học phí theo quy định của Trường. 5. Lập kế hoạch học tập cụ thể theo các yêu cầu về bằng cấp của Trường về chương trình ĐTTX đã được công bố để có thể được cấp bằng tốt nghiệp. 6. Chấp hành Quy chế này và quy định liên quan về ĐTTX của Trường. 7. Chủ động li…
```

**Rank 2 | `chunk_0050` | score `0.545455` | document `virhe4qa_8d5eeb2986483f0c0504`**

```text
Điều 12. Tốt nghiệp Chương trình Tài năng Sinh viên sẽ được cấp bằng "Cử nhân/Kỹ sư Tài năng" (Honor Program) của Trường ĐHCNTT – ĐHQG HCM nếu hội đủ các điều kiện sau: - Đang là sinh viên của CTTN. - Hoàn tất chương trình đúng hạn – đủ điều kiện để được cấp bằng theo đúng ngành học của lớp CTTN tương ứng. Nếu sinh viên đã bảo vệ KLTN đúng hạn nhưng chưa đủ điều kiện tốt nghiệp, Khoa có thể xem xét hoàn cảnh cụ thể để đề nghị BĐH và trình BGH phê duyệt cho phép gia hạn tối đa 1 học kỳ để hoàn tất CTĐT và được cấp bằng CTTN. - Có điểm KLTN  7.0, ĐTBTL  7.0 và điểm rèn luyện từ loại Khá trở lên. - Có trình độ Anh văn đạt chuẩn đầu ra của CTTN do Trường quy định. Các sinh viên không đạt một trong các điều kiện nêu trên sẽ nhận bằng tốt nghiệp như sinh viên chương trình chuẩn khi đã đạt đủ các điều kiện được quy định trong quy chế đào tạo theo học chế tín chỉ của Trường; đồng thời sinh vi…
```

**Rank 3 | `chunk_0117` | score `0.533333` | document `virhe4qa_f97d7f975931894918ac`**

```text
Điều 19. Điều kiện xét tốt nghiệp và công nhận tốt nghiệp 1. Định kỳ theo kế hoạch đã được Hiệu trưởng phê duyệt, những sinh viên có đủ các điều kiện sau đây có thể nộp hồ sơ đề nghị xét tốt nghiệp: - Tại thời điểm xét tốt nghiệp sinh viên không bị truy cứu trách nhiệm hình sự, không bị kỷ luật từ mức đình chỉ học tập; - Hoàn thành nghĩa vụ học phí; - Hoàn thành chương trình đào tạo theo quy định; 2. Căn cứ biên bản và đề nghị của Hội đồng xét tốt nghiệp, Hiệu trưởng ký quyết định công nhận tốt nghiệp cho những sinh viên đủ điều kiện theo quy định.
```

**Rank 4 | `chunk_0194` | score `0.444444` | document `virhe4qa_dc17d6c33c4c33682ef6`**

```text
Điều 33. Điều kiện xét tốt nghiệp và công nhận tốt nghiệp 1. Mỗi năm Trường có 4 đợt xét tốt nghiệp và cấp bằng tốt nghiệp đại học, lịch xét tốt nghiệp được ghi trong kế hoạch năm học. Để được Trường xét cấp bằng tốt nghiệp, sinh viên nộp hồ sơ đề nghị xét tốt nghiệp khi đã đáp ứng đủ các điều kiện sau đây: - Cho đến thời điểm xét tốt nghiệp, sinh viên không đang trong thời gian bị truy cứu trách nhiệm hình sự hoặc bị kỷ luật từ mức đình chỉ học tập trở lên. - Đã hoàn thành nghĩa vụ học phí. - Đã hoàn thành các môn học, tích lũy đủ số tín chỉ theo đúng chương trình đào tạo. - Đã hoàn thành các môn học Giáo dục thể chất. - Có chứng chỉ Giáo dục quốc phòng-An ninh. - Đạt chuẩn ngoại ngữ xét tốt nghiệP. - Đạt điểm rèn luyện tích lũy tối thiểu là 50 điểm. - Đã hoàn trả sách mượn cho Thư viện. 2. Căn cứ biên bản và đề nghị của Hội đồng xét tốt nghiệp, Hiệu trưởng ký quyết định công nhận tốt …
```

**Rank 5 | `chunk_0089` | score `0.340909` | document `virhe4qa_c072ac06f88b20b3bd13`**

```text
Điều 15. Công nhận kết quả học tập Khi có nhu cầu công nhận kết quả học tập từ các chương trình đào tạo trình độ đại học khác, sinh viên nộp đơn xin công nhận kết quả học tập kèm các hồ sơ liên quan cho Phòng Đào tạo Đại học thông qua Trạm ĐTTX chính. Hội đồng khoa quản lý chương trình ĐTTX hoặc hội đồng chuyên môn được Hiệu trưởng thành lập có trách nhiệm xem xét, quyết định công nhận kết quả học tập để chuyển đổi, miễn trừ những môn học mà sinh viên đã tích lũy ở các chương trình đào tạo cấp văn bằng khác. Số tín chỉ được công nhận kết quả học tập để chuyển đổi, miễn trừ tích lũy từ các trường khác ngoài Trường ĐHCNTT không được vượt quá 50% tổng số tín chỉ của chương trình ĐTTX. Hội đồng chuyên môn được Hiệu trưởng thành lập trên cơ sở đề xuất của P.ĐTĐH bao gồm: đại diện Ban Giám hiệu, đại diện lãnh đạo các đơn vị: P.ĐTĐH, Khoa chuyên môn quản lý chương trình ĐTTX, Trạm ĐTTX liên qu…
```


---

## 23. `query_066`

**Question:** Số buổi seminar ngoại khóa của CTTN có giới hạn hay không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `3` |
| Dense first gold rank | `6` |
| Sparse first gold rank | `1` |
| Gold chunk | `chunk_0120` |
| Gold document | `virhe4qa_1c466c63cf51a2b45f7a` |
| Gold source index | `8071` |
| Hybrid top 1 | `chunk_0019` (score `0.666667`) |

### Gold context

```text
Điều  2.	Giải thích từ ngữ
Sinh viên thuộc chương trình tài năng có 02 hình thức là chính thức và dự bị, nằm trong tổng chỉ tiêu của chương trình:
-	Sinh viên chính thức: đảm bảo đáp ứng các tiêu chuẩn theo yêu cầu và được hưởng đầy đủ các quyền lợi của chương trình.
-	Sinh viên dự bị: cùng điều kiện học tập và học cùng chương trình đào tạo với sinh viên chính thức nhưng không được hưởng chính sách về học bổng tài năng. Sinh viên dự bị bao gồm các sinh viên trong lớp tài năng vi phạm điều kiện đạt sinh viên chính thức nhưng chưa bị loại ra khỏi chương trình trong các đợt xét sau mỗi học kỳ, và sinh viên mới tuyển bổ sung vào chương trình. 
Môn học cốt lõi: là môn học quan trọng trong CTĐT, là phần kiến thức không thể thiếu trong lĩnh vực chuyên môn liên quan tới ngành đào tạo chương trình tài năng. Danh sách môn học cốt lõi do Khoa đề nghị trong đề án mở chương trình tài năng.
Seminar ngoại khóa: được tổ chức ngoài buổi học theo thời khóa biểu chính thức để tăng cường kỹ năng cho sinh viên lớp chương trình tài năng. Số buổi seminar phải hạn chế để không làm tăng quá mức khối lượng học tập của sinh viên.
Đơn vị quản lý chương trình: là VPCTĐB, có nhiệm vụ triển khai mọi hoạt động học tập, quản lý sinh viên thuộc CTTN.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0019` | score `0.666667` | document `virhe4qa_19690d6debbd2505c914`**

```text
Điều 10. Giảng dạy các môn CTTN CTTN phải được thực hiện trên quan điểm lấy người học làm trung tâm. Người học phải được tạo điều kiện để thể hiện vai trò chủ động trong tiến trình học tập. Người học phải đóng vai trò chủ động trong hoạt động học tập, thay vì thụ động tiếp nhận kiến thức. Sinh viên CTTN sẽ học cùng với sinh viên các lớp chương trình chuẩn trong các môn được đào tạo chung, các môn học cốt lõi dành riêng cho sinh viên CTTN được tổ chức lớp học riêng. Khoa quản lý chuyên môn có trách nhiệm chọn các cán bộ có kinh nghiệm để phụ trách giảng dạy. Các môn học tài năng và KLTN phải do CBGD có học vị tiến sĩ hoặc giảng viên chính, hoặc thạc sĩ tốt nghiệp ở các trường Đại học thuộc các nước tiên tiến, đúng ngành hoặc thuộc ngành gần đảm nhiệm. Trong tuần đầu tiên của học kỳ, CBGD phải thông báo công khai cho sinh viên về đề cương giảng dạy môn học; trong đó đặc biệt chú ý các thô…
```

**Rank 2 | `chunk_0274` | score `0.666667` | document `virhe4qa_c31538b810cd4921a313`**

```text
Điều 9. Tuyển bổ sung và loại ra khỏi chương trình, xét chính thức và dự bị Đối tượng tham gia CTTN là những sinh viên có năng lực xuất sắc, do đó, sau mỗi học kỳ BĐH quyết định việc loại sinh viên khỏi lớp tài năng, tuyển bổ sung sinh viên từ chương trình chuẩn vào lớp tài năng, xét chuyển đổi sinh viên chính thức và dự bị. Đầu mỗi học kỳ, Khoa xét và đề nghị lên BĐH các danh sách sinh viên tuyển bổ sung, bị loại ra khỏi các lớp CTTN hoặc danh sách sinh viên chính thức và dự bị theo các tiêu chuẩn như sau: 1. Loại khỏi chương trình Tại thời điểm xem xét, sinh viên rơi vào một trong các trường hợp sau: - Chưa tốt nghiệp khi đã quá thời gian thiết kế của khóa học và không có lý do đặc biệt. - Không đăng ký học đầy đủ các môn học CTTN bắt buộc trong học kỳ. - ĐTBTL nhỏ hơn 6,5 – tính tương ứng sau học kỳ 1 và sau học kỳ hè (kết quả học tập của học kỳ hè sẽ được tính chung vào kết quả học …
```

**Rank 3 | `chunk_0120` | score `0.642857` | document `virhe4qa_1c466c63cf51a2b45f7a`**

```text
Điều 2. Giải thích từ ngữ Sinh viên thuộc chương trình tài năng có 02 hình thức là chính thức và dự bị, nằm trong tổng chỉ tiêu của chương trình: - Sinh viên chính thức: đảm bảo đáp ứng các tiêu chuẩn theo yêu cầu và được hưởng đầy đủ các quyền lợi của chương trình. - Sinh viên dự bị: cùng điều kiện học tập và học cùng chương trình đào tạo với sinh viên chính thức nhưng không được hưởng chính sách về học bổng tài năng. Sinh viên dự bị bao gồm các sinh viên trong lớp tài năng vi phạm điều kiện đạt sinh viên chính thức nhưng chưa bị loại ra khỏi chương trình trong các đợt xét sau mỗi học kỳ, và sinh viên mới tuyển bổ sung vào chương trình. Môn học cốt lõi: là môn học quan trọng trong CTĐT, là phần kiến thức không thể thiếu trong lĩnh vực chuyên môn liên quan tới ngành đào tạo chương trình tài năng. Danh sách môn học cốt lõi do Khoa đề nghị trong đề án mở chương trình tài năng. Seminar ngo…
```

**Rank 4 | `chunk_0064` | score `0.350000` | document `virhe4qa_3abd8382b4312b3ad46f`**

```text
Điều 13. Quy định về tài chính 1. Học bổng sinh viên Học bổng chương trình: học bổng được cấp cho sinh viên theo từng học kỳ – một học kỳ tính là 5.0 tháng. Mức học bổng hàng năm do Hiệu trưởng quyết định. Tất cả các sinh viên tài năng theo danh sách chính thức từng học kỳ đều được hưởng học bổng này. Học bổng khuyến khích học tập: sinh viên tài năng được tham gia xét hưởng học bổng khuyến khích học tập theo quy định của nhà nước tương tự như các sinh viên chương trình khác (xét chung theo khóa, Khoa-Ngành). 2. Khen thưởng sinh viên Căn cứ vào tình hình kinh phí và hoạt động của các lớp CTTN, Hiệu trưởng quyết định thêm các hình thức khen thưởng sau: - Sinh viên đạt thành tích xuất sắc trong các cuộc thi học thuật. - Tuyên dương nỗ lực phấn đấu và tích cực tham gia phong trào, do tập thể lớp bình chọn. 3. Chi nghiệp vụ chuyên môn đặc biệt khác Ngoài các khoản chi thường xuyên kể trên, đ…
```

**Rank 5 | `chunk_0172` | score `0.326923` | document `virhe4qa_eee1040f5afc88d187a4`**

```text
Điều 3. Mục tiêu đào tạo Mục tiêu đào tạo của CTTN nhằm: - Tuyển chọn và tạo điều kiện phát triển cho các sinh viên ưu tú, đào tạo nguồn nhân lực chất lượng cao, cán bộ đầu ngành cho các đơn vị sản xuất, hoạt động kinh tế, cán bộ giảng dạy cho các trường đại học, cao đẳng tại TP. HCM và trong cả nước. - Sinh viên được phát triển toàn diện về kiến thức, kỹ năng, thái độ và ngoại ngữ. - Sinh viên được định hướng để phát huy năng lực sở trường, có tầm nhìn và kiến thức rộng; tăng cường hỗ trợ về hoạt động học thuật, nghiên cứu khoa học và công nghệ.
```


---

## 24. `query_075`

**Question:** Trường hợp chưa nhận chứng chỉ GDQP-AN thì có thể đăng ký xét tốt nghiệp không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `3` |
| Dense first gold rank | `2` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0194` |
| Gold document | `virhe4qa_dc17d6c33c4c33682ef6` |
| Gold source index | `2614` |
| Hybrid top 1 | `chunk_0117` (score `0.750000`) |

### Gold context

```text
Điều  33. Điều kiện xét tốt nghiệp và công nhận tốt nghiệp
1.  Mỗi năm Trường có 4 đợt xét tốt nghiệp và cấp bằng tốt nghiệp đại học, lịch xét tốt nghiệp được ghi trong kế hoạch năm học. Để được Trường xét cấp bằng tốt nghiệp, sinh viên nộp hồ sơ đề nghị xét tốt nghiệp khi đã đáp ứng đủ các điều kiện sau đây: 
-        Cho đến thời điểm xét tốt nghiệp, sinh viên không đang trong thời gian bị truy cứu trách nhiệm hình sự hoặc bị kỷ luật từ mức đình chỉ học tập trở lên.
-        Đã hoàn thành nghĩa vụ học phí.
-        Đã hoàn thành các môn học, tích lũy đủ số tín chỉ theo đúng chương trình đào tạo.
-        Đã hoàn thành các môn học Giáo dục thể chất.
-        Có chứng chỉ Giáo dục quốc phòng-An ninh.
-        Đạt chuẩn ngoại ngữ xét tốt nghiệP.
-        Đạt điểm rèn luyện tích lũy tối thiểu là 50 điểm.
-        Đã hoàn trả sách mượn cho Thư viện.
2.   Căn cứ biên bản và đề nghị của Hội đồng xét tốt nghiệp, Hiệu trưởng ký quyết định công nhận tốt nghiệp cho những sinh viên đủ điều kiện theo quy định.
3. Hội đồng xét tốt nghiệp do Hiệu trưởng hoặc Phó Hiệu trưởng được Hiệu trưởng ủy quyền làm Chủ tịch, Trưởng phòng hoặc Phó Trưởng phòng Đào tạo Đại học làm thư ký; các thành viên khác là lãnh đạo các khoa quản lý ngành đào tạo, lãnh đạo Phòng Công tác Sinh viên.
4. Sinh viên đủ điều kiện tốt nghiệp được Hiệu trưởng ra quyết định công nhận tốt nghiệp và được cấp bằng tốt nghiệp trong vòng 03 tháng tính từ ngày có quyết định công nhận tốt nghiệP.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0117` | score `0.750000` | document `virhe4qa_f97d7f975931894918ac`**

```text
Điều 19. Điều kiện xét tốt nghiệp và công nhận tốt nghiệp 1. Định kỳ theo kế hoạch đã được Hiệu trưởng phê duyệt, những sinh viên có đủ các điều kiện sau đây có thể nộp hồ sơ đề nghị xét tốt nghiệp: - Tại thời điểm xét tốt nghiệp sinh viên không bị truy cứu trách nhiệm hình sự, không bị kỷ luật từ mức đình chỉ học tập; - Hoàn thành nghĩa vụ học phí; - Hoàn thành chương trình đào tạo theo quy định; 2. Căn cứ biên bản và đề nghị của Hội đồng xét tốt nghiệp, Hiệu trưởng ký quyết định công nhận tốt nghiệp cho những sinh viên đủ điều kiện theo quy định.
```

**Rank 2 | `chunk_0275` | score `0.700000` | document `virhe4qa_9ee423b212481d1ec26d`**

```text
Điều 9. Văn bằng, chứng chỉ/chứng nhận được sử dụng để công nhận đạt chuẩn xét tốt nghiệp Để được xét tốt nghiệp sinh viên phải hoàn tất các môn học tiếng Anh trong chương trình giảng dạy tiếng Anh tại Điều 3 và có một trong các văn bằng, chứng chỉ/chứng nhận được quy định như sau: 1. Văn bằng tốt nghiệp đại học/trên đại học trong nước, nước ngoài mà ngành học hoặc ngôn ngữ sử dụng toàn phần trong đào tạo (không thông qua phiên dịch) là một trong ba ngoại ngữ: tiếng Anh, tiếng Pháp, tiếng Nhật. 2. Chứng chỉ/chứng nhận ngoại ngữ: Sinh viên có một trong các loại chứng chỉ/chứng nhận tiếng Anh, có chứng chỉ/chứng nhận tiếng Pháp, hoặc tiếng Nhật tối thiểu như sau Đối với chương trình văn bằng 2, liên thông, chương trình chuẩn phải đạt chứng chỉ tiếng Anh TOEIC Nghe-Đọc đạt từ 450 trở lên và TOEIC Nói-Viết đạt từ 185 trở lên hoặc TOEFL iBT đạt từ 45 trở lên hoặc IELTS đạt 4.5, chứng chỉ Cam…
```

**Rank 3 | `chunk_0194` | score `0.666667` | document `virhe4qa_dc17d6c33c4c33682ef6`**

```text
Điều 33. Điều kiện xét tốt nghiệp và công nhận tốt nghiệp 1. Mỗi năm Trường có 4 đợt xét tốt nghiệp và cấp bằng tốt nghiệp đại học, lịch xét tốt nghiệp được ghi trong kế hoạch năm học. Để được Trường xét cấp bằng tốt nghiệp, sinh viên nộp hồ sơ đề nghị xét tốt nghiệp khi đã đáp ứng đủ các điều kiện sau đây: - Cho đến thời điểm xét tốt nghiệp, sinh viên không đang trong thời gian bị truy cứu trách nhiệm hình sự hoặc bị kỷ luật từ mức đình chỉ học tập trở lên. - Đã hoàn thành nghĩa vụ học phí. - Đã hoàn thành các môn học, tích lũy đủ số tín chỉ theo đúng chương trình đào tạo. - Đã hoàn thành các môn học Giáo dục thể chất. - Có chứng chỉ Giáo dục quốc phòng-An ninh. - Đạt chuẩn ngoại ngữ xét tốt nghiệP. - Đạt điểm rèn luyện tích lũy tối thiểu là 50 điểm. - Đã hoàn trả sách mượn cho Thư viện. 2. Căn cứ biên bản và đề nghị của Hội đồng xét tốt nghiệp, Hiệu trưởng ký quyết định công nhận tốt …
```

**Rank 4 | `chunk_0143` | score `0.300000` | document `virhe4qa_8afc10b2b9227422bbe5`**

```text
Điều 22. Không hoàn tất học phần Trường hợp vì những lý do chính đáng không thể dự thi, kiểm tra (ốm đau, tai nạn, việc gia đình đột xuất,…), sinh viên được xem xét giải quyết cho nhận điểm chưa hoàn tất học phần (hoãn thi), ký hiệu bằng chữ I. 1. Trước khi kết thúc học kỳ, sinh viên nộp đơn trình bày rõ lý do không thể hoàn tất học phần cùng các giấy tờ minh chứng cần thiết cho cán bộ giảng dạy học phần đó và P.ĐTĐH. Trường hợp đột xuất và có lý do chính đáng, sinh viên phải nộp trong vòng 3 ngày kể từ ngày thi kết thúc học phần để được xem xét. 2. Cán bộ giảng dạy phụ trách học phần, khoa/bộ môn quản lý chương trình đào tạo và P.ĐTĐH xem xét và quyết định sinh viên có được nhận điểm I hay không. Nếu không được chấp thuận, sinh viên tự ý bỏ thi sẽ nhận điểm không (0) cho học phần đó. 3. Nếu được nhận điểm I, trong thời gian tối đa là 2 học kỳ chính tiếp theo, sinh viên phải làm đơn đăn…
```

**Rank 5 | `chunk_0085` | score `0.291667` | document `virhe4qa_37318b15d819dcedcaa6`**

```text
Điều 14. Đăng ký học tập Sinh viên được đăng ký học và thi các môn học trong chương trình đào tạo do bất kỳ một CSĐT nào thuộc ĐHQG-HCM hoặc hệ thống các trường thành viên của ASEAN University Network tổ chức giảng dạy. Việc chuyển đổi và công nhận tín chỉ được thực hiện theo quy định tại Điều 27 của Quy chế này. Nếu đăng ký học tại Trường thì đầu mỗi học kỳ, sinh viên phải tìm hiểu, nghiên cứu để nắm được chương trình giáo dục, các học phần được mở trong học kỳ và đăng ký các học phần qua hệ thống đăng ký hoặc bằng phiếu đăng ký theo quy định của Trường. Riêng sinh viên khóa tuyển mới, học kỳ đầu tiên sẽ học theo thời khóa biểu được xếp sẵn dựa trên kế hoạch giảng dạy mẫu theo chương trình đào tạo. 1. Số tín chỉ tối thiểu, tối đa Số tín chỉ tối thiểu, tối đa được tính bao gồm số các tín chỉ đăng ký tại Trường hoặc CSĐT khác. a) Trong học kỳ chính: - Số tín chỉ đăng ký học n trong mỗi h…
```


---

## 25. `query_097`

**Question:** Đơn vị phụ trách thực hiện công tác chấm trắc nghiệm là đơn vị nào?

| Field | Value |
|---|---|
| Hybrid first gold rank | `3` |
| Dense first gold rank | `6` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0112` |
| Gold document | `virhe4qa_6d2582de9eda27704ab6` |
| Gold source index | `5313` |
| Hybrid top 1 | `chunk_0098` (score `0.700000`) |

### Gold context

```text
Điều  18. Quy trình chấm thi
1.	Đầu vào, đầu ra, thời gian:
Đầu vào: túi bài thi/dữ liệu về bài thi
Đầu ra: túi bài thi/dữ liệu về bài thi (có điểm trên bài thi/dữ liệu về bài thi), bảng điểm
Thời gian: Quy trình được tính bằng ngày (tính cả ngày nghỉ), diễn ra theo mốc thời gian: ngày thi của một môn học t.
2.	Sơ đồ tóm tắt
Quy trình chấm thi sẽ diễn ra như sau. Khoa sẽ tiến hành phân công cán bộ chấm thi. Sau đó khoa sẽ chuyển bài thi trắc nghiệm cho Phòng Đào tạo Đại học để quét phiểu trả lời trắc nghiệm (hoặc khoa sẽ tự chấm nếu đó là bài thi tự luận). Phòng Đào tạo Đại học/ Văn phòng Đặc biệt sẽ chuyển file kết quả chấm về Khoa để các cán bộ chấm thi ở khoa quy đổi điểm. Sau khi có điểm (cả trắc nghiệm và tự luận), cán bộ chấm thi sẽ nhập điểm, in và nộp bảng điểm. Sau đó Khoa sẽ tiến hành tập hợp và nộp điểm, hồ sơ thi về Phòng Đào tạo Đại học/ Văn phòng Đặc biệt để kiểm tra và tiến hành lưu trữ bảng điểm và hồ sơ thi.
3.	Nội dung quy trình
Bước 1: Phân công cán bộ chấm thi. Khoa sẽ phân công cán bộ chấm thi cho từng túi bài thi/phòng thi. Thời gian hoàn thành là 4 ngày kể từ ngày thi của môn học (tính cả ngày nghỉ). Đơn vị thực hiện là Khoa, không có đơn bị phối hợp. Biểu mẫu đi kèm gồm bảng phân công chấm thi (THI-M10).

Bước 2: Chấm thi trắc nghiệm. Các công việc bao gồm: Khoa nộp phiếu trả lời trắc nghiệm cho Phòng Đào tạo Đại học/ Văn phòng Đặc biệt để quét; Phòng Đào tạo Đại học/ Văn phòng Đặc biệt sử dụng phần mềm chấm thi trắc nghiệm để quét phiếu trả lời trắc nghiệm; Sau đó chuyển file kết quả chấm về Khoa để cán bộ chấm thi quy đổi thành điểm chính thức. Thời hạn hoàn thành là 20 ngày kể từ ngày thi của môn học (tính cả ngày nghỉ). Đơn vị thực hiện là Phòng Đào tạo Đại học/ Văn phòng Đặc biệt, Khoa và cán bộ chấm thi, không có đơn vị hỗ trợ. Biểu mẫu phần này bao gồm: phiếu trả lời trắc nghiệm; bảng điểm (THI-M03); Sổ theo dõi bàn giao bài thi và bảng điểm (THI-M08).

Bước 3: Chấm thi tự luận. Cán bộ chấm thi tiến hành chấm thi. Thời hạn hoàn thành là 20 ngày kể từ ngày thi của môn học (tính cả ngày nghỉ). Đơn vị thực hiện là cán bộ chấm thi, không có đơn vị hỗ trợ. Biểu mẫu kèm theo sẽ là bảng điểm (THI-M03).

Bước 4: Nhập điểm, công bố điểm và nộp điểm. Cán bộ chấm thi nhập điểm vào Hệ thống quản lý điểm, xuất bảng điểm từ hệ thống, ký tên và nộp bảng điểm cho Khoa/Phòng Đào tạo Đại học. Điểm được nhập vào hệ thống sẽ được công bố tự động cho sinh viên. Thời hạn hoàn thành là 20 ngày kể từ ngày thi (tính cả ngày nghỉ). Đơn vị thực hiện là Khoa, cán bộ chấm thi, cán bộ giảng dạy. Đơn vị hỗ trợ là Khoa. Các biểu mẫu đi kèm gồm: bảng điểm (THI-M03); Sổ theo dõi bàn giao bài thi và bảng ghi điểm (THI-M08).

Bước 5: Tập hợp điểm, nộp điểm và hồ sơ thi. Khoa photo 01 bản của bảng điểm để lưu tại Khoa, chuyển bản chính bảng điểm cùng bản chính danh sách thi, các giấy phép dự thi cho Phòng Đào tạo Đại học. Thời gian hoàn thành là 25 ngày kể từ ngày thi của môn học (tính cả ngày nghỉ). Đơn vị thực hiện là Khoa. Đơn vị hỗ trợ là Phòng Đào tạo Đại học/ Văn phòng Đặc biệt. Biểu mẫu sẽ gồm bảng điểm (THI-M03); Sổ theo dõi bàn giao bài thi và bảng ghi điểm (THI-M08).

Bước 6: Kiểm tra điểm. Kiểm tra điểm trên bài thi với điểm được nhập vào hệ thống. Thời gian hoàn thành là 60 ngày kể từ ngày thi của môn học(tính cả ngày nghỉ). Đơn vị thực hiện là Phòng Đào tạo Đại học/ Văn phòng Đặc biệt. Không có đơn vị hỗ trợ và không có biểu mẫu kèm theo.

Bước 7: Lưu trữ. Lưu trữ bản chính bảng điểm thi và các hồ sơ liên quan. Thời gian thực hiện là 60 ngày kể từ ngày thi của môn học (tính cả ngày nghỉ). Đon vị thực hiện là Phòng Đào tạo Đại học/ Văn phòng Đặc biệt. Không có đơn vị hỗ trợ và không có biểu mẫu kèm theo.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0098` | score `0.700000` | document `virhe4qa_a9cac8d1751cf9cda397`**

```text
Điều 16. Chấm thi, nhập điểm và công bố điểm 1. ĐVQLMH của môn học có trách nhiệm tổ chức công tác chấm thi cho môn học mà mình quản lý. Khoa chịu trách nhiệm chính về sự chính xác, công bằng và các khía cạnh chuyên môn khác của việc chấm thi. 2. Đối với kỳ thi cuối học kỳ, các môn học có nhiều hơn 01 cán bộ giảng dạy phải có cán bộ chấm thi cho một lớp học khác với cán bộ giảng dạy của lớp học đó (chấm chéo). 3. Qui trình nhập điểm Bước 1: Nhận bài thi/dữ liệu về bài thi - Sau ngày thi, cán bộ chấm thi nhận túi bài thi/dữ liệu về bài thi tại đơn vị tổ chức thi. Bước 2: Cập nhật phân công chấm thi - Đơn vị quản lý môn học gửi danh sách phân công cán bộ chấm thi về P.ĐTĐH/VPĐB (Sử dụng theo mẫu quy định, cập nhật đầy đủ các thông tin liên quan và ký xác nhận lưu trữ bản giấy) ngay sau khi kết thúc môn thi để cập nhập bảng phân công chấm thi lên hệ thống quản lý đào tạo. Bước 3: Nhập điểm…
```

**Rank 2 | `chunk_0180` | score `0.514085` | document `virhe4qa_a15a72b59e2547ea5282`**

```text
Điều 3. Hoạt động thanh tra, kiểm tra, giám sát công tác thi Phòng Thanh tra Pháp chế và Đảm bảo Chất lượng có trách nhiệm tổ chức thanh tra, kiểm tra và giám sát công tác tổ chức thi.
```

**Rank 3 | `chunk_0112` | score `0.476191` | document `virhe4qa_6d2582de9eda27704ab6`**

```text
Điều 18. Quy trình chấm thi 1. Đầu vào, đầu ra, thời gian: Đầu vào: túi bài thi/dữ liệu về bài thi Đầu ra: túi bài thi/dữ liệu về bài thi (có điểm trên bài thi/dữ liệu về bài thi), bảng điểm Thời gian: Quy trình được tính bằng ngày (tính cả ngày nghỉ), diễn ra theo mốc thời gian: ngày thi của một môn học t. 2. Sơ đồ tóm tắt Quy trình chấm thi sẽ diễn ra như sau. Khoa sẽ tiến hành phân công cán bộ chấm thi. Sau đó khoa sẽ chuyển bài thi trắc nghiệm cho Phòng Đào tạo Đại học để quét phiểu trả lời trắc nghiệm (hoặc khoa sẽ tự chấm nếu đó là bài thi tự luận). Phòng Đào tạo Đại học/ Văn phòng Đặc biệt sẽ chuyển file kết quả chấm về Khoa để các cán bộ chấm thi ở khoa quy đổi điểm. Sau khi có điểm (cả trắc nghiệm và tự luận), cán bộ chấm thi sẽ nhập điểm, in và nộp bảng điểm. Sau đó Khoa sẽ tiến hành tập hợp và nộp điểm, hồ sơ thi về Phòng Đào tạo Đại học/ Văn phòng Đặc biệt để kiểm tra và tiế…
```

**Rank 4 | `chunk_0222` | score `0.370370` | document `virhe4qa_954fe80222865e12bc56`**

```text
Điều 5. Trách nhiệm chuẩn bị và tổ chức thi P.ĐTĐH, Văn phòng các Chương trình đặc biệt (VPĐB) và các khoa, bộ môn, trung tâm (gọi tắt là Đơn vị quản lý môn học - ĐVQLMH) có trách nhiệm chuẩn bị và tổ chức thi cho những môn học do mình quản lý. Đơn vị có trách nhiệm chuẩn bị và tổ chức thi cho môn học được gọi tắt là Đơn vị tổ chức thi.
```

**Rank 5 | `chunk_0106` | score `0.316667` | document `virhe4qa_df17347662387e814a99`**

```text
Điều 17. Quản lý điểm thi 1. Cán bộ chấm thi chịu trách nhiệm về tính chính xác của thông tin điểm thi được nhập và công bố cho SV trên Hệ thống quản lý điểm trong thời hạn chấm thi và nộp điểm. 2. P.ĐTĐH/VPĐB chịu trách nhiệm kiểm tra thông tin điểm thi trên Hệ thống quản lý điểm so với điểm được ghi trên bài thi, tiếp nhận và xử lý khiếu nại của SV về điểm thi và cấp bảng điểm theo yêu cầu. 3. Phòng Dữ liệu và Công nghệ Thông tin có trách nhiệm đảm bảo an toàn cho dữ liệu điểm trên Hệ thống quản lý điểm; đảm bảo chỉ cấp quyền nhập và chỉnh sửa điểm cho cán bộ chấm thi đối với thành phần điểm và lớp mà mình phụ trách chấm thi trong thời hạn chấm thi và nộp điểm. Mọi thao tác trên dữ liệu điểm phải được ghi nhận lại đầy đủ và chính xác (người nhập điểm, người chỉnh sửa điểm, thời gian và lý do chỉnh sửa).
```


---

## 26. `query_007`

**Question:** Ban giám hiệu nhà trường có trách nhiệm gì?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `2` |
| Sparse first gold rank | `3` |
| Gold chunk | `chunk_0198` |
| Gold document | `virhe4qa_06d792ed3048eb2fed78` |
| Gold source index | `7129` |
| Hybrid top 1 | `chunk_0109` (score `0.590909`) |

### Gold context

```text
Điều  4.	Tổ chức và điều hành CT CLC
Ban Giám hiệu giao nhiệm vụ cho đơn vị quản lý triển khai chương trình, phối hợp chặt chẽ với đơn vị chuyên môn phụ trách ngành đào tạo.
Đơn vị quản lý triển khai chịu trách nhiệm vận hành chương trình và báo cáo định kỳ cho Ban Giám hiệu.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0109` | score `0.590909` | document `virhe4qa_0c7f9f0f2cf778cbb9f7`**

```text
Điều 18. Hoạt động kiểm tra, giám sát – Ban điều hành CTGT trường ĐHCNTT có trách nhiệm kiểm tra, giám sát các khâu trong công tác quản lý giáo trình tại trường theo đúng Quy định về CTGT của trường ĐHCNTT. – Các Khoa, CBGD tham gia công tác biên soạn giáo trình phục vụ đào tạo tại trường ĐHCNTT có trách nhiệm báo cáo tiến độ thực hiện việc biên soạn theo yêu cầu của Ban điều hành CTGT trường.
```

**Rank 2 | `chunk_0198` | score `0.583333` | document `virhe4qa_06d792ed3048eb2fed78`**

```text
Điều 4. Tổ chức và điều hành CT CLC Ban Giám hiệu giao nhiệm vụ cho đơn vị quản lý triển khai chương trình, phối hợp chặt chẽ với đơn vị chuyên môn phụ trách ngành đào tạo. Đơn vị quản lý triển khai chịu trách nhiệm vận hành chương trình và báo cáo định kỳ cho Ban Giám hiệu.
```

**Rank 3 | `chunk_0121` | score `0.519231` | document `virhe4qa_2810252459b3a6c87c21`**

```text
Điều 2. Phân cấp quản lý công tác giáo trình 2.1. Hiệu trưởng ra quyết định thành lập Ban Điều hành Công tác giáo trình (gọi tắt là Ban Điều hành CTGT), thành phần gồm có: Hiệu trưởng/Phó Hiệu trưởng phụ trách đào tạo làm Trưởng ban, Trưởng/Phó phòng đào tạo làm ủy viên thường trực kiêm thư ký, cán bộ – viên chức khác làm ủy viên. 2.2. Trưởng Ban Điều hành CTGT chịu trách nhiệm trước Hiệu trưởng về tổ chức hoạt động của mảng công tác giáo trình và trước Chủ nhiệm CTGT ĐHQG về chuyên môn. 2.3. Chức năng của Ban Điều hành CTGT cụ thể như sau: • Tổ chức xây dựng kế hoạch biên soạn giáo trình căn cứ theo chương trình giáo dục, kế hoạch giảng dạy và học tập đối với các ngành đào tạo đã được ĐHQG cho phép đào tạo. • Lập kế hoạch xuất bản giáo trình hàng năm trình ĐHQG đề nghị hỗ trợ kinh phí giáo trình. • Chỉ đạo các Khoa đăng ký, tham gia biên soạn giáo trình. • Tổ chức các hội đồng thẩm địn…
```

**Rank 4 | `chunk_0214` | score `0.450000` | document `virhe4qa_9f79972f4ed1ac75695d`**

```text
Điều 5. Trách nhiệm của Ban Điều hành cấp Trường Đề xuất phương hướng và xét duyệt kế hoạch phát triển CTTN của Trường để trình Ban Giám hiệu trường và BĐH của ĐHQG HCM. Chuẩn bị các điều kiện cơ sở vật chất; tài chính; chương trình đào tạo; tổ chức xây dựng qui chế quy định liên quan tới việc tuyển chọn và chế độ chính sách phục vụ nhằm đảm bảo cho chương trình hoạt động có hiệu quả. Tổ chức xét tuyển và triển khai hoạt động của chương trình theo quy định. Chỉ đạo và theo dõi việc thực hiện chương trình tại các đơn vị. Định kỳ báo cáo Ban Giám hiệu về các hoạt động của chương trình.
```

**Rank 5 | `chunk_0084` | score `0.351852` | document `virhe4qa_c8b08b6a6529cb3ff6b0`**

```text
Điều 14. Trách nhiệm của đơn vị phụ trách quản lý hạ tầng công nghệ thông tin - truyền thông 1. Quản lý, vận hành và đảm bảo an ninh, an toàn: hệ thống máy chủ, cổng thông tin và hạ tầng kết nối mạng phục vụ DHTT, DHKH. 2. Cấp phát tài khoản, tạo lớp học phần, phân quyền cho người dùng trên các hệ thống; hỗ trợ kỹ thuật cho giảng viên và sinh viên trong quá trình giảng dạy và học tập; hỗ trợ bộ phận chức năng thực hiện nhiệm vụ quản lý, thanh tra, kiểm tra. 3. Tham gia giám sát quá trình DHTT, DHKH; kịp thời phát hiện, xử lý và báo cáo lãnh đạo đơn vị các hiện tượng bất thường trong quá trình DHTT, DHKH; lập các báo cáo liên quan khi được yêu cầu. 4. Tạm ngưng hoặc vô hiệu hóa các khóa học, các nội dung trên khóa học và tài khoản người dùng vi phạm các quy định của pháp luật hiện hành và các điều khoản trong quy định này.
```


---

## 27. `query_020`

**Question:** Cập nhật về học phí có được thông tin đến cho sinh viên hệ ĐTTX không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `1` |
| Sparse first gold rank | `5` |
| Gold chunk | `chunk_0082` |
| Gold document | `virhe4qa_136f96987b6b28250e9a` |
| Gold source index | `3002` |
| Hybrid top 1 | `chunk_0007` (score `0.666667`) |

### Gold context

```text
Điều  14. Thông báo kế hoạch đào tạo của Trường
1.  Đầu khoá học, Trạm ĐTTX chính có trách nhiệm thông báo cho sinh viên về:
-	Chương trình đào tạo toàn khóa cho từng ngành học.
-	Quy chế đào tạo và các quy định của Trường.
-	Quyền lợi và nghĩa vụ của sinh viên.
2.  Đầu mỗi học kỳ, Trạm ĐTTX có trách nhiệm thông báo cho sinh viên về:
-	Thông tin cập nhật chương trình đào tạo, học phí (nếu có).
-	Kế hoạch học tập, thời khóa biểu của học kỳ.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0007` | score `0.666667` | document `virhe4qa_cd985b886f0dad0b5712`**

```text
Thông báo Thời điểm và mức thu học phí gia hạn đối với sinh viên hệ đại học chính quy Căn cứ quyết định số 546/QĐ-ĐHCNTT, ngày 30/08/2019 của Hiệu trưởng Trường Đại học Công nghệ Thông tin (ĐHCNTT) về việc ban hành quy chế đào taoụ theo học chế tín chỉ cho hệ đại học chính quy; Căn cứ thông báo số 02/TB-ĐTĐH, ngày 9/6/2020 của Trưởng phòng Đào tạo Đại học – Trường ĐHCNTT về việc thu học phí đối với sinh viên (SV) hệ đại học chính quy từ học kỳ 1 năm học 2020 – 2021; Phòng Kế hoạch Tài chính thông báo về việc áp dụng mức thu học phí gia hạn (HPGH) theo Điều 4, Quyết định số 546/QĐ-ĐHCNTT như sau: 1. Đối tượng áp dụng: SV đã quá thời gian học theo thiết kế chương trình đào tạo (CTĐT). 2. Mức thu HPGH = t * học phí học kỳ của học kỳ cuối cùng theo thiết kế CTĐT, hệ số t: được xác định theo bảng sau đây: - Học kỳ thứ 1 + học kỳ thứ 2. Hệ số t = 10%. - Học kỳ thứ 3 + học kỳ thứ 4. Hệ số t = …
```

**Rank 2 | `chunk_0082` | score `0.666667` | document `virhe4qa_136f96987b6b28250e9a`**

```text
Điều 14. Thông báo kế hoạch đào tạo của Trường 1. Đầu khoá học, Trạm ĐTTX chính có trách nhiệm thông báo cho sinh viên về: - Chương trình đào tạo toàn khóa cho từng ngành học. - Quy chế đào tạo và các quy định của Trường. - Quyền lợi và nghĩa vụ của sinh viên. 2. Đầu mỗi học kỳ, Trạm ĐTTX có trách nhiệm thông báo cho sinh viên về: - Thông tin cập nhật chương trình đào tạo, học phí (nếu có). - Kế hoạch học tập, thời khóa biểu của học kỳ.
```

**Rank 3 | `chunk_0144` | score `0.642857` | document `virhe4qa_0d970ef217e73b381ec2`**

```text
Điều 22. Quyền và trách nhiệm của người học 1. Được cung cấp đầy đủ thông tin về tuyển sinh, thời hạn đăng ký nộp hồ sơ, chương trình ĐTTX, điều kiện công nhận giá trị chuyển đổi kết quả học tập, kế hoạch đào tạo, quy định về ĐTTX, yêu cầu về bằng cấp và các chính sách ĐTTX của Trường. 2. Được quyền tham gia học tập các tín chỉ cùng với hệ đào tạo chính quy, hệ vừa làm vừa học theo quy định của Trường. 3. Được cung cấp đầy đủ các thông tin về đánh giá công nhận chuyển đổi kết quả học tập và có thể đề nghị xem xét lại việc đánh giá công nhận kết quả học tập. 4. Nộp hồ sơ đầy đủ và đúng thời gian đã được Trường công bố; nộp lệ phí và học phí theo quy định của Trường. 5. Lập kế hoạch học tập cụ thể theo các yêu cầu về bằng cấp của Trường về chương trình ĐTTX đã được công bố để có thể được cấp bằng tốt nghiệp. 6. Chấp hành Quy chế này và quy định liên quan về ĐTTX của Trường. 7. Chủ động li…
```

**Rank 4 | `chunk_0110` | score `0.291667` | document `virhe4qa_92640ad22e84af2da079`**

```text
Điều 18. Chuyển ngành, chuyển hệ đào tạo, chuyển trường, chuyển trạm ĐTTX 1. Chuyển ngành Sinh viên hệ ĐTTX được xin chuyển sang ngành đào tạo từ xa khác của Trường nếu đủ điều kiện trúng tuyển ngành đào tạo của khóa tuyển tương ứng. Sinh viên nộp đơn xin chuyển ngành cho P.ĐTĐH. Hiệu trưởng ra quyết định chuyển ngành trên cơ sở đề nghị của P.ĐTĐH. 2. Chuyển hệ đào tạo Sinh viên học hệ vừa học vừa làm, hệ đại học chính quy của Trường được chuyển sang học hệ ĐTTX. Sinh viên nộp đơn xin chuyển hệ đào tạo cho P.ĐTĐH. Hiệu trưởng ra quyết định chuyển hệ đào tạo trên cơ sở đề nghị của P.ĐTĐH. 3. Chuyển trạm ĐTTX Sinh viên hệ ĐTTX được xin chuyển từ trạm ĐTTX này sang trạm ĐTTX khác. Sinh viên nộp đơn xin chuyển trạm ĐTTX cho P.ĐTĐH. Hiệu trưởng ra quyết định chuyển trạm ĐTTX trên cơ sở đề nghị của P.ĐTĐH. 4. Chuyển trường Sinh viên được chuyển trường nếu có đủ các điều kiện sau: - Trong thời…
```

**Rank 5 | `chunk_0151` | score `0.288462` | document `virhe4qa_778ffa1ff440004c5fa7`**

```text
Điều 24. Chế độ báo cáo 1. Từ ngày 01 tháng 12 đến trước ngày 15 tháng 12 hàng năm, các Trạm ĐTTX gửi báo cáo cho Hiệu trưởng thông qua P.ĐTĐH bao gồm: Tuyển sinh; quy mô đào tạo; tổ chức đào tạo; cấp bằng tốt nghiệp trong năm; và dự kiến kế hoạch tuyển sinh năm sau. Nội dung báo cáo phải có đánh giá các hoạt động ĐTTX của Trạm ĐTTX và đề xuất giải pháp để củng cố, phát triển ĐTTX.
```


---

## 28. `query_024`

**Question:** Hiệu trưởng có thể cấp văn bằng tốt nghiệp bậc tiến sĩ được không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `1` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0057` |
| Gold document | `virhe4qa_8364fb9d71ddb34ed3f9` |
| Gold source index | `731` |
| Hybrid top 1 | `chunk_0083` (score `0.833333`) |

### Gold context

```text
Điều  12. Thẩm quyền cấp văn bằng, chứng chỉ
1. Thẩm quyền cấp văn bằng: Bằng tốt nghiệp đại học, bằng thạc sĩ, bằng tiến sĩ do Hiệu trưởng Trường cấp.
2. Thẩm quyền cấp chứng chỉ: Hiệu trưởng Trường cấp hoặc ủy quyền cho thủ trưởng đơn vị trực thuộc cấp theo quy định.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0083` | score `0.833333` | document `virhe4qa_024864f27ed0da9e11a9`**

```text
Điều 14. Thời hạn cấp văn bằng, chứng chỉ 1. Hiệu trưởng Trường ĐHCNTT có trách nhiệm cấp văn bằng cho người học trong thời hạn: a) 30 ngày kể từ ngày có quyết định công nhận tốt nghiệp đại học. b) 30 ngày kể từ ngày có quyết định công nhận tốt nghiệp và cấp bằng thạc sĩ. c) 30 ngày kể từ ngày có quyết định công nhận học vị tiến sĩ và cấp bằng tiến sĩ. 2. Hiệu trưởng hoặc thủ trưởng đơn vị trực thuộc được ủy quyền có trách nhiệm cấp chứng chỉ cho người học chậm nhất là 30 ngày kể từ ngày kết thúc khóa đào tạo, bồi dưỡng nâng cao trình độ học vấn, nghề nghiệp. 3. Trong thời gian chờ cấp văn bằng, người học đã tốt nghiệp được Hiệu trưởng Trường ĐHCNTT cấp giấy chứng nhận tốt nghiệp tạm thời (theo mẫu Phụ lục 7, 8 kèm theo Quy chế này).
```

**Rank 2 | `chunk_0057` | score `0.833333` | document `virhe4qa_8364fb9d71ddb34ed3f9`**

```text
Điều 12. Thẩm quyền cấp văn bằng, chứng chỉ 1. Thẩm quyền cấp văn bằng: Bằng tốt nghiệp đại học, bằng thạc sĩ, bằng tiến sĩ do Hiệu trưởng Trường cấp. 2. Thẩm quyền cấp chứng chỉ: Hiệu trưởng Trường cấp hoặc ủy quyền cho thủ trưởng đơn vị trực thuộc cấp theo quy định.
```

**Rank 3 | `chunk_0194` | score `0.400000` | document `virhe4qa_dc17d6c33c4c33682ef6`**

```text
Điều 33. Điều kiện xét tốt nghiệp và công nhận tốt nghiệp 1. Mỗi năm Trường có 4 đợt xét tốt nghiệp và cấp bằng tốt nghiệp đại học, lịch xét tốt nghiệp được ghi trong kế hoạch năm học. Để được Trường xét cấp bằng tốt nghiệp, sinh viên nộp hồ sơ đề nghị xét tốt nghiệp khi đã đáp ứng đủ các điều kiện sau đây: - Cho đến thời điểm xét tốt nghiệp, sinh viên không đang trong thời gian bị truy cứu trách nhiệm hình sự hoặc bị kỷ luật từ mức đình chỉ học tập trở lên. - Đã hoàn thành nghĩa vụ học phí. - Đã hoàn thành các môn học, tích lũy đủ số tín chỉ theo đúng chương trình đào tạo. - Đã hoàn thành các môn học Giáo dục thể chất. - Có chứng chỉ Giáo dục quốc phòng-An ninh. - Đạt chuẩn ngoại ngữ xét tốt nghiệP. - Đạt điểm rèn luyện tích lũy tối thiểu là 50 điểm. - Đã hoàn trả sách mượn cho Thư viện. 2. Căn cứ biên bản và đề nghị của Hội đồng xét tốt nghiệp, Hiệu trưởng ký quyết định công nhận tốt …
```

**Rank 4 | `chunk_0187` | score `0.340909` | document `virhe4qa_52f85800d1441c973d06`**

```text
Điều 3. Trách nhiệm của các đơn vị, cá nhân trong việc quản lý văn bằng, chứng chỉ 1. Hiệu trưởng chịu trách nhiệm chung trong việc quản lý, cấp phát văn bằng, chứng chỉ. 2. Phòng Đào tạo Đại học (PĐTĐH) có trách nhiệm quản lý việc cấp văn bằng đại học, chứng chỉ; thực hiện các thủ tục đề nghị cấp phôi bằng đại học, chứng chỉ từ ĐHQG-HCM, quản lý phôi, thông tin in lên phôi và tổ chức thực hiện công tác lưu trữ, cấp phát, thu hồi, hủy bỏ bằng đại học, chứng chỉ; bản sao bằng tốt nghiệp đại học, chứng chỉ của Trường ĐHCNTT. 3. Phòng Đào tạo Sau đại học & Khoa học Công nghệ (PĐTSĐH-KHCN) có trách nhiệm quản lý việc cấp văn bằng thạc sĩ, tiến sĩ; thực hiện các thủ tục đề nghị cấp phôi bằng từ ĐHQG-HCM, quản lý phôi, thông tin in lên phôi và tổ chức thực hiện công tác lưu trữ, cấp phát, thu hồi, hủy bỏ bằng thạc sĩ, tiến sĩ; bản sao bằng thạc sĩ, tiến sĩ của Trường ĐHCNTT. 4. Phòng Tổ chức …
```

**Rank 5 | `chunk_0287` | score `0.326923` | document `virhe4qa_772f8cc6d22836eae64f`**

```text
Điều 9: Xét tốt nghiệp và cấp bằng 1. Người học sau khi hoàn thành chương trình đào tạo phần trình độ đại học theo Điều 5 và thỏa điều kiện cấp bằng theo quy chế đào tạo trình độ đại học hiện hành của Trường thì được cấp bằng tốt nghiệp đại học theo ngành ĐH-ThS. 2. Người học sau khi hoàn thành phần trình độ thạc sĩ theo Điều 5 và thỏa điều kiện cấp bằng theo quy chế đào tạo trình độ thạc sĩ hiện hành của Trường thì được cấp bằng tốt nghiệp thạc sĩ theo ngành ĐH-ThS.
```


---

## 29. `query_025`

**Question:** Hằng năm phương thức tuyển sinh được công bố ở đâu?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `5` |
| Sparse first gold rank | `1` |
| Gold chunk | `chunk_0272` |
| Gold document | `virhe4qa_d94c3d6cc1e929dc426b` |
| Gold source index | `7803` |
| Hybrid top 1 | `chunk_0254` (score `0.700000`) |

### Gold context

```text
Điều  8. Điều kiện và phương thức tuyển sinh
8.1 Điều kiện xét tuyển
Sinh viên trúng tuyển CTTT phải đạt các yêu cầu:
Đảm bảo điều kiện đầu vào đối với hệ đại học chính quy theo quy định của Bộ GD&ĐT và Trường ĐHCNTT.
Hoặc có chứng chỉ quốc tế uy tín thỏa điều kiện được xác định trong đề án tuyển sinh hàng năm của Trường.
Trong đó, trường hợp thí sinh là người nước ngoài phải có văn bằng tốt nghiệp tối thiểu tương đương bằng tốt nghiệp trung học phổ thông của Việt Nam, văn bằng phải được công nhận theo quy định của Bộ Giáo dục và Đào tạo.
8.2 Phương thức tuyển sinh
Chỉ tiêu của CTTT nằm trong tổng chỉ tiêu tuyển sinh đại học chính quy của toàn trường.
Phương thức tuyển sinh được công bố trong đề án tuyển sinh hàng năm của Trường.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0254` | score `0.700000` | document `virhe4qa_e2646234bffb213cab1f`**

```text
Điều 7. Tuyển sinh 1. Hàng năm, Trường có văn bản giao chỉ tiêu tuyển sinh cho từng Trạm ĐTTX. 2. Công tác tuyển sinh hệ ĐTTX thực hiện theo quy định hiện hành về tuyển sinh hệ ĐTTX của ĐHQG-HCM và Bộ Giáo dục và Đào tạo.
```

**Rank 2 | `chunk_0272` | score `0.666667` | document `virhe4qa_d94c3d6cc1e929dc426b`**

```text
Điều 8. Điều kiện và phương thức tuyển sinh 8.1 Điều kiện xét tuyển Sinh viên trúng tuyển CTTT phải đạt các yêu cầu: Đảm bảo điều kiện đầu vào đối với hệ đại học chính quy theo quy định của Bộ GD&ĐT và Trường ĐHCNTT. Hoặc có chứng chỉ quốc tế uy tín thỏa điều kiện được xác định trong đề án tuyển sinh hàng năm của Trường. Trong đó, trường hợp thí sinh là người nước ngoài phải có văn bằng tốt nghiệp tối thiểu tương đương bằng tốt nghiệp trung học phổ thông của Việt Nam, văn bằng phải được công nhận theo quy định của Bộ Giáo dục và Đào tạo. 8.2 Phương thức tuyển sinh Chỉ tiêu của CTTT nằm trong tổng chỉ tiêu tuyển sinh đại học chính quy của toàn trường. Phương thức tuyển sinh được công bố trong đề án tuyển sinh hàng năm của Trường.
```

**Rank 3 | `chunk_0258` | score `0.583333` | document `virhe4qa_4f32cfc12430da63f772`**

```text
Điều 8. Phương thức xét tuyển đầu vào Căn cứ vào số lượng đăng ký xét tuyển hàng năm, BĐH quyết định chỉ tiêu tuyển vào lớp tài năng và trình BGH phê duyệt. Việc xét tuyển đầu vào được áp dụng 1 trong 2 phương án sau: 1. Tuyển từ năm 1 – theo kết quả đầu vào tuyển sinh Chỉ tiêu tuyển sinh tối đa là 30 sinh viên/chương trình, nằm trong tổng chỉ tiêu toàn trường và đảm bảo điều kiện không quá 20% chỉ tiêu của ngành tương ứng và không quá 10% tổng chỉ tiêu của trường. Sinh viên sau khi làm thủ tục nhập học sẽ nộp đơn xin xét tuyển vào CTTN. Đối tượng tuyển sinh là các sinh viên: - Tự nguyện tham gia vào CTTN. - Đã trúng tuyển vào hệ chính quy của Trường Đại học Công nghệ Thông tin, dựa trên các phương thức trúng tuyển theo thứ tự ưu tiên sau đây: +Diện tuyển thẳng. +Diện ưu tiên xét tuyển thẳng. +Diện ưu tiên xét tuyển theo tiêu chuẩn của Bộ GD&ĐT. +Diện ưu tiên xét tuyển theo tiêu chuẩn c…
```

**Rank 4 | `chunk_0278` | score `0.583333` | document `virhe4qa_de39a3d41112cdd76fef`**

```text
Điều 9. Phương thức xét tuyển Việc xét tuyển vào CT CLC thực hiện theo một trong hai phương thức sau đây: 9.1. Tuyển sinh viên năm nhất Thực hiện theo đề án tuyển sinh hàng năm của hệ đại học chính quy. Chỉ tiêu tuyển vào CT CLC nằm trong tổng chỉ tiêu tuyển sinh hàng năm của Trường 9.2. Tuyển sinh viên năm trên Tuyển bổ sung vào CT CLC vào đầu mỗi học kỳ nhưng không muộn hơn cuối năm thứ hai. Nếu ngành đào tạo CT CLC có tiến hành phân ngành/chuyên ngành vào giữa khóa học thì bắt buộc phải tổ chức tuyển bổ sung vào CT CLC không muộn hơn thời điểm phân ngành/chuyên ngành này. Việc xét tuyển thực hiện theo các tiêu chí sau: - Sinh viên tự nguyện tham gia vào CT CLC. - Sinh viên đang theo học cùng khóa, cùng ngành với lớp CT CLC tương ứng. Trường hợp cần thiết Khoa có thể thông báo tuyển từ sinh viên một số ngành/chuyên ngành khác cùng khóa nếu ngành đó chưa có sự khác biệt đáng kể về chươ…
```

**Rank 5 | `chunk_0255` | score `0.291667` | document `virhe4qa_74c9de793531f062878f`**

```text
Điều 7. Tuyển sinh 1. Chỉ tiêu tuyển sinh: Chỉ tiêu tuyển sinh chương trình ĐH-ThS do Hiệu trưởng quyết định, không vượt quá 50% tổng chỉ tiêu đào tạo trình độ thạc sĩ của ngành tương ứng. 2. Thông báo tuyển sinh: Phòng ĐTSĐH thông báo thông tin về tuyển sinh chương trình ĐH-ThS, trong đó nêu rõ những thông tin sau đây: a. Tên chương trình, tên ngành đào tạo, mã ngành đào tạo; b. Thời gian đào tạo; c. Phương thức tuyển sinh; d. Đối tượng và điều kiện tuyển sinh; e. Số lần tuyển sinh trong năm; f. Chỉ tiêu tuyển sinh; g. Hình thức và thời gian đào tạo; h. Địa điểm đào tạo; i. Mức học phí. 3. Hội đồng tuyển sinh: Hội đồng tuyển sinh chương trình ĐH-ThS do Hiệu trưởng ra quyết định thành lập (gồm đại diện lãnh đạo Phòng ĐTĐH, lãnh đạo Phòng ĐTSĐH, một số lãnh đạo khoa, phòng liên quan) có trách nhiệm thực hiện xét tuyển để xác định người học trúng tuyển vào chương trình ĐH-ThS. Sau khi tốt…
```


---

## 30. `query_038`

**Question:** Nghĩa vụ của Phòng Thanh tra Pháp chế và Đảm bảo Chất lượng trong quy trình tổ chức thi là gì?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `1` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0166` |
| Gold document | `virhe4qa_92b0be9687b651b0654b` |
| Gold source index | `5642` |
| Hybrid top 1 | `chunk_0180` (score `0.833333`) |

### Gold context

```text
Điều  27. Trách nhiệm của Phòng Thanh tra Pháp chế và Đảm bảo Chất lượng
Tổ chức thanh tra, kiểm tra và giám sát công tác tổ chức thi.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0180` | score `0.833333` | document `virhe4qa_a15a72b59e2547ea5282`**

```text
Điều 3. Hoạt động thanh tra, kiểm tra, giám sát công tác thi Phòng Thanh tra Pháp chế và Đảm bảo Chất lượng có trách nhiệm tổ chức thanh tra, kiểm tra và giám sát công tác tổ chức thi.
```

**Rank 2 | `chunk_0166` | score `0.833333` | document `virhe4qa_92b0be9687b651b0654b`**

```text
Điều 27. Trách nhiệm của Phòng Thanh tra Pháp chế và Đảm bảo Chất lượng Tổ chức thanh tra, kiểm tra và giám sát công tác tổ chức thi.
```

**Rank 3 | `chunk_0026` | score `0.450000` | document `virhe4qa_7f37ffd42956999da52e`**

```text
Điều 10. Kiểm tra, thanh tra Phòng Thanh tra pháp chế - Đảm bảo chất lượng có trách nhiệm tổ chức kiểm tra, thanh tra nội bộ việc tổ chức thực hiện các quy định về đánh giá, cập nhật CTĐT của Trường theo quy định này.
```

**Rank 4 | `chunk_0225` | score `0.416667` | document `virhe4qa_a4f98999335b259b255a`**

```text
Điều 5. Tổ chức thực hiện - Phòng Đào tạo Đại học có trách nhiệm quản lý toàn bộ quá trình giảng dạy - học tập. - Phòng Thanh tra Pháp chế và Đảm bảo Chất lượng có nhiệm vụ thanh tra, giám sát, đảm bảo quá trình giảng dạy - học tập tuân thủ các quy định của Trường. - Các Khoa, Bộ môn, Trung tâm Ngoại ngữ, Văn phòng các chương trình đặc biệt và các đơn vị phụ trách chuyên môn cho môn học có trách nhiệm phối hợp mở lớp, phân công cán bộ giảng dạy và quản lý chất lượng giảng dạy. - Các cán bộ giảng dạy có trách nhiệm thực hiện nhiệm vụ được phân công và đảm bảo chất lượng giảng dạy theo các quy định của Trường.
```

**Rank 5 | `chunk_0154` | score `0.233766` | document `virhe4qa_84d877effaeafcfd7e93`**

```text
Điều 24. Trách nhiệm của P.ĐTĐH, VPĐB 1. Lập kế hoạch và điều hành công tác tổ chức thi. 2. Xếp lịch thi; lập các danh sách SV dự thi; 3. Chuẩn bị thi, tổ chức thi, tổ chức chấm thi và chấm phúc khảo cho những môn học do P.ĐTĐH quản lý; 4. Lập danh sách miễn giảm coi thi và gửi danh sách miễn giảm coi thi cho Phòng DL&CNTT hỗ trợ phân công cán bộ coi thi; 5. Kiểm tra điểm sau khi được nhập vào Hệ thống quản lý điểm; 6. Lưu trữ bài thi và hồ sơ thi.
```


---

## 31. `query_056`

**Question:** Quy định về học phí về đào tạo liên thông từ trình độ đại học lên trình độ thạc sĩ hệ chính quy như thế nào?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `1` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0042` |
| Gold document | `virhe4qa_38c7280793ba4270bde0` |
| Gold source index | `4266` |
| Hybrid top 1 | `chunk_0297` (score `0.833333`) |

### Gold context

```text
Điều  11. Quy định về học phí     
1. Các học phần trong chương trình đào tạo trình độ thạc sĩ tổ chức giảng dạy trong chương trình đào tạo trình độ đại học thì học phí được xác định theo quy định đối với chương trình đại học chuẩn cùng ngành ĐH-ThS. 
2. Các học phần học còn lại trong chương trình đào tạo trình độ thạc sĩ sau khi người học tốt nghiệp đại học thì học phí được tính theo quy định đối với chương trình đào tạo trình độ thạc sĩ hiện hành của Trường.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0297` | score `0.833333` | document `virhe4qa_31d7f0e5afe10c15cf33`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Văn bản này quy định về tuyển sinh, tổ chức và quản lý đào tạo đối với chương trình đào tạo liên thông từ trình độ đại học lên trình đô thạc sĩ hệ chính quy của Trường Đại học Công nghệ Thông tin – ĐHQG-HCM (sau đây gọi tắt là chương trình ĐH-ThS). 2. Quy định này áp dụng đối với tổ chức và cá nhân có liên quan đến chương trình ĐH-ThS.
```

**Rank 2 | `chunk_0042` | score `0.833333` | document `virhe4qa_38c7280793ba4270bde0`**

```text
Điều 11. Quy định về học phí 1. Các học phần trong chương trình đào tạo trình độ thạc sĩ tổ chức giảng dạy trong chương trình đào tạo trình độ đại học thì học phí được xác định theo quy định đối với chương trình đại học chuẩn cùng ngành ĐH-ThS. 2. Các học phần học còn lại trong chương trình đào tạo trình độ thạc sĩ sau khi người học tốt nghiệp đại học thì học phí được tính theo quy định đối với chương trình đào tạo trình độ thạc sĩ hiện hành của Trường.
```

**Rank 3 | `chunk_0293` | score `0.450000` | document `virhe4qa_d447188b9c7756a04e95`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Quy chế này quy định những điều chung nhất về đào tạo đại học theo hình thức chính quy (gọi tắt là hệ đại học chính quy) của Trường Đại học Công nghệ Thông tin thuộc ĐHQG-HCM (gọi tắt là Trường). 2. Quy chế này áp dụng đối với các đơn vị, cá nhân liên quan trong đào tạo hệ đại học chính quy. 3. Quy định đào tạo đại học theo hình thức đào tạo từ xa (gọi tắt là hệ đại học từ xa) và đào tạo các chương trình đặc biệt của Trường được xây dựng, điều chỉnh phù hợp với đặc thù hệ đào tạo/chương trình dựa trên cơ sở quy chế này.
```

**Rank 4 | `chunk_0007` | score `0.375000` | document `virhe4qa_cd985b886f0dad0b5712`**

```text
Thông báo Thời điểm và mức thu học phí gia hạn đối với sinh viên hệ đại học chính quy Căn cứ quyết định số 546/QĐ-ĐHCNTT, ngày 30/08/2019 của Hiệu trưởng Trường Đại học Công nghệ Thông tin (ĐHCNTT) về việc ban hành quy chế đào taoụ theo học chế tín chỉ cho hệ đại học chính quy; Căn cứ thông báo số 02/TB-ĐTĐH, ngày 9/6/2020 của Trưởng phòng Đào tạo Đại học – Trường ĐHCNTT về việc thu học phí đối với sinh viên (SV) hệ đại học chính quy từ học kỳ 1 năm học 2020 – 2021; Phòng Kế hoạch Tài chính thông báo về việc áp dụng mức thu học phí gia hạn (HPGH) theo Điều 4, Quyết định số 546/QĐ-ĐHCNTT như sau: 1. Đối tượng áp dụng: SV đã quá thời gian học theo thiết kế chương trình đào tạo (CTĐT). 2. Mức thu HPGH = t * học phí học kỳ của học kỳ cuối cùng theo thiết kế CTĐT, hệ số t: được xác định theo bảng sau đây: - Học kỳ thứ 1 + học kỳ thứ 2. Hệ số t = 10%. - Học kỳ thứ 3 + học kỳ thứ 4. Hệ số t = …
```

**Rank 5 | `chunk_0211` | score `0.309524` | document `virhe4qa_7db163f3d846cdf43465`**

```text
Điều 4. Điều kiện mở chương trình đào tạo liên thông 1. Khoa được đăng ký mở chương trình ĐH-ThS đối với các ngành đã đạt chứng nhận kiểm định quốc tế cấp chương trình đào tạo trình độ đại học hoặc thạc sĩ được Bộ Giáo dục và Đào tạo công nhận và còn trong thời hạn; hoặc các ngành có chương trình tài năng trình độ đại học. 2. Các trường hợp khác do Hiệu trưởng quyết định, trình Giám đốc ĐHQG-HCM phê duyệt.
```


---

## 32. `query_059`

**Question:** SHD là viết tắt của gì?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `3` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0173` |
| Gold document | `virhe4qa_b79a8dee715051148c9c` |
| Gold source index | `382` |
| Hybrid top 1 | `chunk_0122` (score `1.000000`) |

### Gold context

```text
Điều  3.	Phân loại giáo trình
3.1.	Sách chuyên khảo: là tài liệu có nội dung chủ yếu từ kết quả nghiên cứu sâu và tương đối toàn diện về một vấn đề của chuyên gia trình độ cao, được sử dụng để giảng dạy trong cơ sở giáo dục. 
3.2.	Sách giáo trình (GT): là tài liệu chính đã được cơ sở giáo dục phê duyệt, dùng trong giảng dạy và học tập cho giảng viên, sinh viên. Sách giáo trình cụ thể hóa các yêu cầu về nội dung kiến thức, kỹ năng cơ bản, chuẩn đầu ra đã ban hành đối với mỗi môn học, ngành đào tạo, trình độ đào tạo, đáp ứng yêu cầu về phương pháp giáo dục, kiểm tra và đánh giá chất lượng đào tạo, có nội dung phù hợp với nội dung của chương trình giáo dục đã được phê duyệt theo quy định của ĐHQG.
3.3.	Tài liệu tham khảo (TLTK): là tài liệu được biên soạn dưới dạng bài giảng, tài liệu biên dịch, tài liệu dịch và tài liệu có nội dung phù hợp với một phần nội dung chương trình giáo dục hiện hành.
3.4.	Sách hướng dẫn (SHD): là tài liệu được biên soạn sử dụng trong việc hướng dẫn thí nghiệm, hướng dẫn thực hành, hướng dẫn đồ án môn học, hướng dẫn giải bài tập mẫu, từ điển chuyên ngành… và tài liệu sử dụng trong công tác quản lý giáo dục.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0122` | score `1.000000` | document `virhe4qa_57a571d0ef2c0aafec02`**

```text
Điều 2. Một số thuật ngữ, chữ viết tắt sử dụng trong quy định này KLTN: Khóa luận tốt nghiệp ĐHCNTT: Đại học Công nghệ Thông tin – ĐHQG-HCM Trường: Trường ĐHCNTT P.ĐTĐH: Phòng Đào tạo Đại học Khoa: gọi chung cho Khoa, Bộ môn quản lý sinh viên Hội đồng: Hội đồng bảo vệ KLTN CBHD: Cán bộ hướng dẫn CBPB: Cán bộ phản biện TV: Thành viên Hội đồng SV: Sinh viên
```

**Rank 2 | `chunk_0173` | score `0.583333` | document `virhe4qa_b79a8dee715051148c9c`**

```text
Điều 3. Phân loại giáo trình 3.1. Sách chuyên khảo: là tài liệu có nội dung chủ yếu từ kết quả nghiên cứu sâu và tương đối toàn diện về một vấn đề của chuyên gia trình độ cao, được sử dụng để giảng dạy trong cơ sở giáo dục. 3.2. Sách giáo trình (GT): là tài liệu chính đã được cơ sở giáo dục phê duyệt, dùng trong giảng dạy và học tập cho giảng viên, sinh viên. Sách giáo trình cụ thể hóa các yêu cầu về nội dung kiến thức, kỹ năng cơ bản, chuẩn đầu ra đã ban hành đối với mỗi môn học, ngành đào tạo, trình độ đào tạo, đáp ứng yêu cầu về phương pháp giáo dục, kiểm tra và đánh giá chất lượng đào tạo, có nội dung phù hợp với nội dung của chương trình giáo dục đã được phê duyệt theo quy định của ĐHQG. 3.3. Tài liệu tham khảo (TLTK): là tài liệu được biên soạn dưới dạng bài giảng, tài liệu biên dịch, tài liệu dịch và tài liệu có nội dung phù hợp với một phần nội dung chương trình giáo dục hiện hà…
```

**Rank 3 | `chunk_0179` | score `0.404762` | document `virhe4qa_5ebde2154d8e4e5c2f3a`**

```text
Điều 3. Giải thích từ ngữ và chữ viết tắt Trường: Trường Đại học Công nghệ Thông tin, Đại học Quốc gia Thành phố Hồ Chí Minh. Phòng ĐTĐH: Phòng Đào tạo đại học, Trường Đại học Công nghệ Thông tin. Phòng ĐTSĐH: Phòng Đào tạo Sau đại học và Khoa học Công nghệ, Trường Đại học Công nghệ Thông tin. Phòng DL&CNTT: Phòng Dữ liệu và Công nghệ Thông tin Ngành ĐH-ThS: Ngành của chương trình ĐH-ThS. Chương trình/Ngành ĐH đang học: Chương trình/Ngành học trình độ đại học của sinh viên khi dự tuyển vào chương trình ĐH-ThS. Người học: sinh viên, học viên tham gia chương trình ĐH-ThS.
```

**Rank 4 | `chunk_0232` | score `0.375000` | document `virhe4qa_80f3313df339c1076ef9`**

```text
Điều 6. Báo cáo tiến độ thực hiện KLTN Ngoài việc báo cáo theo định kỳ do CBHD quy định, SV thực hiện KLTN bắt buộc phải báo cáo tiến độ làm việc giữa kỳ theo kế hoạch chung của Trường. Mục đích của việc kiểm tra tiến độ giữa kỳ: – Rà soát lại tiến độ thực hiện. – Phát hiện những trở ngại (nếu có) từ phía CBHD hoặc từ phía SV để có biện pháp xử lý kịp thời. Các biện pháp và hình thức xử lý: – Điều chỉnh tên, khối lượng, nội dung hay phương hướng đề tài – Thay thế hoặc bổ sung CBHD – Đình chỉ việc thực hiện KLTN nếu xét thấy không có khả năng tiếp tục đưa đề tài hoàn tất đúng hạn Các trường hợp SV bị đình chỉ KLTN sẽ được trưởng Khoa xem xét và quyết định. SV bị đình chỉ KLTN sẽ nhận điểm không (0) đối với các tín chỉ tương ứng. Khoa tổng hợp kết quả báo cáo giữa kỳ của các SV, các đề nghị thay đổi và gởi cho P. ĐTĐH.
```

**Rank 5 | `chunk_0245` | score `0.234483` | document `virhe4qa_c13af3503610e4775548`**

```text
Điều 7. Nộp KLTN Khi hết thời gian thực hiện KLTN theo quy định của Trường, SV phải báo cáo việc thực hiện KLTN và kết quả cho CBHD. CBHD cho nhận xét theo mẫu Phiếu nhận xét của Trường. Sau khi có ý kiến đồng ý của CBHD, SV phải hoàn thành và nộp cho Khoa đúng hạn báo cáo KLTN. Yêu cầu đối với báo cáo KLTN: – KLTN phải được thực hiện đúng quy cách theo quy định của trường (Phụ lục 2) – KLTN phải có ý kiến thống nhất về nội dung và sự đồng ý cho phép SV bảo vệ kèm chữ ký của CBHD – Các KLTN phải được nộp 3 bản giống nhau: 1 bản để trình Hội đồng chấm KLTN, 1 bản cho CBHD và 1 bản cho CBPB.
```


---

## 33. `query_063`

**Question:** Sinh viên khi đi thi có cần phải mang theo giấy tờ cá nhân như CCCD, thẻ sinh viên hay không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `2` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0072` |
| Gold document | `virhe4qa_86d02346db46a96d3597` |
| Gold source index | `5004` |
| Hybrid top 1 | `chunk_0210` (score `1.000000`) |

### Gold context

```text
Điều  13. Trách nhiệm của sinh viên dự thi
1. SV phải có mặt tại phòng thi trước 15 phút theo thời gian ghi trong lịch thi do P.ĐTĐH công bố. SV đến chậm quá 15 phút sau khi đã bóc đề thi thì không được dự thi.
2. Khi vào phòng thi, SV phải tuân thủ các quy định sau đây:
a. Xuất trình giấy tờ cá nhân hợp lệ khi CBCT yêu cầu;
b. Không được mang vào khu vực thi và phòng thi vũ khí, chất gây nổ, gây cháy, bia, rượu. Không được hút thuốc trong phòng thi;
c. Trước khi làm bài thi phải ghi đầy đủ họ tên, MSSV vào giấy thi, giấy nháp;
d. Bài làm phải viết rõ ràng, sạch sẽ, không nhàu nát. Nghiêm cấm làm bài bằng hai thứ mực, mực đỏ, bút chì (trừ hình tròn vẽ bằng com-pa được dùng bút chì). Các phần viết hỏng phải dùng thước gạch chéo, không dùng bút xóa;
e. Phải bảo vệ bài làm của mình, không được xem bài của SV khác, không được trao đổi ý kiến, trao đổi tài liệu khi làm bài; Không được sử dụng các vật dụng giúp gian lận trong khi thi như: tài liệu bị cấm sử dụng, phương tiện thông tin liên lạc,…;
f. Nếu cần hỏi CBCT điều gì phải hỏi công khai. Phải giữ gìn trật tự, im lặng trong phòng thi. Trường hợp ốm đau bất thường phải báo cáo để CBCT xử lý;
g. Khi hết giờ thi phải ngừng làm bài và chờ CBCT gọi tên để nộp bài. Không làm được bài, SV cũng phải nộp giấy thi. Khi nộp bài, SV phải tự ghi rõ số tờ giấy thi đã nộp và ký tên xác nhận vào bản danh sách theo dõi SV;
h. SV chỉ được ra khỏi phòng thi sau 2/3 thời gian làm bài và sau khi đã nộp bài làm và đề thi cho CBCT, trừ trường hợp ốm đau cần cấp cứu do CB trực lãnh đạo thi quyết định.
3. Khi dự thi các môn trắc nghiệm:
a. SV phải làm bài thi trên phiếu TLTN được in sẵn; bài làm phải có chữ kí của CBCT. Trên phiếu TLTN chỉ được viết một thứ mực, không phải là mực đỏ. Các ô số báo danh, ô mã đề thi, ô trả lời chỉ được tô bằng bút chì đen. Trong trường hợp tô nhầm hoặc muốn thay đổi câu trả lời, SV phải tẩy sạch chì ở ô cũ, rồi tô kín ô khác mà mình lựa chọn;
b. Điền chính xác và đủ thông tin vào các mục trống ở phía trên phiếu TLTN, điền chính xác mã đề thi vào hai phiếu thu bài thi;
c. Khi nhận đề thi phải để đề thi dưới tờ phiếu TLTN; không được xem đề thi khi CBCT chưa cho phép;
d. Phải kiểm tra đề thi để đảm bảo: đề thi có đủ số lượng câu trắc nghiệm như đã ghi trong đề; nội dung đề được in rõ ràng, không thiếu chữ, mất nét; tất cả các trang của đề thi đều ghi cùng một mã đề thi. Nếu có những chi tiết bất thường trong đề thi, hoặc có 2 đề thi trở lên, SV phải báo ngay cho CBCT để xử lý;
e. Khi hết giờ làm bài thi trắc nghiệm, có lệnh thu bài SV phải ngừng làm bài, đặt phiếu TLTN lên trên đề thi và chờ nộp phiếu TLTN theo hướng dẫn của CBCT. SV không làm được bài vẫn phải nộp phiếu TLTN. Khi nộp phiếu TLTN, SV phải ký tên vào phiếu thu bài thi;
4. Đối với môn thi trên máy tính tại phòng máy:
a. Chỉ được phép truy cập internet hoặc mạng cục bộ theo quy định ghi trên đề thi.
b. Thực hiện nộp bài thi vào thư mục hoặc vị trí được đề thi chỉ định.
c. Nghiêm cấm việc tự ý tạo thư mục chia sẻ khi không có sự cho phép của CBCT.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0210` | score `1.000000` | document `virhe4qa_a10e6d7003e6e9a03db1`**

```text
Điều 4. Điều kiện dự thi Sinh viên (SV) được dự thi nếu đáp ứng các điều kiện sau đây: 1. SV có tên trong danh sách thi hoặc có giấy vào phòng thi được cấp bởi Phòng Đào tạo Đại học (P.ĐTĐH). SV có đăng ký môn học hợp lệ trong học kỳ và đóng học phí đầy đủ trước thời hạn quy định được dự thi. 2. Khi dự thi, SV mang theo một trong những giấy tờ chứng minh cá nhân hợp lệ sau đây: thẻ SV được cấp bởi Trường ĐH CNTT, chứng minh nhân dân, căn cước công dân hoặc bằng lái xe.
```

**Rank 2 | `chunk_0072` | score `0.666667` | document `virhe4qa_86d02346db46a96d3597`**

```text
Điều 13. Trách nhiệm của sinh viên dự thi 1. SV phải có mặt tại phòng thi trước 15 phút theo thời gian ghi trong lịch thi do P.ĐTĐH công bố. SV đến chậm quá 15 phút sau khi đã bóc đề thi thì không được dự thi. 2. Khi vào phòng thi, SV phải tuân thủ các quy định sau đây: a. Xuất trình giấy tờ cá nhân hợp lệ khi CBCT yêu cầu; b. Không được mang vào khu vực thi và phòng thi vũ khí, chất gây nổ, gây cháy, bia, rượu. Không được hút thuốc trong phòng thi; c. Trước khi làm bài thi phải ghi đầy đủ họ tên, MSSV vào giấy thi, giấy nháp; d. Bài làm phải viết rõ ràng, sạch sẽ, không nhàu nát. Nghiêm cấm làm bài bằng hai thứ mực, mực đỏ, bút chì (trừ hình tròn vẽ bằng com-pa được dùng bút chì). Các phần viết hỏng phải dùng thước gạch chéo, không dùng bút xóa; e. Phải bảo vệ bài làm của mình, không được xem bài của SV khác, không được trao đổi ý kiến, trao đổi tài liệu khi làm bài; Không được sử dụng…
```

**Rank 3 | `chunk_0059` | score `0.500000` | document `virhe4qa_b19d42dc855293638921`**

```text
Điều 12. Trách nhiệm của cán bộ coi thi 1. CBCT phải có mặt tại địa điểm tập trung của đơn vị tổ chức thi ít nhất 15 phút trước giờ bắt đầu thi để nhận danh sách thi, giấy thi, giấy nháp, túi đề thi (yêu cầu kiểm tra kỹ niêm phong túi đề) và nghe phổ biến các quy định cần thiết (trong trường hợp cần thiết). 2. Trước giờ thi 10 phút, tại phòng thi, các CBCT phải hoàn tất đánh số chỗ ngồi theo danh sách (dùng số thứ tự SV trong danh sách để đánh số) – tuyệt đối không để SV tự sắp chỗ trong phòng thi. Trong thời gian coi thi, CBCT kiểm tra giấy tờ chứng minh cá nhân hợp lệ, đối chiếu hình, đối chiếu tên với danh sách dự thi. CBCT không được cho vào phòng thi các SV không có tên trong danh sách và cũng không có giấy vào phòng thi được cấp bởi P.ĐTĐH. Nếu SV có khiếu nại, CBCT hướng dẫn SV tới ngay P.ĐTĐH để xác minh giải quyết. CBCT lưu ý thu lại giấy vào phòng thi của SV để bàn giao cùng t…
```

**Rank 4 | `chunk_0085` | score `0.311111` | document `virhe4qa_37318b15d819dcedcaa6`**

```text
Điều 14. Đăng ký học tập Sinh viên được đăng ký học và thi các môn học trong chương trình đào tạo do bất kỳ một CSĐT nào thuộc ĐHQG-HCM hoặc hệ thống các trường thành viên của ASEAN University Network tổ chức giảng dạy. Việc chuyển đổi và công nhận tín chỉ được thực hiện theo quy định tại Điều 27 của Quy chế này. Nếu đăng ký học tại Trường thì đầu mỗi học kỳ, sinh viên phải tìm hiểu, nghiên cứu để nắm được chương trình giáo dục, các học phần được mở trong học kỳ và đăng ký các học phần qua hệ thống đăng ký hoặc bằng phiếu đăng ký theo quy định của Trường. Riêng sinh viên khóa tuyển mới, học kỳ đầu tiên sẽ học theo thời khóa biểu được xếp sẵn dựa trên kế hoạch giảng dạy mẫu theo chương trình đào tạo. 1. Số tín chỉ tối thiểu, tối đa Số tín chỉ tối thiểu, tối đa được tính bao gồm số các tín chỉ đăng ký tại Trường hoặc CSĐT khác. a) Trong học kỳ chính: - Số tín chỉ đăng ký học n trong mỗi h…
```

**Rank 5 | `chunk_0081` | score `0.290909` | document `virhe4qa_f3bdbf76826bb0c1f4f4`**

```text
Điều 14. Quy trình tổ chức thi (đối với hình thức tự luận, trắc nghiệm) 1. Đầu vào, đầu ra, thời gian: Đầu vào: Lịch thi, danh sách CBCT, túi đề thi, sổ theo dõi bàn giao đề thi và bài thi. Đầu ra: Túi bài thi, sổ theo dõi bàn giao đề thi và bài thi có thông tin bàn giao, danh sách CBCT cập nhật (khi có sự thay đổi). Thời gian: Quy trình diễn ra trong ngày thi. 2. Sơ đồ tóm tắt Quy trình tổ chức thi đối với hình thức tự luận, trắc nghiệm được diễn ra theo quá trình sau. Túi đề thi được Khoa/ Phòng Đào tạo Đại học/ Văn phòng Đặc biệt giao cho cán bộ coi thi. Cán bộ coi thi sẽ khi nhận túi đề thi, đánh số chỗ ngồi, đọc tên thí sinh vào phòng thi. Tiếp theo, cán bộ coi thi sẽ kiểm tra giấy tờ tuỳ thân và nhận diện sinh viên dự thi. Sau khi kiếm tra thông tin của sinh viên, bắt đầu phát đề thi, bao quát phòng thi, báo cáo sự cố. Nếu có sự cố xảy ra, báo cáo cho Khoa/ Phòng Đào tạo Đại học/ …
```


---

## 34. `query_065`

**Question:** Sinh viên tài năng có được tham gia xét hưởng học bổng khuyến khích tài năng như sinh viên các chương trình khác không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `2` |
| Sparse first gold rank | `1` |
| Gold chunk | `chunk_0064` |
| Gold document | `virhe4qa_3abd8382b4312b3ad46f` |
| Gold source index | `8040` |
| Hybrid top 1 | `chunk_0120` (score `0.833333`) |

### Gold context

```text
Điều  13.	Quy định về tài chính 
1.	Học bổng sinh viên
Học bổng chương trình: học bổng được cấp cho sinh viên theo từng học kỳ – một học kỳ tính là 5.0 tháng. Mức học bổng hàng năm do Hiệu trưởng quyết định. Tất cả các sinh viên tài năng theo danh sách chính thức từng học kỳ đều được hưởng học bổng này. 
Học bổng khuyến khích học tập: sinh viên tài năng được tham gia xét hưởng học bổng khuyến khích học tập theo quy định của nhà nước tương tự như các sinh viên chương trình khác (xét chung theo khóa, Khoa-Ngành).


2.	Khen thưởng sinh viên
Căn cứ vào tình hình kinh phí và hoạt động của các lớp CTTN, Hiệu trưởng quyết định thêm các hình thức khen thưởng sau:
-	Sinh viên đạt thành tích xuất sắc trong các cuộc thi học thuật.
-	Tuyên dương nỗ lực phấn đấu và tích cực tham gia phong trào, do tập thể lớp bình chọn.
3.	Chi nghiệp vụ chuyên môn đặc biệt khác
Ngoài các khoản chi thường xuyên kể trên, đề án CTTN khuyến khích sinh viên tham gia nghiên cứu khoa học, hỗ trợ việc giao lưu tham quan, trao đổi học tập với cơ sở bên ngoài và tham gia các Hội nghị Hội thảo chuyên môn. Các trường hợp này do Khoa quản lý đề xuất BĐH xem xét và trình BGH phê duyệt.
Chương  1.	ĐIỀU KHOẢN THI HÀNH
Quy định này có hiệu lực thi hành kể từ ngày ký. Các quy định trước đây trái với quy định này không còn hiệu lực. Việc điều chỉnh, bổ sung các điều khoản của quy định do Hiệu trưởng quyết định.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0120` | score `0.833333` | document `virhe4qa_1c466c63cf51a2b45f7a`**

```text
Điều 2. Giải thích từ ngữ Sinh viên thuộc chương trình tài năng có 02 hình thức là chính thức và dự bị, nằm trong tổng chỉ tiêu của chương trình: - Sinh viên chính thức: đảm bảo đáp ứng các tiêu chuẩn theo yêu cầu và được hưởng đầy đủ các quyền lợi của chương trình. - Sinh viên dự bị: cùng điều kiện học tập và học cùng chương trình đào tạo với sinh viên chính thức nhưng không được hưởng chính sách về học bổng tài năng. Sinh viên dự bị bao gồm các sinh viên trong lớp tài năng vi phạm điều kiện đạt sinh viên chính thức nhưng chưa bị loại ra khỏi chương trình trong các đợt xét sau mỗi học kỳ, và sinh viên mới tuyển bổ sung vào chương trình. Môn học cốt lõi: là môn học quan trọng trong CTĐT, là phần kiến thức không thể thiếu trong lĩnh vực chuyên môn liên quan tới ngành đào tạo chương trình tài năng. Danh sách môn học cốt lõi do Khoa đề nghị trong đề án mở chương trình tài năng. Seminar ngo…
```

**Rank 2 | `chunk_0064` | score `0.833333` | document `virhe4qa_3abd8382b4312b3ad46f`**

```text
Điều 13. Quy định về tài chính 1. Học bổng sinh viên Học bổng chương trình: học bổng được cấp cho sinh viên theo từng học kỳ – một học kỳ tính là 5.0 tháng. Mức học bổng hàng năm do Hiệu trưởng quyết định. Tất cả các sinh viên tài năng theo danh sách chính thức từng học kỳ đều được hưởng học bổng này. Học bổng khuyến khích học tập: sinh viên tài năng được tham gia xét hưởng học bổng khuyến khích học tập theo quy định của nhà nước tương tự như các sinh viên chương trình khác (xét chung theo khóa, Khoa-Ngành). 2. Khen thưởng sinh viên Căn cứ vào tình hình kinh phí và hoạt động của các lớp CTTN, Hiệu trưởng quyết định thêm các hình thức khen thưởng sau: - Sinh viên đạt thành tích xuất sắc trong các cuộc thi học thuật. - Tuyên dương nỗ lực phấn đấu và tích cực tham gia phong trào, do tập thể lớp bình chọn. 3. Chi nghiệp vụ chuyên môn đặc biệt khác Ngoài các khoản chi thường xuyên kể trên, đ…
```

**Rank 3 | `chunk_0274` | score `0.500000` | document `virhe4qa_c31538b810cd4921a313`**

```text
Điều 9. Tuyển bổ sung và loại ra khỏi chương trình, xét chính thức và dự bị Đối tượng tham gia CTTN là những sinh viên có năng lực xuất sắc, do đó, sau mỗi học kỳ BĐH quyết định việc loại sinh viên khỏi lớp tài năng, tuyển bổ sung sinh viên từ chương trình chuẩn vào lớp tài năng, xét chuyển đổi sinh viên chính thức và dự bị. Đầu mỗi học kỳ, Khoa xét và đề nghị lên BĐH các danh sách sinh viên tuyển bổ sung, bị loại ra khỏi các lớp CTTN hoặc danh sách sinh viên chính thức và dự bị theo các tiêu chuẩn như sau: 1. Loại khỏi chương trình Tại thời điểm xem xét, sinh viên rơi vào một trong các trường hợp sau: - Chưa tốt nghiệp khi đã quá thời gian thiết kế của khóa học và không có lý do đặc biệt. - Không đăng ký học đầy đủ các môn học CTTN bắt buộc trong học kỳ. - ĐTBTL nhỏ hơn 6,5 – tính tương ứng sau học kỳ 1 và sau học kỳ hè (kết quả học tập của học kỳ hè sẽ được tính chung vào kết quả học …
```

**Rank 4 | `chunk_0091` | score `0.366667` | document `virhe4qa_06af9d2367b44324df31`**

```text
Điều 15. Học bổng Sinh viên CTTT cũng được xét nhận học bổng khuyến khích học tập của Nhà nước theo quy định của Trường như sinh viên chương trình đại trà. Học bổng của CTTT: - Học bổng học tập: căn cứ trên kết quả học tập và rèn luyện mỗi học kỳ của sinh viên, Trường sẽ cấp 03 suất học bổng dành cho 03 sinh viên xuất sắc nhất của mỗi khóa (ĐTBHK >= 8.0, Điểm rèn luyện đạt loại Khá trở lên; trường hợp có nhiều sinh viên cùng ĐTBHK thì xét theo kết quả điểm rèn luyện và ưu tiên sinh viên tham gia đầy đủ các hoạt động do đơn vị quản lý tổ chức). Học bổng bao gồm 01 suất học bổng toàn phần và 02 suất học bổng bán phần tương ứng mức học phí học kỳ áp dụng cho học kỳ tiếp theo mà sinh viên phải đóng. - Học bổng tân sinh viên: căn cứ trên kết quả và phương thức xét tuyển đại học, Trường sẽ cấp 03 suất học bổng dành cho 03 tân sinh viên có kết quả xét tuyển cao nhất, bao gồm 01 suất học bổng t…
```

**Rank 5 | `chunk_0050` | score `0.366667` | document `virhe4qa_8d5eeb2986483f0c0504`**

```text
Điều 12. Tốt nghiệp Chương trình Tài năng Sinh viên sẽ được cấp bằng "Cử nhân/Kỹ sư Tài năng" (Honor Program) của Trường ĐHCNTT – ĐHQG HCM nếu hội đủ các điều kiện sau: - Đang là sinh viên của CTTN. - Hoàn tất chương trình đúng hạn – đủ điều kiện để được cấp bằng theo đúng ngành học của lớp CTTN tương ứng. Nếu sinh viên đã bảo vệ KLTN đúng hạn nhưng chưa đủ điều kiện tốt nghiệp, Khoa có thể xem xét hoàn cảnh cụ thể để đề nghị BĐH và trình BGH phê duyệt cho phép gia hạn tối đa 1 học kỳ để hoàn tất CTĐT và được cấp bằng CTTN. - Có điểm KLTN  7.0, ĐTBTL  7.0 và điểm rèn luyện từ loại Khá trở lên. - Có trình độ Anh văn đạt chuẩn đầu ra của CTTN do Trường quy định. Các sinh viên không đạt một trong các điều kiện nêu trên sẽ nhận bằng tốt nghiệp như sinh viên chương trình chuẩn khi đã đạt đủ các điều kiện được quy định trong quy chế đào tạo theo học chế tín chỉ của Trường; đồng thời sinh vi…
```


---

## 35. `query_067`

**Question:** Số lượng sinh viên tối thiểu của một lớp học cho các môn đại cương là bao nhiêu?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `3` |
| Sparse first gold rank | `1` |
| Gold chunk | `chunk_0060` |
| Gold document | `virhe4qa_867edfa78d8598fcefe0` |
| Gold source index | `1721` |
| Hybrid top 1 | `chunk_0240` (score `0.833333`) |

### Gold context

```text
Điều  12. Tổ chức lớp
1.  Lớp học phần: Những sinh viên theo học cùng một học phần trong cùng một khoảng thời gian và cùng một giảng viên tạo thành một lớp học phần. Mỗi lớp học phần được ký hiệu bằng một mã số riêng do Trường quy định. Lớp học phần sẽ được mở nếu số lượng sinh viên đăng ký:
-	Tối thiểu là 50 sinh viên đối với các môn học đại cương và các môn học cơ sở nhóm ngành.
-	Các môn học chuyên ngành bắt buộc và chuyên đề tốt nghiệp tối thiểu là 20 sinh viên. 
-	Các môn học ngoại ngữ nằm trong chương trình đào tạo cho sinh viên chính quy được mở với số lượng tối thiểu là 20 sinh viên.
-	Các học phần như Thực tập doanh nghiệp, Khóa luận tốt nghiệp, môn học đồ án được mở không hạn chế số lượng.
-	Các môn học còn lại tối thiểu là 30 sinh viên. Trong trường hợp đặc biệt, theo đề nghị của sinh viên, khoa/bộ môn quản lý ngành đào tạo thì P. ĐTĐH có thể mở lớp và thực hiện theo quy định Trường.
2.  Lớp sinh viên: áp dụng theo quy chế Công tác sinh viên của Trường.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0240` | score `0.833333` | document `virhe4qa_79a67d25082fae702d85`**

```text
Điều 6. Tổ chức lớp Lớp học phần: - Quy mô lớp học không quá 50 SV/lớp đối với môn học lý thuyết, không quá 20 sinh viên/nhóm đối với lớp thực hành và không quá 30 sinh viên/nhóm thảo luận và giải bài tập. - Lớp học phần sẽ được mở nếu số lượng SV đăng ký tối thiểu 30 SV/lớp đối với các môn học thuộc kiến thức đại cương, tối thiểu 15 SV/lớp đối với các môn học thuộc kiến thức cơ sở chung, cơ sở ngành và chuyên ngành, tối thiểu 10 SV/lớp đối với các môn ngoại ngữ. Các trường hợp khác do Hiệu trưởng quyết định dựa trên tình hình thực tế triển khai. Lớp sinh hoạt: Sinh viên một khóa tuyển được bố trí vào 01 lớp sinh hoạt do 01 cố vấn học tập quản lý.
```

**Rank 2 | `chunk_0060` | score `0.750000` | document `virhe4qa_867edfa78d8598fcefe0`**

```text
Điều 12. Tổ chức lớp 1. Lớp học phần: Những sinh viên theo học cùng một học phần trong cùng một khoảng thời gian và cùng một giảng viên tạo thành một lớp học phần. Mỗi lớp học phần được ký hiệu bằng một mã số riêng do Trường quy định. Lớp học phần sẽ được mở nếu số lượng sinh viên đăng ký: - Tối thiểu là 50 sinh viên đối với các môn học đại cương và các môn học cơ sở nhóm ngành. - Các môn học chuyên ngành bắt buộc và chuyên đề tốt nghiệp tối thiểu là 20 sinh viên. - Các môn học ngoại ngữ nằm trong chương trình đào tạo cho sinh viên chính quy được mở với số lượng tối thiểu là 20 sinh viên. - Các học phần như Thực tập doanh nghiệp, Khóa luận tốt nghiệp, môn học đồ án được mở không hạn chế số lượng. - Các môn học còn lại tối thiểu là 30 sinh viên. Trong trường hợp đặc biệt, theo đề nghị của sinh viên, khoa/bộ môn quản lý ngành đào tạo thì P. ĐTĐH có thể mở lớp và thực hiện theo quy định Tr…
```

**Rank 3 | `chunk_0248` | score `0.500000` | document `virhe4qa_92753479328002083b88`**

```text
Điều 7. Tổ chức lớp - Lớp học phần: • Quy mô lớp học không quá 50 SV/lớp đối với môn học lý thuyết. • Lớp học phần sẽ được mở nếu số lượng SV đăng ký tối thiểu 30 SV/lớp đối với các môn học thuộc kiến thức đại cương và cơ sở nhóm ngành, tối thiểu 15 SV/lớp đối với các môn học thuộc kiến thức cơ sở ngành và chuyên ngành, tối thiểu 10 SV/lớp đối với các môn ngoại ngữ. Các trường hợp khác do Hiệu trưởng quyết định dựa trên tình hình thực tế triển khai. - Lớp sinh hoạt: Sinh viên một khóa tuyển được bố trí vào 01 lớp sinh hoạt do 01 cố vấn học tập quản lý. Quy mô mỗi lớp sinh hoạt không quá 100 SV/lớp.
```

**Rank 4 | `chunk_0085` | score `0.375000` | document `virhe4qa_37318b15d819dcedcaa6`**

```text
Điều 14. Đăng ký học tập Sinh viên được đăng ký học và thi các môn học trong chương trình đào tạo do bất kỳ một CSĐT nào thuộc ĐHQG-HCM hoặc hệ thống các trường thành viên của ASEAN University Network tổ chức giảng dạy. Việc chuyển đổi và công nhận tín chỉ được thực hiện theo quy định tại Điều 27 của Quy chế này. Nếu đăng ký học tại Trường thì đầu mỗi học kỳ, sinh viên phải tìm hiểu, nghiên cứu để nắm được chương trình giáo dục, các học phần được mở trong học kỳ và đăng ký các học phần qua hệ thống đăng ký hoặc bằng phiếu đăng ký theo quy định của Trường. Riêng sinh viên khóa tuyển mới, học kỳ đầu tiên sẽ học theo thời khóa biểu được xếp sẵn dựa trên kế hoạch giảng dạy mẫu theo chương trình đào tạo. 1. Số tín chỉ tối thiểu, tối đa Số tín chỉ tối thiểu, tối đa được tính bao gồm số các tín chỉ đăng ký tại Trường hoặc CSĐT khác. a) Trong học kỳ chính: - Số tín chỉ đăng ký học n trong mỗi h…
```

**Rank 5 | `chunk_0224` | score `0.311111` | document `virhe4qa_df5a8af281af7a0e162f`**

```text
Điều 5. Tổ chức chương trình Các lớp CTTT được ưu tiên về cơ sở vật chất cho việc học tập và nghiên cứu. Các lớp CTTT được trang bị phòng học riêng có các thiết bị hỗ trợ giảng dạy và học tập hiện đại; có đủ giáo trình, tài liệu tham khảo trong, ngoài nước và được cập nhật thường xuyên; có thư viện và thư viện điện tử cho giảng viên và sinh viên tra cứu và sử dụng trong giảng dạy, học tập và NCKH. Về chất lượng quản lý và giảng dạy: Các lớp CTTT được quản lý và giảng dạy bởi các cán bộ có chuyên môn giỏi và có kinh nghiệm trong công tác, đảm bảo chất lượng đào tạo và dịch vụ hỗ trợ chất lượng cao cho sinh viên. Năm học đầu tiên sinh viên CTTT phải học tập trung tiếng Anh để đáp ứng điều kiện học các môn chuyên ngành hoàn toàn bằng tiếng Anh. Các lớp tiếng Anh được tổ chức tối đa 30 sinh viên theo trình độ khác nhau, tạo điều kiện cho việc giảng dạy tiếng Anh một cách tốt nhất. Đơn vị ch…
```


---

## 36. `query_074`

**Question:** Trường có những phương thức dạy và học nào?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `2` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0184` |
| Gold document | `virhe4qa_5546569cf6194e5a6d20` |
| Gold source index | `4054` |
| Hybrid top 1 | `chunk_0054` (score `0.700000`) |

### Gold context

```text
Điều  3. Mục đích của phương thức DHTT và DHKH
Bên cạnh phương thức dạy học trực tiếp, Trường triển khai các phương thức dạy học trực tuyến, dạy học kết hợp nhằm những mục đích sau đây:
1. Tăng cường ứng dụng công nghệ thông tin và truyền thông trong đào tạo; Phát triển năng lực tự học, tự nghiên cứu cho sinh viên; Đáp ứng nhu cầu học tập linh hoạt, đa dạng của sinh viên, phù hợp với chủ trương của Nhà nước, Bộ Giáo dục & Đào tạo, ĐHQG-HCM và với xu hướng đào tạo hiện đại hiện nay trên thế giới.
2. Nhằm chuẩn bị sẵn sàng chuyển đổi phương thức dạy và học một cách linh hoạt, không làm gián đoạn công tác đào tạo khi không thể tổ chức đào tạo theo hình thức trực tiếp do các nguyên nhân khách quan như thiên tai, dịch bệnh kéo dài hoặc những khó khăn từ thực tế khác và vẫn đảm bảo chất lượng đào tạo.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0054` | score `0.700000` | document `virhe4qa_a6928745429f2dfa0b83`**

```text
Điều 12. Phương thức giảng dạy môn học Môn học trong chương trình đào tạo được tổ chức giảng dạy kết hợp theo một hoặc cả ba phương thức: + Tự học tại nhà: sinh viên chủ yếu tự học sử dụng các loại tài liêu học được Trường cung cấp, đồng thời, sinh viên trao đổi, thảo luận về nội dung môn học qua mạng. + Học tập trung: Mỗi môn học có thể được tổ chức giảng dạy tập trung tại Trạm ĐTTX để hướng dẫn sinh viên học tập, thực hành những phần khó, giải đáp thắc mắc. + Học trực tuyến: Giảng viên giảng dạy, hướng dẫn sinh viên học tập trao đổi, thảo luận thông qua các hệ thống phần mềm giảng dạy trực tuyến.
```

**Rank 2 | `chunk_0184` | score `0.666667` | document `virhe4qa_5546569cf6194e5a6d20`**

```text
Điều 3. Mục đích của phương thức DHTT và DHKH Bên cạnh phương thức dạy học trực tiếp, Trường triển khai các phương thức dạy học trực tuyến, dạy học kết hợp nhằm những mục đích sau đây: 1. Tăng cường ứng dụng công nghệ thông tin và truyền thông trong đào tạo; Phát triển năng lực tự học, tự nghiên cứu cho sinh viên; Đáp ứng nhu cầu học tập linh hoạt, đa dạng của sinh viên, phù hợp với chủ trương của Nhà nước, Bộ Giáo dục & Đào tạo, ĐHQG-HCM và với xu hướng đào tạo hiện đại hiện nay trên thế giới. 2. Nhằm chuẩn bị sẵn sàng chuyển đổi phương thức dạy và học một cách linh hoạt, không làm gián đoạn công tác đào tạo khi không thể tổ chức đào tạo theo hình thức trực tiếp do các nguyên nhân khách quan như thiên tai, dịch bệnh kéo dài hoặc những khó khăn từ thực tế khác và vẫn đảm bảo chất lượng đào tạo.
```

**Rank 3 | `chunk_0015` | score `0.571429` | document `virhe4qa_e12c1ed7b0c7a0093879`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Văn bản này quy định về việc dạy và học theo phương thức trực tuyến (DHTT) và phương thức kết hợp (DHKH) cho hệ đại học chính quy của Trường Đại học Công nghệ Thông tin – ĐHQG.HCM (gọi tắt là Trường). 2. Quy định này áp dụng với các đơn vị và cá nhân có liên quan đến việc dạy và học theo phương thức DHTT, DHKH tại Trường.
```

**Rank 4 | `chunk_0226` | score `0.416667` | document `virhe4qa_97f9542af4a7ba8a9e75`**

```text
Điều 5. Tổ chức đào tạo phương thức DHTT và DHKH 1. ĐVQLMH lên kế hoạch cụ thể về phương thức giảng dạy đối với từng môn học, đảm bảo tổng số tín chỉ các môn học giảng dạy theo phương thức trực tuyến không được chiếm quá 30% tổng số tín chỉ của toàn bộ chương trình đào tạo. 2. Mỗi học kỳ, các đơn vị quản lý môn học lập thời khóa biểu các lớp học theo quy trình chung của Trường, ghi chú rõ phương thức dạy và học trong thời khóa biểu để SV nắm rõ khi đăng ký học phần (ĐKHP). ĐVQLMH chịu trách nhiệm kiểm tra, đảm bảo các điều kiện mở lớp theo Điều 6 của Quy định này khi gửi đề nghị mở lớp (thời khóa biểu) cho đơn vị quản lý đào tạo. Đơn vị quản lý đào tạo rà soát, duyệt mở lớp theo quy định. ĐVQLMH mở lớp học theo phương thức DHTT, DHKH đồng thời với lớp học theo phương thức dạy học trực tiếp để sinh viên được quyền lựa chọn khi ĐKHP. 3. Trong trường hợp đặc biệt như thiên tai, dịch bệnh v…
```

**Rank 5 | `chunk_0239` | score `0.361111` | document `virhe4qa_8cd09bb404f7a0af001e`**

```text
Điều 6. Trường hợp, điều kiện mở lớp theo phương thức DHTT và DHKH 1. Phương thức DHTT (thỏa tất cả điều kiện sau): a) Môn học phải có đầy đủ học liệu điện tử cho toàn bộ nội dung môn học theo đề cương môn học. b) Trường hợp môn học chưa có đầy đủ học liệu điện tử, Trường chỉ cho phép đối với giảng viên là chuyên gia đang ở nước ngoài. Trường hợp này, giảng viên ở nước ngoài lên lớp trực tuyến qua phần mềm Microsoft Teams (xem quy định tại Điều 10) theo thời khóa biểu; ĐVQLMH phải phân công thêm giảng viên cùng tham gia giảng dạy hoặc phân công thêm trợ giảng lý thuyết. c) Hiệu trưởng duyệt mở lớp đối với phương thức này. 2. Phương thức DHKH (thỏa tất cả điều kiện sau): a) Kế hoạch giảng dạy kết hợp phải được xác định rõ từ đầu học kỳ; b) Môn học phải có đầy đủ học liệu điện tử cho tối thiểu 1/3 nội dung môn học theo đề cương môn học;
```


---

## 37. `query_084`

**Question:** Văn bằng, chứng chỉ có bị hủy bỏ không?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `2` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0187` |
| Gold document | `virhe4qa_52f85800d1441c973d06` |
| Gold source index | `1398` |
| Hybrid top 1 | `chunk_0145` (score `1.000000`) |

### Gold context

```text
Điều  3. Trách nhiệm của các đơn vị, cá nhân trong việc quản lý văn bằng, chứng chỉ
1. Hiệu trưởng chịu trách nhiệm chung trong việc quản lý, cấp phát văn bằng, chứng chỉ.
2. Phòng Đào tạo Đại học (PĐTĐH) có trách nhiệm quản lý việc cấp văn bằng đại học, chứng chỉ; thực hiện các thủ tục đề nghị cấp phôi bằng đại học, chứng chỉ từ ĐHQG-HCM, quản lý phôi, thông tin in lên phôi và tổ chức thực hiện công tác lưu trữ, cấp phát, thu hồi, hủy bỏ bằng đại học, chứng chỉ; bản sao bằng tốt nghiệp đại học, chứng chỉ của Trường ĐHCNTT.
3. Phòng Đào tạo Sau đại học & Khoa học Công nghệ (PĐTSĐH-KHCN) có trách nhiệm quản lý việc cấp văn bằng thạc sĩ, tiến sĩ; thực hiện các thủ tục đề nghị cấp phôi bằng từ ĐHQG-HCM, quản lý phôi, thông tin in lên phôi và tổ chức thực hiện công tác lưu trữ, cấp phát, thu hồi, hủy bỏ bằng thạc sĩ, tiến sĩ; bản sao bằng thạc sĩ, tiến sĩ của Trường ĐHCNTT.
4. Phòng Tổ chức Hành chính (PTCHC) có trách nhiệm phối hợp với PĐTĐH và PĐTSĐH-KHCN trong việc in thông tin cấp bằng lên phôi văn bằng theo danh sách người học tốt nghiệp đính kèm Quyết định công nhận tốt nghiệp của Hiệu trưởng Trường ĐHCNTT theo đúng mẫu tương ứng; trình Hiệu trưởng ký và đóng dấu văn bằng, chứng chỉ; in các loại phôi chứng chỉ thuộc thẩm quyền của Trường theo quy định.
5. Các đơn vị trực thuộc Trường có đào tạo, cấp chứng chỉ chịu trách nhiệm quản lý việc in thông tin lên phôi và cấp phát chứng chỉ cho người học.
6. Phòng Thanh tra - Pháp chế - Đảm bảo Chất lượng (PTTPC-ĐBCL) có trách nhiệm thực hiện công tác thanh tra, kiểm tra việc thực hiện các quy định về văn bằng, chứng chỉ.
7. Các đơn vị được phân công quản lý việc cấp văn bằng, chứng chỉ có trách nhiệm:
a) Kiểm tra, đối chiếu và ghi chính xác, đầy đủ các thông tin ghi trên văn bằng, chứng chỉ. Cung cấp các thông tin dự kiến ghi trên văn bằng, chứng chỉ cho người học để người học kiểm tra tính chính xác của các thông tin trước khi ghi trên văn bằng, chứng chỉ; yêu cầu người học xác nhận về việc đã kiểm tra thông tin, ký xác nhận các yêu cầu chỉnh sửa thông tin và cung cấp các căn cứ yêu cầu chỉnh sửa thông tin. Các thông tin liên quan đến khai sinh của người học ghi trên văn bằng, chứng chỉ phải căn cứ vào giấy khai sinh hợp lệ và hồ sơ trúng tuyển của người học;
b) Tổ chức in, cấp văn bằng, chứng chỉ đúng thẩm quyền và đúng thời hạn theo quy định tại Điều 14 của Quy chế này.
c) Lập đầy đủ hồ sơ làm căn cứ để cấp phát, quản lý văn bằng, chứng chỉ và lưu trữ vĩnh viễn.
d) Bảo đảm tính chính xác và chịu trách nhiệm về các thông tin trong hồ sơ, trong sổ gốc cấp văn bằng, chứng chỉ.
đ) Cung cấp thông tin trong sổ gốc cấp văn bằng, chứng chỉ và thông tin trong hồ sơ tốt nghiệp để người được cấp văn bằng, chứng chỉ có căn cứ đề nghị chỉnh sửa văn bằng, chứng chỉ.
e) Chỉnh sửa nội dung văn bằng, chứng chỉ theo quy định tại Điều 18, Điều 19, Điều 20, Điều 21 của Quy chế này.
g) Bảo quản, lưu giữ văn bằng, chứng chỉ trong trường hợp người học chưa đến nhận văn bằng, chứng chỉ.
h) Đảm bảo cơ sở vật chất, trang thiết bị in, phòng chống cháy nổ để bảo quản phôi, văn bằng, chứng chỉ.
i) Thu hồi, hủy bỏ văn bằng, chứng chỉ theo quy định tại Điều 22 của Quy chế này.
k) Cấp bản sao văn bằng, chứng chỉ từ sổ gốc theo quy định tại Chương V của Quy chế này.
l) Khi cấp văn bằng, chứng chỉ cho người học phải lập sổ gốc văn bằng, chứng chỉ theo mẫu quy định của ĐHQG-HCM.
m) Đối với phôi văn bằng, chứng chỉ bị hư hỏng, viết sai, chất lượng không bảo đảm, chưa sử dụng do thay đổi mẫu phôi thì lập hội đồng hủy phôi bằng, có biên bản ghi rõ số lượng, số hiệu và tình trạng văn bằng, chứng chỉ trước khi hủy. Quy định này cũng áp dụng đối với văn bằng, chứng chỉ bị ghi sai và đã được người có thẩm quyền cấp văn bằng, chứng chỉ ký, đóng dấu nhưng người được cấp văn bằng, chứng chỉ chưa ký nhận.
n) Trường hợp phôi văn bằng, chứng chỉ bị mất thì phải có trách nhiệm lập biên bản, báo cáo lên Hiệu trưởng, thông báo ngay với cơ quan công an nơi gần nhất và ĐHQG-HCM để xử lý kịp thời.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0145` | score `1.000000` | document `virhe4qa_0719a48662653974a928`**

```text
Điều 22. Thu hồi, hủy bỏ văn bằng, chứng chỉ 1. Văn bằng, chứng chỉ bị thu hồi trong các trường hợp sau đây: a) Có hành vi gian lận trong tuyển sinh, học tập, thi cử, bảo vệ đồ án, khóa luận tốt nghiệp, luận văn, luận án hoặc gian lận trong việc làm hồ sơ để được cấp văn bằng, chứng chỉ. b) Cấp cho người không đủ điều kiện. c) Do người không có thẩm quyền cấp. d) Bị tẩy xóa, sửa chữa. đ) Để cho người khác sử dụng. e) Do lỗi của Trường. 2. Trường ĐHCNTT có trách nhiệm thu hồi và hủy bỏ văn bằng, chứng chỉ. Trường hợp Trường đã sáp nhập, chia, tách, giải thể thì cơ quan có thẩm quyền thu hồi, hủy bỏ văn bằng, chứng chỉ là cơ quan đang quản lý sổ gốc cấp văn bằng, chứng chỉ. 3. Trường ra quyết định thu hồi, hủy bỏ văn bằng, chứng chỉ. Nội dung của quyết định ghi rõ lý do thu hồi, hủy bỏ. Quyết định được đăng tải trên cổng thông tin điện tử của cơ quan có thẩm quyền thu hồi, hủy bỏ văn bằng…
```

**Rank 2 | `chunk_0187` | score `0.666667` | document `virhe4qa_52f85800d1441c973d06`**

```text
Điều 3. Trách nhiệm của các đơn vị, cá nhân trong việc quản lý văn bằng, chứng chỉ 1. Hiệu trưởng chịu trách nhiệm chung trong việc quản lý, cấp phát văn bằng, chứng chỉ. 2. Phòng Đào tạo Đại học (PĐTĐH) có trách nhiệm quản lý việc cấp văn bằng đại học, chứng chỉ; thực hiện các thủ tục đề nghị cấp phôi bằng đại học, chứng chỉ từ ĐHQG-HCM, quản lý phôi, thông tin in lên phôi và tổ chức thực hiện công tác lưu trữ, cấp phát, thu hồi, hủy bỏ bằng đại học, chứng chỉ; bản sao bằng tốt nghiệp đại học, chứng chỉ của Trường ĐHCNTT. 3. Phòng Đào tạo Sau đại học & Khoa học Công nghệ (PĐTSĐH-KHCN) có trách nhiệm quản lý việc cấp văn bằng thạc sĩ, tiến sĩ; thực hiện các thủ tục đề nghị cấp phôi bằng từ ĐHQG-HCM, quản lý phôi, thông tin in lên phôi và tổ chức thực hiện công tác lưu trữ, cấp phát, thu hồi, hủy bỏ bằng thạc sĩ, tiến sĩ; bản sao bằng thạc sĩ, tiến sĩ của Trường ĐHCNTT. 4. Phòng Tổ chức …
```

**Rank 3 | `chunk_0295` | score `0.392857` | document `virhe4qa_0b53603367abed66c611`**

```text
Điều 1. Phạm vi điều chỉnh và đối tượng áp dụng 1. Quy chế này quy định về việc quản lý văn bằng giáo dục đại học, sau đại học và các loại chứng chỉ (sau đây gọi tắt là văn bằng, chứng chỉ) của Trường Đại học Công nghệ Thông tin (ĐHCNTT); gồm: quản lý văn bằng, chứng chỉ; nội dung, ngôn ngữ, phương thức ghi trong văn bằng, chứng chỉ; cấp phát, chỉnh sửa, thu hồi, hủy bỏ văn bằng, chứng chỉ; cấp bản sao văn bằng từ sổ gốc; kiểm tra, thanh tra, xử lý vi phạm. 2. Quy chế này áp dụng đối với tất cả các đơn vị, cá nhân trong và ngoài Trường ĐHCNTT có liên quan đến công tác quản lý, cấp phát, sử dụng văn bằng, chứng chỉ của Trường ĐHCNTT.
```

**Rank 4 | `chunk_0206` | score `0.325000` | document `virhe4qa_f6befe36bf5b4e3847be`**

```text
Điều 4. Quyền và nghĩa vụ của người được cấp văn bằng, chứng chỉ Người được cấp văn bằng, chứng chỉ có các quyền sau đây: a) Yêu cầu Trường cấp bản sao, chứng thực văn bằng, chứng chỉ khi có nhu cầu. b) Yêu cầu Trường cấp văn bằng, chứng chỉ đúng thời hạn quy định tại Điều 14; ghi chính xác, đầy đủ các thông tin trên văn bằng, chứng chỉ; chỉnh sửa các nội dung ghi trên văn bằng, chứng chỉ theo quy định tại Quy chế này. c) Yêu cầu Trường cung cấp thông tin trong sổ gốc cấp văn bằng, chứng chỉ và thông tin trong hồ sơ tốt nghiệp để có căn cứ đề nghị chỉnh sửa văn bằng, chứng chỉ. Người được cấp văn bằng, chứng chỉ có các nghĩa vụ sau đây: a) Cung cấp chính xác, đầy đủ các thông tin cần thiết để ghi trong nội dung văn bằng, chứng chỉ. b) Kiểm tra tính chính xác các thông tin ghi trên văn bằng, chứng chỉ trước khi ký nhận văn bằng, chứng chỉ. c) Phải có giấy ủy quyền theo quy định của pháp …
```

**Rank 5 | `chunk_0075` | score `0.321429` | document `virhe4qa_09a10fba0ad38ed3d729`**

```text
Điều 13. Điều kiện cấp văn bằng, chứng chỉ Người học được cấp văn bằng, chứng chỉ khi đảm bảo các điều kiện sau: 1. Văn bằng được cấp sau khi người học hoàn thành chương trình giáo dục, chương trình đào tạo theo cấp học, trình độ đào tạo và đạt các điều kiện khác theo quy định của quy chế đào tạo đại học, thạc sĩ, tiến sĩ. 2. Chứng chỉ: a) Được cấp sau khi người học hoàn thành chương trình đào tạo hoặc bồi dưỡng nâng cao trình độ học vấn, nghề nghiệp theo chương trình do Bộ GD&ĐT quy định hoặc ban hành. b) Được cấp cho cá nhân có nhu cầu được đánh giá năng lực sử dụng CNTT hoặc có nhu cầu được cấp chứng chỉ ứng dụng CNTT theo quy định của Bộ GD&ĐT. 3. Không đang trong thời gian bị truy cứu trách nhiệm hình sự.
```


---

## 38. `query_099`

**Question:** Để Ban Giám hiệu có thể biết được toàn bộ hoạt động của chương trình thì đơn vị nào có trách nhiệm báo cáo cho Ban Giám hiệu?

| Field | Value |
|---|---|
| Hybrid first gold rank | `2` |
| Dense first gold rank | `2` |
| Sparse first gold rank | `2` |
| Gold chunk | `chunk_0214` |
| Gold document | `virhe4qa_9f79972f4ed1ac75695d` |
| Gold source index | `8127` |
| Hybrid top 1 | `chunk_0198` (score `1.000000`) |

### Gold context

```text
Điều  5.	Trách nhiệm của Ban Điều hành cấp Trường
Đề xuất phương hướng và xét duyệt kế hoạch phát triển CTTN của Trường để trình Ban Giám hiệu trường và BĐH của ĐHQG HCM. 
Chuẩn bị các điều kiện cơ sở vật chất; tài chính; chương trình đào tạo; tổ chức xây dựng qui chế quy định liên quan tới việc tuyển chọn và chế độ chính sách phục vụ nhằm đảm bảo cho chương trình hoạt động có hiệu quả.
Tổ chức xét tuyển và triển khai hoạt động của chương trình theo quy định.
Chỉ đạo và theo dõi việc thực hiện chương trình tại các đơn vị.
Định kỳ báo cáo Ban Giám hiệu về các hoạt động của chương trình.
```

### Hybrid top 5 candidates

**Rank 1 | `chunk_0198` | score `1.000000` | document `virhe4qa_06d792ed3048eb2fed78`**

```text
Điều 4. Tổ chức và điều hành CT CLC Ban Giám hiệu giao nhiệm vụ cho đơn vị quản lý triển khai chương trình, phối hợp chặt chẽ với đơn vị chuyên môn phụ trách ngành đào tạo. Đơn vị quản lý triển khai chịu trách nhiệm vận hành chương trình và báo cáo định kỳ cho Ban Giám hiệu.
```

**Rank 2 | `chunk_0214` | score `0.666667` | document `virhe4qa_9f79972f4ed1ac75695d`**

```text
Điều 5. Trách nhiệm của Ban Điều hành cấp Trường Đề xuất phương hướng và xét duyệt kế hoạch phát triển CTTN của Trường để trình Ban Giám hiệu trường và BĐH của ĐHQG HCM. Chuẩn bị các điều kiện cơ sở vật chất; tài chính; chương trình đào tạo; tổ chức xây dựng qui chế quy định liên quan tới việc tuyển chọn và chế độ chính sách phục vụ nhằm đảm bảo cho chương trình hoạt động có hiệu quả. Tổ chức xét tuyển và triển khai hoạt động của chương trình theo quy định. Chỉ đạo và theo dõi việc thực hiện chương trình tại các đơn vị. Định kỳ báo cáo Ban Giám hiệu về các hoạt động của chương trình.
```

**Rank 3 | `chunk_0202` | score `0.375000` | document `virhe4qa_2248b836aecbf765c1aa`**

```text
Điều 4. Bộ máy tổ chức và quản lý ĐTTX Các đơn vị chính trong bộ máy tổ chức và quản lý ĐTTX gồm: 1. Trung tâm Phát triển Công nghệ Thông tin: Là Trạm ĐTTX chính của Trường, là đầu mối quản lý tất cả sinh viên chương trình ĐTTX và tổ chức hoạt động ĐTTX của Trường đối với tất cả các ngành đào tạo mà Trường ĐHCNTT được phép ĐTTX; làm việc với các đơn vị, địa phương để thiết lập và hỗ trợ Trường quản lý các Trạm ĐTTX khác; chịu trách nhiệm chính trong việc phối hợp các đơn vị và các Trạm ĐTTX để triển khai các hoạt động tuyển sinh và tổ chức ĐTTX; đồng thời thực hiện các nhiệm vụ của một Trạm ĐTTX quy định tại Điều 5 của Quy chế này. 2. Các Khoa chuyên môn: chịu trách nhiệm quản lý chuyên môn theo ngành/chuyên ngành đào tạo được giao, chủ trì việc tổ chức xây dựng chương trình đào tạo, xây dựng học liệu ĐTTX, xây dựng ngân hàng đề thi (nếu có) cho những môn học thuộc trách nhiệm quản lý, …
```

**Rank 4 | `chunk_0071` | score `0.297619` | document `virhe4qa_2239af18e782a693b9f0`**

```text
Điều 13. Thông báo kế hoạch đào tạo 1. Đầu khoá học, Trường có trách nhiệm thông báo cho sinh viên về: - Chương trình đào tạo toàn khóa cho từng ngành học. - Quy chế học tập và các quy định của Trường. - Quyền lợi và nghĩa vụ của sinh viên. 2. Đầu mỗi năm học, Trường có trách nhiệm thông báo cho sinh viên về: - Kế hoạch giảng dạy, học tập của năm học. - Các cập nhật hoặc thay đổi trong chương trình đào tạo, chương trình môn học, học phí (nếu có). 3. Đầu mỗi học kỳ, Trường có trách nhiệm thông báo cho sinh viên về: - Thời khóa biểu giảng dạy, học tập của học kỳ. - Danh mục các học phần và số lượng tín chỉ của mỗi học phần dự kiến giảng dạy trong học kỳ, điều kiện để đăng ký học các học phần đó. - Số lớp học dự kiến tổ chức cho mỗi học phần và thời khoá biểu cho các lớp học.
```

**Rank 5 | `chunk_0001` | score `0.285714` | document `virhe4qa_7339d5d3b4cae6a902ea`**

```text
1. QUY ĐỊNH CHUNG - Phòng Đào tạo Đại học (P. ĐTĐH) là đơn vị trực tiếp tiếp nhận thông tin và xử lý việc báo thay đổi liên quan đến giảng dạy (nghỉ dạy, thay đổi cán bộ giảng dạy) và đăng ký dạy bù của cán bộ giảng dạy. - Phòng Thanh tra pháp chế và Đảm bảo chất lượng (P. TTPC&ĐBCL) là đơn vị phối hợp với P. ĐTĐH, chịu trách nhiệm thanh tra, giám sát việc giảng dạy; thống kê và báo cáo định kỳ về tình hình giảng dạy cho Ban Giám hiệu và các bên liên quan. - CBGD phải dạy đủ số tiết theo qui định của môn học (qui định trong đề cương môn học). Các tiết nghỉ dạy phải được đăng ký dạy bù sau hoặc trước đó cho đầy đủ. - CBGD phải báo cho P. ĐTĐH việc thay đổi giảng dạy (nghỉ dạy, thay đổi CBGD tạm thời). Trong trường hợp đột xuất, CBGD phải thông báo ngay cho P. ĐTĐH chậm nhất là 15 phút sau khi buổi học bắt đầu và gửi giấy báo nghỉ trong vòng 5 ngày sau buổi dạy đã cho nghỉ. CBGD không đượ…
```

