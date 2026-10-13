# Trang 3 – AI Team Design · Saving Tracker AI

> Nháp. Team cần xác nhận các gap có đúng với thực tế không.

## 1. Team Architecture: **Embedded**

Team chỉ có vài người và đang ở giai đoạn MVP, nên không cần hub AI riêng. Mỗi mảng (AI, backend/bảo mật, UX) do một người trực tiếp phụ trách ngay trong team sản phẩm, họp sync ngắn hàng tuần. Chưa có nhiều sản phẩm để dùng chung một nhóm AI trung tâm, nên Centralized và Hybrid chưa cần.

## 2. Core Roles và Extended Roles

**Core (cần ngay):**
| Vai trò | Vì sao cần ở MVP |
|---|---|
| Product Owner | Chốt phạm vi, làm việc với cố vấn tài chính và đối tác API |
| AI Engineer | Làm OCR/LLM đọc hóa đơn và guardrail cho phần gợi ý |
| Backend & Security | Lưu dữ liệu tài chính nhạy cảm an toàn |
| UI/UX | Giữ luồng nhập và cảnh báo đơn giản, cân bằng với yêu cầu bảo mật |

**Extended (chỉ khi scale):**
- Legal / Compliance (dữ liệu cá nhân, quy định tư vấn tài chính)
- MLOps / Evals (theo dõi chất lượng OCR/LLM liên tục)
- Domain Expert tài chính toàn thời gian
- AI Ethics / Governance

## 3. Priority Resourcing (3 gap)

| Capability gap | Cách bổ sung | Vì sao | Khi nào cần |
|---|---|---|---|
| Chuyên môn tài chính và giới hạn tư vấn | **Partner** với cố vấn tài chính (cũng là S3 trong Stakeholder Map) | Team không cần tuyển full-time ở MVP, nhưng cần người xác định "rủi ro đỏ" | Trước khi mở phần gợi ý cho người dùng thử |
| Kết nối dữ liệu ngân hàng (Open API) | **Partner** với aggregator có sẵn sandbox (S4) | Tự xây kết nối ngân hàng quá tốn thời gian và rủi ro tuân thủ. MVP có phương án dự phòng là nhập hóa đơn thủ công | Sau khi MVP nhập thủ công chạy ổn |
| Review bảo mật độc lập | **Outsource** một lần | Cần góc nhìn bên ngoài về dữ liệu nhạy cảm, không cần người cố định | Trước khi cho người dùng ngoài team thử dữ liệu thật |

Chưa chọn Hire cho gap nào, vì ở MVP không cần thêm người cố định.

## 4. Squad Goal

"Team của chúng tôi sở hữu **luồng đọc hóa đơn và cảnh báo chi tiêu của Saving Tracker AI** và chịu trách nhiệm đưa **sản phẩm** từ **prototype OCR chưa kiểm chứng với người dùng thật** đến **MVP an toàn mà nhóm người dùng thử đầu tiên tin dùng**."

## GATE 3 – tự kiểm tra
- [x] Có kiến trúc kèm lý do
- [x] Core và Extended tách rõ
- [x] 3 gap, mỗi gap có cách bổ sung, lý do và thời điểm
- [x] Có Squad Goal
- [ ] Cần team xác nhận: hiện trạng "prototype OCR" trong Squad Goal có đúng không
