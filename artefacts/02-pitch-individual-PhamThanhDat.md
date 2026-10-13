# Bản cá nhân – Pitch Phase 2 · Saving Tracker AI

**Người thực hiện:** Phạm Thành Đạt (AI Engineer)

## Pitch gửi nhóm người dùng thử đầu tiên

**Kết luận / Đề xuất:** Mình muốn mời bạn thử luồng chụp hóa đơn của Saving Tracker AI để kiểm chứng liệu trích xuất tự động có giúp ghi nhận chi tiêu nhanh hơn nhập tay hay không. Mục tiêu hiện tại không phải chứng minh AI đã chính xác, mà là đo lỗi thực tế để team biết cần sửa gì trước.

**Lý do:** Là người phụ trách pipeline OCR/LLM, mình thấy rủi ro lớn nhất là AI đọc sai tên cửa hàng, ngày hoặc tổng tiền mà người dùng không phát hiện kịp. Nếu mỗi hóa đơn đều phải kiểm tra và sửa nhiều trường, thời gian tiết kiệm được sẽ mất. Chỉ có thử nghiệm với hóa đơn thật (đã che thông tin nhạy cảm) mới cho biết mức lỗi này có chấp nhận được không.

**Bằng chứng:** Repo hiện mới mô tả định hướng dùng OCR/LLM để đọc hóa đơn và phân loại chi tiêu. Chưa có bộ eval chuẩn, chưa có số liệu accuracy theo trường, chưa có so sánh thời gian nhập tự động với nhập thủ công. Vì vậy mình chưa khẳng định sản phẩm tốt hơn cách làm hiện tại — đây là giả thuyết cần đo.

**Small ask:** Khi bản thử nghiệm sẵn sàng, bạn có thể dành khoảng 15 phút nhập tối đa 3 hóa đơn mẫu đã che thông tin nhạy cảm, cho phép sửa trước khi lưu, rồi cho biết trường nào sai nhiều nhất và bạn có muốn dùng tiếp không? Mình sẽ ghi thời gian thao tác, số trường phải sửa và 3 lỗi phổ biến nhất để đưa vào backlog eval trước 27/10/2026.

## Tự kiểm tra trước khi chia sẻ

- [x] Nêu đề xuất ngay từ đầu.
- [x] Có lý do gắn với vai trò AI Engineer và rủi ro lỗi OCR.
- [x] Phân biệt giả thuyết với bằng chứng; không bịa số liệu accuracy.
- [x] Small ask cụ thể về thời lượng, nhiệm vụ và output đo được.
- [ ] Chờ bộ 30 hóa đơn chuẩn và baseline eval hoàn thành.
- [ ] Bổ sung kết quả đo thực tế sau khi chạy eval và user testing.
