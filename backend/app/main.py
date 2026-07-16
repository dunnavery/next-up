from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# POST endpoint to create a book
@app.post("/books/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
	db_book = db.query(models.Book).filter(models.Book.title == book.title).first()
	if db_book:
		raise HTTPException(status_code=400, detail="Book already exists")
	
	new_book = models.Book(
		title=book.title,
		author=book.author,
		genre=book.genre,
		status=book.status,
		rating=book.rating,
	)
	db.add(new_book)
	db.commit()
	db.refresh(new_book)  # Refreshes object to get the generated ID
	return new_book

# GET endpoint to fetch all users
@app.get("/books/", response_model=List[schemas.BookResponse])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
	books = db.query(models.Book).offset(skip).limit(limit).all()
	return books

# DELETE endpoint to delete a book by id
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
	db_book = db.query(models.Book).filter(models.Book.id == book_id).first()

	if not db_book:
		raise HTTPException(status_code=400, detail="Book not found")
	
	db.delete(db_book)
	db.commit()
