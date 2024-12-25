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

        return redirect(url_for('main.form_medicine',symptom=symptom,predict=predict))

@doctor.route('/doctor/add-medicine', methods=['GET', 'POST'])
def add_medicine():
    if request.method == 'POST':

        symptom = request.form.get('symptom')
        predict = request.form.get('predict')

        medicineCode = request.form.get('medicineCode')
        medicineName = request.form.get('medicineName')
        medicineUnit = request.form.get('medicineUnit')
        medicineQuantity = request.form.get('medicineQuantity')
        medicineEffect = request.form.get('medicineEffect')
        medicineUsage = request.form.get('medicineUsage')


@doctor.route('/infor-doctor', methods=['GET', 'POST'])
def infor_doctor():
    if request.method == 'POST':
        name = request.form.get('name')
        cccd = request.form.get('cccd')
        address = request.form.get('address')
        sex = request.form.get('sex')
        birth = request.form.get('birth')
        phone = request.form.get('sdt')
        id = in_u.add_infor_user(name, cccd, address, sex, birth, phone)
        in_u.mapping_account_user(id)