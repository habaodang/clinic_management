
from app import db
from app.models import User,Account,LichKham
from fpdf import FPDF
import os

def export_to_pdf(output_file='static/lich_kham.pdf'):
    try:
        # Truy xuất dữ liệu từ database
        records = db.session.query(LichKham).all()

        if not records:
            print("Không có dữ liệu để xuất PDF.")
            return

        # Tạo PDF
        class PDF(FPDF):
            def header(self):
                self.set_font('DejaVuSans', 'B', 12)
                self.cell(0, 10, 'Danh sách Lịch Khám', border=0, ln=1, align='C')

            def footer(self):
                self.set_y(-15)
                self.set_font('DejaVuSans', 'I', 8)
                self.cell(0, 10, f'Page {self.page_no()}', align='C')

        pdf = PDF()
        pdf.add_page()

        # Thêm font DejaVu Sans với các kiểu khác nhau
        pdf.add_font('DejaVuSans', '', 'D:/WorkSpaceCode/Flask/Clinic management/app/static/resources/dejavu-fonts-ttf-2.37/dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf', uni=True)  # Regular font
        pdf.add_font('DejaVuSans', 'B', 'D:/WorkSpaceCode/Flask/Clinic management/app/static/resources/dejavu-fonts-ttf-2.37/dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Bold.ttf', uni=True)  # Bold font
        pdf.add_font('DejaVuSans', 'I', 'D:/WorkSpaceCode/Flask/Clinic management/app/static/resources/dejavu-fonts-ttf-2.37/dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Italic.ttf', uni=True)  # Italic font (nếu có)

        # Dùng font DejaVu Sans
        pdf.set_font('DejaVuSans', '', 12)

        # Thêm tiêu đề cột
        pdf.set_font('DejaVuSans', 'B', 12)
        pdf.cell(30, 10, 'ID', border=1)
        pdf.cell(50, 10, 'Time', border=1)
        pdf.cell(50, 10, 'Status', border=1)
        pdf.ln()

        # Thêm dữ liệu vào PDF
        pdf.set_font('DejaVuSans', '', 12)
        for record in records:
            pdf.cell(30, 10, str(record.id), border=1)
            pdf.cell(50, 10, str(record.time), border=1)
            pdf.cell(50, 10, str(record.status), border=1)
            pdf.ln()

        # Lưu file PDF
        pdf.output(output_file)
        print(f"Dữ liệu đã được xuất thành công vào {output_file}")

    except Exception as e:
        print(f"Lỗi khi xuất PDF: {e}")
