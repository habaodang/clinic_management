
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)
@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/doctor')
def doctor():
    return render_template('home_doctor.html')


