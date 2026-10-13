# Trang 1 – Stakeholder Map & Strategy · Saving Tracker AI

> Nháp theo mô tả đề tài. Cột "Stance" và "Căn cứ" là giả định ban đầu, team phải sửa theo thực tế trước khi chốt. Chỗ `[TODO]` cần owner, deadline hoặc bằng chứng thật.

## 1. Danh sách stakeholder (đã gộp, loại trùng)

| # | Stakeholder cụ thể | Influence | Interest | Vùng | Stance | Căn cứ stance |
|---|---|---|---|---|---|---|
| S1 | Giảng viên lớp chấm và review bài lab | Cao | Cao | Champion | Ủng hộ | [TODO: feedback đã nhận] |
| S2 | 5–10 người dùng thử đầu tiên (bạn bè, sinh viên đi làm thêm) | Thấp | Cao | Supporter | Ủng hộ | [TODO: số người đã thử] |
| S3 | Cố vấn tài chính cá nhân (1–2 người) | Cao | Thấp (chưa thể hiện quan tâm) | Blocker | **Trung lập** | Chưa gặp. Có thể lo rủi ro "AI tư vấn đầu tư sai"; stance chưa được xác minh trực tiếp |
| S4 | Đơn vị cung cấp Open API / aggregator ngân hàng | Cao | Thấp | Blocker | **Chưa ủng hộ** | Chưa có quan hệ. Họ không có lý do ưu tiên một team sinh viên |
| S5 | Chuyên gia bảo mật / pháp lý dữ liệu cá nhân (người review) | Cao | Thấp | Blocker | Trung lập | Dữ liệu tài chính nhạy cảm, họ chỉ quan tâm khi có rủi ro |
| S6 | Thành viên team nắm AI/OCR (tech lead) | Cao | Cao | Champion | Ủng hộ | Là người build trực tiếp |
| S7 | Người dùng đại trà chưa biết sản phẩm | Thấp | Thấp | Bystander | Trung lập | Theo dõi qua thử nghiệm sau |

Quadrant được xác định theo Influence × Interest; stance được ghi riêng theo mức ủng hộ thực tế. S3 và S5 nằm ở vùng Blocker do influence cao và chưa thể hiện interest cao, dù stance hiện ghi trung lập. Stance của S1, S2 và S6 cũng cần xác minh bằng feedback hoặc trao đổi thực tế.

## 2. Ma trận

| | Interest thấp | Interest cao |
|---|---|---|
| **Influence cao** | S4 (chưa ủng hộ), S5 (trung lập), S3 (trung lập) | S1 (ủng hộ), S6 (ủng hộ) |
| **Influence thấp** | S7 (trung lập) | S2 (ủng hộ) |

## 3. Bốn stakeholder ưu tiên và chiến lược

### Ủng hộ mạnh (tận dụng)

**S1 – Giảng viên lớp**
1. *Quan tâm:* bài làm bám đúng dự án thật, phạm vi rõ, có bằng chứng và demo chạy được.
2. *Giúp / cản:* cho feedback về phạm vi MVP và chất lượng 4 artefact, đồng thời là người chấm. Có thể trừ điểm nếu phạm vi quá rộng hoặc hứa vượt bằng chứng.
3. *Hành động 1–2 tuần:* gửi demo OCR mới trước **[TODO thứ Sáu ngày …]** kèm 1 câu hỏi cụ thể: "phạm vi MVP gồm OCR + cảnh báo, hoãn phần tư vấn đầu tư, có hợp lý không?". Owner: [TODO].

**S2 – Nhóm người dùng thử đầu tiên**
1. *Quan tâm:* nhập chi tiêu nhanh, ít công, cảnh báo hữu ích.
2. *Giúp / cản:* cung cấp hóa đơn thật và feedback. Có thể bỏ nếu OCR sai nhiều hoặc họ lo lộ dữ liệu.
3. *Hành động 1–2 tuần:* mời 5 người chụp 10 hóa đơn mỗi người (có thể che thông tin nhạy cảm). Đo tỷ lệ OCR đúng và hỏi 3 câu về mức tin tưởng. Owner: [TODO]. Hạn: [TODO].

### Có rủi ro cản trở (ưu tiên thuyết phục)

**S3 – Cố vấn tài chính**
1. *Quan tâm:* khách hàng và uy tín không bị ảnh hưởng bởi lời khuyên sai từ AI. Họ cũng muốn giữ vai trò của mình.
2. *Giúp / cản:* nếu đồng ý, họ góp ý guardrail và tăng độ tin cậy. Nếu phản đối, họ có thể khiến phần tư vấn đầu tư mất tính thuyết phục.
3. *Hành động 1–2 tuần:* tìm 1–2 cố vấn qua người quen của các thành viên và xin gặp 30 phút. Mang 1 trang mô tả: AI chỉ gợi ý tích lũy mang tính tham khảo, có disclaimer, không khuyến nghị sản phẩm cụ thể. Hỏi 3 tình huống họ sẽ coi là "rủi ro đỏ". Owner: [TODO]. Hạn: [TODO].

**S4 – Đơn vị Open API / aggregator**
1. *Quan tâm:* tuân thủ, bảo mật, và đối tác có quy mô hoặc cam kết rõ.
2. *Giúp / cản:* không có API thì không đồng bộ giao dịch tự động. Họ có thể từ chối hoặc im lặng.
3. *Hành động 1–2 tuần:* tìm bản sandbox hoặc tài liệu công khai của 2 đơn vị, gửi 1 email ngắn xin sandbox cho mục đích học thuật. Song song, giữ phương án dự phòng là nhập hóa đơn thủ công, để MVP không phụ thuộc họ. Owner: [TODO]. Hạn: [TODO].

## GATE 1 – tự kiểm tra
- [x] Có 7 stakeholder và đã map Influence × Interest
- [x] Có stance sơ bộ cho từng stakeholder; một số stance cần xác minh
- [x] Có 4 hành động ưu tiên được mô tả
- [ ] Cần điền owner/deadline và xác minh stance bằng bằng chứng thật
