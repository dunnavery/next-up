from typing import Optional
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    cover_url: Optional[str] = None
    description: Optional[str] = None
    published_year: Optional[int] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str | None
    cover_url: str | None
    description: str | None
    published_year: int | None

    class Config:
        from_attributes = True  # Pydantic can read from SQLAlchemy ORM models
        