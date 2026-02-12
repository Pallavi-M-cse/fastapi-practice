
from fastapi import APIRouter
from app.schemas import UserCreate
from app.services import add_user,get_all_users

router=APIRouter()

@router.post("/users")
def create_user(user:UserCreate):
    created_user=add_user(user.dict())
    return{
        "message":"User created",
        "user":created_user
    }
@router.get("/users")
def list_users():
    return get_all_users()
