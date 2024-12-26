from flask import Blueprint, render_template, redirect, url_for, request,session,jsonify
from flask_login import login_user, logout_user,current_user,login_required
from datetime import datetime
import app.controller.history as his
import app.controller.PDF as pdf
import app.controller.medicine as medicine
from app.models import Thuoc

doctor = Blueprint('doctor', __name__)

@doctor.route('/doctor/sick-predict', methods=['GET', 'POST'])
def sick_predict():
    if request.method == 'POST':
        symptom = request.form.get('symptom')
        predict = request.form.get('predict')

        session['symptom']=symptom
        session['predict']=predict

        return redirect(url_for('main.form_medicine'))

@doctor.route('/doctor/add-medicine', methods=['GET', 'POST'])
def add_medicine():
    if request.method == 'POST':
        medicineCode = request.form.get('medicineCode')
        medicineName = request.form.get('medicineName')
        medicineUnit = request.form.get('medicineUnit')
        medicineQuantity = request.form.get('medicineQuantity')
        medicineEffect = request.form.get('medicineEffect')
        medicineUsage = request.form.get('medicineUsage')


@doctor.route('/doctor/search-medicine', methods=['POST'])
def search_medicine():
    if request.method == 'POST':
        # Lấy tên thuốc từ request
        search_medicine_name = request.json.get('search_medicine', '').strip()  # Lấy tên thuốc từ frontend

        if not search_medicine_name:
            return jsonify([])  # Nếu không có tên thuốc, trả về danh sách rỗng

        # Sử dụng SQLAlchemy để tìm kiếm thuốc theo tên
        results = Thuoc.query.filter(Thuoc.name.ilike(f"%{search_medicine_name}%")).all()

        # Tạo danh sách kết quả trả về dưới dạng JSON
        result_list = [
            {
                "id": med.id,
                "name": med.name,
                "unit": med.unit,
                "quantity": med.quantity
            }
            for med in results
        ]

        # Trả về kết quả dưới dạng JSON
        return jsonify(result_list)


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