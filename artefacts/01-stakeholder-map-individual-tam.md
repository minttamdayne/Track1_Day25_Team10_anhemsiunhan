
# Bản cá nhân – Stakeholder Map · Saving Tracker AI

**Người thực hiện:** Đinh Thị Minh Tâm

## 1. Danh sách stakeholder cá nhân

| # | Stakeholder | Influence | Interest | Stance sơ bộ | Căn cứ / điều cần xác minh |
|---|---|---|---|---|---|
| 1 | Giảng viên hoặc mentor trực tiếp review Saving Tracker AI | Cao | Cao | Chưa xác minh | Có thể góp ý và đánh giá định hướng dự án, nhưng chưa có feedback cụ thể được ghi nhận trong repo. |
| 2 | Nhóm 5 sinh viên có thói quen ghi chép chi tiêu hoặc thường xuyên mua sắm | Thấp | Cao (dự kiến) | Chưa xác minh | Là nhóm người dùng mục tiêu có thể kiểm chứng nhu cầu và trải nghiệm. Chưa có kết quả thử nghiệm thực tế. |
| 3 | Thành viên phụ trách phát triển AI/OCR trong team | Cao | Cao | Ủng hộ – giả định | Trực tiếp ảnh hưởng đến khả năng triển khai chức năng đọc hóa đơn, nhưng chưa xác nhận mức độ sẵn sàng và cam kết thực tế. |
| 4 | Người có chuyên môn về Product/UX có thể đánh giá luồng ghi nhận chi tiêu | Trung bình | Trung bình | Chưa xác minh | Có thể phát hiện thao tác phức tạp hoặc những điểm khiến người dùng không muốn tiếp tục sử dụng ứng dụng. |
| 5 | Chuyên gia bảo mật dữ liệu cá nhân có thể review MVP | Cao | Thấp (dự kiến) | Chưa xác minh | Dữ liệu hóa đơn có thể chứa thông tin cá nhân. Chưa có chuyên gia cụ thể được liên hệ. |
| 6 | Đơn vị cung cấp dịch vụ OCR/LLM API mà team cân nhắc sử dụng | Cao | Thấp | Chưa xác minh | Có thể ảnh hưởng đến chi phí, chất lượng trích xuất và khả năng vận hành. Chưa xác nhận nhà cung cấp hoặc điều kiện sử dụng. |
| 7 | Đơn vị cung cấp Open API/aggregator ngân hàng | Cao | Thấp | Chưa xác minh | Có thể hỗ trợ đồng bộ giao dịch ở giai đoạn mở rộng. Chưa có đối tác hay phản hồi chính thức. |

*Influence và Interest là đánh giá ban đầu theo vai trò dự kiến. Các stakeholder chưa được định danh hoặc chưa tiếp xúc cần được xác minh trước khi chốt Stakeholder Map chung.*

## 2. Stakeholder cá nhân ưu tiên

**Nhóm sinh viên có nhu cầu quản lý chi tiêu cá nhân** là stakeholder mình ưu tiên tiếp cận trước.

Theo mình, rủi ro quan trọng của Saving Tracker AI không chỉ là AI có đọc hóa đơn chính xác hay không, mà còn là liệu người dùng có thực sự muốn sử dụng ứng dụng để ghi nhận chi tiêu thường xuyên hay không.

Nếu việc chụp hóa đơn, kiểm tra thông tin và sửa lỗi mất nhiều thời gian hơn nhập thủ công, người dùng có thể không thấy giá trị của sản phẩm dù công nghệ OCR hoạt động tốt.

Vì vậy, mình đề xuất trong 1–2 tuần tới mời 5 sinh viên thuộc nhóm người dùng mục tiêu trải nghiệm luồng nhập hóa đơn. Team nên quan sát thời gian hoàn thành tác vụ, số lần phải chỉnh sửa kết quả AI và thu thập phản hồi về những thao tác gây khó khăn.

Kết quả này sẽ giúp nhóm quyết định nên ưu tiên cải thiện độ chính xác OCR, thiết kế trải nghiệm nhập liệu hay tính năng cảnh báo ngân sách.

Đây là kế hoạch kiểm chứng, chưa phải kết quả đã thực hiện.

## 3. Việc cần xác nhận trước khi gộp với nhóm

- [ ] Nhóm đã xác định rõ chân dung người dùng mục tiêu và nhu cầu quản lý chi tiêu của họ chưa?
- [ ] Đã có người dùng thực sự thử tính năng đọc hóa đơn chưa? Nếu có, cần bổ sung kết quả và bằng chứng.
- [ ] Thành viên nào đang chịu trách nhiệm chính về AI/OCR và chất lượng đầu ra?
- [ ] Team đã chọn nhà cung cấp OCR/LLM nào chưa? Cần kiểm tra chi phí, chính sách dữ liệu và giới hạn API.
- [ ] Các stakeholder được đánh giá Influence cao có thực sự tác động trực tiếp đến MVP hiện tại không?
- [ ] Mọi stance chưa được kiểm chứng phải tiếp tục ghi là "Chưa xác minh", không tự suy diễn thành "Ủng hộ" hoặc "Phản đối".
