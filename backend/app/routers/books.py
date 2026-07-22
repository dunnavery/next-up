from fastapi import APIRouter

router = APIRouter(
    prefix="/books"
)

@router.get("/")
def read_books():
    return [{"title": "Book 1"}, {"title": "Book 2"}]

@router.get("/{book_id}")
def read_book(book_id: int):
    return {"title": f"Book {book_id}"}

@router.post("/")
def create_book():
    return {"message": "Book created"}
