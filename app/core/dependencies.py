from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.user import User
from app.db.database import get_db

# OAuth2-схема для отримання токена з HTTP-запиту
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

class TokenData(BaseModel):
    """
    Модель для зберігання даних, отриманих із JWT токена.

    Атрибути:
    ----------
    email : Optional[str]
        Email користувача, отриманий з токена.
    role : Optional[str]
        Роль користувача (наприклад, "admin", "user").
    """
    email: Optional[str] = None
    role: Optional[str] = None

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """
    Отримує поточного користувача з бази даних на основі JWT токена.

    Аргументи:
    -----------
    token : str
        JWT токен, отриманий через OAuth2PasswordBearer.
    db : Session
        Сесія бази даних SQLAlchemy.

    Повертає:
    ---------
    User
        Об'єкт користувача з бази даних.

    Викликає HTTPException з кодом 401, якщо токен недійсний або користувач не знайдений.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Недійсні облікові дані",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    return user

def get_current_admin_user(token_data: TokenData = Depends(get_current_user)):
    """
    Перевіряє, чи є поточний користувач адміністратором.

    Аргументи:
    ----------
    token_data : TokenData
        Дані користувача, отримані через Depends(get_current_user).

    Повертає:
    ---------
    TokenData
        Дані користувача, якщо він має роль адміністратора.

    Викликає HTTPException з кодом 403, якщо роль користувача не "admin".
    """
    if token_data.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Недостатньо прав для виконання цієї дії"
        )
    return token_data
