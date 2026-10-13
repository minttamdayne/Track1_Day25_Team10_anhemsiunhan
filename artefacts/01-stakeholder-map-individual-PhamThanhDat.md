# Bản cá nhân – Stakeholder Map · Saving Tracker AI

**Người thực hiện:** Phạm Thành Đạt (AI Engineer)

## 1. Danh sách stakeholder cá nhân

| # | Stakeholder | Influence | Interest | Stance sơ bộ | Căn cứ / điều cần xác minh |
|---|---|---|---|---|---|
| 1 | Giảng viên/mentor trực tiếp review dự án | Cao | Cao | Chưa xác minh | Có ảnh hưởng đến phạm vi MVP và tiêu chí đánh giá; chưa có feedback cụ thể được ghi nhận. |
| 2 | Nhóm 5 sinh viên dự kiến thử nghiệm Saving Tracker AI | Thấp | Cao (dự kiến) | Chưa xác minh | Nguồn feedback về độ chính xác OCR và thời gian nhập liệu; chưa có kết quả thử nghiệm. |
| 3 | Product Owner (Đinh Thị Minh Tâm) – người chốt phạm vi MVP | Cao | Cao | Ủng hộ – giả định | Quyết định trường dữ liệu cần trích xuất và tiêu chí chấp nhận; cần xác nhận qua backlog. |
| 4 | Backend Developer (Nguyễn Khánh Linh) – người tích hợp pipeline OCR/LLM | Cao | Cao | Ủng hộ – giả định | Ảnh hưởng trực tiếp đến khả năng đưa eval vào chu kỳ build; cần xác nhận interface. |
| 5 | Chuyên gia bảo mật/pháp lý dữ liệu có thể review MVP | Cao | Thấp | Chưa xác minh | Có thể yêu cầu che/xóa thông tin nhạy cảm trước khi eval; chưa có người review cụ thể. |
| 6 | Đơn vị cung cấp Open API/aggregator ngân hàng | Cao* | Thấp | Chưa xác minh | Chỉ ảnh hưởng nếu MVP mở rộng sang đồng bộ giao dịch; chưa liên hệ đối tác nào. |
| 7 | Cố vấn tài chính cá nhân có thể tham vấn guardrail gợi ý | Trung bình | Trung bình | Chưa xác minh | Có thể xác định giới hạn an toàn cho phần gợi ý tích lũy; chưa liên hệ. |

*Influence của S6 phụ thuộc phạm vi: nếu MVP chỉ đọc hóa đơn thủ công, ảnh hưởng trực tiếp thấp.*

*Các mức Influence, Interest và stance là giả thuyết phục vụ thảo luận nhóm, không phải quan điểm đã xác nhận của stakeholder.*

## 2. Stakeholder cá nhân ưu tiên

**Backend Developer (người tích hợp pipeline)** là stakeholder mình ưu tiên phối hợp, vì mình là AI Engineer phụ trách OCR/LLM eval.

Nếu interface giữa pipeline trích xuất và backend lưu trữ không thống nhất (schema trường, format đáp án chuẩn, cách log lỗi), bộ 30 hóa đơn eval mình xây sẽ khó chạy lặp lại sau mỗi lần cập nhật. Trong 1–2 tuần tới, mình đề xuất cùng backend chốt schema 3 trường (tên cửa hàng, ngày giao dịch, tổng tiền) và vị trí lưu kết quả eval trước deadline 27/10/2026.

## 3. Việc cần xác nhận trước khi gộp với nhóm

- [ ] Schema 3 trường trích xuất đã được Product Owner và Backend thống nhất chưa?
- [ ] Hóa đơn mẫu đã che thông tin nhạy cảm chưa, ai chịu trách nhiệm che?
- [ ] Kết quả eval lưu ở đâu để Product Owner dùng cho quyết định pilot?
- [ ] Stance các bên vẫn ghi "chưa xác minh" cho đến khi có trao đổi/feedback thực tế.
- [ ] Không dùng số liệu OCR accuracy nào chưa đo được làm bằng chứng.
