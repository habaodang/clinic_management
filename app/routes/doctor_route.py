from flask import Blueprint, render_template, redirect, url_for, request,session
from flask_login import login_user, logout_user,current_user,login_required
from datetime import datetime
import app.controller.history as his
import app.controller.PDF as pdf

doctor = Blueprint('doctor', __name__)

@doctor.route('/doctor/sick-predict', methods=['GET', 'POST'])
def sick_predict():
    if request.method == 'POST':

        symptom = request.form.get('symptom')
        predict = request.form.get('predict')

        return redirect(url_for('main.form_medicine'))
