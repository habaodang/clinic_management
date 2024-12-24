from flask import Blueprint, render_template, redirect, url_for, request,session,flash
from flask_login import login_user, logout_user,current_user,login_required
from datetime import datetime
import app.controller.infor_user as inf
import app.controller.create_account as cra

admin = Blueprint('admin', __name__)

@admin.route('/admin/aduser', methods=['GET', 'POST'])
def add_user_ad():
    if request.method.__eq__('POST'):
        name_account = request.form.get('name_account')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        role = request.form.get('role')

        result, mess = inf.is_format_password(password)

        if result:
            if password == confirm_password:
                account = cra.create_account(name_account=name_account,password=password, email=email,role=role)
                return redirect(url_for('main.add_admin'))
            else:
                flash('Mật khẩu không khớp', 'error')
                return redirect(url_for('main.add_admin'))
        else:
            flash(mess, 'error')
            return redirect(url_for('main.add_admin'))

    flash('Đăng ký thất bại không tìm thấy dữ liêu', 'error')
    # Hiển thị trang đăng ký
    return redirect(url_for('main.add_admin'))
