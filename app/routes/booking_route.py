from flask import Blueprint, render_template, redirect, url_for, request,session
from flask_login import login_user, logout_user,current_user
import app.models as mdl
import app.controller.medical_book as med
import app.controller.convert_data as cnv

booking = Blueprint('booking', __name__)

@booking.route('booking/form1', methods=['GET', 'POST'])
def get_booking_first_form():
    if request.method == 'POST':
        date = request.form.get('date')
        time = request.form.get('time')
        location = request.form.get('location')
        package = request.form.get('package')

        return redirect(url_for('main.appointment1', date=date, time=time, location=location, package=package))

@booking.route('booking/form2', methods=['GET', 'POST'])
def get_booking_second_form():
    if request.method == 'POST':
        # Lấy dữ liệu từ form 1
        date = request.form.get('date')
        time = request.form.get('time')
        location = request.form.get('location')
        package = request.form.get('package')

        # du lieu tu form 2
        doctor = request.form.get('doctor')
        department = request.form.get('department')
        note = request.form.get('note')

        #xu ly du lieu chuyen du lieu thoi gian
        time_conv=cnv.convert_to_time(time)

        print(doctor)
        mess=med.add_booking(date=date,time=time_conv,location=location,package=package,doctor_id=doctor,department_id=department,note=note)


        return redirect(url_for('main.index_login'))


