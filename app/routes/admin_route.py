from flask import Blueprint, render_template, redirect, url_for, request,session,flash, jsonify
from flask_login import login_user, logout_user,current_user,login_required
from datetime import datetime
import app.controller.infor_user as inf
import app.controller.create_account as cra
import app.models as mdl
import app.controller.infor_user as in_u

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
                name = request.form.get('name')
                cccd = request.form.get('cccd')
                address = request.form.get('address')
                sex = request.form.get('sex')
                birth = request.form.get('birth')
                phone = request.form.get('sdt')

                print(role)
                if role == 'DOCTOR':
                    id_department = request.form.get('department')
                    qualification = request.form.get('qualification')
                    id = in_u.add_infor_doctor(name, cccd, address, sex, birth, phone,role=role,degree=qualification,id_department=id_department)
                    in_u.mapping_account(name_account=name_account,user_id=id)

                    return redirect(url_for('main.add_admin'))

                if role == 'NURSE':
                    id_department = request.form.get('department')
                    id = in_u.add_infor_nurse(name, cccd, address, sex, birth, phone, role=role,id_department=id_department)
                    in_u.mapping_account(name_account=name_account, user_id=id)
                    return redirect(url_for('main.add_admin'))

                if role == 'CASHIER':
                    id = in_u.add_infor_cashier(name, cccd, address, sex, birth, phone, role=role)
                    in_u.mapping_account(name_account=name_account, user_id=id)
                    return redirect(url_for('main.add_admin'))

                if role == 'PATIENT':
                    id = in_u.add_infor_user(name, cccd, address, sex, birth, phone)
                    in_u.mapping_account_user(id)
                    return redirect(url_for('main.add_admin'))

                return 'ko dc'

            else:
                flash('Mật khẩu không khớp', 'error')
                return redirect(url_for('main.add_admin'))
        else:
            flash(mess, 'error')
            return redirect(url_for('main.add_admin'))

    flash('Đăng ký thất bại không tìm thấy dữ liêu', 'error')
    # Hiển thị trang đăng ký
    return redirect(url_for('main.add_admin'))
@admin.route('/report')
def report():
    return render_template('report.html')

@admin.route('/api/revenue')
def get_revenue_data():
    data = {
        "labels": ["01/09", "02/09", "03/09", "04/09"],
        "revenues": [10322000, 10020000, 10322000, 10322000]
    }
    return jsonify(data)