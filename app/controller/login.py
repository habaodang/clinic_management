import hashlib
import app.models as mdl

def check_login(user_name,password):
    # name va password khong null
    if user_name and password:
        password=str(hashlib.md5(password.strip().encode('utf-8')).hexdigest()) # bam mat khau
        return  mdl.Account.query.filter(mdl.Account.name_account.__eq__(user_name.strip()),mdl.Account.password.__eq__(password))

