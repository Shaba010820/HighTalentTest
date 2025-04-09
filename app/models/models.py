from datetime import datetime
from typing import List

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Table(Base):
    __tablename__ = 'table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    seats: Mapped[int] = mapped_column(Integer())
    location: Mapped[str] = mapped_column(String(100))

    reservations: Mapped[List["Reservation"]] = relationship(
        back_populates="table", cascade="all, delete-orphan"
    )


class Reservation(Base):
    __tablename__ = 'reservation'

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_name: Mapped[str] = mapped_column(String(30))
    table_id: Mapped[int] = mapped_column(ForeignKey('table.id', ondelete="CASCADE"))
    reservation_time: Mapped[datetime] = mapped_column(DateTime())
    duration_minutes: Mapped[int] = mapped_column(Integer())

    table: Mapped["Table"] = relationship(back_populates="reservations")