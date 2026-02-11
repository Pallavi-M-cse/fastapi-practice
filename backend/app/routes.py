
from fastapi import APIRouter
from app.schemas import UserCreate

router=APIRouter()

@router.post("/users")
def create_user(user:UserCreate):
    return{
        "message":"User created",
        "user":user
    }

