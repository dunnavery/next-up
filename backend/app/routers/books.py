from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models import Book
from schemas import BookCreate, BookResponse
from database import get_db

router = APIRouter(
    prefix="/books"
)

@router.get("/", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_books = db.query(Book).offset(skip).limit(limit).all()
    return db_books


@router.get("/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.title == book.title).first()
    if db_book:
        raise HTTPException(status_code=400, detail="Book already exists")
    new_book = Book(
        title=book.title,
        author=book.author,
        genre=book.genre,
        cover_url=book.cover_url,
        description=book.description,
        published_year=book.published_year
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.patch("/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book
