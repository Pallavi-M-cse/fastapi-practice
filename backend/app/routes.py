
from fastapi import APIRouter
from schemas import UserCreate
from services import add_user,get_all_users
from fastapi import Depends
from sqlalchemy.orm import Session
from db_config import get_db


router=APIRouter()

@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    created_user = add_user(db, user.dict())
    return created_user

@router.get("/users")
def list_users(db:Session = Depends(get_db)):
    return get_all_users()
