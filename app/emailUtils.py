# from typing import List
# from fastapi_mail import FastMail, MessageSchema,ConnectionConfig





# conf = ConnectionConfig(
#     MAIL_USERNAME = "Fuhad Aminu",
#     MAIL_PASSWORD = "Indomitables@123",
#     MAIL_FROM = "fuhad.aminu16@kwasu.edu.ng",
#     MAIL_PORT = 587,
#     MAIL_SERVER = "smtp.office365.com",
#     MAIL_TLS = True,
#     MAIL_SSL = False,
#     USE_CREDENTIALS = True,
#     VALIDATE_CERTS = True
# )



# async def send_email(subject:str, recipient:List, message:str):
#     message = MessageSchema(
#         subject=subject,
#         recipients=recipient,
#         body=message,
#         subtype='html'
#     )
    
#     fm =FastMail(conf)
#     await fm.send_message(message)
    