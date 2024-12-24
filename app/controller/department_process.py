from app import login_manager
from flask_login import current_user
from app.models import User,Account,LichKham,Department,Doctor
from app import db

def get_department():
    return Department.query.all()

def get_name_department(id):
    khoa= Department.query.filter(Department.id.__eq__(id.strip())).first()
    return khoa.name

def get_doctor():
    return Doctor.query.all()

def get_doctor_by_id(id):
    if id:
        return Doctor.query.filter(Doctor.id.__eq__(id.strip())).first()
    else:
        return None