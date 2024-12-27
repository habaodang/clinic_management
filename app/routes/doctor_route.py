from flask import Blueprint, render_template, redirect, url_for, request,session,jsonify
from flask_login import login_user, logout_user,current_user,login_required
from datetime import datetime
import app.controller.history as his
import app.controller.PDF as pdf
import app.controller.medicine as medicine
import app.controller.doctor as dct
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
        medicineCode = request.form.get('medicineId')
        medicinequan = request.form.get('medicinequan')

        print('code thuoc ',medicineCode)
        print('sl thuoc ',medicinequan)
        symptom=session['symptom']
        predict = session['predict']
        id_patient= session['id_patient']
        id_lichkham= session['lich_id']

        id_phieukham=dct.them_phieu_kham(trieuchung=symptom, chandoan=predict, patient_id=id_patient, doctor_id=current_user.user.id)
        id_hoadon=dct.them_hoadon(id_phieukham)
        id_chitietdon=dct.them_chitietdonthuoc(  hoa_don_id=id_hoadon,
            thuoc_id=medicineCode,
            so_luong=int(medicinequan))

        dct.tinh_tong_tien_hoa_don(id_hoadon)

        dct.cap_nhap_trang_thai_lichkham(id_lichkham)

        return redirect(url_for('main.form_doctor'))







@doctor.route('/doctor/search-medicine', methods=['POST'])
def search_medicine():
    if request.method == 'POST':
        # Nhận chuỗi tìm kiếm từ JavaScript
        search_query = request.form.get('medicineName')

        # Sử dụng hàm tìm kiếm của bạn để lấy danh sách thuốc
        list_medicene_search = medicine.search_medicine_name(search_query)
        print(list_medicene_search)
        return redirect(url_for('main.form_find'))


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