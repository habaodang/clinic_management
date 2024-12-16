
import hashlib
from app.models import Account
from app import db

def create_account(name_account, password, email, role):
    if name_account and password and role:
        hashed_password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        account = Account(name_account=name_account, password=hashed_password, email=email, role=role)
        db.session.add(account)
        db.session.commit()
        return 'Tạo tài khoản thành công'
    return 'Tạo tài khoản không thành công'


