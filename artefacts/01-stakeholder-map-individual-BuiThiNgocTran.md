# Bản cá nhân – Stakeholder Map · Saving Tracker AI

**Người thực hiện:** Bùi Thị Ngọc Trân

## 1. Danh sách stakeholder cá nhân

| # | Stakeholder | Influence | Interest | Stance sơ bộ | Căn cứ / điều cần xác minh |
|---|---|---|---|---|---|
| 1 | Giảng viên hoặc mentor phụ trách đánh giá dự án | Cao | Cao | Chưa xác minh | Có thể góp ý về phạm vi và tính khả thi của MVP; chưa có phản hồi cụ thể được ghi nhận. |
| 2 | Nhóm sinh viên thường xuyên thanh toán bằng tiền mặt và giữ hóa đơn mua hàng | Thấp | Cao (dự kiến) | Chưa xác minh | Có thể có nhu cầu giảm thao tác ghi chép chi tiêu, nhưng chưa có dữ liệu xác nhận nhu cầu. |
| 3 | Thành viên team phụ trách thiết kế giao diện và trải nghiệm người dùng | Cao | Cao | Ủng hộ – giả định | Có thể quyết định mức độ dễ sử dụng của luồng nhập hóa đơn và theo dõi ngân sách. Cần xác nhận người phụ trách thực tế. |
| 4 | Thành viên phụ trách Backend và lưu trữ dữ liệu | Cao | Cao | Ủng hộ – giả định | Chịu ảnh hưởng trực tiếp từ các yêu cầu lưu trữ giao dịch, đồng bộ dữ liệu và bảo vệ thông tin người dùng. |
| 5 | Người dùng thử quan tâm đến quyền riêng tư dữ liệu tài chính | Thấp | Cao (dự kiến) | Chưa xác minh | Có thể lo ngại khi phải cung cấp hóa đơn chứa thông tin cá nhân. Chưa có phản hồi thực tế. |
| 6 | Người có chuyên môn bảo mật hoặc pháp lý dữ liệu cá nhân | Cao | Thấp (dự kiến) | Chưa xác minh | Có thể review cách thu thập, lưu trữ và xóa dữ liệu. Chưa có người cụ thể tham gia. |
| 7 | Cố vấn tài chính cá nhân có thể đánh giá nội dung gợi ý tích lũy | Trung bình | Trung bình | Chưa xác minh | Có thể góp ý về phạm vi gợi ý tài chính và rủi ro đưa thông tin không phù hợp. Chưa liên hệ. |

*Các mức Influence, Interest và stance được xây dựng như giả thuyết để phục vụ thảo luận nhóm, không đại diện cho quan điểm đã được xác nhận của stakeholder.*

## 2. Stakeholder cá nhân ưu tiên

**Người dùng thử quan tâm đến quyền riêng tư dữ liệu tài chính** là stakeholder mình ưu tiên tìm hiểu.

Saving Tracker AI cần người dùng cung cấp hóa đơn để hệ thống nhận diện và quản lý giao dịch. Tuy nhiên, hóa đơn có thể chứa thông tin cá nhân hoặc dữ liệu mà người dùng không muốn chia sẻ.
Theo mình, nếu ứng dụng chưa giải thích rõ dữ liệu được sử dụng vào mục đích gì, lưu trữ trong bao lâu và người dùng có thể xóa dữ liệu như thế nào, họ có thể ngần ngại sử dụng ngay từ lần đầu.

Trong 1–2 tuần tới, mình đề xuất nhóm chuẩn bị một bản mô tả ngắn về cách xử lý dữ liệu và trao đổi với 5 người dùng tiềm năng. Mỗi người được xem luồng tải hóa đơn và thông tin quyền riêng tư dự kiến, sau đó chia sẻ những điểm còn lo ngại hoặc chưa hiểu rõ.

Từ phản hồi thu được, team có thể điều chỉnh giao diện xin quyền sử dụng dữ liệu, nội dung thông báo và quy trình xóa hóa đơn trước khi mở rộng thử nghiệm.

Hoạt động này mới ở mức đề xuất. Nhóm chưa có bằng chứng để khẳng định người dùng đang lo ngại hoặc tin tưởng sản phẩm.

## 3. Việc cần xác nhận trước khi gộp với nhóm

- [ ] Nhóm đã thống nhất loại dữ liệu nào cần thu thập để phục vụ chức năng đọc hóa đơn chưa?
- [ ] Hiện dữ liệu hóa đơn có được lưu trữ không? Nếu có, ai có quyền truy cập?
- [ ] Đã có quy trình xóa hoặc ẩn thông tin nhạy cảm trước khi đưa dữ liệu vào hệ thống AI chưa?
- [ ] Người dùng mục tiêu đã được hỏi về mối lo ngại đối với dữ liệu cá nhân chưa?
- [ ] Ai trong team chịu trách nhiệm cuối cùng về việc xử lý dữ liệu người dùng?
- [ ] Cần kiểm chứng stance trực tiếp thay vì mặc định rằng người dùng sẵn sàng chia sẻ hóa đơn.