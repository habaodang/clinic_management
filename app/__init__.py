from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Cấu hình ứng dụng
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rin2406@localhost/app?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Khởi tạo SQLAlchemy
    db.init_app(app)

    # Đăng ký Blueprint
    from app.routes import register_routes
    register_routes(app)

    # Tạo bảng (chỉ khi chạy lần đầu)
    with app.app_context():
        db.create_all()

    return app




