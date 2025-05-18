from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Enum
from sqlalchemy.sql import func
from app.db.database import Base
import enum

class UserRole(str, enum.Enum):
    """
    Перелік ролей користувачів.
    """
    ADMIN = "admin"
    USER = "user"

class User(Base):
    """
    Модель таблиці 'users' для збереження інформації про користувачів.

    Атрибути:
        id (int): Унікальний ідентифікатор користувача (PK).
        email (str): Електронна пошта користувача, унікальна, обов'язкова.
        username (str): Ім'я користувача, унікальне, обов'язкове.
        password_hash (str): Хешований пароль користувача.
        role (UserRole): Роль користувача (admin або user), за замовчуванням 'user'.
        is_active (bool): Статус активності користувача, за замовчуванням True.
        created_at (datetime): Час створення запису, встановлюється автоматично.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
