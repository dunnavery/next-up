from fastapi import APIRouter, Session, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models import UserBook
from schemas import UserBookCreate, UserBookResponse
from database import get_db

router = APIRouter(
    prefix="/library"
)

CURRENT_USER_ID = 1  # Placeholder for the current user ID

@router.get("/", response_model=List[UserBookResponse], status_code=status.HTTP_200_OK)
def get_library(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_library = db.query(UserBook).offset(skip).limit(limit).all()
    return db_library


@router.post("/", response_model=UserBookResponse, status_code=status.HTTP_201_CREATED)
def add_book_to_library(book: UserBookCreate, db: Session = Depends(get_db)):
    # Check if the book is already in the user's library
    existing_entry = db.query(UserBook).filter(UserBook.user_id == CURRENT_USER_ID, UserBook.book_id == book_id).first()
    if existing_entry:
        raise HTTPException(status_code=400, detail="Book already in library")

    new_entry = UserBook(
        user_id=CURRENT_USER_ID,
        book_id=book.book_id,
        status=book.status,
        rating=book.rating
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.patch("/{book_id}", response_model=UserBookResponse, status_code=status.HTTP_200_OK)
def update_library_book(book_id: int, userBook: UserBookCreate, db: Session = Depends(get_db)):
    db_library_book = db.query(UserBook).filter(UserBook.book_id == book_id).first()
    if not db_library_book:
        raise HTTPException(status_code=404, detail="Book not found in library")
    for key, value in userBook.dict().items():
        setattr(db_library_book, key, value)
    db.commit()
    db.refresh(db_library_book)
    return db_library_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_library_book(book_id: int, db: Session = Depends(get_db)):
    db_library_book = db.query(UserBook).filter(UserBook.book_id == book_id).first()
    if not db_library_book:
        raise HTTPException(status_code=400, detail="Book not found in library")
    db.delete(db_library_book)
    db.commit()
    