from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .config import DATABASE_URL, ALGORITHM, SECRET_KEY

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to SnippetCode API"}


@app.post('/')
def create_user():
    