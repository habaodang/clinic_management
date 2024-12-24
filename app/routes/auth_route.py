from flask import Blueprint, render_template, redirect, url_for, request,session,flash
from flask_login import login_user, logout_user,current_user
import hashlib

from flask import Blueprint, render_template, redirect, url_for, request, session, jsonify
from flask_login import login_user, logout_user, current_user
import app.controller.login as lg
import app.controller.create_account as cra
import app.controller.infor_user as inf
import app.models as mdl
from werkzeug.security import generate_password_hash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/verify', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        otp = request.form.get('otp')

        # Kiểm tra mã OTP
        if otp == session.get('verification_code'):
            # Lấy thông tin người dùng từ session
            user_registration = session.get('user_registration')
            user_name = user_registration['name_user']
            password = user_registration['password']
            email = user_registration['email']

            # Tạo đối tượng Account thay vì User
            account = mdl.Account(
                name_account=user_name,
                email=email,
                password=password,
                role=mdl.UserRole.USER  # Hoặc vai trò khác tùy thuộc vào yêu cầu
            )

            # Tạo đối tượng User
            user = mdl.User(
                id=account.user_id,
            )

            # Lưu Account vào cơ sở dữ liệu
            mdl.db.session.add(account)
            mdl.db.session.commit()

            login_user(account)

            # Xóa thông tin tạm thời khỏi session
            session.pop('user_registration', None)
            session.pop('verification_code', None)

            # Chuyển hướng tới trang chủ hoặc trang đăng nhập
            return redirect(url_for('main.login'))  # Hoặc trang khác bạn muốn

        else:
            # Nếu mã OTP không đúng
            return render_template('verify.html', error_message="Mã OTP không đúng. Vui lòng thử lại.")

    return render_template('verify.html')

# Hàm tạo mã xác thực ngẫu nhiên
def generate_verification_code(length=6):
    return ''.join(random.choices('0123456789', k=length))


def send_verification_email(user_email, user_name, verification_code):
    # Cấu hình trực tiếp thông tin email và mật khẩu
    sender_email = 'lehongduc201204@gmail.com'  # Thay bằng email của bạn
    sender_password = 'oade kznb ccvc vgnt'  # Thay bằng mật khẩu hoặc mật khẩu ứng dụng

    subject = "Xác Thực Tài Khoản"
    body = f"""
    Chào {user_name},

    Đây là mã xác thực tài khoản của bạn:
    ---------------------------
    Mã xác thực: {verification_code}
    ---------------------------

    Vui lòng nhập mã này vào trang web để hoàn tất đăng ký.

    Trân trọng,
    Đội Hỗ Trợ
    """

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = user_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user_email, message.as_string())
        return True
    except Exception as e:
        print(f"Lỗi gửi email: {e}")
        return False
# Route đăng nhập
@auth_bp.route('/login/data', methods=['GET', 'POST'])
def user_signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = lg.check_login(username, password)
        if user:
            login_user(user)
            if user.role == mdl.UserRole.DOCTOR:
                return redirect(url_for('main.doctor'))
            if user.role == mdl.UserRole.NURSE:
                return redirect(url_for('main.nurse'))
            if user.role == mdl.UserRole.PATIENT:
                return redirect(url_for('main.index_login'))

        flash('Tài khoản hoặc mật khẩu không chính xác', 'error')

        return redirect(url_for('main.login'))
    return redirect(url_for('main.login'))

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
        # result,mess=inf.is_format_password(password)

        if password == re_en_password:
            account = cra.create_account(name_account=user_name, password=password, email=email,
                                         role=mdl.UserRole.PATIENT)
            return redirect(url_for('main.login'))

    #     if result:
    #         if password == re_en_password:
    #             account = cra.create_account(name_account=user_name, password=password, email=email, role=mdl.UserRole.PATIENT)
    #             return redirect(url_for('main.login'))
    #         else:
    #             flash('Mật khẩu không khớp', 'error')
    #             return redirect(url_for('main.register'))
    #     else:
    #         flash(mess, 'error')
    #         return redirect(url_for('main.register'))
    # flash('Đăng ký thất bại không tìm thấy dữ liêu', 'error')
    return redirect(url_for('main.register'))

        # Kiểm tra mật khẩu và xác nhận mật khẩu
        if password != re_en_password:
            return 'Mật khẩu không khớp. Vui lòng thử lại.'

        # Mã hóa mật khẩu trước khi lưu
        hashed_password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        # Tạo mã xác thực ngẫu nhiên
        verification_code = generate_verification_code()

        # Lưu thông tin đăng ký tạm thời vào session
        session['verification_code'] = verification_code
        session['user_registration'] = {
            'name_user': user_name,
            'password': hashed_password,
            'email': email
        }

        # Gửi email xác thực
        if send_verification_email(email, user_name, verification_code):
            # Chuyển hướng tới file `verify.html` để nhập mã OTP
            return render_template('verify.html')
        else:
            # Nếu gửi email thất bại, thông báo lỗi
            return 'Không thể gửi email xác thực. Vui lòng thử lại sau.'

    # Hiển thị trang đăng ký
    return render_template('register.html')
