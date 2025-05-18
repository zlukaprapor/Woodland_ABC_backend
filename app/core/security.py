from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from jose import jwt
from typing import Dict, Any, Optional
from app.core.config import settings

# Контекст для хешування паролів з використанням алгоритму pbkdf2_sha256
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Хешує пароль за допомогою pbkdf2_sha256.

    Args:
        password (str): Пароль у відкритому вигляді.

    Returns:
        str: Хешований пароль.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Перевіряє, чи відповідає відкритий пароль хешованому.

    Args:
        plain_password (str): Пароль у відкритому вигляді.
        hashed_password (str): Хешований пароль для перевірки.

    Returns:
        bool: True, якщо пароль правильний, інакше False.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Створює JWT токен з вказаними даними і часом життя.

    Args:
        data (Dict[str, Any]): Дані для кодування у токен (наприклад, email, роль).
        expires_delta (Optional[timedelta]): Час дії токена. Якщо None, використовується налаштування за замовчуванням.

    Returns:
        str: Зашифрований JWT токен.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
