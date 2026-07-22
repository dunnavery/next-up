from fastapi import APIRouter

router = APIRouter()

@router.get("/library/")
def get_library():
    return {"message": "Welcome to the Library!"}

@router.post("/library/")
def add_book_to_library(book: dict):
    # Here you would typically add the book to the database
    return {"message": "Book added to library", "book": book}

@router.delete("/library/{book_id}")
def remove_book_from_library(book_id: int):
    # Here you would typically remove the book from the database
    return {"message": "Book removed from library", "book_id": book_id}
