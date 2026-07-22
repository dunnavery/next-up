from fastapi import APIRouter

router = APIRouter()

@router.get("/profile/")
def get_profile():
    return {"message": "Welcome to your Profile!"}
