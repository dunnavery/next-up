from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False, index=True, nullable=False)
    author = Column(String, unique=False, index=True, nullable=False)
    genre = Column(String, unique=False, nullable=True)
    status = Column(String, unique=False, nullable=False)
    rating = Column(Integer, unique=False, nullable=True)
    created_at = Column(TIMESTAMP, unique=False, nullable=False)
    updated_at = Column(TIMESTAMP, unique=False, nullable=False)
    