from app import login_manager
from flask_login import current_user
from sqlalchemy import func
import hashlib
from app.models import User,Account
from app import db


def create_id(role):

    id=role[0:2].upper()
    count = User.query.filter(User.id.like(f"{id}%")).count()+1
    return f'{id}{count:08d}'

def add_infor_user(name,cccd,address,sex,birth,phone):
    if name and cccd and address and sex and birth and phone:
        v_role = current_user.role.value
        id=create_id(v_role)
        user = User(id=id,name=name,cccd=cccd,address=address,phone=phone,sex=sex,birth=birth)
        db.session.add(user)
        db.session.commit()
        return id


def mapping_account_user(user_id):
    current_user.user_id=user_id
    db.session.commit()
