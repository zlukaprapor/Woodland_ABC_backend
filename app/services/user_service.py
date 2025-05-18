from sqlalchemy.orm import Session
from app.models.user import User, UserRole
from app.schemas.user import UserCreate
from app.core.security import hash_password
from fastapi import HTTPException, status
from app.core.logger import logger

def get_user_by_email(db: Session, email: str) -> User:
    """
    Отримує користувача за email.

    Args:
        db (Session): Сесія бази даних SQLAlchemy.
        email (str): Email користувача.

    Returns:
        User: Об'єкт користувача, якщо знайдено, інакше None.

    Логи:
        Виводить warning, якщо користувача з таким email не знайдено.
        Виводить error у випадку помилки при пошуку.
    """
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            logger.warning(f"Користувача з email {email} не знайдено")
        return user
    except Exception as e:
        logger.error(f"Помилка при пошуку користувача: {str(e)}")
        raise


def get_user_by_username(db: Session, username: str) -> User:
    """
    Отримує користувача за username.

    Args:
        db (Session): Сесія бази даних SQLAlchemy.
        username (str): Ім'я користувача.

    Returns:
        User: Об'єкт користувача, якщо знайдено, інакше None.
    """
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate, role: UserRole = UserRole.USER) -> User:
    """
    Створює нового користувача.

    Args:
        db (Session): Сесія бази даних SQLAlchemy.
        user (UserCreate): Схема з даними нового користувача.
        role (UserRole, optional): Роль користувача. За замовчуванням UserRole.USER.

    Raises:
        HTTPException: Якщо користувач з таким email або username вже існує.

    Returns:
        User: Створений об'єкт користувача.
    """
    # Перевірка, чи існує користувач з таким email
    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Користувач з таким email вже існує"
        )

    # Перевірка, чи існує користувач з таким username
    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Користувач з таким ім'ям користувача вже існує"
        )

    # Хешування паролю
    hashed_password = hash_password(user.password)

    # Створення нового користувача
    db_user = User(
        email=user.email,
        username=user.username,
        password_hash=hashed_password,
        role=role
    )

    # Збереження користувача в базі даних
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
