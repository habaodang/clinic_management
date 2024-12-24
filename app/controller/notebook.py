from app import login_manager
from flask_login import current_user
from app.models import User,Account,LichKham
from app import db

def get_examination_history():
    patient_id = current_user.user.id
    print(patient_id)
    return LichKham.query.filter(LichKham.patient_id.__eq__(patient_id.strip())).all()
