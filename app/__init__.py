from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rin2406@localhost/app?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(routes.bp)


db=SQLAlchemy(app=app)

