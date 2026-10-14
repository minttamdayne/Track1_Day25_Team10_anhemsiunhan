
# Phase 2 — Pitch & RACI Matrix

**Team:** Team 10 – anhemsiunhan  
**Dự án:** Saving Tracker AI  
**Thời gian:** 30 phút  
**Hình thức:** Team → Cá nhân → Team

> Các thông tin chưa được kiểm chứng được ghi rõ là giả định. RACI đã gắn với thành viên thực tế của team.

## 1. Team — Pitch theo Conclusion First

**Stakeholder được chọn:** S2 – Nhóm sinh viên dự kiến dùng thử Saving Tracker AI.

### Kết luận / Đề xuất

Team muốn mời 5 sinh viên trải nghiệm Saving Tracker AI để kiểm chứng liệu việc chụp hóa đơn và tự động ghi nhận giao dịch có giúp theo dõi chi tiêu thuận tiện hơn nhập liệu thủ công hay không.

### Lý do

1. **Giảm công sức ghi chép:** Việc nhập từng giao dịch có thể khiến người dùng khó duy trì thói quen theo dõi chi tiêu. OCR/LLM được kỳ vọng giúp giảm thao tác này.

2. **Kiểm chứng chất lượng AI:** Nếu hệ thống đọc sai hóa đơn và người dùng phải chỉnh sửa nhiều, lợi ích tự động hóa có thể không còn rõ ràng.

3. **Phát triển đúng nhu cầu:** Phản hồi thực tế sẽ giúp team ưu tiên các chức năng mang lại giá trị thay vì mở rộng tính năng theo giả định.

### Bằng chứng hiện có

Repository đã mô tả định hướng ứng dụng OCR/LLM để đọc hóa đơn, ghi nhận giao dịch và cảnh báo chi tiêu.

Tuy nhiên, hiện chưa có số liệu được xác nhận về độ chính xác OCR, thời gian tiết kiệm hoặc mức độ hài lòng của người dùng. Do đó, nhóm chưa khẳng định sản phẩm tốt hơn cách nhập thủ công.

### Small ask

Khi phiên bản thử nghiệm sẵn sàng, bạn có thể dành 15 phút thực hiện thao tác nhập tối đa 3 hóa đơn mẫu đã che thông tin nhạy cảm và chia sẻ những bước gây khó khăn không?

Team sẽ ghi nhận thời gian thao tác, số lỗi cần sửa và phản hồi để xác định 3 vấn đề ưu tiên cải thiện.

## 2. Team — Phản biện & cách xử lý

**Phản biện:**

"AI đọc hóa đơn chưa chắc chính xác. Nếu phải kiểm tra và sửa lại nhiều lần thì dùng ứng dụng có thể còn mất thời gian hơn nhập thủ công."

**Cách phản hồi:**

Đây là giả thuyết nhóm cần kiểm chứng, không phải vấn đề có thể giải quyết chỉ bằng việc cam kết AI sẽ chính xác.

Nhóm đề xuất:

1. Chuẩn bị bộ hóa đơn mẫu có đáp án chuẩn.
2. Đo độ chính xác của các trường: ngày giao dịch, tên cửa hàng và tổng tiền.
3. Cho người dùng kiểm tra và chỉnh sửa thông tin trước khi lưu.
4. So sánh thời gian hoàn thành tác vụ với cách nhập thủ công.

Nếu kết quả OCR chưa đủ tốt, nhóm sẽ ưu tiên cải thiện trích xuất và trải nghiệm chỉnh sửa trước khi mở rộng tính năng.

## 3. Cá nhân — Viết lại Pitch

Mỗi thành viên tự viết lại thông điệp theo cấu trúc Conclusion First → Lý do → Evidence → Small ask.

| Thành viên | Góc nhìn cá nhân | Nội dung |
|---|---|---|
| Đinh Thị Minh Tâm | Product & User Validation | Kiểm chứng liệu OCR có thực sự giúp người dùng ghi nhận chi tiêu thuận tiện hơn. |
| Bùi Thị Ngọc Trân | Trust & Privacy | Minh bạch việc xử lý dữ liệu để người dùng có cơ sở quyết định tham gia thử nghiệm. |
| Nguyễn Khánh Linh | Financial Safety | Giới hạn gợi ý tích lũy và xác định các trường hợp AI không nên đưa ra khuyến nghị. |
| Ngô Lê Thuỷ Tiên | Data Security | Xin review cách lưu trữ, bảo vệ và xóa dữ liệu hóa đơn. |
| Phạm Thành Đạt | AI Evals & OCR quality | Kiểm chứng lỗi trích xuất bằng bộ eval và user testing trước khi khẳng định lợi ích. |

**Thông điệp tổng hợp đề xuất:**

Saving Tracker AI hướng đến việc giảm thao tác ghi nhận chi tiêu bằng công nghệ đọc hóa đơn. Trong giai đoạn MVP, nhóm ưu tiên kiểm chứng tính hữu ích, độ chính xác và sự tin tưởng của người dùng trước khi phát triển các tính năng tài chính nâng cao.

> Các bản Pitch cá nhân cần được lưu riêng để chứng minh quá trình Team → Cá nhân → Team. Thành viên xác nhận nội dung của mình trước khi nhóm sử dụng làm bản chính thức.

## 4. Team — RACI Matrix

### 4.1. Quy ước

- **R (Responsible):** Người trực tiếp thực hiện.
- **A (Accountable):** Người chịu trách nhiệm cuối cùng.
- **C (Consulted):** Người được tham vấn.
- **I (Informed):** Người được cập nhật.
- **A/R:** Một vai trò vừa thực hiện vừa chịu trách nhiệm.

### 4.2. RACI cho 6 công việc quan trọng

| Công việc | Product Owner | AI Engineer | Backend & Security | UI/UX | Mentor |
|---|---|---|---|---|---|
| Chốt phạm vi và yêu cầu MVP | **A/R** | C | C | C | I |
| Chuẩn bị dữ liệu và xây pipeline OCR/LLM | C | **A/R** | C | I | I |
| Thiết kế và triển khai bảo mật dữ liệu | C | C | **A/R** | C | I |
| Xây dựng giao diện nhập và theo dõi chi tiêu | C | C | C | **A/R** | I |
| Đánh giá độ chính xác OCR và xử lý lỗi | **A** | R | C | C | I |
| Tổ chức user testing và quyết định pilot | **A** | C | C | R | I |

### 4.3. Giải thích phân quyền

**Product Owner** chịu trách nhiệm cuối cùng về phạm vi MVP, tiêu chí đánh giá và quyết định pilot. Vai trò này bảo đảm team ưu tiên giải quyết nhu cầu người dùng.

**AI Engineer** trực tiếp phát triển OCR/LLM và đo chất lượng trích xuất. Với hoạt động đánh giá OCR, Product Owner là Accountable để kết quả kỹ thuật được xem xét cùng tiêu chí sử dụng thực tế.

**Backend & Security** chịu trách nhiệm về xử lý và lưu trữ dữ liệu, quyền truy cập và các biện pháp bảo vệ thông tin.

**UI/UX** chịu trách nhiệm thiết kế luồng nhập liệu và trực tiếp tổ chức user testing, giúp team quan sát hành vi thay vì chỉ dựa vào ý kiến người dùng.

**Mentor** được cập nhật tiến độ và tham vấn khi nhóm cần đánh giá lại phạm vi hoặc phương pháp thực hiện.

### 4.4. Phân công người đảm nhiệm vai trò

| Thành viên | Vai trò chính | Vai trò kiêm nhiệm |
|---|---|---|
| Đinh Thị Minh Tâm | Product Owner / Project Manager | Stakeholder Management, User Research |
| Bùi Thị Ngọc Trân | UI/UX Designer | User Testing, Privacy UX |
| Phạm Thành Đạt | AI Engineer | OCR/LLM Evaluation, Data Preparation |
| Nguyễn Khánh Linh | Backend Developer | API Integration, Database Management |
| Ngô Lê Thuỷ Tiên | Security & Quality Assurance | Data Privacy, Software Testing |

**Trách nhiệm chính:**

- **Đinh Thị Minh Tâm:** Xác định phạm vi MVP, quản lý tiến độ, điều phối nhóm, làm việc với stakeholder và chịu trách nhiệm về quyết định phát triển sản phẩm.
- **Bùi Thị Ngọc Trân:** Thiết kế giao diện, tối ưu trải nghiệm nhập hóa đơn, tổ chức kiểm thử người dùng và ghi nhận phản hồi.
- **Phạm Thành Đạt:** Phát triển pipeline OCR/LLM, chuẩn bị dữ liệu kiểm thử và đánh giá chất lượng trích xuất thông tin.
- **Nguyễn Khánh Linh:** Phát triển backend, thiết kế cơ sở dữ liệu và tích hợp API giữa AI với ứng dụng.
- **Ngô Lê Thuỷ Tiên:** Kiểm tra chất lượng phần mềm, đánh giá rủi ro bảo mật và phối hợp xây dựng quy trình bảo vệ dữ liệu cá nhân.

## 5. GATE 2 — Tự kiểm tra

- [x] Pitch trình bày kết luận trước.
- [x] Có 3 lý do gắn với nhu cầu và giá trị sản phẩm.
- [x] Phân biệt bằng chứng hiện có với giả định.
- [x] Small ask cụ thể, có thời lượng và kết quả mong muốn.
- [x] Có 1 phản biện chính và hành động giảm rủi ro.
- [x] Có RACI cho 6 công việc.
- [x] Mỗi công việc có đúng 1 Accountable.
- [x] Xác nhận bản Pitch cá nhân của từng thành viên (đủ 5/5 thành viên: Tâm, Trân, Đạt, Linh, Tiên).
- [x] Bổ sung Pitch cá nhân của Phạm Thành Đạt (xem artefacts/02-pitch-individual-PhamThanhDat.md).
- [x] Gắn tên thành viên thực tế vào RACI.
- [x] Đã thiết lập kế hoạch đo lường kết quả OCR/user testing trong 30 ngày.

**Trạng thái:** Hoàn thiện theo bằng chứng hiện có; các giả định kỹ thuật đã có kế hoạch đo lường thực nghiệm cụ thể.
