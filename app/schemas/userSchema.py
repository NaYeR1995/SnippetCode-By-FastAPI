from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID
from app.schemas.SnippetSchema import SnippetS
from app.schemas.categorySchema import Category



class UserBase(BaseModel):
    full_name: str
    email: str
    role: str = "User"
    active: bool

    model_config = {"from_attributes": True}



class UserCreate(BaseModel):
    full_name: str
    password: str
    email: str


    model_config = {"from_attributes": True}


class UserShow(UserBase):
    id: UUID
    createdAt: datetime
    updatedAt: datetime
    refreshToken: Optional[str] = None
    categories: List[Category] = []
    snippets: List[SnippetS] = []

    model_config = {"from_attributes": True}
