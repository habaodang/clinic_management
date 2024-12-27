from flask import Blueprint, render_template, redirect, url_for, request,session,jsonify
from flask_login import login_user, logout_user,current_user,login_required
import app.controller.hoadon as hdon
cashier = Blueprint('cashier', __name__)

@cashier.route('comfirm-bill',methods=['POST','GET'])
def comfirm_bill():
    hoadon_id = request.args.get('hoadon')
    hdon.update_status(hoadon_id)
    return redirect(url_for('main.payment_invoice'))