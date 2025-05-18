from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Створення об'єкта engine для підключення до бази даних
engine = create_engine(settings.DATABASE_URL)

# Конфігурація сесії для роботи з базою даних
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для декларації моделей SQLAlchemy
Base = declarative_base()

def get_db():
    """
    Генератор сесії бази даних.

    Використовується як залежність у маршрутах FastAPI для отримання сесії бази даних.
    Забезпечує відкриття сесії при вході у маршрут і автоматичне закриття після завершення роботи.

    Yields:
        Session: Активна сесія SQLAlchemy для роботи з базою даних.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
