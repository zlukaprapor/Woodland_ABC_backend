from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Створення об'єкта engine для підключення до бази даних
engine = create_engine(settings.DATABASE_URL)

# Створення сесії
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Створення базового класу для моделей
Base = declarative_base()

# Функція для отримання сесії з базою даних
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()