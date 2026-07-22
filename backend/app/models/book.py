from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database import Base
from datetime import datetime, timezone

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False, index=True, nullable=False)
    author = Column(String, unique=False, index=True, nullable=False)
    genre = Column(String, unique=False, nullable=True)

    cover_url = Column(String, unique=False, nullable=True)
    description = Column(String, unique=False, nullable=True)
    published_year = Column(Integer, unique=False, nullable=True)
    