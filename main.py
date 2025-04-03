from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.v1.routes import auth

app = FastAPI()

# Створення таблиць у базі даних
Base.metadata.create_all(bind=engine)

# Додавання маршруту до додатку
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
