from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.user_service import get_user_by_email, create_user
from app.schemas.user import UserCreate

router = APIRouter()

@router.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Перевірка, чи користувач вже існує в базі
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Створення нового користувача
    new_user = create_user(db, user)
    return {"message": "User created successfully", "user": new_user}
