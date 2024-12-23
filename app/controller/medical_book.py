from app import login_manager
from flask_login import current_user
from sqlalchemy import func
import hashlib
from app.models import User,Account,LichKham
from app import db

def add_booking(date,time,location,package,note,department_id,doctor_id):
    if date and time and location  and package and department_id and note:
        patient_id = current_user.user.id
        lichkham=LichKham(date=date,time=time,location=location,package=package,note=note,patient_id=patient_id,department_id=department_id)

        # kiem tra benh nhan co chon bac si khong
        if doctor_id:
            lichkham.doctor_id=doctor_id
        db.session.add(lichkham)
        db.session.commit()

        return 'ok'
    return 'khong ddc'
