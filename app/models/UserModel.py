from sqlalchemy import Column, String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from typing import List
import uuid
from enum import Enum as PyEnum
from app.models.base import GUID
from app.database import Base
from app.models.snippatModel import Snippet_code
from app.models.categoreModel import Category





class Role(PyEnum):
    Admin = "Admin"
    User = "User"
    SuperAdmin = "SuperAdmin"

class User(Base):
    __tablename__ = 'users'

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(Role), default=Role.User)
    active = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.now(timezone.utc))
    updatedAt = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    refreshToken = Column(String )
    
    snippets = relationship("Snippet_code", back_populates="user")
    categories = relationship("Category", back_populates="user")
