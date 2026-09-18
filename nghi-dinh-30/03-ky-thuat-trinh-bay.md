# 03. Kỹ thuật trình bày văn bản hành chính

> **Trạng thái GĐ1:** Đã sửa các lỗi P0 về kiểu chữ địa danh/thời gian, trích yếu và khoảng cách dòng; đối chiếu với Điều 9 và Phụ lục I Nghị định 30/2020/NĐ-CP.

## 1. Quy định chung

| Nội dung | Quy định |
|---|---|
| Khổ giấy | A4 (210 mm × 297 mm) |
| Kiểu trình bày | Theo chiều dài khổ A4 |
| Định lề | Trên 20–25 mm; dưới 20–25 mm; trái 30–35 mm; phải 15–20 mm |
| Phông chữ | Times New Roman, bộ mã Unicode theo TCVN 6909:2001 |
| Màu chữ | Đen |
| Số trang | Chữ số Ả Rập, cỡ 13–14, canh giữa trong phần lề trên; đánh từ số 1 nhưng không hiển thị số trang thứ nhất |

Trường hợp văn bản có bảng, biểu lớn không làm thành phụ lục riêng thì có thể trình bày theo chiều rộng của trang giấy.

## 2. Cỡ chữ và kiểu chữ một số thành phần chính

| Thành phần | Loại chữ | Cỡ chữ | Kiểu chữ |
|---|---:|---:|---|
| Quốc hiệu | In hoa | 12–13 | Đứng, đậm |
| Tiêu ngữ | In thường | 13–14 | Đứng, đậm |
| Tên cơ quan chủ quản trực tiếp | In hoa | 12–13 | Đứng |
| Tên cơ quan, tổ chức ban hành | In hoa | 12–13 | Đứng, đậm |
| Số, ký hiệu | In thường | 13 | Đứng |
| **Địa danh và thời gian** | In thường | **13–14** | **Nghiêng** |
| Tên loại văn bản | In hoa | 13–14 | Đứng, đậm |
| **Trích yếu của văn bản có tên loại** | In thường | **13–14** | **Đứng, đậm** |
| **Trích yếu công văn** | In thường | **12–13** | **Đứng** |
| Nội dung chính | In thường | 13–14 | Đứng |
| Quyền hạn/chức vụ người ký | Theo trường hợp | 13–14 | Đứng, đậm |
| Họ tên người ký | In thường | 13–14 | Đứng, đậm |

Các rule P0 tương ứng được mã hóa trong `rules/administrative/nd30/appendix-i/`.

## 3. Căn cứ ban hành

Khi văn bản có phần căn cứ ban hành:

- trình bày bằng chữ in thường, kiểu chữ nghiêng, cỡ 13–14;
- mỗi căn cứ xuống dòng;
- cuối mỗi căn cứ dùng dấu chấm phẩy (`;`);
- dòng căn cứ cuối cùng kết thúc bằng dấu chấm (`.`).

Việc **có cần căn cứ hay không** phụ thuộc tên loại và nội dung văn bản; không phải mọi văn bản hành chính đều phải có phần căn cứ.

## 4. Nội dung văn bản

Phần nội dung:

- chữ in thường, kiểu đứng, cỡ 13–14;
- canh đều hai lề;
- khi xuống dòng, chữ đầu dòng lùi 1 cm hoặc 1,27 cm;
- khoảng cách giữa các đoạn văn **tối thiểu 6 pt**;
- khoảng cách giữa các dòng **tối thiểu dòng đơn và tối đa 1,5 lines**.

Không được diễn giải thành “1.15 trở lên” vì cách diễn đạt đó bỏ mất giới hạn tối đa 1,5 lines.

## 5. Phụ lục

Kỹ thuật trình bày phụ lục phải theo đúng Phụ lục I, bao gồm tên phụ lục, số thứ tự, tiêu đề và thông tin chỉ dẫn kèm theo tương ứng với từng trường hợp.

Khi xây validator, không nên áp một kiểu trình bày duy nhất cho mọi phụ lục mà phải xét đúng loại thành phần và mẫu nguồn.

---

**Nguồn chuẩn:** Điều 9 và Phụ lục I Nghị định 30/2020/NĐ-CP.  
**Lưu ý:** các giá trị nội bộ như giãn dòng 1,2 hoặc chọn cố định cỡ 14 là `organization profile`, không phải giá trị duy nhất mà Nghị định bắt buộc.
