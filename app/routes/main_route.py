from flask import Blueprint, render_template,redirect

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/medicalBook')
def medical_book():
    return render_template('medicalBook.html')

@main_bp.route('/register')
def register():
    return render_template('register.html')

@main_bp.route('/login')
def login():
    return render_template('login.html')

@main_bp.route('/indexLogin')
def index_login():
    return render_template('indexLogin.html')

@main_bp.route('/logout')
def logout_process():
    return redirect('/login')

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
def appointment():
    return render_template('appointment.html')

@main_bp.route('/appointment_body1')
def appointment1():
    return render_template('appointment/body1.html')

@main_bp.route('/medicalPackage')
def medical_package():
    return render_template('medicalPackage/medicalPackage.html')

@main_bp.route('/specialty')
def specialty():
    return render_template('specialty/specialty.html')

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

@main_bp.route('/package')
def package_index():
    return render_template('detailPackage/package.html')

@main_bp.route('/packageLogin1')
def package_login1():
    return render_template('detailPackage/packageLogin1.html')