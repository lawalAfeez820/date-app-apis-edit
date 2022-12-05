from operator import mod
import cloudinary
import cloudinary.uploader
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from sqlalchemy.orm import Session


from sqlalchemy import desc, func




from app import oauth2, utils, database

from .. import schemas, models


router = APIRouter(
    prefix='/interest',
    tags=['interest']
)



@router.post('/')
async def get_users(interests:schemas.UserInterest,db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    user = db.query(models.User).filter(
        models.User.id == current_user.id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
        
    

    

    interest = models.Interest(owner_id=current_user.id, **interests.dict())
    


    db.add(interest)
    db.commit()
    db.refresh(interest)

    return interest


# # @router.get('/images/{id}')
# # async def get_users(id:int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user),):

# #     # images = db.query(models.Images, func.count(models.Images.id).label("images")).join(
# #     #     models.User, models.User.id == models.Images.owner_id, isouter=True).group_by(models.Users.id).filter(models.Post.id == id).first()

# #     user_image=db.query(models.Images).filter(models.Images.owner_id==id).all()
 
# #     # new_image = models.Images(owner_id=current_user.id, image_url=image_url)
# #     # print(new_image)

# #     # db.add(new_image)
# #     # db.commit()
# #     # db.refresh(new_image)

# #     return user_image

# # @router.get('/')
# # async def get_users(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user),):

# #     # images = db.query(models.Images, func.count(models.Images.id).label("images")).join(
# #     #     models.User, models.User.id == models.Images.owner_id, isouter=True).group_by(models.Users.id).filter(models.Post.id == id).first()

# #     user_image=db.query(models.Images).filter(models.Images.owner_id==current_user.id).order_by(desc(models.Images.id)).limit(5).all()
 
# #     # new_image = models.Images(owner_id=current_user.id, image_url=image_url)
# #     # print(new_image)

# #     # db.add(new_image)
# #     # db.commit()
# #     # db.refresh(new_image)

# #     return user_image




# # @router.get('/all',)
# # def get_users(db: Session = Depends(database.get_db),):
# #     users = db.query(models.User,models.Images ).join(
# #          models.Images, models.User.id == models.Images.owner_id, isouter=True).filter()
# #     print (users)
    


# #     return users.first()