from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from .database import Base, engine, SessionLocal, get_db

from .schemas.userSchema import UserShow, UserCreate
from .schemas.SnippetSchema import SnippetS, SnippetCreate, snippetWithCate, snippetWithCateShow
from app.schemas.categorySchema import CategoryCreate, Category

from app.models.userModel import User
from app.models.snippatModel import Snippet_code
from app.models.categoreModel import Category


# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to SnippetCode API"}


@app.post("/createUser", response_model=UserShow)
def create_user(user: UserCreate,  db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
            raise HTTPException(status_code=400, detail="Email already registered")
    try:
        new_user = User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User created successfully", "user": new_user}

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the user"
        ) from e
    finally:
        db.close()

@app.post("/createCode", response_model=snippetWithCateShow)
def create_code(code: snippetWithCate, db: Session = Depends(get_db)):
    try:
        cate_data = {"name": code.category.name}  

        new_cate = Category(**cate_data) 
        db.add(new_cate)
        db.commit()
        db.refresh(new_cate)

        code_data = {
            "title": code.title,
            "code": code.code,
            "language": code.language,
            "description": code.description,
            "categoryId": new_cate.id  
        }

        new_code = Snippet_code(**code_data) 
        db.add(new_code)
        db.commit()
        db.refresh(new_code)

        return snippetWithCate(
            title=new_code.title,
            code=new_code.code,
            language=new_code.language,
            description=new_code.description,
            category=(new_cate.id, new_cate.name)
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the snippet: {str(e)}"
        )

    finally:
        db.close()
