from sqlalchemy.orm.session import Session
from db.models import DbUser
from schemas import UserBase
from .hash import Hash

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    return db.query(DbUser)


def get_user(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()

def update(db:Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()

def delete(db: Session, id: int):
    user = get_user(db, id)
    db.delete(user)
    db.commit()
    