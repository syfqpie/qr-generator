from datetime import datetime
from typing import Optional
# from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from pydantic.types import UUID4
import uuid

# Shared properties
class ItemBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool]


# Properties to receive on item creation
class ItemCreate(ItemBase):
    name: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    name: Optional[str]
    description: Optional[str]
    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: uuid.UUID
    name: Optional[str]
    description: Optional[str]
    is_active: Optional[bool]
    created_at: Optional[datetime]
    modified_at: Optional[datetime]

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass


class UserBase(BaseModel):
    username: str
    email: str = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
