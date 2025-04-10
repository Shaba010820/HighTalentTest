from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ReservationBase(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int


class ReservationCreate(ReservationBase):
    pass


class ReservationRead(ReservationBase):
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)
