# Trang 2 – Pitch & RACI · Saving Tracker AI

> Nháp. Các chỗ `[TODO]` cần số liệu thật. Không điền số chưa đo, vì pitch không được hứa vượt bằng chứng.

## 1. Pitch gửi S3 – Cố vấn tài chính

**Kết luận:** Team đề xuất ứng dụng chỉ đưa ra *gợi ý tích lũy mang tính tham khảo* từ dữ liệu chi tiêu của chính người dùng, không khuyến nghị sản phẩm đầu tư cụ thể. Chúng tôi muốn bạn kiểm tra giới hạn đó có đủ an toàn không.

**Lý do:**
1. Người dùng trẻ bỏ việc ghi chi tiêu vì nhập tay tốn công. OCR/LLM đọc hóa đơn giúp bỏ bước này.
2. Phần gợi ý chỉ dựa trên số liệu chi tiêu của người dùng và có disclaimer, nên không thay vai trò cố vấn của bạn.
3. Bạn là người hiểu rõ nhất tình huống nào là "rủi ro đỏ" và đó là chỗ team còn thiếu.

**Bằng chứng:** [TODO: OCR đọc đúng X/Y hóa đơn thật; Z người đã dùng thử; feedback chính]. Phần tư vấn **chưa được kiểm chứng** với ai ngoài team.

**Small ask:** 30 phút xem 3 tình huống mẫu (ví dụ chi vượt ngân sách, gợi ý tiết kiệm hàng tháng, câu hỏi "có nên mua cổ phiếu X không") và cho biết câu trả lời nào AI không nên đưa ra. Sau buổi này team sẽ gửi lại bản guardrail đã chỉnh trong [TODO] ngày.

## 2. Phản biện có khả năng cao nhất

**Phản biện:** "AI có thể đưa lời khuyên tài chính sai, và người dùng sẽ làm theo."

**Trả lời (dựa trên hành động giảm rủi ro):**
- MVP chỉ gợi ý tiết kiệm dựa trên dữ liệu chi tiêu của người dùng, không gợi ý sản phẩm hay mã đầu tư.
- Câu hỏi về đầu tư cụ thể bị từ chối và chuyển sang disclaimer. Team sẽ có bộ test câu hỏi này, [TODO: số ca test và tỷ lệ từ chối đúng].
- Cố vấn là người duyệt các ca "rủi ro đỏ" trước khi mở phần này cho người dùng thử.

## 3. Phiên bản cá nhân (Bước 3, mỗi người tự viết)

Mỗi thành viên viết lại pitch bằng lời của mình theo đúng 4 phần (kết luận, lý do, bằng chứng, small ask), rồi chia sẻ. Team chọn các câu rõ nhất.

| Thành viên | Câu kết luận của bạn | Câu small ask của bạn |
|---|---|---|
| [TODO] | [TODO] | [TODO] |

*Mục đích của bước này là kiểm tra từng người có hiểu thông điệp thật hay chỉ đồng ý với bản nháp.*

## 4. RACI Matrix (1 A duy nhất mỗi hàng)

Cột là **vai trò**, không cần gắn tên cá nhân.

| Công việc (1–2 tháng tới) | Product Owner | AI Engineer | Backend & Security | UI/UX | Cố vấn tài chính | Đơn vị Open API | Giảng viên |
|---|---|---|---|---|---|---|---|
| Chốt use case và phạm vi MVP | **A**/R | C | C | C | C | I | I |
| Xây pipeline OCR/LLM đọc hóa đơn | I | **A**/R | C | I | I | I | I |
| Bảo mật và quyền riêng tư dữ liệu | C | C | **A**/R | I | I | I | I |
| Xin sandbox và kết nối Open API | **A** | I | R | I | I | C | I |
| Guardrail cho phần gợi ý tích lũy | **A** | R | C | I | C | I | I |
| Thiết kế luồng nhập và cảnh báo | C | I | C | **A**/R | I | I | I |
| Test với người dùng thật | **A**/R | C | I | C | I | I | I |
| Quyết định release bản thử nghiệm | **A** | C | C | C | C | I | I |

**Lý do chọn A cho hai hàng dễ gây tranh cãi:**
- Guardrail: A = Product Owner, R = AI Engineer. Người làm và người duyệt tách nhau để tránh tự làm tự duyệt.
- Test với người dùng thật: A/R = Product Owner, vì kết quả test quyết định phạm vi release.

> Team nhỏ thì một người có thể vừa R vừa A (ghi "A/R"). Cần ghi rõ ai đảm nhiệm mỗi vai trò, vì một người có thể kiêm nhiều vai trò.

## GATE 2 – tự kiểm tra
- [x] Pitch có kết luận, lý do, bằng chứng, small ask
- [x] Có 1 phản biện và câu trả lời
- [ ] Bằng chứng còn `[TODO]`: chưa có số liệu thật
- [ ] Bước cá nhân chưa làm
- [x] RACI: 7 hàng, mỗi hàng đúng 1 A (cần team xác nhận người nhận từng vai trò)
