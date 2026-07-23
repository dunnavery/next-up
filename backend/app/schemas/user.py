from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True  # Pydantic can read from SQLAlchemy ORM models
