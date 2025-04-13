from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.v1.routes import auth, lesson_first
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings

# Створення таблиць у базі даних
Base.metadata.create_all(bind=engine)

# Ініціалізація FastAPI додатку
app = FastAPI(
    title="Learning App API",
    description="API для навчального додатку",
    version="1.0.0"
)

# Додавання CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Монтування статичних файлів
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIRECTORY), name="media")

# Включення роутерів
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Автентифікація"])
app.include_router(lesson_first.router, prefix="/api/v1/lessons_first", tags=["Уроки"])

# Кореневий ендпоінт для перевірки працездатності API
@app.get("/")
def root():
    return {"status": "API працює", "version": "1.0.0"}