from sqlalchemy.orm import Session
from .models import User

def add_user(db: Session, user_data: dict):
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
def update_user(db : Session, user_id:int,user_data:dict):
    db_user=db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None
    for key,value in user_data.items():
        setattr(db_user,key,value)
    db.commit()
    db.refresh(db_user)

    return db_user

def delete_user(db:Session ,user_id:int):
    db_user = db.query(User).filter(User.id==user_id).first()

    if not db_user:

        db.delete(db_user)
        db.commit()
    return db_user