from flask import Blueprint
from app.controller import qr


bp = Blueprint('main', __name__)

@bp.route('/')
def home():

    return 'hello'
