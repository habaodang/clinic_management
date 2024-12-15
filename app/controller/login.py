import hashlib
import app.models as mdl
from app import login_manager


#kiem tra tai khoan mat khau co chinh xac
def check_login(user_name,password):
    # name va password khong null
    if user_name and password:
        password=str(hashlib.md5(password.strip().encode('utf-8')).hexdigest()) # bam mat khau
        return  mdl.Account.query.filter(mdl.Account.name_account.__eq__(user_name.strip()),mdl.Account.password.__eq__(password)).first()

#kiem tra trang thai co dang nhap
def is_active(id_account):
    if id_account:
        account=mdl.Account.query.filter(mdl.Account.id.__eq__(id_account)).first()
        return account.status

# Định nghĩa user_loader
@login_manager.user_loader
def load_user(user_id):

    # Tìm người dùng trong cơ sở dữ liệu dựa trên user_id
    return mdl.Account.query.get(int(user_id))

