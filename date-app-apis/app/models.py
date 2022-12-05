from cgitb import text
from codecs import getencoder
from datetime import datetime, timezone
from email.policy import default
from http import server
from sqlite3 import Timestamp
from time import timezone
from typing import List, Type
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship
#from sqlalchemy_utils import URLType

from .database import Base

from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    firstname = Column(String, nullable=False, server_default='user')
    lastname = Column(String, nullable=False, server_default='user')
    othername = Column(String, nullable=True, server_default='')
    phone = Column(String, nullable=False, server_default='')
    occupation = Column(String, nullable=True, server_default='')
    gender = Column(String, nullable=True, server_default='')
    income =  Column(String, nullable=False, server_default='')
    address =  Column(String, nullable=False, server_default='')
    state =  Column(String, nullable=False, server_default='')
    # dob =  Column(String, nullable=False, server_default='')
    age =  Column(String, nullable=False, server_default='')
    grant = Column(String, nullable=False, server_default='')
    credit_score = Column(String, nullable=False, server_default='')
    grant_reason = Column(String, nullable=False, server_default='')
    passcode = Column(String, nullable=False, server_default='')
    
    
    
    
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=True)
    # gender = Column(String, nullable=False, server_default='male')
    # age = Column(String, nullable=False, server_default='age')
    # image_url = Column(String, nullable=False)
    

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False)
    #is_active = Column(Boolean, default=True,nullable=False)

   # items = relationship("Item", back_populates="owner")


class Images(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True, nullable=False)

    image_url = Column(String, nullable=False)

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default='now()')

    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"))

    owner = relationship("User")
 
 
class Codes(Base):
    __tablename__ = "codes"
    id = Column(Integer, primary_key=True, index=True, nullable=False)

    email = Column(String,  nullable=False)
    
    reset_code = Column(String, nullable=False)
    
    status = Column(String,nullable=False)
    
    

    expired_in = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default='now()')


    
# class Interest(Base):
#     __tablename__ = "interest"
#     id = Column(Integer, primary_key=True, index=True, nullable=False)

#     interests = Column(ARRAY(String), nullable=False, server_default=None)

#     created_at = Column(TIMESTAMP(timezone=True),
#                         nullable=False, server_default='now()')

#     owner_id = Column(Integer, ForeignKey(
#         "users.id", ondelete="CASCADE"))

#     owner = relationship("User")
