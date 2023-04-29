from fastapi import FastAPI
from app.models import models 
from app.controller.database import engine
from app.router.urls import router
models.base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=router)