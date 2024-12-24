from app import login_manager
from flask_login import current_user
from sqlalchemy import func
import hashlib
from app.models import User,Account,Patient
from app import db
import re

#tao ma user
def create_id(role):

    id=role[0:2].upper()
    count = User.query.filter(User.id.like(f"{id}%")).count()+1
    return f'{id}{count:08d}'

#xac thuc thong tin
def add_infor_user(name,cccd,address,sex,birth,phone):
    if name and cccd and address and sex and birth and phone:
        v_role = current_user.role.value
        id=create_id(v_role)
        patient = Patient(id=id,name=name,cccd=cccd,address=address,phone=phone,sex=sex,birth=birth)
        db.session.add(patient)
        db.session.commit()
        return id

# lien ket mot account voi mot thong tin user
def mapping_account_user(user_id):
    current_user.user_id=user_id
    db.session.commit()

def is_format_password(password):
    if len(password) < 8:
        return False, "Mật khẩu phải có ít nhất 8 ký tự."

    if not re.search(r'[A-Z]', password):
        return False, "Mật khẩu phải chứa ít nhất một chữ cái viết hoa."

    if not re.search(r'[a-z]', password):
        return False, "Mật khẩu phải chứa ít nhất một chữ cái viết thường."

    if not re.search(r'\d', password):
        return False, "Mật khẩu phải chứa ít nhất một chữ số."

    if not re.search(r'[!@#$%^&*()\-_=+]', password):
        return False, "Mật khẩu phải chứa ít nhất một ký tự đặc biệt (!@#$%^&*()-_+=)."

    return True, "Mật khẩu hợp lệ."

def change_password(id,password):
    pass


