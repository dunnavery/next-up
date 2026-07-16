from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from database import Base
from datetime import datetime, timezone

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False, index=True, nullable=False)
    author = Column(String, unique=False, index=True, nullable=False)
    genre = Column(String, unique=False, nullable=True)
    
    status = Column(String, unique=False, nullable=False, default="Want to Read")
    rating = Column(Integer, unique=False, nullable=True)
    
    created_at = Column(TIMESTAMP, unique=False, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, unique=False, nullable=False, default=datetime.utcnow, onupdate=datetime.now(timezone.utc))
    