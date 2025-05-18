from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole


class UserBase(BaseModel):
    """
    Загальна базова схема користувача.
    """
    email: EmailStr = Field(..., description="Email користувача")
    username: str = Field(..., min_length=3, max_length=50, description="Ім'я користувача")


class UserCreate(UserBase):
    """
    Схема для створення нового користувача.
    """
    password: str = Field(..., min_length=8, description="Пароль користувача")


class UserLogin(BaseModel):
    """
    Схема для аутентифікації користувача (логін).
    """
    email: EmailStr = Field(..., description="Email користувача")
    password: str = Field(..., description="Пароль користувача")


class UserResponse(UserBase):
    """
    Схема відповіді з даними користувача.
    """
    id: int = Field(..., description="Унікальний ідентифікатор користувача")
    role: UserRole = Field(..., description="Роль користувача")
    is_active: bool = Field(..., description="Статус активності користувача")

    class Config:
        from_attributes = True  # Автоматичне створення з ORM моделей


class Token(BaseModel):
    """
    Схема для JWT токена та пов’язаної інформації про користувача.
    """
    access_token: str = Field(..., description="JWT токен доступу")
    token_type: str = Field(..., description="Тип токена, зазвичай 'bearer'")
    user: UserResponse = Field(..., description="Дані користувача, що відповідають токену")
