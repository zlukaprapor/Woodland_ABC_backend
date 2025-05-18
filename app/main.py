from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.v1.routes import auth, lesson, progress
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.core.logger import logger

# Створення таблиць у базі даних, якщо вони ще не створені
Base.metadata.create_all(bind=engine)

# Ініціалізація FastAPI додатку
app = FastAPI(
    title="Learning App API",
    description="API для навчального додатку",
    version="1.0.0"
)

# Додавання CORS middleware для дозволу запитів з певних origin-ів
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,  # Дозволені джерела запитів
    allow_credentials=True,
    allow_methods=["*"],  # Дозволені HTTP методи
    allow_headers=["*"],  # Дозволені заголовки
)

# Монтування директорії зі статичними файлами, щоб вони були доступні за URL /uploads
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIRECTORY), name="media")

# Підключення роутерів для різних частин API з відповідними префіксами і тегами
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Автентифікація"])
app.include_router(lesson.router, prefix="/api/v1/lessons", tags=["Уроки"])
app.include_router(progress.router, prefix="/api/v1/progress", tags=["Прогрес"])

@app.get("/")
def root():
    """
    Кореневий ендпоінт для перевірки працездатності API.
    Повертає статус роботи та версію API.
    """
    return {"status": "API працює", "version": "1.0.0"}

@app.on_event("startup")
async def startup_event():
    """Обробник події запуску додатку"""
    logger.info("🚀 Програма запущена")

@app.on_event("shutdown")
async def shutdown_event():
    """Обробник події зупинки додатку"""
    logger.info("🛑 Програма зупинена")
