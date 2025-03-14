from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/' ,response_model=UserDisplay)
def create_user(request: UserBase,
                 db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

@router.get('/', response_model=List[UserDisplay])
def get_users(db: Session = Depends(get_db)):
    return db_user.get_users(db)


@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

@router.put('/{id}')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    db_user.update(db, id, request)
    return 'ok'

@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user.delete(db, id)
    return 'ok'

