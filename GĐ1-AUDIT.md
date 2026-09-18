# GĐ1 Audit — Nghị định 30/2020/NĐ-CP

## Phạm vi checkpoint

Checkpoint này xử lý các lỗi P0/P1 đã xác định trong 7 guide hiện hữu và tạo Canonical Rules đầu tiên cho các điểm có thể kiểm tra độc lập.

Nguồn đối chiếu chính:

- Nghị định 30/2020/NĐ-CP, Điều 1–14;
- Phụ lục I;
- Phụ lục III;
- Cơ sở dữ liệu quốc gia về văn bản pháp luật và Cổng Thông tin điện tử Chính phủ.

Không coi GĐ1 là hoàn tất mapping toàn bộ 38 điều + 6 phụ lục. Phần đó thuộc GĐ2.

## Các lỗi P0/P1 đã xử lý

| ID | File | Vấn đề cũ | Kết quả GĐ1 |
|---|---|---|---|
| P0-01 | 01 | Gộp tổ chức chính trị/xã hội vào nhóm áp dụng trực tiếp | Đã tách đúng hai nhóm theo Điều 2 |
| P0-02 | 01 | Rút gọn giá trị pháp lý VBĐT thành “có ký số” | Đã yêu cầu chữ ký số người có thẩm quyền + cơ quan/tổ chức |
| P1-01 | 01 | Diễn giải “5 nguyên tắc” không đúng cấu trúc Điều 4 | Đã tách 1 nguyên tắc và nhóm yêu cầu |
| P1-02 | 01 | Mô tả trách nhiệm Văn thư/người soạn thảo không bám Điều 6/10 | Đã sửa và dẫn đúng điều |
| P1-03 | 02 | Dễ suy mọi văn bản đều có heading tên loại | Đã nêu ngoại lệ trình bày của công văn |
| P1-04 | 02 | Ô 9a/9b chưa tách rõ | Đã tách `Kính gửi` và `Nơi nhận` |
| P0-03 | 03 | Địa danh/thời gian ghi chữ đứng | Đã sửa thành chữ nghiêng 13–14 |
| P0-04 | 03 | Trích yếu văn bản có tên loại thiếu đậm | Đã sửa thành đứng, đậm 13–14 |
| P0-05 | 03 | Khoảng cách dòng “1.15 trở lên” | Đã sửa: tối thiểu dòng đơn, tối đa 1,5 lines |
| P2-01 | 04 | “Tiểu mục mới bổ sung” không có provenance | Đã loại bỏ |
| P1-05 | 04 | Gợi ý bố cục lẫn với rule bắt buộc | Đã tách mục recommendation |
| P0-06 | 05 | `QYĐ` | Đã sửa thành `QyĐ` |
| P2-02 | 05 | Nhận định lịch sử/đếm mẫu không có locator | Đã bỏ hoặc chuyển sang trạng thái cần map GĐ2 |
| P0-07 | 06 | Sai thứ tự quản lý văn bản đi | Đã sửa đúng Điều 14 |
| P1-06 | 06 | Gán mặc định kiểm tra thể thức cho Văn thư | Đã sửa thành “người được giao trách nhiệm” theo Điều 12 |
| P1-07 | 07 | Checklist bắt buộc tên loại cho mọi văn bản | Đã thêm điều kiện riêng cho công văn |
| P1-08 | 07 | Không phân biệt legal review với auto-fix | Đã thêm `NEEDS_REVIEW` và safety guard |

## Canonical Rules đã tạo

- `ND30.ART5.1.ELECTRONIC.AUTHORIZED_SIGNER_SIGNATURE`
- `ND30.ART5.1.ELECTRONIC.ORGANIZATION_SIGNATURE`
- `ND30.PL1.I.II.4.C.PLACE_DATE_ITALIC`
- `ND30.PL1.I.II.5.A.SUBJECT_BOLD`
- `ND30.PL1.I.II.5.A.SUBJECT_FONT_SIZE`
- `ND30.PL1.I.II.5.B.OFFICIAL_LETTER_SUBJECT_FONT_SIZE`
- `ND30.PL1.I.II.5.B.OFFICIAL_LETTER_SUBJECT_NOT_BOLD`
- `ND30.PL1.I.II.6.E.BODY_LINE_SPACING`
- `ND30.PL3.I.ABBR.QUY_DINH`
- `ND30.ART14.OUTGOING_WORKFLOW_ORDER`

Các rule trên được đánh dấu `maturity: verified` vì locator và nội dung đã được đối chiếu trực tiếp trong checkpoint này.

## Việc cố ý chưa làm

- Chưa map toàn bộ Điều 1–38.
- Chưa map toàn bộ Phụ lục I–VI.
- Chưa tạo production DOCX parser/formatter.
- Chưa biến toàn bộ checklist thành generated artifact.
- Chưa tạo rule về mọi quyền hạn ký, nơi nhận, số/ký hiệu, bản sao, dấu mật/khẩn.
- Chưa triển khai legal-range profile checking bằng code.

## Gate sang checkpoint tiếp theo

GĐ1 checkpoint này PASS khi:

1. 7 guide không còn các lỗi P0/P1 nêu trên.
2. Source manifest NĐ30 hợp lệ theo `source.schema.json`.
3. 10 Canonical Rules hợp lệ theo `rule.schema.json`.
4. Rule IDs không trùng.
5. Rule source ID đều tồn tại trong registry.
6. Không có rule `SAFE` nào thay đổi nội dung pháp lý/semantic.
