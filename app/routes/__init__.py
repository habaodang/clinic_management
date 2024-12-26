from app.routes.auth_route import auth_bp
from app.routes.main_route import main_bp
from app.routes.notebook import note_book
from app.routes.booking_route import booking
from app.routes.nurse_route import nurse
from app.routes.doctor_route import doctor
from app.routes.admin_route import admin
from app.routes.cashier_route import cashier

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(note_book, url_prefix='/notebook')
    app.register_blueprint(booking, url_prefix='/booking')
    app.register_blueprint(nurse, url_prefix='/nurse')
    app.register_blueprint(doctor, url_prefix='/doctor')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(cashier, url_prefix='/cashier')
