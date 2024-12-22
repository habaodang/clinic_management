from flask import Blueprint, render_template, redirect, url_for, request,session
from flask_login import login_user, logout_user,current_user
import app.controller.login as lg
import app.controller.create_account as cra
import app.models as mdl


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login/data', methods=['GET', 'POST'])
def user_signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = lg.check_login(username, password)
        if user:
            login_user(user)
            return redirect(url_for('main.index_login'))

        return 'Login failed'
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/register/data', methods=['GET', 'POST'])
def user_register():
    if request.method.__eq__('POST'):
        user_name = request.form.get('name_user')
        password = request.form.get('password')
        re_en_password = request.form.get('re_en_password')
        email = request.form.get('email')
        if password == re_en_password:
            account = cra.create_account(name_account=user_name, password=password, email=email, role=mdl.UserRole.USER)
            return redirect(url_for('main.index'))
        else:
            return 'khong dk'
    return 'khong dk'



