from flask import Blueprint, render_template, redirect, url_for, request,session
from flask_login import login_user, logout_user,current_user,login_required
import app.controller.infor_user as in_u
import app.controller.notebook as nte
import app.controller.hoadon as hdon

import app.models as mdl

note_book = Blueprint('notebook', __name__)

#lay thong tin xac thuc thong tin nguoi dung
@login_required
@note_book.route('/authenticate',methods=['GET','POST'])
def authenticate():
    if request.method == 'POST':
        name = request.form.get('name')
        cccd = request.form.get('cccd')
        address = request.form.get('address')
        sex = request.form.get('sex')
        birth = request.form.get('birth')
        phone = request.form.get('sdt')
        id = in_u.add_infor_user(name, cccd, address, sex, birth, phone)
        in_u.mapping_account_user(id)
        return redirect(url_for('main.index_login'))

# @login_required
# @note_book.route('/examination_history')
# def examination_history():
#
#     return f'{lichkham}'

# @note_book.route('/bill')
# def notebook_bill():


