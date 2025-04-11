from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.user_service import get_user_by_email, create_user
from app.schemas.user import UserCreate, UserLogin
from app.core.security import verify_password, create_access_token
from app.core.dependencies import get_current_admin_user

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

@router.post("/login")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.email, "role": db_user.role})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "email": db_user.email,
            "username": db_user.username,
            "role": db_user.role
        }
    }

@router.post("/admin", dependencies=[Depends(get_current_admin_user)])
def only_for_admins():
    return {"message": "Welcome, admin!"}