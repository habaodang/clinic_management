from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Enum, Time, DateTime, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db
from enum import Enum as Pyenmu
from flask_login import UserMixin


# Định nghĩa Enum trong Python
class UserRole(Pyenmu):
    PATIENT = 'PA'
    DOCTOR = 'DO'
    NURSE = 'NU'
    CASHIER = 'CA'
    USER="US"

class PackageMedical(Pyenmu):
    VIP = 'VIP'
    NORMAL = 'NORMAL'


# Base User model with inheritance for Nurse, Doctor, Cashier, Patient
class User(db.Model):
    __tablename__ = 'user'

    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100),nullable=False)
    sex = Column(String(3),nullable=False)
    birth = Column(Date,nullable=False)
    phone = Column(String(10),nullable=False)
    cccd = Column(String(12),nullable=False)


    # Relationships
    account = relationship('Account', uselist=False, back_populates='user',lazy=False)

class Account(db.Model,UserMixin):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name_account = Column(String(50), nullable=False,unique=True)
    password = Column(String(200), nullable=False)
    email = Column(db.String(150),nullable=False,unique=True)
    role = Column(Enum(UserRole), nullable=False)
    Status = Column(Boolean, nullable=False,default=False)
    date_created = Column(Date, nullable=False,default=datetime.now)

    # Foreign key
    user_id = db.Column(String(10), ForeignKey('user.id'))

    # Relationships
    user = db.relationship('User', back_populates='account',lazy=False)

class Nurse(User):
    __tablename__ = 'nurse'

    id = Column(String(10), db.ForeignKey('user.id'), primary_key=True)
    id_department=Column(Integer, db.ForeignKey('department.id'))
    # Relationships
    department = relationship('Department', back_populates='nurse',lazy=False)
    lich_kham = relationship('LichKham', back_populates='nurse', lazy=False)


class Department(db.Model):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50), nullable=False)

    # Relationships
    nurse = relationship('Nurse', back_populates='department',lazy=False)
    doctor = db.relationship('Doctor', back_populates='department', lazy=False)
    lich_kham = relationship('LichKham', back_populates='department', lazy=False)


class Doctor(User):
    __tablename__ = 'doctor'

    id = Column(String(10), ForeignKey('user.id'), primary_key=True)
    degree = Column(String(50))

    id_department=Column(Integer, ForeignKey('department.id'),nullable=False)
    department = db.relationship('Department', back_populates='doctor', lazy=False)

    # Relationships
    phieu_kham = relationship('PhieuKham', back_populates='doctor',lazy=False)
    lich_kham = relationship('LichKham', back_populates='doctor', lazy=False)



class Cashier(User):
    __tablename__ = 'cashier'

    id = Column(String(10), ForeignKey('user.id'), primary_key=True)

class Patient(User):
    __tablename__ = 'patient'

    id = Column(String(10), ForeignKey('user.id'), primary_key=True)

    # Relationships
    lich_kham = relationship('LichKham', back_populates='patient',lazy=False)
    phieu_kham = relationship('PhieuKham', back_populates='patient',lazy=False)

class LichKham(db.Model):
    __tablename__ = 'lich_kham'

    id = Column(Integer, primary_key=True,autoincrement=True)
    time = Column(Time, nullable=False)
    status = Column(String(150),default=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    date = Column(Date, nullable=False)
    location = Column(String(150), nullable=False)
    package = Column(Enum(PackageMedical), nullable=False)
    note = Column(String(150), nullable=False)

    doctor_id = Column(String(10), ForeignKey('doctor.id'))
    doctor = relationship("Doctor", back_populates="lich_kham")

    # Tham chiếu đến bảng y tá
    nurse_id = Column(String(10), ForeignKey('nurse.id'))
    nurse = relationship("Nurse", back_populates="lich_kham",lazy=False)

    # Tham chiếu đến bảng bệnh nhân
    patient_id = Column(String(10), ForeignKey('patient.id'),nullable=False)
    patient = relationship("Patient", back_populates="lich_kham",lazy=False)

    # Tham chiếu đến bảng khoa
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship("Department", back_populates="lich_kham",lazy=False)


class PhieuKham(db.Model):
    __tablename__ = 'phieu_kham'

    id = Column(Integer, primary_key=True)

    # Foreign keys
    patient_id = Column(String(10), ForeignKey('patient.id'))
    doctor_id = Column(String(10), ForeignKey('doctor.id'))

    # Relationships
    patient = relationship('Patient', back_populates='phieu_kham')
    doctor = relationship('Doctor', back_populates='phieu_kham')
    hoa_don = relationship('HoaDon', back_populates='phieu_kham')
    chi_tiet_don_thuoc = relationship('ChiTietDonThuoc', back_populates='phieu_kham',lazy=False)

class HoaDon(db.Model):
    __tablename__ = 'hoa_don'

    id = db.Column(Integer, primary_key=True)
    payment_date = Column(Date, nullable=False)
    bill_money = Column(Float, nullable=False)
    # Foreign key
    phieu_kham_id = Column(Integer, ForeignKey('phieu_kham.id'))

    # Relationships
    phieu_kham = relationship('PhieuKham', back_populates='hoa_don',lazy=False)

class ChiTietDonThuoc(db.Model):
    __tablename__ = 'chi_tiet_don_thuoc'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

    # Foreign keys
    phieu_kham_id = Column(Integer, ForeignKey('phieu_kham.id'))
    thuoc_id = Column(Integer, ForeignKey('thuoc.id'))

    # Relationships
    phieu_kham = relationship('PhieuKham', back_populates='chi_tiet_don_thuoc',lazy=False)
    thuoc = relationship('Thuoc', back_populates='chi_tiet_don_thuoc',lazy=False)

class Thuoc(db.Model):
    __tablename__ = 'thuoc'

    stt = Column(Integer, primary_key=True, autoincrement=True)  # STT tự tăng
    id = Column(Integer, nullable=False, unique=True)
    code = Column(String(10), nullable=False, unique=True)
    name = Column(String(150), nullable=False)
    unit = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    effect = Column(String(200), nullable=False)
    usage = Column(String(200), nullable=False)

    # Relationships
    chi_tiet_don_thuoc = relationship('ChiTietDonThuoc', back_populates='thuoc',lazy=False)
