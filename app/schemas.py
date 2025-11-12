# app/schemas.py
from __future__ import annotations
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, HttpUrl, ConfigDict

class ErrorResponse(BaseModel):
    detail: str

# Optional pagination envelope
class PageMeta(BaseModel):
    total: int = Field(ge=0)
    limit: int = Field(ge=1, le=200, default=50)
    skip: int = Field(ge=0, default=0)

class Page(BaseModel):
    meta: PageMeta

# Incoming signup payload, validates email and password length 
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=256)

# What to return to customers
class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TagBase(BaseModel):
    name: str = Field(min_length=1, max_length=64)

class TagOut(TagBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

# Create, update, and out
class BookmarkCreate(BaseModel):
    url: HttpUrl
    tags: Optional[List[str]] = Field(default_factory=list)
# Patch payload
class BookmarkUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=500)
    description: Optional[str] = Field(default=None, max_length=4000)
    favicon: Optional[str] = Field(default=None, max_length=2000)
    tags: Optional[List[str]] = None
    is_archived: Optional[bool] = None

class BookmarkOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    url: HttpUrl
    title: str = ""
    description: str = ""
    favicon: str = ""
    code: Optional[str] = None
    is_archived: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    tags: List[TagOut] = Field(default_factory=list)


class HealthOut(BaseModel):
    status: str = "ok"
