from sqlalchemy import text

from app.db.database import SessionLocal

try:
    db = SessionLocal()
    db.execute(text("SELECT 1"))  # Виконуємо тестовий SQL-запит
    print("✅ Підключення до БД успішне!")
except Exception as e:
    print("❌ Помилка підключення до БД:", e)
finally:
    db.close()
