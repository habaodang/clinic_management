from app import login_manager
from flask_login import current_user
from sqlalchemy import func
from app.models import User,Account,LichKham,PhieuKham,HoaDon,ChiTietHoaDon
from app import db
from datetime import datetime

from app.routes.main_route import payment_return


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


def them_chitietdonthuoc(hoa_don_id,thuoc_id,so_luong):
    # Kiểm tra nếu tất cả tham số cần thiết đều có giá trị hợp lệ
    if hoa_don_id and thuoc_id and so_luong > 0 :
        print('vo ham chi teit')
        # Tạo mới một chi tiết đơn thuốc
        chi_tiet = ChiTietHoaDon(
            hoa_don_id=hoa_don_id,
            thuoc_id=thuoc_id,
            so_luong=so_luong
        )

        # Thêm chi tiết đơn thuốc vào cơ sở dữ liệu
        db.session.add(chi_tiet)
        db.session.commit()



def tinh_tong_tien_hoa_don(hoa_don_id):
    # Kiểm tra nếu hóa đơn tồn tại
    hoa_don = HoaDon.query.get(hoa_don_id)
    if not hoa_don:
        return "Hóa đơn không tồn tại"

    print(hoa_don_id)
    # Lấy tất cả các chi tiết hóa đơn liên quan đến hóa đơn này
    chi_tiet_don_thuoc = ChiTietHoaDon.query.filter(ChiTietHoaDon.hoa_don_id==hoa_don_id).all()

    # Tính tổng tiền từ các chi tiết hóa đơn
    tong_tien = sum(chi_tiet.so_luong * chi_tiet.thuoc.price for chi_tiet in chi_tiet_don_thuoc)

    print('tong tien teruoc', tong_tien)
    for ch in chi_tiet_don_thuoc:
        print('thuoc', ch.thuoc.price,ch.so_luong)
    # Cộng thêm 100 tiền khám
    tong_tien += 100000

    # Cập nhật tổng tiền trong hóa đơn
    hoa_don.tong_tien = tong_tien
    db.session.commit()


def cap_nhap_trang_thai_lichkham(id_lichkham):
        # Lấy đối tượng lịch khám cần cập nhật
    lich_kham = LichKham.query.filter(LichKham.id==id_lichkham).first()


    # Kiểm tra giá trị hiện tại của status_doctor
    if lich_kham.status_doctor == 0:
        lich_kham.status_doctor = 1  # Cập nhật giá trị
        db.session.commit()

