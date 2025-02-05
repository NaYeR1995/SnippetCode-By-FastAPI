import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.sqlite import TEXT
from ..database import Base
from .UserModel import User


class User(Base):
    
    __tablename__ = "users"

    id = Column(TEXT, primary_key=True, default=lambda: str(uuid.uuid4()))    
    user_name = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)
    snippets_id = db.Column(db.Integer, db.ForeignKey("snippets.id"))


    snippets = db.relationship("Snippet", back_populates="owner")
