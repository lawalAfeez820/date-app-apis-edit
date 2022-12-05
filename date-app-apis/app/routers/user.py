from collections import UserDict
from datetime import datetime
from operator import mod
import cloudinary
import cloudinary.uploader
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from datetime import datetime, timezone


from sqlalchemy import func




from app import oauth2, utils, database

from .. import schemas, models


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserDetails,name='Register User')
async def create_user(user: schemas.UserCreate,db: Session = Depends(database.get_db),):
    
    user1 = db.query(models.User).filter(
        models.User.email == user.email).first()

    print(user.password)
    

    if user1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Email has been used")
        
    
    
    user.passcode = user.password

    hashed_password = utils.hash(user.password)

    user.password = hashed_password
    user.created_at = datetime.now(timezone.utc)

    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/all', response_model=List[schemas.UserDetails],name='Fetch All Users')
def get_users(db: Session = Depends(database.get_db),):
    users = db.query(models.User).all()
    return users


@router.get('/', response_model=schemas.UserDetails,name='Fetch User Details')
def get_users(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    users = db.query(models.User).filter(
        models.User.id == current_user.id).first()
    return users


@router.post('/time',name='3hrs Time Lag Feature')
async def get_users(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    

    user = db.query(models.User.created_at).filter(
        models.User.id == current_user.id).first()
    
    created_at = user['created_at']
    
    time_difference = datetime.now(timezone.utc) - created_at
    
    time_difference_in_seconds =  time_difference.total_seconds()
    result = False
    
    if time_difference_in_seconds > 3600:
        result = True 
    
   
    print( time_difference_in_seconds )
    print(created_at)

    return (result)



