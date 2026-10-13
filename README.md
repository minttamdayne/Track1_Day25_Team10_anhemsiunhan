# Team10 – anhemsiunhan · AI Team Lab (Track 1)

### Phase 0 — Chốt phạm vi & cách làm

**Thời gian:** 5 phút  
**Hình thức:** Team  
**Dự án:** Saving Tracker AI

---
### 1. Thành viên nhóm

| STT | Họ và tên |
|-----|-----------|
| 1 | Đinh Thị Minh Tâm |
| 2 | Bùi Thị Ngọc Trân |
| 3 | Phạm Thành Đạt |
| 4 | Nguyễn Khánh Linh |
| 5 | Ngô Lê Thuỷ Tiên |

**Quy mô nhóm:** 5 thành viên.

### 2. Tên dự án

**Saving Tracker AI — Ứng dụng quản lý chi tiêu cá nhân tích hợp trí tuệ nhân tạo.**

Saving Tracker AI là ứng dụng hỗ trợ người dùng theo dõi, phân loại và quản lý chi tiêu cá nhân. Dự án ứng dụng công nghệ OCR kết hợp LLM để nhận diện thông tin từ hóa đơn, giảm thao tác nhập liệu thủ công, đồng thời hỗ trợ tổng hợp chi tiêu, theo dõi ngân sách và đưa ra cảnh báo phù hợp.

### 3. Mục tiêu hiện tại (1–3 tháng)

Trong 1–3 tháng tới, nhóm tập trung phát triển và kiểm chứng MVP (Minimum Viable Product) của Saving Tracker AI, với các mục tiêu:

1. **Hoàn thiện MVP:** Xây dựng các tính năng cốt lõi gồm nhập hóa đơn, trích xuất dữ liệu bằng OCR/LLM, phân loại giao dịch và theo dõi chi tiêu.
2. **Đánh giá chất lượng AI:** Xây dựng bộ dữ liệu kiểm thử để đo độ chính xác trong việc nhận diện thông tin hóa đơn và phân loại khoản chi.
3. **Kiểm chứng trải nghiệm người dùng:** Tổ chức thử nghiệm với nhóm người dùng mục tiêu, ghi nhận phản hồi về tính dễ sử dụng, độ tin cậy và giá trị thực tế.
4. **Cải thiện sản phẩm:** Dựa trên kết quả kiểm thử để ưu tiên sửa lỗi, tối ưu trải nghiệm và nâng cao tính ổn định của MVP.

**Kết quả kỳ vọng:** Có một MVP hoạt động được, có kết quả đánh giá chất lượng AI và phản hồi thực tế từ người dùng để làm cơ sở cho giai đoạn phát triển tiếp theo.

### 4. Trưởng nhóm / Người tổng hợp

- **Trưởng nhóm:** Đinh Thị Minh Tâm
- **Người quản lý repository:** Đinh Thị Minh Tâm
- **Trách nhiệm:**
  - Quản lý repository GitHub chung của nhóm.
  - Phân công và theo dõi tiến độ thực hiện các phase.
  - Tổng hợp, rà soát và cập nhật đầy đủ 4 artefact.
  - Kiểm tra tính nhất quán giữa các artefact.
  - Đảm bảo README.md và PDF cuối cùng đáp ứng yêu cầu nộp bài.

### 5. Format làm bài

- **Định dạng làm việc:** Google Docs.
- **Quản lý phiên bản:** GitHub.
- **Định dạng nộp cuối:** PDF tối đa 4 trang.

**Repository:**
https://github.com/minttamdayne/Track1_Day25_Team10_anhemsiunhan

### 6. Các artefact cần hoàn thành

| Phase | Artefact |
|-------|----------|
| Phase 1 | Stakeholder Map & Strategy |
| Phase 2 | Pitch & RACI Matrix |
| Phase 3 | AI Team Design & Priority Resourcing |
| Phase 4 | Team Health & Growth Plan 30 ngày |

### 7. Nguyên tắc thực hiện

- Sử dụng chính dự án Saving Tracker AI.
- Những phần cá nhân phải được thực hiện độc lập trước khi tổng hợp.
- Các quyết định của team cần dựa trên thông tin và bằng chứng thực tế.
- Không tự tạo dữ liệu phỏng vấn, kết quả kiểm thử hoặc điểm Team Health.
- Mỗi công việc trong RACI có đúng một Accountable.
- Mỗi hành động trong Growth Plan có owner, deadline và tiêu chí hoàn thành cụ thể.

**Demo:** 

### 8. Tóm tắt kết quả Phase 1–4

#### Stakeholder Map & Strategy

Nhóm xác định 7 stakeholder theo ma trận Influence × Interest và dùng đúng nhãn theo vùng:

| Vùng | Stakeholder chính | Cách tiếp cận |
|---|---|---|
| Champion | S1 Mentor; S6 AI/OCR lead | Cập nhật tiến độ, xin phản hồi và xác nhận vai trò |
| Supporter | S2 Nhóm 5 người dùng thử | Mời thử nghiệm, đo thời gian và số lần chỉnh sửa |
| Blocker | S3 Cố vấn tài chính; S4 Open API; S5 Bảo mật/pháp lý | Làm rõ điều kiện, giảm rủi ro phụ thuộc và review dữ liệu |
| Bystander | S7 Người dùng chưa tiếp cận | Theo dõi và tiếp cận khi MVP sẵn sàng |

Bốn stakeholder ưu tiên có owner, deadline và kết quả mong đợi trong [Stakeholder Map](artefacts/01-stakeholder-map.md). Các stance và kết quả thử nghiệm chưa có bằng chứng được ghi rõ là chưa xác minh.

#### Pitch & RACI

Kết luận của pitch là mời 5 sinh viên thử Saving Tracker AI trong 15 phút với tối đa 3 hóa đơn mẫu đã che thông tin nhạy cảm. Nhóm đo thời gian thao tác, số lỗi cần sửa và 3 vấn đề ưu tiên. Phản biện chính là OCR có thể sai và khiến người dùng mất nhiều thời gian hơn nhập thủ công; cách xử lý là xây bộ eval, cho phép sửa trước khi lưu và so sánh hai cách nhập.

RACI gồm 6 công việc và mỗi công việc có đúng một Accountable. Vai trò được gắn với thành viên: Tâm (Product Owner), Đạt (AI Engineer), Linh (Backend), Trân (UI/UX), Tiên (Security/QA). Chi tiết xem [Pitch & RACI](artefacts/02-pitch-raci.md).

#### AI Team Design & Priority Resourcing

- **Architecture:** Embedded, phù hợp với team nhỏ đang làm MVP.
- **Core roles:** Product Owner, AI Engineer, Backend & Security, UI/UX.
- **Capability gaps:** chuyên môn tài chính, kết nối Open API, AI Evals và review bảo mật độc lập.
- **Resourcing:** Partner với cố vấn tài chính và aggregator; Develop bộ eval trong team; Outsource review bảo mật một lần. Chưa chọn Hire vì MVP chưa cần nhân sự cố định.

Chi tiết xem [AI Team Design](artefacts/03-ai-team-design.md).

#### Team Health & Growth Plan

| Khía cạnh | Điểm TB |
|---|---:|
| Chất lượng AI | 2.6/5 |
| Tiến độ | 3.0/5 |
| Tinh thần team | 4.4/5 |
| Tốc độ ra sản phẩm | 2.6/5 |

Vấn đề ưu tiên là thiếu quy trình đánh giá AI và tích hợp kết quả vào chu kỳ MVP. Năng lực cần nâng là AI Evals/Quality Evaluation, owner là Phạm Thành Đạt.

Ba hành động trong 30 ngày:

1. Đạt xây 30 hóa đơn chuẩn và baseline eval trước 27/10/2026.
2. Tâm phối hợp Linh chia MVP thành task nhỏ, theo dõi GitHub và có ít nhất 2 review trước 03/11/2026.
3. Trân phối hợp Tâm thử nghiệm với 5 người dùng và tổng hợp 3 vấn đề ưu tiên trước 12/11/2026.

Chi tiết xem [Team Health & Growth Plan](artefacts/04-team-health-growth-plan.md).

### 9. Consistency Check & Gate 5

- S2, S4 và S5 trong Stakeholder Map xuất hiện trong Pitch/RACI và kế hoạch resourcing.
- Capability gap AI Evals ở Phase 3 liên quan trực tiếp đến điểm Chất lượng AI 2.6/5 ở Phase 4.
- Owner Growth Plan khớp với vai trò trong RACI.
- Repository có README.md, 4 artefact team, artefact cá nhân và PDF tối đa 4 trang.
- Các nội dung chưa có dữ liệu thật không được trình bày như kết quả đã đạt.

## Artefact (đóng gói thành PDF ≤ 4 trang)
1. [Stakeholder Map](artefacts/01-stakeholder-map.md)
2. [Pitch & RACI](artefacts/02-pitch-raci.md)
3. [AI Team Design](artefacts/03-ai-team-design.md)
4. [Team Health & Growth Plan](artefacts/04-team-health-growth-plan.md)

**Bản cá nhân**

| Thành viên | Stakeholder Map | Pitch |
|---|---|---|
| Tâm | [01](artefacts/01-stakeholder-map-individual-linh.md) | [02](artefacts/02-pitch-individual-linh.md) |
| Trân | [01](artefacts/01-stakeholder-map-individual-BuiThiNgocTran.md) | [02](artefacts/02-pitch-individual-BuiThiNgocTran.md) |
| Đạt | [01](artefacts/01-stakeholder-map-individual-PhamThanhDat.md) | [02](artefacts/02-pitch-individual-PhamThanhDat.md) |
| Linh | [01](artefacts/01-stakeholder-map-individual-tam.md) | [02](artefacts/02-pitch-individual-tam.md) |
| Tiên | [01](artefacts/01-stakeholder-map-individual-tien.md) | [02](artefacts/02-pitch-individual-tien.md) |

PDF nộp: [Day25_AI-Team-Lab_Team10.pdf](output/pdf/Day25_AI-Team-Lab_Team10.pdf) (bản chính thức, tối đa 4 trang).
