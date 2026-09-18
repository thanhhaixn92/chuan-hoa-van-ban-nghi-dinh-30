# 07. Checklist kiểm tra văn bản trước khi ban hành

> **Trạng thái GĐ1:** Checklist đã được sửa các lỗi P0/P1. Đây là lớp hỗ trợ thực hành, không phải tuyên bố rằng mọi mục đều áp dụng cho mọi văn bản. Về lâu dài checklist này phải được sinh từ Canonical Rules đã `verified`.

## A. Xác định phạm vi trước khi kiểm tra

- [ ] Đã xác định đúng **chủ thể ban hành** và văn bản có thuộc phạm vi áp dụng trực tiếp của Nghị định 30 hay không.
- [ ] Đã xác định đúng **regime**: văn bản hành chính / văn bản quy phạm pháp luật / văn bản chuyên ngành / hệ khác.
- [ ] Đã xác định đúng **loại văn bản** và ngày ban hành để chọn rule có hiệu lực phù hợp.

Nếu chưa xác định chắc regime, không tự động sửa cấu trúc văn bản.

## B. Kiểm tra thành phần thể thức

- [ ] Quốc hiệu và Tiêu ngữ đúng quy định.
- [ ] Tên cơ quan, tổ chức ban hành đúng.
- [ ] Số, ký hiệu đúng trường hợp áp dụng.
- [ ] Địa danh và thời gian ban hành đúng nội dung và định dạng.
- [ ] Tên loại và trích yếu được xử lý đúng theo loại văn bản.
- [ ] **Nếu là công văn:** không tạo heading `CÔNG VĂN`; kiểm tra trích yếu ở ô 5b sau `V/v`.
- [ ] Có nội dung văn bản.
- [ ] Quyền hạn/chức vụ, họ tên và chữ ký người có thẩm quyền đúng trường hợp.
- [ ] Dấu/chữ ký số của cơ quan, tổ chức được xử lý đúng giai đoạn phát hành.
- [ ] `Kính gửi`/`Nơi nhận` được trình bày đúng trường hợp áp dụng.

## C. Kiểm tra kỹ thuật trình bày

- [ ] Khổ A4 và hướng trang đúng; trường hợp bảng/biểu lớn được xử lý theo ngoại lệ của Phụ lục I.
- [ ] Lề trang: trên 20–25 mm; dưới 20–25 mm; trái 30–35 mm; phải 15–20 mm.
- [ ] Phông Times New Roman, Unicode theo TCVN 6909:2001, màu đen.
- [ ] Địa danh và thời gian: chữ nghiêng, cỡ 13–14.
- [ ] Văn bản có tên loại: trích yếu cỡ 13–14, đứng, đậm.
- [ ] Công văn: trích yếu cỡ 12–13, đứng.
- [ ] Nội dung: cỡ 13–14; canh đều; đầu dòng 1 cm hoặc 1,27 cm.
- [ ] Khoảng cách đoạn tối thiểu 6 pt.
- [ ] Khoảng cách dòng từ dòng đơn đến tối đa 1,5 lines.
- [ ] Số trang đúng quy định; trang đầu không hiển thị số.

## D. Kiểm tra bố cục và nội dung

- [ ] Nếu dùng Phần/Chương/Mục/Tiểu mục/Điều thì các cấp này có tiêu đề.
- [ ] Số thứ tự và cách trình bày Phần/Chương/Mục/Tiểu mục/Điều/Khoản/Điểm đúng quy định.
- [ ] Căn cứ ban hành, nếu có, đúng nội dung và kỹ thuật trình bày.
- [ ] Nội dung thuộc thẩm quyền và đã được người có trách nhiệm kiểm tra.
- [ ] Số liệu, tên cơ quan, tổ chức, cá nhân, ngày tháng được kiểm chứng.

Các câu hỏi về **thẩm quyền, căn cứ pháp lý, nội dung pháp lý** phải được coi là `NEEDS_REVIEW` hoặc kiểm tra chuyên môn; không nên auto-fix bằng AI.

## E. Kiểm tra trước và sau ký

### Trước ký

- [ ] Người đứng đầu đơn vị soạn thảo đã kiểm tra nội dung.
- [ ] Người được giao trách nhiệm đã kiểm tra thể thức, kỹ thuật trình bày.
- [ ] Bản thảo đã được người có thẩm quyền ký văn bản duyệt.

### Sau ký — văn bản đi

Kiểm tra theo đúng thứ tự Điều 14:

- [ ] 1. Đã cấp số, thời gian ban hành.
- [ ] 2. Đã đăng ký văn bản đi.
- [ ] 3. Đã nhân bản/đóng dấu theo trường hợp văn bản giấy hoặc ký số của cơ quan, tổ chức đối với văn bản điện tử.
- [ ] 4. Đã phát hành và theo dõi việc chuyển phát.
- [ ] 5. Đã lưu văn bản đi.

## F. Trường hợp điện tử, mật, khẩn hoặc có phụ lục

- [ ] Văn bản điện tử có chữ ký số của **người có thẩm quyền**.
- [ ] Văn bản điện tử có chữ ký số của **cơ quan, tổ chức** theo quy định.
- [ ] Văn bản mật/khẩn có dấu chỉ phù hợp và tuân thủ pháp luật chuyên ngành có liên quan.
- [ ] Phụ lục được trình bày, đánh số và liên kết đúng trường hợp.
- [ ] Nếu tài liệu đã ký số/protected, chỉ audit; không tự động sửa làm ảnh hưởng tính toàn vẹn.

---

**Nguồn chuẩn:** Điều 5, Điều 8–14 và Phụ lục I–III Nghị định 30/2020/NĐ-CP.  
**Kiến trúc v2:** kết quả kiểm tra phải phân biệt `PASS`, `FAIL`, `NOT_APPLICABLE`, `NOT_EVALUATED`, `NEEDS_REVIEW`.
