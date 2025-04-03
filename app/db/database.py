from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()  # Завантажуємо змінні середовища з файлу .env

# Перевірка наявності DATABASE_URL в змінних середовища
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in environment variables")

# Створення об'єкта engine для підключення до бази даних
engine = create_engine(DATABASE_URL)

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

# Створення таблиць (якщо вони не існують)
# Це потрібно для того, щоб таблиці були створені автоматично в базі даних
Base.metadata.create_all(bind=engine)
