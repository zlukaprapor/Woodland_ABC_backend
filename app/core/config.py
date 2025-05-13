from pathlib import Path
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List
load_dotenv()


class Settings(BaseSettings):
    # База даних
    DATABASE_URL: str

    # JWT налаштування
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Налаштування CORS
    CORS_ORIGINS: list[str] = ["http://localhost:8000","http://localhost:5173",]

    # Директорії для файлів
    UPLOAD_DIRECTORY: str = "uploads"

    # Піддиректорії для уроків
    LETTER_SUBDIRECTORY: str = "letters"
    OBJECT_SUBDIRECTORY: str = "objects"
    AUDIO_SUBDIRECTORY: str = "audio"
    QUIZ_SUBDIRECTORY: str = "quiz"

    # Допустимі формати файлів
    VALID_IMAGE_TYPES: list[str] = ["image/jpeg", "image/png", "image/webp"]
    VALID_AUDIO_TYPES: list[str] = ["audio/mpeg", "audio/mp3", "audio/wav"]
    VALID_QUIZ_TYPES: list[str] = ["application/json"]

    class Config:
        env_file = ".env"
        case_sensitive = True


# Ініціалізація налаштувань
settings = Settings()

# Створення необхідних директорій
Path(settings.UPLOAD_DIRECTORY).mkdir(parents=True, exist_ok=True)