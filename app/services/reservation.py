from datetime import timedelta
from sqlalchemy.orm import Session
from app.models.models import Reservation


def is_conflicting_reservation(db: Session, table_id: int, start_time, duration_minutes: int):
    end_time = start_time + timedelta(minutes=duration_minutes)

    intersections = db.query(Reservation).filter(
        Reservation.table_id == table_id,
        Reservation.reservation_time < end_time,
        (Reservation.reservation_time + timedelta(minutes=Reservation.duration_minutes)) > start_time
    ).first()

    return intersections is not None
