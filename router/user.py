from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from db.database import get_db
from db import db_user
from schemas import UserBase, UserDisplay
from typing import List

router = APIRouter(prefix="/user", tags=["user"])


# create user
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# read all users
@router.get("/", response_model=List[UserDisplay])
def get_all_users(
    db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)
):
    return db_user.get_all_users(db)


# read one  user
@router.get("/{id}", response_model=UserDisplay)
def get_user_by_username(
    username: str,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_user.get_user_by_username(db, username)


# update user details
@router.post("/{id}/update")
def update_user_details(
    id: int,
    request: UserBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_user.update_user(db, id, request)


# delete user details
@router.get("/delete/{id}")
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_user.delete_user(db, id)
