from datetime import timedelta, datetime
from sqlalchemy import func
from app import db
from app.models import ChiTietHoaDon, Thuoc, HoaDon


def get_revenue_data():
    today = datetime.utcnow().date()
    start_date = today - timedelta(days=30)  # Adjust the date range as needed

    # Querying the database
    revenue_data = db.session.query(
        func.date(HoaDon.ngay_lap).label('date'),
        func.count(HoaDon.id).label('patients'),
        func.sum(HoaDon.tong_tien).label('revenue')
    ).filter(HoaDon.ngay_lap >= start_date).group_by(func.date(HoaDon.ngay_lap)).all()

    labels = [str(record.date) for record in revenue_data]
    revenues = [record.revenue for record in revenue_data]
    details = [{"date": str(record.date), "patients": record.patients, "revenue": record.revenue, "rate": 0, "kpi": 0}
               for record in revenue_data]

    return {
        "labels": labels,
        "revenues": revenues,
        "details": details
    }

def get_drug_data():
    # Querying the database
    drug_data = db.session.query(
        Thuoc.name.label('name'),
        func.sum(ChiTietHoaDon.so_luong).label('quantity')
    ).join(ChiTietHoaDon, Thuoc.id == ChiTietHoaDon.thuoc_id).group_by(Thuoc.name).all()
    labels = [record.name for record in drug_data]
    values = [record.quantity for record in drug_data]
    details = [{"name": record.name, "quantity": record.quantity, "rate": 0} for record in drug_data]
    return {
        "labels": labels,
        "values": values,
        "details": details
    }