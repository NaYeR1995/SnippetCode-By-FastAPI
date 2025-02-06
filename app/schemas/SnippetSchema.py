from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID
from app.database import Base
from app.schemas.categorySchema import CategoryBase, Category, CategoryShow



class SnippetBase(BaseModel):
    title: str
    code: str
    language: str
    description: Optional[str] = None

    model_config = {"from_attributes": True}


class SnippetCreate(SnippetBase):
    pass
    model_config = {"from_attributes": True}

class SnippetS(SnippetBase):
    id: int
    categoryId: int
    createdAt: datetime
    updatedAt: datetime

    model_config = {"from_attributes": True}

class snippetWithCate(SnippetBase):
    category: Category  # Nested Category model
 
    model_config = {"from_attributes": True}


class snippetWithCateShow(SnippetBase):
    CategoryShow: CategoryShow
 
    model_config = {"from_attributes": True}
