
from fastapi import APIRouter
from schemas import UserCreate, UserResponse
from services import add_user,get_all_users, get_user_by_id
from fastapi import Depends
from sqlalchemy.orm import Session
from db_config import get_db
from fastapi import HTTPException


router=APIRouter()

@router.post("/users",response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    return add_user(db,user.dict())

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user