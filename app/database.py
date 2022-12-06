import time
import psycopg2
import cloudinary
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# password = 'indomitables123'
# user_name = 'postges'
# host = 'localhost'
# db_name = 'dateapp'
# SQLALCHEMY_DATABASE_URL =  f"postgresql://{user_name}:{password}@{host}:5433/{db_name}"

cloudinary.config( 
  cloud_name = "hujwafevi", 
  api_key = "282969132628724", 
  api_secret = "KotkJF_mNQQxvQiAQFFF9zFC4a0" 
)

password = 'kJ6d2ZWySSkr9KdW8mdPkDihQC3MGso9'
user_name = 'date_app_user'
host = 'dpg-ce74bekgqg4eemouqsmg-a.oregon-postgres.render.com'
db_name = 'date_app'
SQLALCHEMY_DATABASE_URL =  f"postgresql://{user_name}:{password}@{host}/{db_name}"



engine = create_engine(
        f"postgresql://{user_name}:{password}@{host}/{db_name}"
    #f"postgresql://{user_name}:{password}@{host}:5433/{db_name}
    # f"postgresql://postgres:indomitables123@localhost/dateapp"
    # SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='dateapp', user='postgres',
#                                 password='indomitables123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
