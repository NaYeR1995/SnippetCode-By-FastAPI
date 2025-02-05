import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.sqlite import TEXT
from ..database import Base
from .UserModel import User


class Snippet(Base):
    __tablename__ = "snippets"

    id = db.Column(TEXT, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    owner = db.relationship("User", back_populates="snippets")
