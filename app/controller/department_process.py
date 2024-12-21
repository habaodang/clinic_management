from app import login_manager
from flask_login import current_user
from app.models import User,Account,LichKham,Department
from app import db

def get_department():
    return Department.query.all()

def get_name_department(id):
    khoa= Department.query.filter(Department.id.__eq__(id.strip())).first()
    return khoa.name
