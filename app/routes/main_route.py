from flask import Blueprint, render_template,redirect,request,url_for
from app import login_manager
from flask_login import login_required,logout_user,current_user
import app.models as mdl
import app.controller.department_process as depp
import app.controller.notebook as nte
import app.controller.department_process as depp
import app.controller.history as his
from app.models import LichKham

main_bp = Blueprint('main', __name__)

# Cấu hình trang đăng nhập
login_manager.login_view = 'main.login'

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/medicalBook')
@login_required
def medical_book():

    return render_template('medicalBook.html',status_auth=current_user.user_id,user=current_user.user)

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
    list_lichkham = nte.get_examination_history()
    return render_template('medicalbook/schedule.html',list_lichkham=list_lichkham,name_department='sdfsf')

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
    return render_template('setting/passwd.html',name_user=current_user.name_account)

@main_bp.route('/appointment')
@login_required
def appointment():
    return render_template('appointment.html')

@main_bp.route('/appointmentLogin')
@login_required
def appointment_login():
    return render_template('appointmentLogin.html',packages=mdl.PackageMedical)


@main_bp.route('/appointment_body1')
def appointment1():
    date = request.args.get('date')
    time = request.args.get('time')
    location = request.args.get('location')
    package = request.args.get('package')

    #lay cac khoa
    list_khoa=depp.get_department()

    return render_template('appointment/body1.html',date=date, time=time, location=location, package=package,list_khoa=list_khoa)

@main_bp.route('/medicalPackage')
def medical_package():
    return render_template('medicalPackage/medicalPackage.html')

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
    list_lichkham = his.get_appointmant_all()
    return render_template('doctor/formDoctor.html',list_lichkham=list_lichkham)

@main_bp.route('/lookupDoctor')
def look_doctor():
    return render_template('doctor/lookupDoctor.html')

@main_bp.route('/settingDoctor')
def setting_doctor():
    return render_template('doctor/settingDoctor.html')

@main_bp.route('/scheduleDoctor')
def schedule_doctor():
    return render_template('doctor/scheduleDoctor.html')

@main_bp.route('/themeDoctor')
def theme_doctor():
    return render_template('doctor/themeDoctor.html')


@main_bp.route('/package')
def package_index():
    return render_template('detailPackage/package.html')
@main_bp.route('/packageNormal')
def package_normal():
    return render_template('detailPackage/packageNormal.html')

@main_bp.route('/packageVIP')
def package_vip():
    return render_template('detailPackage/packageVIP.html')

@main_bp.route('/packageNormalLG')
def package_normal_lg():
    return render_template('detailPackage/pkNormalLogin.html')

@main_bp.route('/packageVIPLG')
def package_vip_lg():
    return render_template('detailPackage/pkVIPLogin.html')

@main_bp.route('/formMedicine')
def form_medicine():
    return render_template('doctor/formMedicine.html')

@main_bp.route('/formConfirm')
def form_confirm():
    lich_id = request.args.get('lich_id')
    lichkham = his.get_appointment_id(lich_id)
    return render_template('doctor/formConfirm.html',lichkham=lichkham)

@main_bp.route('/authenticate')
def authenticate():
    return render_template('medicalbook/authenticate.html')




# nurse
@main_bp.route('/nurse')
def nurse():
    return render_template('home_nurse.html')
@main_bp.route('/scheduleNurse')
def schedule_nurse():
    return render_template('nurse/scheduleNurse.html')
@main_bp.route('/formNurse')
def form_nurse():
    list_lichkham = his.get_appointmant_all()
    return render_template('nurse/formNurse.html',list_lichkham=list_lichkham)

@main_bp.route('/lookupNurse')
def look_nurse():
    return render_template('nurse/lookupNurse.html')

@main_bp.route('/settingNurse')
def setting_nurse():
    return render_template('nurse/settingNurse.html')


@main_bp.route('/formCheck')
def form_check():
    lich_id = request.args.get('lich_id')
    lichkham=his.get_appointment_id(lich_id)
    return render_template('nurse/formCheck.html',lichkham=lichkham)

#cashier
@main_bp.route('/cashier')
def cashier():
    return render_template('home_cashier.html')
@main_bp.route('/scheduleCashier')
def schedule_cashier():
    return render_template('cashier/scheduleCashier.html')
@main_bp.route('/paymentInvoice')
def payment_invoice():
    return render_template('cashier/paymentInvoice.html')

@main_bp.route('/lookupCashier')
def look_cashier():
    return render_template('cashier/lookupCashier.html')

@main_bp.route('/settingCashier')
def setting_cashier():
    return render_template('cashier/settingCashier.html')

@main_bp.route('/formInvoice')
def view_Invoice():
    return render_template('cashier/formInvoice.html')

#admin
@main_bp.route('/admin')
def home_admin():
    return render_template('home_admin.html')
@main_bp.route('/regulations')
def regulation_admin():
    return render_template('admin/regulations.html')

@main_bp.route('/report')
def report_admin():
    return render_template('admin/report.html')
@main_bp.route('/searchAdmin')
def search_admin():
    return render_template('admin/search.html')
@main_bp.route('/settingAdmin')
def setting_admin():
    return render_template('admin/settingAdmin.html')

