from app import login_manager
from flask_login import current_user
from sqlalchemy import func
from app.models import User,Account,LichKham,PhieuKham,HoaDon,ChiTietHoaDon
from app import db
from datetime import datetime

def them_phieu_kham(trieuchung, chandoan, patient_id, doctor_id):
    if trieuchung and chandoan and patient_id and doctor_id:
        phieukham = PhieuKham(
            trieuchung=trieuchung,
            chandoan=chandoan,
            patient_id=patient_id,
            doctor_id=doctor_id
        )
        db.session.add(phieukham)
        db.session.commit()
        return phieukham.id


def them_hoadon(phieu_kham_id):
    hoadon=HoaDon(phieu_kham_id=phieu_kham_id)
    db.session.add(hoadon)
    db.session.commit()
    return hoadon.id


def them_chitietdonthuoc(hoa_don_id,thuoc_id,so_luong,don_gia):
    # Kiểm tra nếu tất cả tham số cần thiết đều có giá trị hợp lệ
    if hoa_don_id and thuoc_id and so_luong > 0 and don_gia > 0:
        # Tạo mới một chi tiết đơn thuốc
        chi_tiet = ChiTietHoaDon(
            hoa_don_id=hoa_don_id,
            thuoc_id=thuoc_id,
            so_luong=so_luong,
            don_gia=don_gia
        )

        # Thêm chi tiết đơn thuốc vào cơ sở dữ liệu
        db.session.add(chi_tiet)
        db.session.commit()

        # Trả về ID của chi tiết đơn thuốc vừa thêm vào
        return chi_tiet.id
    else:
        return "Thông tin không hợp lệ"


def tinh_tong_tien_hoa_don(hoa_don_id):
    # Kiểm tra nếu hóa đơn tồn tại
    hoa_don = HoaDon.query.get(hoa_don_id)
    if not hoa_don:
        return "Hóa đơn không tồn tại"

    # Lấy tất cả các chi tiết hóa đơn liên quan đến hóa đơn này
    chi_tiet_don_thuoc = ChiTietHoaDon.query.filter_by(hoa_don_id=hoa_don_id).all()

    # Tính tổng tiền từ các chi tiết hóa đơn
    tong_tien = sum(chi_tiet.so_luong * chi_tiet.don_gia for chi_tiet in chi_tiet_don_thuoc)

    # Cộng thêm 100 tiền khám
    tong_tien += 100

    # Cập nhật tổng tiền trong hóa đơn
    hoa_don.tong_tien = tong_tien
    db.session.commit()

    # Trả về tổng tiền
    return tong_tien

def cap_nhap_trang_thai_lichkham(id_lichkham):
    try:
        # Lấy đối tượng lịch khám cần cập nhật
        lich_kham = LichKham.query.filter(LichKham.id==lich_kham_id).first()

        if lich_kham is None:
            return {"success": False, "message": "Không tìm thấy lịch khám với ID đã cho."}

        # Kiểm tra giá trị hiện tại của status_doctor
        if lich_kham.status_doctor == 0:
            lich_kham.status_doctor = 1  # Cập nhật giá trị
            db.session.commit()
            return {"success": True, "message": "Cập nhật status_doctor thành công."}
        else:
            return {"success": False, "message": "status_doctor đã là 1, không cần cập nhật."}
    except SQLAlchemyError as e:
        db.session.rollback()  # Hoàn tác giao dịch nếu có lỗi
        return {"success": False, "message": f"Lỗi khi cập nhật status_doctor: {str(e)}"}