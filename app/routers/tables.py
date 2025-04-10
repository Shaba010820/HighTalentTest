from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.models import Table
from app.schemas.table import TableCreate, TableRead

router = APIRouter(prefix='/tables', tags=['Tables'])


@router.get('/', response_model=list[TableRead])
def get_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()


@router.post('/', response_model=TableRead, status_code=201)
def create_table(table: TableCreate, db: Session = Depends(get_db)):
    db_table = Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


@router.get('/{table_id}', response_model=TableRead)
def get_table(table_id: int, db: Session = Depends(get_db)):
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Столика с таким id не существует")
    return table


@router.delete('/{table_id}', status_code=204)
def delete_table(table_id: int, db: Session = Depends(get_db)):
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail='Столика с таким id не существует')
    db.delete(table)
    db.commit()

