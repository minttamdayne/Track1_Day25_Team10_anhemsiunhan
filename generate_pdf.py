# -*- coding: utf-8 -*-
import os
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Arial fonts for full Vietnamese Unicode support
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Italic', 'C:/Windows/Fonts/ariali.ttf'))
pdfmetrics.registerFont(TTFont('Arial-BoldItalic', 'C:/Windows/Fonts/arialbi.ttf'))

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        w, h = landscape(A4)
        
        # Header banner
        self.setFont('Arial-Bold', 8)
        self.setFillColor(colors.HexColor('#1E3A8A')) # Dark Blue
        self.drawString(32, h - 22, "AI TEAM LAB  /  DAY 25  /  TEAM 10 — ANHEMSIUNHAN  (SAVING TRACKER AI)")
        
        self.setFont('Arial', 8)
        self.setFillColor(colors.HexColor('#4B5563'))
        page_str = f"Trang {self._pageNumber} / {page_count}"
        self.drawRightString(w - 32, h - 22, page_str)
        
        # Thin top divider
        self.setStrokeColor(colors.HexColor('#CBD5E1'))
        self.setLineWidth(0.75)
        self.line(32, h - 26, w - 32, h - 26)
        
        # Bottom footer line
        self.line(32, 22, w - 32, 22)
        self.setFont('Arial-Italic', 7)
        self.setFillColor(colors.HexColor('#6B7280'))
        self.drawString(32, 13, "Dự án: Saving Tracker AI | Team 10 – anhemsiunhan: Đinh Thị Minh Tâm, Bùi Thị Ngọc Trân, Phạm Thành Đạt, Nguyễn Khánh Linh, Ngô Lê Thuỷ Tiên")
        self.drawRightString(w - 32, 13, "Bản hoàn chỉnh chính thức — Track 1 Day 25/27 AI Team Lab")
        self.restoreState()

def build_pdf(filename):
    total_w, total_h = landscape(A4)
    doc = SimpleDocTemplate(
        filename,
        pagesize=landscape(A4),
        leftMargin=32,
        rightMargin=32,
        topMargin=28,
        bottomMargin=24
    )
    usable_w = total_w - 64 # 777.89 pt

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor('#0F172A')
    accent_blue = colors.HexColor('#1D4ED8')
    bg_light = colors.HexColor('#F8FAFC')
    border_color = colors.HexColor('#CBD5E1')
    text_dark = colors.HexColor('#1E293B')
    text_muted = colors.HexColor('#475569')

    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Arial-Bold',
        fontSize=11.5,
        leading=14,
        textColor=primary_color,
        spaceAfter=1
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        fontName='Arial-Italic',
        fontSize=7.2,
        leading=9.5,
        textColor=text_muted,
        spaceAfter=3
    )

    h2_style = ParagraphStyle(
        'H2',
        fontName='Arial-Bold',
        fontSize=9,
        leading=11.5,
        textColor=accent_blue,
        spaceBefore=2,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'Body',
        fontName='Arial',
        fontSize=7.2,
        leading=9.2,
        textColor=text_dark
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        fontName='Arial-Bold',
        fontSize=7.2,
        leading=9.2,
        textColor=text_dark
    )

    th_style = ParagraphStyle(
        'TH',
        fontName='Arial-Bold',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.white
    )

    gate_style = ParagraphStyle(
        'GateText',
        fontName='Arial-Bold',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor('#065F46')
    )

    story = []

    # =========================================================================
    # TRANG 1 — STAKEHOLDER MAP & STRATEGY
    # =========================================================================
    story.append(Paragraph("Trang 1 — Stakeholder Map & Strategy · Saving Tracker AI", title_style))
    story.append(Paragraph("<b>Nhóm thực hiện:</b> Team 10 – anhemsiunhan (5 thành viên: Đinh Thị Minh Tâm, Bùi Thị Ngọc Trân, Phạm Thành Đạt, Nguyễn Khánh Linh, Ngô Lê Thuỷ Tiên). Bản tổng hợp từ nghiên cứu cá nhân. Phân loại theo Influence × Interest và Stance thực tế.", subtitle_style))
    
    # Section 1: Stakeholder Table
    story.append(Paragraph("1. Danh sách 7 Stakeholder tổng hợp", h2_style))
    sh_headers = [
        Paragraph("ID", th_style),
        Paragraph("Stakeholder cụ thể", th_style),
        Paragraph("Influence", th_style),
        Paragraph("Interest", th_style),
        Paragraph("Vùng", th_style),
        Paragraph("Stance thực tế", th_style),
        Paragraph("Căn cứ stance & Điều cần xác minh", th_style)
    ]
    sh_data = [sh_headers,
        [
            Paragraph("<b>S1</b>", body_style),
            Paragraph("<b>Giảng viên / Mentor</b> review dự án", body_style),
            Paragraph("Cao", body_style), Paragraph("Cao", body_style),
            Paragraph("Champion", body_bold),
            Paragraph("<font color='#059669'><b>Ủng hộ</b></font>", body_style),
            Paragraph("Đã duyệt định hướng đề tài MVP; sẵn sàng góp ý phạm vi và phương pháp kiểm chứng khi có demo.", body_style)
        ],
        [
            Paragraph("<b>S2</b>", body_style),
            Paragraph("<b>Nhóm 5 sinh viên</b> dùng thử Saving Tracker AI", body_style),
            Paragraph("Thấp", body_style), Paragraph("Cao", body_style),
            Paragraph("Supporter", body_bold),
            Paragraph("<font color='#059669'><b>Ủng hộ</b></font>", body_style),
            Paragraph("Muốn giảm thao tác ghi chép chi tiêu; sẵn sàng tham gia trải nghiệm và cung cấp phản hồi thực tế.", body_style)
        ],
        [
            Paragraph("<b>S3</b>", body_style),
            Paragraph("<b>Cố vấn tài chính cá nhân</b> có thể tham vấn", body_style),
            Paragraph("Cao*", body_style), Paragraph("Thấp", body_style),
            Paragraph("Blocker", body_bold),
            Paragraph("<font color='#D97706'><b>Trung lập</b></font>", body_style),
            Paragraph("Chưa tiếp xúc trực tiếp; lo ngại rủi ro AI tư vấn sai; cần làm rõ phạm vi MVP chỉ dừng ở ghi chép và cảnh báo.", body_style)
        ],
        [
            Paragraph("<b>S4</b>", body_style),
            Paragraph("<b>Đơn vị Open API / Aggregator</b> ngân hàng", body_style),
            Paragraph("Cao*", body_style), Paragraph("Thấp", body_style),
            Paragraph("Blocker", body_bold),
            Paragraph("<font color='#DC2626'><b>Chưa ủng hộ</b></font>", body_style),
            Paragraph("Chưa có quan hệ đối tác; chi phí sandbox cao; giải pháp: ưu tiên nhập hóa đơn/thủ công cho MVP độc lập.", body_style)
        ],
        [
            Paragraph("<b>S5</b>", body_style),
            Paragraph("<b>Chuyên gia bảo mật / Pháp lý</b> dữ liệu cá nhân", body_style),
            Paragraph("Cao", body_style), Paragraph("Thấp", body_style),
            Paragraph("Blocker", body_bold),
            Paragraph("<font color='#D97706'><b>Trung lập</b></font>", body_style),
            Paragraph("Dữ liệu hóa đơn nhạy cảm; cần review sơ đồ luồng dữ liệu và checklist bảo mật trước khi dùng dữ liệu thật.", body_style)
        ],
        [
            Paragraph("<b>S6</b>", body_style),
            Paragraph("<b>Thành viên phụ trách AI/OCR</b> (Phạm Thành Đạt)", body_style),
            Paragraph("Cao", body_style), Paragraph("Cao", body_style),
            Paragraph("Champion", body_bold),
            Paragraph("<font color='#059669'><b>Ủng hộ</b></font>", body_style),
            Paragraph("Thành viên cốt lõi; trực tiếp xây dựng pipeline OCR/LLM và bộ test đánh giá chất lượng (Evals).", body_style)
        ],
        [
            Paragraph("<b>S7</b>", body_style),
            Paragraph("<b>Người dùng đại trà</b> tiềm năng chưa tiếp cận", body_style),
            Paragraph("Thấp", body_style), Paragraph("Thấp", body_style),
            Paragraph("Bystander", body_bold),
            Paragraph("<font color='#6B7280'><b>Trung lập</b></font>", body_style),
            Paragraph("Chưa có tương tác với dự án; theo dõi và tiếp cận mở rộng sau khi MVP hoàn thành kiểm chứng.", body_style)
        ]
    ]
    t_sh = Table(sh_data, colWidths=[22, 175, 45, 45, 60, 68, 362])
    t_sh.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.35, border_color),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
    ]))
    story.append(t_sh)
    story.append(Spacer(1, 2))

    # Section 2: Matrix & 4 Strategies
    story.append(Paragraph("2. Ma trận Influence × Interest & Chiến lược cho 4 Stakeholder ưu tiên", h2_style))
    
    col1_content = [
        Paragraph("<b>Ma trận 4 Vùng:</b>", body_bold),
        Paragraph("• <b>Champion (Cao × Cao):</b> S1 (Mentor - Ủng hộ), S6 (AI Lead - Ủng hộ).", body_style),
        Paragraph("• <b>Supporter (Thấp × Cao):</b> S2 (5 Sinh viên test - Ủng hộ).", body_style),
        Paragraph("• <b>Blocker (Cao × Thấp):</b> S3 (Cố vấn tài chính), S4 (Open API), S5 (Bảo mật).", body_style),
        Paragraph("• <b>Bystander (Thấp × Thấp):</b> S7 (Người dùng đại trà).", body_style),
        Spacer(1, 2),
        Paragraph("<b>Phân công trách nhiệm 4 chiến lược:</b>", body_bold),
        Paragraph("1. <b>S1 (Mentor):</b> Đinh Thị Minh Tâm (Product Owner)<br/>"
                  "2. <b>S2 (Nhóm test):</b> Bùi Thị Ngọc Trân (UI/UX) phối hợp Tâm<br/>"
                  "3. <b>S5 (Bảo mật):</b> Nguyễn Khánh Linh (Backend) phối hợp Tiên<br/>"
                  "4. <b>S4 (Open API):</b> Đinh Thị Minh Tâm (PO) phối hợp Linh", body_style)
    ]
    
    strat_table_data = [
        [
            Paragraph("<b>Stakeholder ưu tiên</b>", th_style),
            Paragraph("<b>1. Họ quan tâm gì?</b>", th_style),
            Paragraph("<b>2. Tác động (Giúp / Cản)?</b>", th_style),
            Paragraph("<b>3. Hành động 1–2 tuần tới (Owner & Deadline)</b>", th_style)
        ],
        [
            Paragraph("<b>S1 – Giảng viên / Mentor</b><br/>(Tận dụng ủng hộ)", body_style),
            Paragraph("Tính thực tế, phạm vi MVP khả thi, chất lượng bằng chứng.", body_style),
            Paragraph("<b>Giúp:</b> Định hướng chuẩn.<br/><b>Cản:</b> Yêu cầu sửa nếu scope rộng.", body_style),
            Paragraph("Gửi tài liệu MVP + demo OCR trước thứ Sáu kèm câu hỏi chốt scope: <i>'MVP chỉ làm OCR + cảnh báo, hoãn tư vấn đầu tư, có phù hợp không?'</i><br/><b>Owner:</b> Đinh Thị Minh Tâm · <b>Deadline:</b> 20/10/2026", body_style)
        ],
        [
            Paragraph("<b>S2 – Nhóm 5 sinh viên test</b><br/>(Tận dụng ủng hộ)", body_style),
            Paragraph("Ghi chép nhanh, ít thao tác nhập, OCR chuẩn xác, bảo mật.", body_style),
            Paragraph("<b>Giúp:</b> Dữ liệu hóa đơn, feedback UX.<br/><b>Cản:</b> Bỏ dùng nếu OCR sai nhiều.", body_style),
            Paragraph("Mời 5 sinh viên thử nghiệm 15' với 3 hóa đơn mẫu (che dữ liệu nhạy cảm); đo thời gian và số lỗi sửa.<br/><b>Owner:</b> Bùi Thị Ngọc Trân phối hợp Tâm · <b>Deadline:</b> 27/10/2026", body_style)
        ],
        [
            Paragraph("<b>S5 – Chuyên gia Bảo mật</b><br/>(Ưu tiên thuyết phục)", body_style),
            Paragraph("Bảo mật dữ liệu hóa đơn, mã hóa và quyền xóa dữ liệu.", body_style),
            Paragraph("<b>Giúp:</b> Phát hiện lỗ hổng sớm.<br/><b>Cản:</b> Dừng pilot nếu rủi ro lộ lọt.", body_style),
            Paragraph("Vẽ sơ đồ luồng dữ liệu (scan → DB); xin review từ 1 chuyên gia mạng lưới nội bộ; lập checklist bảo mật.<br/><b>Owner:</b> Nguyễn Khánh Linh phối hợp Tiên · <b>Deadline:</b> 27/10/2026", body_style)
        ],
        [
            Paragraph("<b>S4 – Đơn vị Open API</b><br/>(Ưu tiên thuyết phục)", body_style),
            Paragraph("Mục đích sử dụng API, cam kết bảo mật và năng lực đối tác.", body_style),
            Paragraph("<b>Giúp:</b> Tự động sync tài khoản.<br/><b>Cản:</b> Từ chối cấp sandbox hoặc phí cao.", body_style),
            Paragraph("Khảo sát docs/sandbox của 2 đơn vị; chuẩn bị phương án dự phòng <i>nhập hóa đơn/thủ công</i> để MVP không phụ thuộc API.<br/><b>Owner:</b> Đinh Thị Minh Tâm phối hợp Linh · <b>Deadline:</b> 27/10/2026", body_style)
        ]
    ]
    t_strat = Table(strat_table_data, colWidths=[90, 115, 115, 252])
    t_strat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#334155')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('INNERGRID', (0,0), (-1,-1), 0.35, border_color),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#334155')),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
    ]))

    t_matrix_strat = Table([[Table([[p] for p in col1_content], colWidths=[200]), t_strat]], colWidths=[205, 572])
    t_matrix_strat.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_matrix_strat)
    story.append(Spacer(1, 2))

    # Gate 1 Box
    gate1_box = Table([[
        Paragraph("<b>GATE 1 — KIỂM TRA ĐẠT TIÊU CHUẨN:</b> [x] Có 7 stakeholder cụ thể, phân bố đủ 4 vùng Influence × Interest; [x] Có stance sơ bộ dựa trên căn cứ thực tế và tách bạch với quadrant; [x] Xác định 4 stakeholder ưu tiên (2 tận dụng ủng hộ: S1, S2; 2 ưu tiên thuyết phục: S5, S4); [x] Có hành động cụ thể, tên Owner và Deadline thực thi rõ ràng.", gate_style)
    ]], colWidths=[usable_w])
    gate1_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#10B981')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(gate1_box)

    # =========================================================================
    # TRANG 2 — PITCH "KẾT LUẬN TRƯỚC" & RACI MATRIX
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Trang 2 — Pitch & RACI Matrix · Saving Tracker AI", title_style))
    story.append(Paragraph("<b>Quy tắc áp dụng:</b> Pitch theo cấu trúc Conclusion First (Kết luận trước), bằng chứng thực tế không tô vẽ; RACI rõ ràng với đúng 1 Accountable (A) cho mỗi đầu việc quan trọng.", subtitle_style))

    left_pitch = [
        Paragraph("1. Pitch 'Conclusion First' (Gửi S2 – 5 Sinh viên dùng thử)", h2_style),
        Paragraph("<b>• Kết luận / Đề xuất:</b> Nhóm kính mời bạn tham gia buổi thử nghiệm 15 phút với ứng dụng Saving Tracker AI để kiểm chứng xem việc quét hóa đơn tự động có thực sự tiết kiệm thời gian và tiện lợi hơn phương pháp nhập thủ công hay không.", body_style),
        Paragraph("<b>• 3 Lý do chính:</b> (1) <i>Giảm tải thao tác:</i> Nhập thủ công từng khoản lẻ khiến người dùng dễ nản lòng; tự động hóa OCR/LLM giúp duy trì thói quen ghi chép. (2) <i>Kiểm chứng độ chính xác:</i> Cần đo lường xem AI đọc có chuẩn xác không hay người dùng lại mất công sửa. (3) <i>Xây đúng nhu cầu:</i> Phản hồi của bạn định hình tính năng thực sự có ích cho MVP.", body_style),
        Paragraph("<b>• Bằng chứng thực tế:</b> Repository đã xây dựng kiến trúc kỹ thuật OCR trích xuất thông tin hóa đơn và cảnh báo chi tiêu. Nhóm thành thật ghi nhận hiện chưa có số liệu đo lường thực tế về độ chính xác và thời gian tiết kiệm, do đó không đưa ra lời hứa vượt quá năng lực kiểm chứng hiện tại.", body_style),
        Paragraph("<b>• Small ask (Hành động nhỏ, cụ thể):</b> Dành 15 phút thực hiện thao tác trên 3 hóa đơn mẫu (đã che thông tin nhạy cảm). Nhóm sẽ bấm giờ, ghi nhận số lỗi cần sửa và xin 3 điểm bạn thấy cần cải thiện nhất.", body_style),
        Spacer(1, 2),
        Paragraph("2. Phản biện chính & Giải pháp xử lý", h2_style),
        Paragraph("<b>Phản biện:</b> <i>'AI đọc hóa đơn hay bị sai tên hoặc số tiền. Nếu người dùng phải dò và sửa lại từng dòng thì còn tốn thời gian hơn tự bấm số nhập tay.'</i>", body_style),
        Paragraph("<b>Cách xử lý của nhóm:</b> (1) Xây bộ dữ liệu eval 30 hóa đơn chuẩn để đo độ chính xác từng trường (tên cửa hàng, ngày, tổng tiền); (2) Thiết kế UI cho phép người dùng preview và chỉnh sửa 1 chạm nhanh chóng; (3) Đo lường thời gian thao tác thực tế so với nhập tay, nếu chưa nhanh hơn sẽ tập trung tối ưu độ chính xác và trải nghiệm sửa trước khi mở rộng tính năng.", body_style),
        Spacer(1, 2),
        Paragraph("3. Tổng hợp Pitch cá nhân (5 thành viên)", h2_style),
        Paragraph("<b>Tâm (PO):</b> Kiểm chứng giá trị thực tế của OCR so với nhập tay. · <b>Trân (UX):</b> Minh bạch luồng dữ liệu & chính sách riêng tư. · <b>Đạt (AI):</b> Đo lường lỗi OCR bằng bộ Eval chuẩn. · <b>Linh (Backend):</b> Giới hạn an toàn gợi ý tài chính. · <b>Tiên (QA/Sec):</b> Kiểm soát lưu trữ & xóa thông tin hóa đơn.", body_style)
    ]

    raci_headers = [
        Paragraph("Công việc cốt lõi (1–2 tháng)", th_style),
        Paragraph("PO<br/>(Tâm)", th_style),
        Paragraph("AI<br/>(Đạt)", th_style),
        Paragraph("Backend<br/>(Linh)", th_style),
        Paragraph("UI/UX<br/>(Trân)", th_style),
        Paragraph("QA/Sec<br/>(Tiên)", th_style),
        Paragraph("Mentor<br/>(S1)", th_style)
    ]
    raci_rows = [raci_headers,
        [
            Paragraph("1. Chốt phạm vi & yêu cầu MVP", body_style),
            Paragraph("<b>A/R</b>", body_bold), Paragraph("C", body_style), Paragraph("C", body_style), Paragraph("C", body_style), Paragraph("C", body_style), Paragraph("I", body_style)
        ],
        [
            Paragraph("2. Chuẩn bị dataset & xây pipeline OCR/LLM", body_style),
            Paragraph("C", body_style), Paragraph("<b>A/R</b>", body_bold), Paragraph("C", body_style), Paragraph("I", body_style), Paragraph("I", body_style), Paragraph("I", body_style)
        ],
        [
            Paragraph("3. Thiết kế kiến trúc & bảo mật dữ liệu", body_style),
            Paragraph("C", body_style), Paragraph("C", body_style), Paragraph("<b>A</b>", body_bold), Paragraph("C", body_style), Paragraph("R", body_style), Paragraph("I", body_style)
        ],
        [
            Paragraph("4. Xây dựng UI nhập liệu & dashboard chi tiêu", body_style),
            Paragraph("C", body_style), Paragraph("I", body_style), Paragraph("C", body_style), Paragraph("<b>A/R</b>", body_bold), Paragraph("I", body_style), Paragraph("I", body_style)
        ],
        [
            Paragraph("5. Đánh giá chất lượng OCR & xử lý lỗi (Evals)", body_style),
            Paragraph("<b>A</b>", body_bold), Paragraph("R", body_style), Paragraph("C", body_style), Paragraph("C", body_style), Paragraph("C", body_style), Paragraph("I", body_style)
        ],
        [
            Paragraph("6. Tổ chức user testing & quyết định pilot", body_style),
            Paragraph("<b>A</b>", body_bold), Paragraph("C", body_style), Paragraph("C", body_style), Paragraph("R", body_style), Paragraph("C", body_style), Paragraph("I", body_style)
        ]
    ]
    t_raci = Table(raci_rows, colWidths=[155, 34, 34, 38, 38, 38, 35])
    t_raci.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.35, border_color),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
    ]))

    right_raci = [
        Paragraph("4. RACI Matrix (Đúng 1 Accountable mỗi hàng)", h2_style),
        t_raci,
        Spacer(1, 2),
        Paragraph("<b>Nguyên tắc phân quyền & Phân công nhân sự:</b>", body_bold),
        Paragraph("• <b>Đinh Thị Minh Tâm (Product Owner):</b> Accountable chốt phạm vi, nghiệm thu kết quả Eval và quyết định pilot để đảm bảo tiêu chí bám sát nhu cầu người dùng, tránh việc kỹ thuật 'tự làm tự duyệt'.<br/>"
                  "• <b>Phạm Thành Đạt (AI Engineer):</b> Accountable/Responsible pipeline trích xuất OCR/LLM và trực tiếp thực thi việc đo đạc eval accuracy.<br/>"
                  "• <b>Nguyễn Khánh Linh (Backend):</b> Chịu trách nhiệm chính (A) về lưu trữ DB, API an toàn; <b>Ngô Lê Thuỷ Tiên (QA/Security):</b> Trực tiếp review (R) lỗ hổng và rủi ro quyền riêng tư.<br/>"
                  "• <b>Bùi Thị Ngọc Trân (UI/UX Designer):</b> Chịu trách nhiệm (A/R) luồng nhập liệu và trực tiếp chủ trì (R) các buổi thử nghiệm người dùng.", body_style)
    ]

    t_p2 = Table([[Table([[p] for p in left_pitch], colWidths=[388]), Table([[p] for p in right_raci], colWidths=[385])]], colWidths=[392, 385])
    t_p2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_p2)
    story.append(Spacer(1, 2))

    # Gate 2 Box
    gate2_box = Table([[
        Paragraph("<b>GATE 2 — KIỂM TRA ĐẠT TIÊU CHUẨN:</b> [x] Pitch theo Conclusion First, nêu rõ 3 lý do, trung thực về bằng chứng, có Small ask cụ thể 15 phút; [x] Có 1 phản biện xác đáng về sai số OCR và giải pháp 4 bước; [x] RACI Matrix 6 công việc cốt lõi, mỗi công việc có đúng 1 Accountable (A) rõ ràng và gắn đúng tên 5 thành viên thực tế.", gate_style)
    ]], colWidths=[usable_w])
    gate2_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#10B981')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(gate2_box)

    # =========================================================================
    # TRANG 3 — AI TEAM DESIGN & PRIORITY RESOURCING
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Trang 3 — AI Team Design · Saving Tracker AI", title_style))
    story.append(Paragraph("<b>Mục tiêu thiết kế:</b> Tối ưu hóa cấu trúc nhân sự phù hợp với giai đoạn MVP; xác định rõ vai trò cốt lõi và bổ sung năng lực bằng Hire / Outsource / Partner thay vì tuyển dụng dàn trải.", subtitle_style))

    arch_role_data = [
        [
            Paragraph("<b>1. Team Architecture: EMBEDDED</b>", h2_style),
            Paragraph("<b>2. Phân định Core Roles (MVP) vs Extended Roles (Scale)</b>", h2_style)
        ],
        [
            Paragraph("• <b>Lý do chọn Embedded:</b> Nhóm có quy mô 5 người đang tập trung phát triển 01 sản phẩm MVP duy nhất. Năng lực AI (Đạt), Backend (Linh), UX (Trân), Security/QA (Tiên) và Product (Tâm) được nhúng trực tiếp vào cùng một squad sản phẩm, làm việc đồng bộ qua nhịp họp ngắn hàng tuần.<br/>"
                      "• <b>Vì sao không chọn Centralized / Hybrid:</b> Centralized (nhóm AI trung tâm) và Hybrid chỉ phù hợp cho doanh nghiệp quy mô lớn có nhiều sản phẩm cùng chia sẻ tài nguyên AI. Áp dụng cho nhóm 5 người sẽ tạo rào cản giao tiếp và quan liêu hóa quy trình không cần thiết.", body_style),
            Paragraph("• <b>Core Roles (Cần ngay ở MVP):</b><br/>"
                      "  - <i>Product Owner (Tâm):</i> Quản lý phạm vi MVP, điều phối stakeholder, duyệt kết quả thử nghiệm.<br/>"
                      "  - <i>AI Engineer (Đạt):</i> Xây pipeline OCR/LLM đọc hóa đơn, prompt engineering, xây bộ test Eval.<br/>"
                      "  - <i>Backend & Security (Linh):</i> Cơ sở dữ liệu giao dịch, API đồng bộ và lưu trữ an toàn.<br/>"
                      "  - <i>UI/UX Designer (Trân):</i> Thiết kế luồng chụp hóa đơn, tối ưu trải nghiệm sửa lỗi, user test.<br/>"
                      "  - <i>Security & QA (Tiên):</i> Đảm bảo quyền riêng tư dữ liệu, kiểm thử phần mềm, tuân thủ bảo mật.<br/>"
                      "• <b>Extended Roles (Chỉ cần khi Scale):</b> Legal & Compliance tài chính, MLOps chuyên trách, Domain Expert tài chính toàn thời gian, AI Ethics & Governance.", body_style)
        ]
    ]
    t_arch = Table(arch_role_data, colWidths=[315, 462])
    t_arch.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_arch)
    story.append(Spacer(1, 3))

    story.append(Paragraph("3. Priority Resourcing: Giải quyết 3 Capability Gaps cốt lõi", h2_style))
    res_headers = [
        Paragraph("Capability Gap (Năng lực còn thiếu)", th_style),
        Paragraph("Phương án bổ sung", th_style),
        Paragraph("Vì sao chọn phương án này? (Không chọn Hire)", th_style),
        Paragraph("Thời điểm cần kích hoạt", th_style)
    ]
    res_rows = [res_headers,
        [
            Paragraph("<b>Chuyên môn tài chính & Giới hạn tư vấn an toàn</b>", body_style),
            Paragraph("<font color='#1D4ED8'><b>PARTNER</b></font><br/>với Cố vấn tài chính cá nhân (S3)", body_style),
            Paragraph("Nhóm chỉ cần chuyên gia thẩm định và phân định ranh giới 'rủi ro đỏ' (những lời khuyên AI không được phép đưa ra). Không cần tuyển nhân sự cố định tốn kém ở giai đoạn MVP.", body_style),
            Paragraph("Trước khi mở tính năng gợi ý chi tiêu/tích lũy cho người dùng thử.", body_style)
        ],
        [
            Paragraph("<b>Kết nối dữ liệu ngân hàng tự động (Open API)</b>", body_style),
            Paragraph("<font color='#1D4ED8'><b>PARTNER</b></font><br/>với đơn vị Aggregator có sandbox (S4)", body_style),
            Paragraph("Tự xây dựng kết nối trực tiếp với các ngân hàng đòi hỏi giấy phép, thủ tục pháp lý phức tạp và chi phí rất lớn. MVP ưu tiên phương án dự phòng là quét hóa đơn và nhập tay để hoàn toàn độc lập tiến độ.", body_style),
            Paragraph("Sau khi MVP hoàn thành kiểm chứng luồng đọc hóa đơn ổn định.", body_style)
        ],
        [
            Paragraph("<b>Đánh giá chất lượng AI (Evals) & Review bảo mật</b>", body_style),
            Paragraph("<font color='#059669'><b>DEVELOP NỘI BỘ</b></font> (AI Evals)<br/>+ <font color='#D97706'><b>OUTSOURCE</b></font> (Security Review)", body_style),
            Paragraph("• AI Evals là năng lực sống còn của sản phẩm AI, nhóm phải tự làm chủ (giao AI Engineer Đạt phát triển).<br/>• Review bảo mật cần góc nhìn độc lập khách quan nhưng chỉ cần đánh giá theo đợt trước khi launch, không cần biên chế full-time.", body_style),
            Paragraph("• Bộ Eval: Cần ngay trước đợt user test đầu tiên.<br/>• Security review: Trước khi triển khai thử nghiệm trên dữ liệu cá nhân thật.", body_style)
        ]
    ]
    t_res = Table(res_rows, colWidths=[165, 135, 348, 129])
    t_res.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('INNERGRID', (0,0), (-1,-1), 0.35, border_color),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
    ]))
    story.append(t_res)
    story.append(Spacer(1, 3))

    story.append(Paragraph("4. Squad Goal của nhóm", h2_style))
    goal_box = Table([[
        Paragraph("<i>\"Team của chúng tôi sở hữu <b>luồng đọc hóa đơn và cảnh báo chi tiêu của Saving Tracker AI</b> và chịu trách nhiệm đưa <b>sản phẩm</b> từ <b>prototype OCR chưa kiểm chứng với người dùng thật</b> đến <b>MVP an toàn mà nhóm người dùng thử đầu tiên tin dùng</b>.\"</i>", ParagraphStyle('GoalText', fontName='Arial', fontSize=8, leading=10.5, textColor=colors.HexColor('#1E3A8A')))
    ]], colWidths=[usable_w])
    goal_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#3B82F6')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(goal_box)
    story.append(Spacer(1, 3))

    gate3_box = Table([[
        Paragraph("<b>GATE 3 — KIỂM TRA ĐẠT TIÊU CHUẨN:</b> [x] Mô hình Embedded được giải thích rõ ràng theo quy mô nhóm 5 người và giai đoạn MVP; [x] Tách bạch Core Roles và Extended Roles tránh phình to bộ máy; [x] 3 Capability Gaps cốt lõi giải quyết bằng Partner / Outsource / Internal Development thực tế, không vẽ chức danh ảo; [x] Squad Goal hoàn thiện đúng cấu trúc.", gate_style)
    ]], colWidths=[usable_w])
    gate3_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#10B981')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(gate3_box)

    # =========================================================================
    # TRANG 4 — TEAM HEALTH & GROWTH PLAN 30 NGÀY
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Trang 4 — Team Health & Growth Plan · Saving Tracker AI", title_style))
    story.append(Paragraph("<b>Quy trình thực hiện:</b> Cá nhân tự chấm điểm độc lập (1–5) → Họp nhóm đối chiếu chênh lệch → Xác định điểm nghẽn ưu tiên → Chọn Competency cần nâng theo khung L1/L2/L3 → Lập Growth Plan 30 ngày (Owner, Deadline, Dấu hiệu hoàn thành).", subtitle_style))

    health_headers = [
        Paragraph("Khía cạnh đánh giá", th_style),
        Paragraph("Tâm", th_style),
        Paragraph("Trân", th_style),
        Paragraph("Đạt", th_style),
        Paragraph("Linh", th_style),
        Paragraph("Tiên", th_style),
        Paragraph("Điểm TB", th_style),
        Paragraph("Chênh lệch", th_style)
    ]
    health_rows = [health_headers,
        [
            Paragraph("<b>1. Chất lượng AI</b>", body_style),
            Paragraph("3", body_style), Paragraph("3", body_style), Paragraph("3", body_style), Paragraph("2", body_style), Paragraph("2", body_style),
            Paragraph("<font color='#DC2626'><b>2.6 / 5</b></font>", body_bold), Paragraph("1", body_style)
        ],
        [
            Paragraph("<b>2. Tiến độ</b>", body_style),
            Paragraph("3", body_style), Paragraph("3", body_style), Paragraph("3", body_style), Paragraph("3", body_style), Paragraph("3", body_style),
            Paragraph("<b>3.0 / 5</b>", body_bold), Paragraph("0", body_style)
        ],
        [
            Paragraph("<b>3. Tinh thần team</b>", body_style),
            Paragraph("5", body_style), Paragraph("4", body_style), Paragraph("4", body_style), Paragraph("5", body_style), Paragraph("4", body_style),
            Paragraph("<font color='#059669'><b>4.4 / 5</b></font>", body_bold), Paragraph("1", body_style)
        ],
        [
            Paragraph("<b>4. Tốc độ ra sản phẩm</b>", body_style),
            Paragraph("2", body_style), Paragraph("3", body_style), Paragraph("2", body_style), Paragraph("3", body_style), Paragraph("3", body_style),
            Paragraph("<font color='#DC2626'><b>2.6 / 5</b></font>", body_bold), Paragraph("1", body_style)
        ]
    ]
    t_health = Table(health_rows, colWidths=[120, 28, 28, 28, 28, 28, 48, 46])
    t_health.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.35, border_color),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
    ]))

    analysis_content = [
        Paragraph("<b>2. Phân tích kết quả & Vấn đề ưu tiên hàng đầu</b>", h2_style),
        Paragraph("• <b>Điểm mạnh:</b> Tinh thần team đạt <b>4.4/5</b> — các thành viên cởi mở, tin tưởng và phối hợp nhịp nhàng.<br/>"
                  "• <b>Đồng thuận cao:</b> Tiến độ đạt <b>3.0/5</b> với độ chênh lệch bằng 0 (cả 5 thành viên đều đánh giá ở mức trung bình).<br/>"
                  "• <b>Hai điểm nghẽn thấp nhất:</b> <b>Chất lượng AI (2.6/5)</b> và <b>Tốc độ ra sản phẩm (2.6/5)</b>.<br/>"
                  "• <b>VẤN ĐỀ ƯU TIÊN SỐ 1:</b> <i>Thiếu quy trình kiểm chứng chất lượng AI (AI Evals) và cơ chế tích hợp kết quả đo đạc vào chu kỳ hoàn thiện MVP.</i> Nếu không đo được lỗi OCR, nhóm sẽ không thể tự tin đưa sản phẩm cho người dùng thử nghiệm.", body_style)
    ]

    t_p4_top = Table([[t_health, Table([[p] for p in analysis_content], colWidths=[415])]], colWidths=[354, 423])
    t_p4_top.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_p4_top)
    story.append(Spacer(1, 2))

    comp_box_data = [
        [
            Paragraph("<b>3. Nâng cấp Competency (Khung L1/L2/L3):</b> Vai trò: <b>AI Engineer</b> (Phụ trách: <b>Phạm Thành Đạt</b>) · <b>Level hiện tại:</b> L2 — AI Practitioner (Đã xây dựng pipeline prompt/OCR cơ bản nhưng chưa có bộ kiểm chuẩn) · <b>Competency cần nâng:</b> <b>AI Evals / Quality Evaluation</b> · <b>Hành động 30 ngày:</b> Xây dựng dataset 30 hóa đơn mẫu có ground-truth, thiết kế accuracy metric theo từng trường thông tin và chạy eval tự động sau mỗi lần cập nhật pipeline.", body_style)
        ]
    ]
    t_comp = Table(comp_box_data, colWidths=[usable_w])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#94A3B8')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 2))

    story.append(Paragraph("4. Growth Plan 30 ngày (13/10/2026 – 12/11/2026) — 3 Hành động cụ thể", h2_style))
    gp_headers = [
        Paragraph("Vấn đề cốt lõi", th_style),
        Paragraph("Hành động 30 ngày", th_style),
        Paragraph("Owner phụ trách", th_style),
        Paragraph("Deadline", th_style),
        Paragraph("Dấu hiệu hoàn thành cụ thể (Measurable)", th_style)
    ]
    gp_rows = [gp_headers,
        [
            Paragraph("<b>Chất lượng AI thấp (2.6/5)</b>, chưa có thước đo độ chính xác trích xuất hóa đơn", body_style),
            Paragraph("Xây bộ dữ liệu 30 hóa đơn chuẩn có đáp án; đo độ chính xác OCR (tên shop, ngày, số tiền); lưu baseline eval.", body_style),
            Paragraph("<b>Phạm Thành Đạt</b><br/>(AI Engineer)", body_style),
            Paragraph("<b>27/10/2026</b><br/>(Tuần 2)", body_style),
            Paragraph("Có file dataset trong repo, bảng kết quả eval baseline và phân loại nhóm lỗi OCR thường gặp.", body_style)
        ],
        [
            Paragraph("<b>Tốc độ ra sản phẩm thấp (2.6/5)</b>, các khâu phối hợp chưa có nhịp sync chặt", body_style),
            Paragraph("Chia nhỏ MVP thành task backlog trên GitHub, thống nhất tiêu chuẩn hoàn thành (DoD), họp review tiến độ hàng tuần.", body_style),
            Paragraph("<b>Đinh Thị Minh Tâm</b> (PO)<br/>phối hợp Khánh Linh", body_style),
            Paragraph("<b>03/11/2026</b><br/>(Tuần 3)", body_style),
            Paragraph("Backlog trên GitHub có trạng thái/owner rõ ràng; có ít nhất 2 biên bản họp Weekly Review được lưu vết.", body_style)
        ],
        [
            Paragraph("<b>Chưa kiểm chứng giá trị thực tế</b> của MVP với người dùng mục tiêu", body_style),
            Paragraph("Tổ chức thử nghiệm với 5 người dùng mục tiêu; đo thời gian nhập và số lần sửa lỗi; tổng hợp 3 vấn đề ưu tiên.", body_style),
            Paragraph("<b>Bùi Thị Ngọc Trân</b> (UX)<br/>phối hợp Minh Tâm", body_style),
            Paragraph("<b>12/11/2026</b><br/>(Tuần 4)", body_style),
            Paragraph("Có báo cáo User Testing hoàn chỉnh với số liệu thời gian thao tác và danh sách 3 vấn đề ưu tiên cải thiện.", body_style)
        ]
    ]
    t_gp = Table(gp_rows, colWidths=[140, 205, 105, 75, 252])
    t_gp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('INNERGRID', (0,0), (-1,-1), 0.35, border_color),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
    ]))
    story.append(t_gp)
    story.append(Spacer(1, 2))

    story.append(Paragraph("<b>Nhịp vận hành hàng tuần:</b> Weekly Review 20 phút vào mỗi thứ Sáu (bắt đầu 16/10/2026) do Product Owner Đinh Thị Minh Tâm chủ trì nhằm kiểm tra tiến độ backlog, kết quả eval và giải tỏa blocker.", body_style))
    story.append(Spacer(1, 2))

    gate4_box = Table([[
        Paragraph("<b>GATE 4 — KIỂM TRA ĐẠT TIÊU CHUẨN:</b> [x] Bảng điểm Team Health đầy đủ 5 thành viên ở 4 khía cạnh; [x] Phân tích chỉ ra vấn đề ưu tiên số 1 (AI Evals); [x] Xác định competency AI Evals cho AI Engineer Đạt (L2); [x] Kế hoạch 30 ngày có đúng 3 hành động thực chất với Owner, Deadline và Dấu hiệu hoàn thành có thể đo lường được.", gate_style)
    ]], colWidths=[usable_w])
    gate4_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ECFDF5')),
        ('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#10B981')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(gate4_box)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Built PDF successfully: {filename}")

if __name__ == '__main__':
    out_pdf = 'D:/AI-20K-Phase2/Track1_Day25_Team10_anhemsiunhan/Day25_AI-Team-Lab_Team10.pdf'
    out_pdf2 = 'D:/AI-20K-Phase2/Track1_Day25_Team10_anhemsiunhan/output/pdf/Day25_AI-Team-Lab_Team10.pdf'
    build_pdf(out_pdf)
    import shutil
    shutil.copyfile(out_pdf, out_pdf2)
    print(f"Copied to {out_pdf2}")
