from flask import Blueprint
from app.controller import qr
from flask import render_template, request, redirect
from flask_login import login_user, logout_user

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route("/logout")
def logout_process():
    logout_user()
    return redirect('/login')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('register.html')



