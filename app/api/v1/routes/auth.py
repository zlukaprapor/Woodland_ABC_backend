from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.user_service import get_user_by_email, create_user
from app.schemas.user import UserCreate, UserLogin, Token
from app.core.security import verify_password, create_access_token
from app.core.dependencies import get_current_admin_user

# Створення окремого роута
router = APIRouter()


@router.post(
    "/register",
    response_model=Token,
    status_code=status.HTTP_201_CREATED,
    summary="Реєстрація нового користувача",
    description="Створює нового користувача і повертає JWT токен для авторизації."
)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Реєстрація користувача.

    - Приймає дані нового користувача.
    - Створює користувача в БД.
    - Генерує JWT токен для авторизації.
    - Повертає токен і дані користувача.
    """
    try:
        new_user = create_user(db, user)
        access_token = create_access_token(data={"sub": new_user.email, "role": new_user.role})
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": new_user
        }
    except HTTPException:
        raise  # Пропускає далі, якщо вже було згенеровано помилку FastAPI
    except Exception as e:
        # Усі інші помилки — повертаємо 500 Internal Server Error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при реєстрації користувача: {str(e)}"
        )


@router.post(
    "/login",
    response_model=Token,
    summary="Авторизація користувача",
    description="Авторизує користувача за email і паролем. Повертає JWT токен при успіху."
)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    """
    Авторизація користувача.

    - Перевіряє наявність користувача в базі даних.
    - Порівнює хеш пароля.
    - Якщо авторизація успішна — повертає токен і дані користувача.
    - Інакше — 401 Unauthorized.
    """
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


@router.get(
    "/admin",
    dependencies=[Depends(get_current_admin_user)],
    summary="Адмінський ендпоінт",
    description="Ендпоінт, доступний лише для користувачів з роллю адміністратора."
)
def only_for_admins():
    """
    Ендпоінт тільки для адміністраторів.

    - Працює лише, якщо користувач автентифікований і має роль 'admin'.
    - Інакше — 403 Forbidden.
    """
    return {"message": "Ласкаво просимо, адміністраторе!"}