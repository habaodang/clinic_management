from flask_login import current_user
from app.models import HoaDon,ChiTietHoaDon,PhieuKham
from app import db

def get_hoadon():
    hoadon=HoaDon.query.all()
    return hoadon


def get_hoadon_by_id(id):
    hoadon=HoaDon.query.filter(HoaDon.id==id).first()
    return hoadon

def update_status(id):
    hoadon = HoaDon.query.filter(HoaDon.id == id).first()
    hoadon.trangthai=True
    db.session.commit()

def get_hoadon_for_patient(id):
    invoices = db.session.query(HoaDon).join(PhieuKham).filter(PhieuKham.patient_id == id).all()
    return invoices

def thanh_toan_onl(id):
    print('vo ham bill')
    hoadon=HoaDon.query.filter(HoaDon.id==id).first()
    print('id hoa don',hoadon.id)
    hoadon.trangthai=True
    db.session.commit()