from pydantic import BaseModel, EmailStr
from typing import  Optional
from datetime import datetime
from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    #interests: list
    othername:Optional[str]
    phone:str
    occupation:Optional[str]
    income:str
    address:str
    state:str
    gender:str
    age: Optional[str]
    grant:str
    credit_score:str
    grant_reason:str
    firstname:str
    lastname:str
    passcode:Optional[str]
    created_at:Optional[datetime]
 

    class Config:
        orm_mode = True
        

class UserInterest(BaseModel):
    
    interests: list
    
    
    
    

    class Config:
        orm_mode = True

    
class UserDetails (UserCreate):
    created_at: datetime
    id:int
    
    class Config:
        orm_mode = True


class ForgotPassword (BaseModel):
    email: EmailStr
    
    
    class Config:
        orm_mode = True
    

class user_error(BaseModel):
    email: Optional[str]
    interests: list
    
    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str] = None
    


class UserImageUpload(BaseModel):
    owner_id: str
    image_url:str
    class Config:
        orm_mode = True
