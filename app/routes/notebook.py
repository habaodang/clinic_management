from flask import Blueprint, render_template, redirect, url_for, request,session
from flask_login import login_user, logout_user,current_user,login_required
import app.controller.login as lg
import app.controller.create_account as cra
import app.models as mdl

note_book = Blueprint('notebook', __name__)

@login_required
@note_book.route('/authenticate',methods=['GET','POST'])
def authenticate():
    if request.method == 'POST':
        name = request.form.get('username')
        address = request.form.get('password')

