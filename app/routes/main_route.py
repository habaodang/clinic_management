from datetime import datetime
from app import vnpay
from xml.etree.ElementTree import tostring

from flask import Blueprint, render_template,redirect,request,url_for
from app import login_manager
from flask_login import login_required,logout_user,current_user
import hashlib
import hmac
import urllib.parse


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

@main_bp.route('/bill', methods=["GET","POST"])
def medical_bill():
    if request.method == "POST":
        bill = int(request.form.get("appointmentMoney"))
        order_id = str(current_user.id)+ datetime.now().__str__()
        vnpay_url = vnpay.generate_payment_url(order_id,bill)
        return redirect(vnpay_url)
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

@main_bp.route('/formDoctor')
def form_doctor():
    return render_template('doctor/formDoctor.html')

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
    return render_template('doctor/formConfirm.html')

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
    return render_template('nurse/formNurse.html')

@main_bp.route('/lookupNurse')
def look_nurse():
    return render_template('nurse/lookupNurse.html')

@main_bp.route('/settingNurse')
def setting_nurse():
    return render_template('nurse/settingNurse.html')
@main_bp.route('/formCheck')
def form_check():
    return render_template('nurse/formCheck.html')

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
def view_invoice():
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

@main_bp.route('/billSuccess')
def payment_return():
    query_params = request.args.to_dict()
    vnp_secure_hash = query_params.pop("vnp_SecureHash", None)
    sorted_params = sorted(query_params.items())
    query_string = "&".join(f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in sorted_params)
    hmac_obj = hmac.new(vnpay.VNP_HASH_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha512)
    expected_hash = hmac_obj.hexdigest()

    is_success = True

    if vnp_secure_hash == expected_hash and query_params.get("vnp_ResponseCode") == "00":
        return render_template("bill_success.html", is_success=True)
    else:
        return render_template("bill_success.html", is_success=False)

