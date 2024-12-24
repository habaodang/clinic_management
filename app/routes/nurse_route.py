from flask import Blueprint, render_template, redirect, url_for, request,session
from flask_login import login_user, logout_user,current_user,login_required
from datetime import datetime
import app.controller.history as his

nurse = Blueprint('nurse', __name__)

# @nurse.route('/fill_appointment')
# def fill_apponitment():
#     date=Datatime.now()
#     lichkham=his.get_appointment()

@nurse.route('/confirm')
def confirm_appointment():
    lich_id = request.args.get('lich_id')
    his.confirm_appointment(lich_id)
    return redirect(url_for('main.form_nurse'))