from flask_login import login_user, logout_user
from flask import Blueprint, render_template, render_template_string, redirect,request,url_for
import app.controller.qr as qr
import app.controller.login as lg

bp = Blueprint('login', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route("/logout")
def logout_process():
    logout_user()
    return redirect(url_for('login'))

@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/indexLogin')
def index_login():
    return render_template('indexLogin.html')


@bp.route('/medicalBook')
def medical_book():
    return render_template('medicalBook.html')


@bp.route('/setting')
def setting():
    return render_template('setting.html')

@bp.route('/register')
def register():
    return render_template('register.html')


@bp.route('/user-login',methods=['POST','GET'])
def user_signin():
    if request.method.__eq__('POST'):
        user_name=request.form.get('username')
        password=request.form.get('password')

        user=lg.check_login(user_name=user_name, password=password)
        if user:
            return redirect(url_for('login.index_login'))
        else:
            return 'khong dk'
    return 'khong dk'

    # return render_template('login.html')