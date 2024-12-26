from app import login_manager
from flask_login import current_user
from app.models import Thuoc
from app import db

def search_medicine_name(search_medicine):
    # return Thuoc.query.filter(Thuoc.name.like(f"%{search_medicine}%")).all()
    result = Thuoc.query.filter(Thuoc.name.like(f"%{search_medicine}%")).all()

    return result