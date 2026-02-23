
from fastapi import APIRouter
from .schemas import UserCreate, UserResponse, UserUpdate
from .services import add_user, delete_user,get_all_users, get_user_by_id, update_user
from fastapi import Depends
from sqlalchemy.orm import Session
from .db_config import get_db
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
@router.put("/users/{user_id}", response_model=UserResponse)
def update_user_route(
    user_id:int,
    user:UserUpdate,
    db:Session = Depends(get_db)
):
    updated_user = update_user(db,user_id,user.dict())

    if not updated_user:
        raise HTTPException(status_code=404,detail="User not found")
    return updated_user
@router.delete("/users/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    success = delete_user(db, user_id)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}