from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import LiteralString

from models import User
from schemas import UserCreate, UserResponse
from database import get_db

router = APIRouter(
    prefix="/profile"
)

# Current user id is a placeholder, down the line this will be handled 
# by authentication and authorization mechanisms (e.g., OAuth2, JWT, etc.)
CURRENT_USER_ID = 1  # Placeholder for the current user ID

@router.post("/")
def create_profile(profile: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=profile.username,
        email=profile.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=UserResponse)
def get_profile(db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == CURRENT_USER_ID).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/", response_model=UserResponse)
def update_profile(profile_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == CURRENT_USER_ID).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in profile_data.dict().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user
