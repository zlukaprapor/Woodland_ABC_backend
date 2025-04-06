from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.v1.routes import auth
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import lesson_first
app = FastAPI()

# Створення таблиць у базі даних
Base.metadata.create_all(bind=engine)

# Додавання маршруту до додатку
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(lesson_first.router, prefix="/api/v1/lessons", tags=["Lessons"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # або ["*"] для всіх, на час розробки
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)