from fastapi import FastAPI
from app.models import models 
from app.controller.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()