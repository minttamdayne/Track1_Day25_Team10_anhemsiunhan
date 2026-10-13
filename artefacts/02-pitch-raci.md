# Trang 2 – Pitch & RACI · Saving Tracker AI

> Bản nháp. Chưa có số liệu OCR, kết quả dùng thử hoặc phản hồi chuyên gia trong repo; không tự điền số chưa đo.

## 1. Pitch gửi S3 – Cố vấn tài chính

**Kết luận:** Team đề xuất MVP chỉ đưa ra *gợi ý tích lũy mang tính tham khảo* từ dữ liệu chi tiêu của chính người dùng, không khuyến nghị sản phẩm đầu tư cụ thể. Chúng tôi muốn bạn kiểm tra giới hạn đề xuất này có đủ an toàn không.

**Lý do:**
1. Người dùng trẻ bỏ việc ghi chi tiêu vì nhập tay tốn công. OCR/LLM đọc hóa đơn giúp bỏ bước này.
2. Team dự kiến giới hạn phần gợi ý vào số liệu chi tiêu của người dùng và thêm disclaimer; đây là guardrail cần được review, chưa phải kết quả đã kiểm chứng.
3. Bạn là người hiểu rõ nhất tình huống nào là "rủi ro đỏ" và đó là chỗ team còn thiếu.

**Bằng chứng:** Repo mô tả prototype OCR chưa được kiểm chứng với người dùng thật. Chưa có số liệu độ chính xác, kết quả dùng thử hoặc đánh giá của cố vấn được ghi lại; vì vậy pitch này nêu đề xuất cần được review, chưa khẳng định sản phẩm đã an toàn hay hiệu quả.

**Small ask:** 30 phút xem 3 tình huống mẫu (ví dụ chi vượt ngân sách, gợi ý tiết kiệm hàng tháng, câu hỏi "có nên mua cổ phiếu X không") và cho biết câu trả lời nào AI không nên đưa ra. Team sẽ dùng phản hồi để chỉnh guardrail trước khi thử tính năng với người dùng.

## 2. Phản biện có khả năng cao nhất

**Phản biện:** "AI có thể đưa lời khuyên tài chính sai, và người dùng sẽ làm theo."

**Trả lời (dựa trên hành động giảm rủi ro):**
- Đề xuất MVP chỉ gợi ý tiết kiệm dựa trên dữ liệu chi tiêu của người dùng, không gợi ý sản phẩm hay mã đầu tư.
- Team dự kiến từ chối câu hỏi đầu tư cụ thể và chuyển sang disclaimer; bộ test và kết quả từ chối cần được xây dựng, đo trước khi thử tính năng với người dùng.
- Cố vấn là người duyệt các ca "rủi ro đỏ" trước khi mở phần này cho người dùng thử.

## 3. Phiên bản cá nhân (Bước 3, mỗi người tự viết)

Mỗi thành viên viết lại pitch bằng lời của mình theo đúng 4 phần (kết luận, lý do, bằng chứng, small ask), rồi chia sẻ. Team chọn các câu rõ nhất.

| Thành viên | Câu kết luận của bạn | Câu small ask của bạn |
|---|---|---|
| Linh | MVP chỉ gợi ý tích lũy tham khảo từ chi tiêu người dùng, không khuyến nghị sản phẩm đầu tư cụ thể. | Xin 30 phút để cố vấn xem 3 tình huống mẫu và chỉ ra trường hợp AI không nên trả lời. |

*Mục đích của bước này là kiểm tra từng người có hiểu thông điệp thật hay chỉ đồng ý với bản nháp.*

## 4. RACI Matrix (1 A duy nhất mỗi hàng)

Cột là **vai trò**, không cần gắn tên cá nhân.

| Công việc (1–2 tháng tới) | Product Owner | AI Engineer | Backend & Security | UI/UX | Cố vấn tài chính | Đơn vị Open API | Giảng viên |
|---|---|---|---|---|---|---|---|
| Chốt phạm vi MVP và phương án kết nối Open API | **A**/R | C | C | C | C | C | I |
| Xây pipeline OCR/LLM đọc hóa đơn | I | **A**/R | C | I | I | I | I |
| Bảo mật và quyền riêng tư dữ liệu | C | C | **A**/R | I | I | I | I |
| Guardrail cho phần gợi ý tích lũy | **A** | R | C | I | C | I | I |
| Thiết kế luồng nhập và cảnh báo | C | I | C | **A**/R | I | I | I |
| Test người dùng và quyết định phạm vi thử nghiệm | **A**/R | C | C | C | C | I | I |

**Lý do chọn A cho hai hàng dễ gây tranh cãi:**
- Guardrail: A = Product Owner, R = AI Engineer. Người làm và người duyệt tách nhau để tránh tự làm tự duyệt.
- Test người dùng và quyết định phạm vi thử nghiệm: A/R = Product Owner, vì kết quả test quyết định mức độ sẵn sàng cho bước thử tiếp theo.

> Team nhỏ thì một người có thể vừa R vừa A (ghi "A/R"). Cần ghi rõ ai đảm nhiệm mỗi vai trò, vì một người có thể kiêm nhiều vai trò.

## GATE 2 – tự kiểm tra
- [x] Pitch có kết luận, lý do, bằng chứng, small ask
- [x] Có 1 phản biện và câu trả lời
- [ ] Bằng chứng sản phẩm chưa có số liệu thật; cần bổ sung khi có kết quả đo hoặc feedback
- [ ] Bước cá nhân: Linh đã có phiên bản; chờ các thành viên còn lại chia sẻ để team chọn câu rõ nhất
- [x] RACI: 6 việc, mỗi việc đúng 1 A (cần team xác nhận người nhận từng vai trò)
