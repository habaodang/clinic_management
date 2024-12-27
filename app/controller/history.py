from app import login_manager
from flask_login import current_user
from sqlalchemy import func
from app.models import User,Account,LichKham
from app import db
from datetime import datetime

def get_appointment_date(date):
    return LichKham.query.filter(LichKham.date==date).all()

def get_appointmant_all():
    return LichKham.query.all()

def get_appointment_id(id):
    return LichKham.query.filter(LichKham.id.__eq__(id)).first()

# y ta xac nhan don
def confirm_appointment(id):
    lichkham=LichKham.query.filter(LichKham.id.__eq__(id)).first()
    lichkham.status=True
    db.session.commit()

# so luong gon dat lich kham
def count_apointment_all():
    return db.session.query(func.count(LichKham.id)).scalar()


def get_appointment_present_id(id):
    now = datetime.now().date()

    lichkham = LichKham.query.filter(
        LichKham.doctor_id == id,
        LichKham.date == now,LichKham.status==1,LichKham.status_doctor==0
    ).all()
    return lichkham

