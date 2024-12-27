from app import login_manager
from flask_login import current_user
from app.models import User,Account,LichKham
from app import db

def get_examination_history(id):
    if id:
        return LichKham.query.filter(LichKham.patient_id.__eq__(id.strip())).all()