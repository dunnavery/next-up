from pydantic import BaseModel, EmailStr

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    genre: str

    class Config:
        from_attributes = True # Pydantic can read from SQLAlchemy ORM models