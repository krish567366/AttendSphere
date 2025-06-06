from pydantic import BaseModel, EmailStr
from typing import List, Optional
import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True # Changed from from_attributes = True for Pydantic v1 compatibility if needed

class RoleBase(BaseModel):
    name: str
    permissions: Optional[List[str]] = []

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True # Changed from from_attributes = True
