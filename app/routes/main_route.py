from flask import Blueprint, render_template,redirect,request,url_for
from app import login_manager
from flask_login import login_required,logout_user,current_user

main_bp = Blueprint('main', __name__)

# Cấu hình trang đăng nhập
login_manager.login_view = 'main.login'

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/medicalBook')
@login_required
def medical_book():

    return render_template('medicalBook.html',status_auth=current_user.user_id)

@main_bp.route('/register')
def register():
    return render_template('register.html')

@main_bp.route('/login')
def login():
    return render_template('login.html')

@main_bp.route('/index-login')
def index_login():
    name_user=request.args.get('name','Khách')
    return render_template('indexLogin.html',name_user=current_user.name_account,status_auth=current_user.user_id)

@main_bp.route('/logout')
def logout_process():
    logout_user()
    return redirect(url_for('main.index'))

@main_bp.route('/schedule')
def medical_schedule():
    return render_template('medicalbook/schedule.html')

@main_bp.route('/bill')
def medical_bill():
    return render_template('medicalbook/bill.html')

@main_bp.route('/history')
def medical_history():
    return render_template('medicalbook/history.html')

@main_bp.route('/setting')
def setting():
    return render_template('setting.html')

@main_bp.route('/info')
def setting_info():
    return render_template('setting/info.html')

@main_bp.route('/theme')
def setting_theme():
    return render_template('setting/theme.html')

@main_bp.route('/passwd')
def setting_passwd():
    return render_template('setting/passwd.html')

@main_bp.route('/appointment')
@login_required
def appointment():
    return render_template('appointment.html')

@main_bp.route('/appointment_body1')
def appointment1():
    return render_template('appointment/body1.html')

@main_bp.route('/medicalPackage')
def medical_package():
    return render_template('medicalPackage.html')

@main_bp.route('/specialty')
def specialty():
    return render_template('specialty.html')