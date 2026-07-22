from fastapi import APIRouter

router = APIRouter()

@router.get("/recommendations/")
def get_recommendations():
    return {"message": "Here are some book recommendations!"}
