from flask import Blueprint, render_template, render_template_string, redirect
from flask_login import logout_user

bp = Blueprint('main', __name__)

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

@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/appointment')
def appointment():
    return render_template('appointment.html')

@bp.route('/appointment_body1')
def appointment1():
    return render_template('appointment/body1.html')

