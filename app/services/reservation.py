from datetime import timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.models import Reservation


def is_conflicting_reservation(db: Session, table_id: int, start_time, duration_minutes: int):
    end_time = start_time + timedelta(minutes=duration_minutes)

    existing_reservations = db.query(Reservation).filter(
        Reservation.table_id == table_id
    ).all()

    for reservation in existing_reservations:
        existing_start = reservation.reservation_time
        existing_end = existing_start + timedelta(minutes=reservation.duration_minutes)
        if (start_time < existing_end) and (end_time > existing_start):
            return True
    return False
