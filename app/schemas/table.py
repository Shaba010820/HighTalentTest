from pydantic import BaseModel


class TableBase(BaseModel):
    name: str
    seats: str
    location: str


class TableCreate(BaseModel):
    pass


class TableRead(BaseModel):
    id: int

    class Config:
        orm_mode = True