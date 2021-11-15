from fastapi import FastAPI
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import models, schemas
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/users")
def test_post(db: Session = Depends(get_db)):

    users = db.query(models.User).all()

    return{"data":users}


@app.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), ):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user