
from os import name
from fastapi import FastAPI, Depends

from .models import Job
from .schemas import CreateJobRequest
from sqlalchemy.orm import Session
from .database import get_db


app = FastAPI()
@app.post("/")
def create(names:str,details: CreateJobRequest, db : Session = Depends(get_db)):
    to_create = Job(
        name=names
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "name": to_create.name
    }
@app.get("/get")
def get_by_d(id:int,db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.id == id).first()