from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from database import Base

class UserBook(Base):
    __tablename__ = "user_books"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, nullable=False)
    status = Column(String, unique=False, nullable=True)  # e.g. Want to Read, Reading, Read
    rating = Column(Integer, unique=False, nullable=True)  # e.g., 1-5 stars
    started_at = Column(TIMESTAMP(timezone=True), nullable=True)
    finished_at = Column(TIMESTAMP(timezone=True), nullable=True)
    notes = Column(String, unique=False, nullable=True)  # User's personal notes about the book

    # Define database foreign key constraint
    # ondelete="CASCADE" PostgreSQL automatically wipes out all child records (user_books) if parent record (user) is deleted
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="books")
