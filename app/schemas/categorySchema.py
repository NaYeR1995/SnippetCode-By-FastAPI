from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID


class CategoryBase(BaseModel):
    name: str
    model_config = {"from_attributes": True}


class CategoryCreate(CategoryBase):
    userId: UUID

    model_config = {"from_attributes": True}

class Category(CategoryBase):
    name: str 
    class Config:
        orm_mode = True

class CategoryShow(CategoryBase):
    id:UUID
    name: str
    class Config:
        orm_mode = True

