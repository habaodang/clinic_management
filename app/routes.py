
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)
@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/doctor')
def doctor():
    return render_template('home_doctor.html')

@bp.route('/base')
def base():
    return render_template('layout/base.html')

@bp.route('/formDoctor')
def form_doctor():
    return render_template('doctor/formDoctor.html')

@bp.route('/lookupDoctor')
def look_doctor():
    return render_template('doctor/lookupDoctor.html')
@bp.route('/tbDoctor')
def tbDoctor():
    return render_template('home_doctor.html')

@bp.route('/settingDoctor')
def setting_doctor():
    return render_template('doctor/settingDoctor.html')

@bp.route('/scheduleDoctor')
def schedule_doctor():
    return render_template('doctor/scheduleDoctor.html')
@bp.route('/themeDoctor')
def themeDoctor():
    return render_template('doctor/themeDoctor.html')

