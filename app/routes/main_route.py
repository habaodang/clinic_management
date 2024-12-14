from flask import Blueprint, render_template

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

@main_bp.route('/index-login')
def index_login():
    return render_template('indexLogin.html')

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/logout')
def logout_process():
    logout_user()
    return redirect('/login')

@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/indexLogin')
def index_login():
    return render_template('indexLogin.html')


@bp.route('/medicalBook')
def medical_book():
    return render_template('medicalBook.html')


@bp.route('/schedule')
def medical_schedule():
    return render_template('medicalbook/schedule.html')

@bp.route('/bill')
def medical_bill():
    return render_template('medicalbook/bill.html')

@bp.route('/history')
def medical_history():
    return render_template('medicalbook/history.html')

@bp.route('/setting')
def setting():
    return render_template('setting.html')

@bp.route('/info')
def setting_info():
    return render_template('setting/info.html')

@bp.route('/theme')
def setting_theme():
    return render_template('setting/theme.html')

@bp.route('/passwd')
def setting_passwd():
    return render_template('setting/passwd.html')

@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/appointment')
def appointment():
    return render_template('appointment.html')

@bp.route('/appointment_body1')
def appointment1():
    return render_template('appointment/body1.html')

@bp.route('/medicalPackage')
def medical_package():
    return render_template('medicalPackage.html')

@bp.route('/specialty')
def specialty():
    return render_template('specialty.html')

