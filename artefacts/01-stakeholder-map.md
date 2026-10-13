
# Phase 1 — Stakeholder Map & Strategy

**Team:** Team 10 – anhemsiunhan  
**Dự án:** Saving Tracker AI  
**Hình thức:** Cá nhân → Team  
**Thời gian:** 20 phút

> Bản tổng hợp dựa trên phân tích cá nhân của các thành viên. Influence và Interest được đánh giá sơ bộ theo phạm vi MVP. Stance chưa có bằng chứng sẽ được ghi là "Chưa xác minh", không mặc định stakeholder ủng hộ hoặc phản đối dự án.

## 1. Danh sách Stakeholder tổng hợp

| ID | Stakeholder cụ thể | Influence | Interest | Vùng | Stance | Căn cứ / Điều cần xác minh |
|---|---|---|---|---|---|---|
| S1 | Giảng viên/mentor trực tiếp hướng dẫn và review dự án | Cao | Cao | Champion | Chưa xác minh | Có ảnh hưởng đến định hướng và đánh giá dự án; chưa ghi nhận feedback cụ thể. |
| S2 | Nhóm 5 sinh viên dự kiến thử nghiệm Saving Tracker AI | Thấp | Cao (dự kiến) | Supporter | Chưa xác minh | Là nhóm có thể cung cấp feedback về tính hữu ích và trải nghiệm; chưa có kết quả thử nghiệm. |
| S3 | Cố vấn tài chính cá nhân có thể tham vấn | Cao* | Thấp | Blocker | Chưa xác minh | Có thể đánh giá giới hạn an toàn của gợi ý tài chính; chưa liên hệ. |
| S4 | Đơn vị cung cấp Open API/aggregator ngân hàng | Cao* | Thấp | Blocker | Chưa xác minh | Có thể ảnh hưởng đến khả năng đồng bộ giao dịch trong tương lai; chưa xác nhận đối tác. |
| S5 | Chuyên gia bảo mật/pháp lý dữ liệu cá nhân có thể review MVP | Cao | Thấp | Blocker | Chưa xác minh | Có thể phát hiện rủi ro xử lý dữ liệu hóa đơn; chưa có người review cụ thể. |
| S6 | Thành viên phụ trách phát triển AI/OCR của team | Cao | Cao | Champion | Ủng hộ – giả định | Có vai trò trực tiếp trong phát triển tính năng AI; cần xác nhận người phụ trách và cam kết. |
| S7 | Người dùng tiềm năng chưa tiếp cận sản phẩm | Thấp | Thấp | Bystander | Chưa xác minh | Chưa có tương tác với dự án; sẽ tiếp cận trong các vòng thử nghiệm sau. |

*Influence của S3 và S4 phụ thuộc phạm vi sản phẩm. Nếu MVP chỉ tập trung đọc hóa đơn và theo dõi chi tiêu, mức ảnh hưởng trực tiếp của hai stakeholder này có thể thấp hơn.*

**Nguyên tắc phân loại:**

- **Influence:** Khả năng tác động đến tiến độ, chất lượng hoặc quyết định quan trọng của dự án.
- **Interest:** Mức độ quan tâm đến việc phát triển và kết quả của dự án.
- **Stance:** Thái độ ủng hộ thực tế, cần được kiểm chứng bằng trao đổi, phản hồi hoặc hành động.

Champion, Blocker, Supporter và Bystander chỉ là nhãn của các vùng Influence × Interest, không đại diện cho thái độ thực tế.

## 2. Stakeholder Matrix

| Influence / Interest | Interest thấp | Interest cao |
|---|---|---|
| **Influence cao** | S3 – Cố vấn tài chính; S4 – Đối tác Open API; S5 – Chuyên gia bảo mật | S1 – Giảng viên/mentor; S6 – AI/OCR Lead |
| **Influence thấp** | S7 – Người dùng tiềm năng chưa tiếp cận | S2 – Nhóm người dùng thử |

### Chiến lược theo từng vùng

| Vùng | Cách tiếp cận |
|---|---|
| Champion | Làm việc chặt chẽ, cập nhật tiến độ và chủ động xin phản hồi. |
| Blocker | Xác định điều kiện hợp tác, giải quyết mối lo và giảm rủi ro phụ thuộc. |
| Supporter | Khuyến khích trải nghiệm, ghi nhận phản hồi và cải thiện sản phẩm. |
| Bystander | Theo dõi nhu cầu và tiếp cận khi sản phẩm sẵn sàng mở rộng. |

## 3. Bốn Stakeholder ưu tiên & chiến lược

Nhóm lựa chọn 2 stakeholder có tiềm năng hỗ trợ trực tiếp và 2 stakeholder cần chủ động xử lý rủi ro.

Việc lựa chọn dựa trên mức độ ảnh hưởng dự kiến, chưa phải kết luận rằng các bên đã ủng hộ hoặc phản đối.

### A. Nhóm có tiềm năng hỗ trợ mạnh

#### S1 — Giảng viên/Mentor

**1. Họ quan tâm điều gì?**

- Dự án giải quyết một vấn đề thực tế.
- Phạm vi MVP rõ ràng và khả thi.
- Có sản phẩm minh họa và bằng chứng kiểm chứng.

**2. Họ có thể giúp hoặc cản trở dự án thế nào?**

Giảng viên/mentor có thể góp ý về phạm vi sản phẩm, phương pháp kiểm chứng và các rủi ro team chưa nhận ra. Nếu team không chứng minh được tính khả thi hoặc đưa ra cam kết vượt quá bằng chứng, dự án có thể bị yêu cầu điều chỉnh.

**3. Hành động trong 1–2 tuần tới**

- Chuẩn bị bản mô tả MVP và demo OCR hiện có (nếu đã sẵn sàng).
- Gửi mentor để xin phản hồi về phạm vi sản phẩm.
- Đặt câu hỏi cụ thể: "Ở giai đoạn MVP, nhóm nên tập trung đọc hóa đơn và cảnh báo ngân sách, đồng thời hoãn tính năng tư vấn đầu tư, có phù hợp không?"

**Owner:** Đinh Thị Minh Tâm (Product Owner)  
**Deadline đề xuất:** 20/10/2026  
**Kết quả mong đợi:** Có phản hồi được ghi nhận và quyết định điều chỉnh phạm vi MVP.

#### S2 — Nhóm người dùng thử đầu tiên

**1. Họ quan tâm điều gì?**

- Ghi chép chi tiêu nhanh và thuận tiện.
- Hạn chế nhập liệu thủ công.
- Kết quả trích xuất hóa đơn chính xác.
- Thông tin cá nhân được bảo vệ.

**2. Họ có thể giúp hoặc cản trở dự án thế nào?**

Người dùng thử giúp team kiểm chứng nhu cầu thực tế và phát hiện vấn đề trải nghiệm. Nếu OCR thường xuyên sai hoặc thao tác quá phức tạp, họ có thể không tiếp tục sử dụng sản phẩm.

**3. Hành động trong 1–2 tuần tới**

- Mời 5 sinh viên thuộc nhóm người dùng mục tiêu tham gia thử nghiệm.
- Dự kiến mỗi người thử tối đa 10 hóa đơn đã che thông tin nhạy cảm.
- Quan sát thời gian nhập hóa đơn và số trường thông tin cần chỉnh sửa.
- Thu thập phản hồi về tính dễ sử dụng, độ tin cậy và giá trị sản phẩm.

**Owner:** Bùi Thị Ngọc Trân (UI/UX), phối hợp Đinh Thị Minh Tâm  
**Deadline đề xuất:** 27/10/2026  
**Kết quả mong đợi:** Báo cáo thử nghiệm, danh sách lỗi và 3 vấn đề ưu tiên cải thiện.

### B. Nhóm có rủi ro cản trở cần xử lý

#### S5 — Chuyên gia bảo mật/pháp lý dữ liệu

**1. Họ quan tâm điều gì?**

- Cách thu thập và xử lý dữ liệu hóa đơn.
- Khả năng kiểm soát truy cập và xóa dữ liệu.
- Việc bảo vệ thông tin người dùng.

**2. Họ có thể giúp hoặc cản trở dự án thế nào?**

Chuyên gia có thể giúp phát hiện lỗ hổng trong thiết kế xử lý dữ liệu. Nếu phát hiện rủi ro nghiêm trọng, team cần điều chỉnh trước khi triển khai thử nghiệm với dữ liệu cá nhân thật.

Hiện chưa có bằng chứng cho thấy chuyên gia phản đối dự án.

**3. Hành động trong 1–2 tuần tới**

- Xây dựng sơ đồ luồng dữ liệu từ khi tải hóa đơn đến khi lưu giao dịch.
- Xác định thông tin cần lưu, thời hạn lưu và quyền truy cập.
- Tìm một người có chuyên môn phù hợp để xin review.
- Tổng hợp các rủi ro và phương án xử lý.

**Owner:** Nguyễn Khánh Linh (Backend), phối hợp Ngô Lê Thuỷ Tiên (Security/QA)  
**Deadline đề xuất:** 27/10/2026  
**Kết quả mong đợi:** Checklist bảo mật và danh sách rủi ro cần khắc phục.

#### S4 — Đơn vị cung cấp Open API/Aggregator

**1. Họ quan tâm điều gì?**

- Mục đích và phạm vi sử dụng API.
- Điều kiện bảo mật và tuân thủ.
- Khả năng đáp ứng yêu cầu kỹ thuật của đối tác.

**2. Họ có thể giúp hoặc cản trở dự án thế nào?**

Đối tác API có thể hỗ trợ đồng bộ giao dịch, giảm phụ thuộc vào nhập liệu thủ công. Tuy nhiên, yêu cầu tích hợp, chi phí hoặc hạn chế quyền truy cập có thể khiến quá trình phát triển kéo dài.

Đây là rủi ro phụ thuộc đối tác, không phải bằng chứng họ phản đối dự án.

**3. Hành động trong 1–2 tuần tới**

- Tìm hiểu tài liệu kỹ thuật và điều kiện sandbox của 2 nhà cung cấp tiềm năng.
- Đánh giá chi phí, bảo mật và khả năng tích hợp.
- Liên hệ xin thông tin sandbox nếu có kênh phù hợp.
- Giữ phương án dự phòng: nhập hóa đơn và giao dịch thủ công cho MVP.

**Owner:** Đinh Thị Minh Tâm (Product Owner), phối hợp Nguyễn Khánh Linh (Backend)  
**Deadline đề xuất:** 27/10/2026  
**Kết quả mong đợi:** Bảng đánh giá 2 lựa chọn API và quyết định có cần tích hợp trong giai đoạn hiện tại hay không.

## 4. Thông tin cần xác minh trước khi chốt

| Nội dung cần xác minh | Hành động tiếp theo |
|---|---|
| Stance của giảng viên/mentor | Thu thập phản hồi thực tế |
| Stance của nhóm người dùng thử | Mời tham gia và ghi nhận mức độ sẵn sàng |
| Vai trò AI/OCR Lead | Xác nhận thành viên phụ trách |
| Chuyên gia bảo mật | Xác định người có thể review |
| Đối tác Open API | Kiểm tra nhu cầu tích hợp và khả năng tiếp cận |
| Owner của 4 chiến lược | Phân công tên thành viên cụ thể |

## 5. Gate 1 — Tự kiểm tra

- [x] Có ít nhất 6 stakeholder cụ thể hoặc nhóm stakeholder được xác định.
- [x] Đã đánh giá Influence × Interest.
- [x] Đã xây dựng Stakeholder Matrix.
- [x] Đã ghi stance sơ bộ và phân biệt với quadrant.
- [x] Đã chọn 4 stakeholder ưu tiên.
- [x] Mỗi stakeholder có mối quan tâm, tác động và hành động cụ thể.
- [x] Có owner theo vai trò và deadline đề xuất.
- [ ] Xác nhận owner bằng tên thành viên.
- [ ] Xác minh stance bằng phản hồi thực tế.
- [ ] Xác nhận đủ 2 stakeholder đang ủng hộ mạnh.

**Trạng thái:** Hoàn thiện theo bằng chứng hiện có; stance và kết quả thử nghiệm vẫn được ghi rõ là chưa xác minh/chưa thực hiện.
