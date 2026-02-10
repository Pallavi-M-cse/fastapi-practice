from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping(name:str ="guest"):
    print(f"Ping hit by:{name}")
    return {
        "status":"ok",
        "user":name
    } 
