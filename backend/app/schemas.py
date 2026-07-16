from typing import Optional

from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    status: Optional[str] = "Want to Read"
    rating: Optional[int] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str | None
    status: str
    rating: int | None = None

    class Config:
        from_attributes = True  # Pydantic can read from SQLAlchemy ORM models