from urllib.parse import quote

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from clinic_management.app import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4' % quote('Totnghiep78@')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(routes.bp)


db=SQLAlchemy(app=app)

