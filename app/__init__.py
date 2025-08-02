from urllib.parse import quote
import os

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
    
    # Get configuration from environment variables
    db_host = os.getenv('DB_HOST', 'localhost')
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD', '123456789a')
    db_name = os.getenv('DB_NAME', 'app')
    secret_key = os.getenv('SECRET_KEY', 'rinnn1510')
    
    # Cấu hình ứng dụng
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = secret_key
    
    # Khởi tạo SQLAlchemy
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Đăng ký Blueprint
    from app.routes import register_routes
    register_routes(app)
    
    # Health check endpoint
    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'service': 'clinic_management'}, 200
    
    # Tạo bảng (chỉ khi chạy lần đầu)
    with app.app_context():
        db.create_all()
        print("Database và các bảng đã được khởi tạo!")
    
    return app
