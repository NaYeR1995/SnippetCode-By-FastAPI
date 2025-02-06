from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from typing import List
import uuid
from app.models.base import GUID
from app.database import Base
# from app.models.userModel import User
# from app.models.categoreModel import Category




class Snippet_code(Base):
    __tablename__ = 'snippet_codes'
    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True, nullable=False)
    code = Column(String, nullable=False)
    language = Column(String, nullable=False)
    description = Column(String, nullable=True)
    userId = Column(GUID(), ForeignKey('users.id'))
    categoryId = Column(GUID(), ForeignKey('categories.id'))
    
    createdAt = Column(DateTime, default=datetime.now(timezone.utc))
    updatedAt = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    category = relationship("Category", back_populates="snippets")
    user = relationship("User", back_populates="snippets")