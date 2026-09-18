# 05. Các loại văn bản hành chính

> **Trạng thái GĐ1:** Đã sửa chữ viết tắt `Quy định` từ `QYĐ` thành `QyĐ` và loại bỏ các nhận định lịch sử/mẫu trình bày chưa được truy xuất nguồn đầy đủ.

## 1. Danh sách 29 loại văn bản hành chính

Điều 7 Nghị định 30/2020/NĐ-CP liệt kê 29 loại:

| STT | Tên loại | Chữ viết tắt theo Phụ lục III |
|---:|---|---|
| 1 | Nghị quyết (cá biệt) | NQ |
| 2 | Quyết định (cá biệt) | QĐ |
| 3 | Chỉ thị | CT |
| 4 | Quy chế | QC |
| 5 | **Quy định** | **QyĐ** |
| 6 | Thông cáo | TC |
| 7 | Thông báo | TB |
| 8 | Hướng dẫn | HD |
| 9 | Chương trình | CTr |
| 10 | Kế hoạch | KH |
| 11 | Phương án | PA |
| 12 | Đề án | ĐA |
| 13 | Dự án | DA |
| 14 | Báo cáo | BC |
| 15 | Biên bản | BB |
| 16 | Tờ trình | TTr |
| 17 | Hợp đồng | HĐ |
| 18 | Công văn | Phụ lục III không quy định chữ viết tắt tên loại riêng |
| 19 | Công điện | CĐ |
| 20 | Bản ghi nhớ | BGN |
| 21 | Bản thỏa thuận | BTT |
| 22 | Giấy ủy quyền | GUQ |
| 23 | Giấy mời | GM |
| 24 | Giấy giới thiệu | GGT |
| 25 | Giấy nghỉ phép | GNP |
| 26 | Phiếu gửi | PG |
| 27 | Phiếu chuyển | PC |
| 28 | Phiếu báo | PB |
| 29 | Thư công | Phụ lục III không quy định chữ viết tắt tên loại riêng |

**Nguồn:** Điều 7 và Phụ lục III.

## 2. Văn bản chuyên ngành không phải là “loại thứ 30”

Điều 4 quy định văn bản chuyên ngành do người đứng đầu cơ quan quản lý ngành, lĩnh vực căn cứ Nghị định để quy định cho phù hợp.

Do đó, danh sách 29 loại ở Điều 7 là danh sách **văn bản hành chính**; không được dùng để kết luận mọi văn bản chuyên ngành đều phải mang một trong 29 tên loại này.

## 3. Về mẫu trình bày

Phụ lục III quy định bảng chữ viết tắt và các mẫu trình bày văn bản hành chính/bản sao. Một mẫu có thể áp dụng cho một nhóm tên loại.

Repository **không dùng số lượng mẫu để suy ra rằng mỗi loại văn bản có một mẫu riêng**. Việc map từng loại vào mẫu sẽ được thực hiện trong GĐ2 bằng source locator cụ thể.

## 4. Phân nhóm để tra cứu — chỉ là convenience layer

Nếu cần phân nhóm theo mục đích sử dụng để tìm kiếm hoặc xây UI, có thể tạo taxonomy riêng. Taxonomy đó phải được gắn `normative: false` và không được thay thế danh sách pháp lý tại Điều 7.

---

**Nguồn chuẩn:** Điều 7 và Phụ lục III Nghị định 30/2020/NĐ-CP.  
**Canonical Rule:** `ND30.PL3.I.ABBR.QUY_DINH`.
