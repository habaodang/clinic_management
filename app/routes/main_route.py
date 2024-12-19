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

@main_bp.route('/indexLogin')
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

@main_bp.route('/appointmentLogin')
@login_required
def appointment_login():
    return render_template('appointmentLogin.html')


@main_bp.route('/appointment_body1')
def appointment1():
    return render_template('appointment/body1.html')

@main_bp.route('/medicalPackage')
def medical_package():
    return render_template('medicalPackage.html')

@main_bp.route('/specialty')
def specialty():
    return render_template('specialty.html')


@main_bp.route('/medicalPackageLogin')
def package_login():
    return render_template('medicalPackage/medicalPackageLogin.html')

@main_bp.route('/specialtyLogin')
def specialty_login():
    return render_template('specialty/specialtyLogin.html')

@main_bp.route('/khoa')
def department_khoa():
    return render_template('department/khoa.html')

@main_bp.route('/khoaLogin')
def department_login():
    return render_template('department/khoaLogin.html')

@main_bp.route('/doctor')
def doctor():
    return render_template('home_doctor.html')

@main_bp.route('/base')
def base():
    return render_template('layout/base_doctor.html')

@main_bp.route('/formDoctor')
def form_doctor():
    return render_template('doctor/formDoctor.html')

@main_bp.route('/lookupDoctor')
def look_doctor():
    return render_template('doctor/lookupDoctor.html')
@main_bp.route('/tbDoctor')
def tbDoctor():
    return render_template('home_doctor.html')

@main_bp.route('/settingDoctor')
def setting_doctor():
    return render_template('doctor/settingDoctor.html')

@main_bp.route('/scheduleDoctor')
def schedule_doctor():
    return render_template('doctor/scheduleDoctor.html')

@main_bp.route('/themeDoctor')
def themeDoctor():
    return render_template('doctor/themeDoctor.html')


@main_bp.route('/package')
def package_index():
    return render_template('detailPackage/package.html')

@main_bp.route('/packageLogin1')
def package_login1():
    return render_template('detailPackage/packageLogin1.html')


@main_bp.route('/formMedicine')
def form_medicine():
    return render_template('doctor/formMedicine.html')

@main_bp.route('/formConfirm')
def form_confirm():
    return render_template('doctor/formConfirm.html')

@main_bp.route('/authenticate')
def authenticate():
    return render_template('medicalbook/authenticate.html')


