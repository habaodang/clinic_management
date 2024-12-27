from urllib.parse import quote

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    # Cấu hình ứng dụng
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456789a@localhost/app?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # key dung de gia ma session
    # app.config["SECRET_KEY"] = "rinnn1510"
    app.secret_key = 'rinnn1510'
    # thiet lap thoi gian session
    # app.permanent_session_lifetime = timedelta(minutes=5)
    # Khởi tạo SQLAlchemy
    db.init_app(app)
    login_manager.init_app(app)
    # Đăng ký Blueprint
    from app.routes import register_routes
    register_routes(app)
    # Tạo bảng (chỉ khi chạy lần đầu)
    with app.app_context():
        db.create_all()
        print("Database và các bảng đã được khởi tạo!")
    return app
