from datetime import datetime
from app import vnpay
from xml.etree.ElementTree import tostring

from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from app import login_manager
from flask_login import login_required,logout_user,current_user
import hashlib
import hmac
import urllib.parse

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
    return render_template('medicalBook.html',status_auth=current_user.user_id,user=current_user,name_user=current_user.name_account)

@main_bp.route('/register')
def register():
    return render_template('register.html')

@main_bp.route('/verify')
def verify():
    return render_template('verify.html')

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
@login_required
def medical_schedule():
    # Xóa tất cả thông báo flash
    session.pop('_flashes', None)
    try:
        # Kiểm tra người dùng đã đăng nhập và có thuộc tính user.id hay không
        patient_id = current_user.user.id

    except AttributeError as e:
        flash('Bạn chưa xác thực thông tin không thể vào lịch hen', 'error')
        return redirect(url_for('main.medical_book'))

    except Exception as e:
        flash(f'Đã xảy ra lỗi: {str(e)}', 'error')
        return redirect(url_for('main.medical_book'))
    else:
        if patient_id:
            # Lấy lịch khám dựa trên patient_id
            list_lichkham = nte.get_examination_history(id=patient_id)
            return render_template('medicalbook/schedule.html', list_lichkham=list_lichkham)
        else:
            flash('Không tìm thấy thông tin bệnh nhân.', 'error')
            return redirect(url_for('main.medical_book'))

@main_bp.route('/bill', methods=["GET","POST"])
def medical_bill():
    if request.method == "POST":
        bill = int(request.form.get("appointmentMoney"))
        order_id = str(current_user.id)+ datetime.now().__str__()
        vnpay_url = vnpay.generate_payment_url(order_id,bill)
        return redirect(vnpay_url)
    return render_template('medicalbook/bill.html',name_user=current_user.name_account)

@main_bp.route('/history')
def medical_history():
    return render_template('medicalbook/history.html',name_user=current_user.name_account)

@main_bp.route('/setting')
def setting():
    return render_template('setting.html',name_user=current_user.name_account)

@main_bp.route('/theme')
def setting_theme():
    return render_template('setting/theme.html',name_user=current_user.name_account)

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
    return render_template('appointmentLogin.html',packages=mdl.PackageMedical,name_user=current_user.name_account)


@main_bp.route('/appointment_body1')
def appointment1():
    date = request.args.get('date')
    time = request.args.get('time')
    location = request.args.get('location')
    package = request.args.get('package')

    #lay cac khoa
    list_khoa=depp.get_department()
    doctors=depp.get_doctor()

    return render_template('appointment/body1.html',date=date, time=time, location=location, package=package,list_khoa=list_khoa,doctors=doctors)

@main_bp.route('/medicalPackage')
def medical_package():
    return render_template('medicalPackage/medicalPackage.html',name_user=current_user.name_account)

@main_bp.route('/specialty')
def specialty():
    return render_template('specialty/specialty.html',name_user=current_user.name_account)

@main_bp.route('/medicalPackageLogin')
def package_login():
    return render_template('medicalPackage/medicalPackageLogin.html')

@main_bp.route('/specialtyLogin')
def specialty_login():
    return render_template('specialty/specialtyLogin.html',name_user=current_user.name_account)

@main_bp.route('/CDCH')
def department_cdch():
    return render_template('department/CDCH.html')

@main_bp.route('/CDCHLogin')
def department_chchlogin():
    return render_template('department/CDCHLogin.html')

@main_bp.route('/CXK')
def department_cxk():
    return render_template('department/CXK.html')

@main_bp.route('/CXKLogin')
def department_cxklogin():
    return render_template('department/CXKLogin.html')

@main_bp.route('/DaLieu')
def department_dalieu():
    return render_template('department/DaLieu.html')

@main_bp.route('/DaLieuLogin')
def department_dalieulogin():
    return render_template('department/DaLieuLogin.html')

@main_bp.route('/NhiKhoa')
def department_nhikhoa():
    return render_template('department/NhiKhoa.html')

@main_bp.route('/NhiKhoaLogin')
def department_nhikhoalogin():
    return render_template('department/NhiKhoaLogin.html')

@main_bp.route('/RHM')
def department_rhm():
    return render_template('department/RHM.html')

@main_bp.route('RHMLogin')
def department_rhmlogin():
    return render_template('department/RHMLogin.html')

@main_bp.route('/SPK')
def department_spk():
    return render_template('department/SPK.html')

@main_bp.route('/SPKLogin')
def department_spklogin():
    return render_template('department/SPKLogin.html')

@main_bp.route('/doctor')
def doctor():
    return render_template('home_doctor.html',user=current_user)

@main_bp.route('/base')
def base():
    return render_template('layout/base_doctor.html',user=current_user)

@main_bp.route('/formDoctor')
def form_doctor():
    id=current_user.user.id
    list_lichkham = his.get_appointment_present_id(id)
    return render_template('doctor/formDoctor.html',list_lichkham=list_lichkham,user=current_user)

@main_bp.route('/lookupDoctor')
def look_doctor():
    return render_template('doctor/lookupDoctor.html',user=current_user)
@main_bp.route('/tbDoctor')
def tbDoctor():
    return render_template('home_doctor.html',user=current_user)

@main_bp.route('/settingDoctor')
def setting_doctor():
    account=current_user
    return render_template('doctor/settingDoctor.html',account=account,user=current_user)

@main_bp.route('/scheduleDoctor')
def schedule_doctor():
    return render_template('doctor/scheduleDoctor.html',user=current_user)

@main_bp.route('/themeDoctor')
def theme_doctor():
    return render_template('doctor/themeDoctor.html',user=current_user)

@main_bp.route('/packageNormal')
def package_normal():
    return render_template('detailPackage/packageNormal.html')

@main_bp.route('/packageVIP')
def package_vip():
    return render_template('detailPackage/packageVIP.html')

@main_bp.route('/packageNormalLG')
def package_normal_lg():
    return render_template('detailPackage/pkNormalLogin.html',name_user=current_user.name_account)

@main_bp.route('/packageVIPLG')
def package_vip_lg():
    return render_template('detailPackage/pkVIPLogin.html',name_user=current_user.name_account)

@main_bp.route('/formMedicine')
def form_medicine():
    return render_template('doctor/formMedicine.html',user=current_user)

@main_bp.route('/formConfirm')
def form_confirm():
    lich_id = request.args.get('lich_id')
    lichkham = his.get_appointment_id(lich_id)
    return render_template('doctor/formConfirm.html',lichkham=lichkham,user=current_user)

@main_bp.route('/authenticate')
def authenticate():
    return render_template('medicalbook/authenticate.html,user=current_user')

# nurse
@main_bp.route('/nurse')
def nurse():
    return render_template('home_nurse.html',user=current_user)

@main_bp.route('/scheduleNurse')
def schedule_nurse():
    return render_template('nurse/scheduleNurse.html',user=current_user)
@main_bp.route('/formNurse')
def form_nurse():
    list_lichkham = his.get_appointmant_all()
    count_lichkham_all=his.count_apointment_all()
    return render_template('nurse/formNurse.html',list_lichkham=list_lichkham,count_lichkham_all=count_lichkham_all,user=current_user)

@main_bp.route('/lookupNurse')
def look_nurse():
    return render_template('nurse/lookupNurse.html',user=current_user)

@main_bp.route('/settingNurse')
def setting_nurse():
    return render_template('nurse/settingNurse.html',user=current_user)


@main_bp.route('/formCheck')
def form_check():
    lich_id = request.args.get('lich_id')
    lichkham=his.get_appointment_id(lich_id)
    return render_template('nurse/formCheck.html',lichkham=lichkham,user=current_user)

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

@main_bp.route('/addAdmin')
def add_admin():
    list_khoa = depp.get_department()
    return render_template('admin/addAdmin.html',roles=mdl.UserRole,list_khoa=list_khoa)

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



