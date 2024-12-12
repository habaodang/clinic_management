from sqlalchemy import Column, Integer, String,Date,Boolean,ForeignKey
from datetime import date,datetime
from app.extension import db
import app


class Account(db.Model):
    __tablename__='account'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name_account=Column(String(50), unique=True,nullable=False)
    password=Column(String(255),nullable=False)
    date_created=Column(Date,nullable=False,default=datetime.now())
    role=Column(String(3),nullable=False)
    status=Column(Boolean,default=False)
    user_id = db.Column(String(10), ForeignKey('user.id'), unique=True)

    # Quan hệ 1-1 với User
    user = db.relationship('User', back_populates='account')




class User(db.Model):
    __tablename__ = 'user'

    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    sex = Column(String(3), nullable=False)
    birth = Column(Date, nullable=False)
    address = Column(String(100), nullable=False)
    phone = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False)
    # Quan hệ 1-1 với Account
    account = db.relationship('Account', back_populates='user', lazy=False)

    type = db.Column(db.String(50))
    # Kế thừa
    __mapper_args__ = {
        'polymorphic_on': type,  # Cột xác định lớp con
        'polymorphic_identity': 'user'  # Giá trị mặc định cho lớp cha
    }

    def __init__(self,type_id):
        self.type_id=type_id

    def get_type_id(self):
        return self.type_id

class Patient(User):
    __tablename__ = 'patients'
    id = Column(String(10), ForeignKey('user.id'), primary_key=True)
    medical_history = db.Column(db.Text)

    __mapper_args__ = {
        'polymorphic_identity': 'patient'  # Giá trị đại diện cho lớp con
    }

    def __init__(self):
        super().__init__('PA')

if __name__=="__main__":
    with app.app.app_context():
        db.create_all()
#     # p1=Patient()

