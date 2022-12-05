from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import database, emailUtils, models, schemas, utils, oauth2
import uuid
from datetime import datetime, timezone

router = APIRouter(
    tags=["Authetication"]
)


@router.post("/login")
def login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    print("jfjfj")

    user = db.query(models.User).filter(
        models.User.email == user_credential.username).first()

    print(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    print(user.id)

    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    print (access_token)

    return {"access_token": access_token, "token_type": "bearer"}


# @router.post("/forgot-password")
# async def login(request:schemas.ForgotPassword, db: Session = Depends(database.get_db)):
    

#     user = db.query(models.User).filter(
#         models.User.email == request.email).first()

    

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
        
#     #create reset code and save
    
#     reset_code = str(uuid.uuid1())
#     expired_in = datetime.now(timezone.utc)
    
#     new_code = models.Codes(email=request.email, reset_code= reset_code, status = '1', expired_in = expired_in)
    
  
#     db.add(new_code)
#     db.commit()
#     db.refresh(new_code)
    
    
#     #sending email
    
#     subject = 'Hello Coder'
    
#     recipient = [request.email]
    
#     message = f'''
#     <!DOCTYPE html>
#     <html> 
#     <title>Reset Password</title> 
#     <body>
#     <div style='width:100%;font-family: monospace;"> 
#         <h1> Hello, {request.email} </h1>
#         <p>Someone has requested a link to reset your password. If you requested this, you can change your password through the button below</p>
#         <a href = "http://127.0.0.1:8000/forgot-password?reset_password_token={reset_code}" style = "box-sizing:border-box;border-color:#1f1e33;text-decoration:none;backgroung-color:#1f8feb;border:solid 1px #1f8feb;border-radius:4px;color:#ffffff;font-weight:bold;margin:0;padding:12px 24px;text-transform:capitalize;display:inline-block\"target=\"_blank\">Reset Your Password</a>
        
#         <p>If you didn't request thie, you can ignore this mail</p>
#         <p>Your password won't change until you access above link and create a new one
#         </p>
    
    
#     </div>
    
#     </body>
    
    
    
#     </html>
    
    
#     '''
    
#     await emailUtils.send_email(subject=subject, recipient=recipient,message=message)

#     return ({
#         "reset_code":reset_code,
#         "code":200,
#         "message" : "We've sent an email with instructions to reset your password."
        
        
#     })

    

