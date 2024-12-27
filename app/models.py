from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Enum, Time, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db
from enum import Enum as PyEnum
from flask_login import UserMixin


class UserRole(PyEnum):
    PATIENT = 'PA'
    DOCTOR = 'DO'
    NURSE = 'NU'
    CASHIER = 'CA'
    USER = 'US'


class PackageMedical(PyEnum):
    VIP = 'VIP'
    NORMAL = 'NORMAL'


class User(db.Model):
    __tablename__ = 'user'

    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    sex = Column(String(3), nullable=False)
    birth = Column(Date, nullable=False)
    phone = Column(String(10), nullable=False)
    cccd = Column(String(12), nullable=False)

    # Relationships
    account = relationship('Account', uselist=False, back_populates='user', lazy=True)


class Account(db.Model, UserMixin):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_account = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    role = Column(Enum(UserRole), nullable=False)
    status = Column(Boolean, nullable=False, default=False)
    date_created = Column(Date, nullable=False, default=datetime.utcnow)

    user_id = Column(String(10), ForeignKey('user.id'))
    user = relationship('User', back_populates='account', lazy=True)


class Nurse(User):
    __tablename__ = 'nurse'

    id = Column(String(10), ForeignKey('user.id'), primary_key=True)
    id_department = Column(Integer, ForeignKey('department.id'))

    # Relationships
    department = relationship('Department', back_populates='nurse', lazy=True)
    lich_kham = relationship('LichKham', back_populates='nurse', lazy=True)


class Department(db.Model):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    nurse = relationship('Nurse', back_populates='department', lazy=True)
    doctor = relationship('Doctor', back_populates='department', lazy=True)
    lich_kham = relationship('LichKham', back_populates='department', lazy=True)


class Doctor(User):
    __tablename__ = 'doctor'

    id = Column(String(10), ForeignKey('user.id'), primary_key=True)
    degree = Column(String(50))

    id_department = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship('Department', back_populates='doctor', lazy=True)

    phieu_kham = relationship('PhieuKham', back_populates='doctor', lazy=True)
    lich_kham = relationship('LichKham', back_populates='doctor', lazy=True)


class Patient(User):
    __tablename__ = 'patient'

    id = Column(String(10), ForeignKey('user.id'), primary_key=True)

    lich_kham = relationship('LichKham', back_populates='patient', lazy=True)
    phieu_kham = relationship('PhieuKham', back_populates='patient', lazy=True)


class LichKham(db.Model):
    __tablename__ = 'lich_kham'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(Time, nullable=False)
    status = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    date = Column(Date, nullable=False)
    location = Column(String(150), nullable=False)
    package = Column(Enum(PackageMedical), nullable=False)
    note = Column(String(150), nullable=False)
    status_doctor = Column(Boolean, default=False)

    doctor_id = Column(String(10), ForeignKey('doctor.id'))
    doctor = relationship("Doctor", back_populates="lich_kham")

    nurse_id = Column(String(10), ForeignKey('nurse.id'))
    nurse = relationship("Nurse", back_populates="lich_kham", lazy=True)

    patient_id = Column(String(10), ForeignKey('patient.id'), nullable=False)
    patient = relationship("Patient", back_populates="lich_kham", lazy=True)

    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship("Department", back_populates="lich_kham", lazy=True)


class PhieuKham(db.Model):
    __tablename__ = 'phieu_kham'

    id = Column(Integer, primary_key=True,autoincrement=True)
    trieuchung = Column(String(300), nullable=False)
    chandoan = Column(String(300), nullable=False)

    patient_id = Column(String(10), ForeignKey('patient.id'))
    doctor_id = Column(String(10), ForeignKey('doctor.id'))

    patient = relationship('Patient', back_populates='phieu_kham')
    doctor = relationship('Doctor', back_populates='phieu_kham')
    hoa_don = relationship('HoaDon', back_populates='phieu_kham', uselist=False)


class HoaDon(db.Model):
    __tablename__ = 'hoa_don'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ngay_lap = Column(Date, nullable=False,default=datetime.utcnow)
    tong_tien = Column(Integer, nullable=True)
    trangthai =Column(Boolean,default=False)
    # Foreign key
    phieu_kham_id = Column(Integer, ForeignKey('phieu_kham.id'), nullable=False)

    # Relationships
    phieu_kham = relationship('PhieuKham', back_populates='hoa_don')
    chi_tiet_hoa_don = relationship('ChiTietHoaDon', back_populates='hoa_don', cascade='all, delete-orphan')

    def tinh_tong_tien(self):
        self.tong_tien = sum(ct.tinh_thanh_tien() for ct in self.chi_tiet_hoa_don)
        return self.tong_tien

    def __repr__(self):
        return f"<HoaDon(id={self.id}, ngay_lap={self.ngay_lap}, tong_tien={self.tong_tien})>"


class ChiTietHoaDon(db.Model):
    __tablename__ = 'chi_tiet_hoa_don'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hoa_don_id = Column(Integer, ForeignKey('hoa_don.id'), nullable=False)
    thuoc_id = Column(Integer, ForeignKey('thuoc.id'), nullable=False)
    so_luong = Column(Integer, nullable=False)


    # Quan hệ
    thuoc = relationship('Thuoc', back_populates='chi_tiet_hoa_don')
    hoa_don = relationship('HoaDon', back_populates='chi_tiet_hoa_don')

    def tinh_thanh_tien(self):
        return self.so_luong * self.don_gia

    def __repr__(self):
        return f"<ChiTietHoaDon(id={self.id}, so_luong={self.so_luong}, don_gia={self.don_gia})>"


class Thuoc(db.Model):
    __tablename__ = 'thuoc'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    unit = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    effect = Column(String(200), nullable=False)
    usage = Column(String(200), nullable=False)
    price = Column(Integer, nullable=False)

    danhmuc_id = Column(Integer, ForeignKey('danhmucthuoc.id'))

    # Quan hệ
    chi_tiet_hoa_don = relationship('ChiTietHoaDon', back_populates='thuoc', lazy=True)
    danh_muc_thuoc = relationship('DanhMucThuoc', back_populates='thuoc', lazy=True)

    def __repr__(self):
        return f"<Thuoc(id={self.id}, name={self.name}, price={self.price})>"


class DanhMucThuoc(db.Model):
    __tablename__ = 'danhmucthuoc'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)

    thuoc = relationship('Thuoc', back_populates='danh_muc_thuoc', lazy=True)
