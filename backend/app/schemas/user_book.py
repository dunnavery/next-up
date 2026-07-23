from typing import Optional
from pydantic import BaseModel

class UserBookCreate(BaseModel):
    user_id: int
    book_id: int
    status: Optional[str] = None  # e.g., "reading", "completed", "wishlist"
    rating: Optional[int] = None  # e.g., 1-5 stars

class UserBookResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    status: Optional[str] = None
    rating: Optional[int] = None

    class Config:
        from_attributes = True  # Pydantic can read from SQLAlchemy ORM models