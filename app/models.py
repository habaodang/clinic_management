from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db

class Account(db.Model):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_account = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    date_created = Column(Date, default=datetime.utcnow)
    email = Column(String(100), nullable=False)
    role = Column(String(3), nullable=False)
    status = Column(Boolean, default=False)
    user_id = Column(String(10), ForeignKey('user.id'), unique=True)

    user = relationship('User', back_populates='account')

class User(db.Model):
    __tablename__ = 'user'
    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    sex = Column(String(3), nullable=False)
    birth = Column(Date, nullable=False)
    address = Column(String(100), nullable=False)
    phone = Column(String(10), nullable=False)

    account = relationship('Account', back_populates='user', lazy=False)

    type = Column(String(50))
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'user'
    }

class Patient(User):
    __mapper_args__ = {
        'polymorphic_identity': 'patient'
    }
    medical_history = Column(String(255))
