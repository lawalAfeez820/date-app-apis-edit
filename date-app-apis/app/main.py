
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from .routers import interests, user,auth,images,interest

app = FastAPI()




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