from fastapi import FastAPI
from .routes import router
from .db_config import engine
from .models import Base

app = FastAPI()
app.include_router(router)

Base.metadata.create_all(bind=engine)