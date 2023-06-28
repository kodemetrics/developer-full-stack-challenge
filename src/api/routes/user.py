from fastapi import APIRouter, Depends, HTTPException, status
from typing import Union, List
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserSchema
from utils import auth
from utils.populate import data_factory
from utils.passcode import PasswordHash
api_router = APIRouter()


@api_router.get("/api/v1/users")
# def fetch_users(db: Session = Depends(get_db), current_user: dict = Depends(auth.get_current_user)):
def fetch_users(db: Session = Depends(get_db)):    
    users = db.query(User).all();
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No user found')

    return {"status": "success", "data": users}


@api_router.post("/api/v1/register", status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    hashpassword = PasswordHash.hash_password(user.password)
    new_user = User(username=user.username, password=hashpassword)
    # new_user = User(username=user.username, password=user.password)
    # new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "success", "data": new_user}


@api_router.post("/api/v1/login")
def login(user: UserSchema,db: Session = Depends(get_db)):
    # data_factory()
    # login = db.query(User).filter(User.id == user.id).first()
    login = db.query(User).filter(User.username == user.username).first()
    token = auth.encode_token(user.username)

    loginResponse = dict()
    loginResponse['id'] = login.id
    loginResponse['username'] = login.username
    loginResponse['createdAt'] = login.createdAt

    if not login:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = f'User Does not Exist')

    if not PasswordHash.verify_password(user.password, login.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'User Does not Exist')

    return {"status": "success", "data": loginResponse, "token": token}
