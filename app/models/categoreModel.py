from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from app.database import Base
from app.models.base import GUID
# from app.models.userModel import User
# from app.models.snippatModel import Snippet_code




class Category(Base):
    __tablename__ = 'categories'

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    userId = Column(GUID(), ForeignKey('users.id'))
    createdAt = Column(DateTime, default=datetime.now(timezone.utc))
    updatedAt = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    user = relationship("User", back_populates="categories")
    snippets = relationship("Snippet_code", back_populates="category")