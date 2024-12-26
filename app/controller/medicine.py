from app import login_manager
from flask_login import current_user
from app.models import Thuoc
from app import db
from app.models import Thuoc
from flask import jsonify
def search_medicine_name(search_medicine):
    # Use .filter and .like for partial match on the medicine name
    result = Thuoc.query.filter(Thuoc.name.ilike(f"%{search_medicine}%")).all()  # Use .ilike() for case-insensitive search

    # If no results found, return an empty list
    if not result:
        return []

    return result