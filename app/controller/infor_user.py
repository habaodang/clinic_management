from app import login_manager
from flask_login import current_user
from sqlalchemy import func
import hashlib
from app.models import User, Account, Patient, Doctor,Nurse
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

def add_infor_doctor(name,cccd,address,sex,birth,phone,role,degree,id_department):
    if name and cccd and address and sex and birth and phone:
        id=create_id(role)
        doctor = Doctor(id=id,name=name,cccd=cccd,address=address,phone=phone,sex=sex,birth=birth,degree=degree,id_department=id_department)
        db.session.add(doctor)
        db.session.commit()
        return id

def add_infor_nurse(name,cccd,address,sex,birth,phone,role,id_department):
    if name and cccd and address and sex and birth and phone:
        id=create_id(role)
        nurse = Nurse(id=id,name=name,cccd=cccd,address=address,phone=phone,sex=sex,birth=birth,id_department=id_department)
        db.session.add(nurse)
        db.session.commit()
        return id


def add_infor_cashier(name,cccd,address,sex,birth,phone,role):
    if name and cccd and address and sex and birth and phone:
        id=create_id(role)
        cashier = Nurse(id=id,name=name,cccd=cccd,address=address,phone=phone,sex=sex,birth=birth)
        db.session.add(cashier)
        db.session.commit()
        return id

def mapping_account(name_account,user_id):
    account=Account.query.filter(Account.name_account.__eq__(name_account.strip())).first()
    account.user_id=user_id
    db.session.commit()


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


