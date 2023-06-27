import uvicorn
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from routes import user, book, author
from utils import auth

# protect routes
protected = [Depends(auth.get_current_user)]

origins = ['*']
# origins = ['http://localhost:3000']

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(user.api_router)
app.include_router(book.api_router, dependencies = protected)
app.include_router(author.api_router, dependencies = protected)


# @app.get("/")
# async def root():
#     return {"Hello": "World"}
