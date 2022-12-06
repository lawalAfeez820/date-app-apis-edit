
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from .routers import interests, user,auth,images,interest
from alembic.config import Config
from alembic import command
import pathlib
from . import database
import os




def run_migrations(script_location: str, dsn: str) -> None:
    
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', script_location)
    alembic_cfg.set_main_option('sqlalchemy.url', dsn)
    command.upgrade(alembic_cfg, 'head')


dir = os.getcwd()+"/alembic"





app = FastAPI()

@app.on_event("startup")
def startup():
    run_migrations(dir, database.SQLALCHEMY_DATABASE_URL)




origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    user.router
  
)
app.include_router(
    
    auth.router
)

app.include_router(
    
    images.router
)

# app.include_router(
    
#     interest.router
# )




@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/")
async def root():
    return {"message": "Hello World"}