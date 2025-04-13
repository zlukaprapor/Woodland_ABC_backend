from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.user_service import get_user_by_email, create_user
from app.schemas.user import UserCreate, UserLogin, Token
from app.core.security import verify_password, create_access_token
from app.core.dependencies import get_current_admin_user

router = APIRouter()

@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """Реєстрація нового користувача"""
    try:
        new_user = create_user(db, user)
        access_token = create_access_token(data={"sub": new_user.email, "role": new_user.role})
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": new_user
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при реєстрації користувача: {str(e)}"
        )

@router.post("/login", response_model=Token)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    """Авторизація користувача"""
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Невірні облікові дані",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": db_user.email, "role": db_user.role})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": db_user
    }

@router.get("/admin", dependencies=[Depends(get_current_admin_user)])
def only_for_admins():
    """Ендпоінт, доступний тільки для адміністраторів"""
    return {"message": "Ласкаво просимо, адміністраторе!"}