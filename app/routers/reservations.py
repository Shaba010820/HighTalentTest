from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.models import Reservation
from app.schemas.reservation import ReservationCreate, ReservationRead
from app.services.reservation import is_conflicting_reservation


router = APIRouter(prefix='/reservations', tags=['Reservations'])


@router.get('/', response_model=list[ReservationRead])
def get_reservations(db: Session = Depends(get_db)):
    return db.query(Reservation).all()


@router.post('/', response_model=ReservationRead, status_code=status.HTTP_201_CREATED)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    if is_conflicting_reservation(db, reservation.table_id, reservation.reservation_time, reservation.duration_minutes):
        raise HTTPException(status_code=400, detail='Стол уже забронирован на этот период времени')

    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)

    return db_reservation


@router.delete('/{reservation_id}', status_code=204)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()

    if not reservation:
        raise HTTPException(status_code=404, detail='Бронь не найдена')

    db.delete(reservation)

    db.commit()