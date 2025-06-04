from pathlib import Path
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List

# Завантажуємо змінні середовища з файлу .env
load_dotenv()


class Settings(BaseSettings):
    """
    Клас налаштувань додатку, який зчитує конфігурацію зі змінних середовища
    або файлу .env за допомогою Pydantic BaseSettings.

    Атрибути:
    ----------
    DATABASE_URL : str
        URL для підключення до бази даних.
    SECRET_KEY : str
        Секретний ключ для JWT токенів.
    ALGORITHM : str
        Алгоритм для JWT, за замовчуванням 'HS256'.
    ACCESS_TOKEN_EXPIRE_MINUTES : int
        Час життя JWT токену в хвилинах, за замовчуванням 30.
    CORS_ORIGINS : list[str]
        Дозволені адреси для CORS-запитів.
    UPLOAD_DIRECTORY : str
        Головна директорія для збереження завантажених файлів.
    LETTER_SUBDIRECTORY : str
        Піддиректорія для збереження зображень літер.
    OBJECT_SUBDIRECTORY : str
        Піддиректорія для збереження зображень об’єктів.
    AUDIO_SUBDIRECTORY : str
        Піддиректорія для збереження аудіофайлів.
    QUIZ_SUBDIRECTORY : str
        Піддиректорія для збереження файлів з вікторинами (quiz).
    VALID_IMAGE_TYPES : list[str]
        Список дозволених MIME-типів для зображень.
    VALID_AUDIO_TYPES : list[str]
        Список дозволених MIME-типів для аудіо.
    VALID_QUIZ_TYPES : list[str]
        Список дозволених MIME-типів для файлів вікторини.
    """

    # База даних
    DATABASE_URL: str

    # JWT налаштування
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Налаштування CORS
    CORS_ORIGINS: list[str] = ["http://localhost:8000", "http://localhost:3000", "http://localhost:5173"]

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
        """Конфігурація Pydantic для завантаження змінних середовища."""
        env_file = ".env"
        case_sensitive = True


# Ініціалізація налаштувань додатку
settings = Settings()

# Створення головної директорії для завантажень (якщо вона не існує)
Path(settings.UPLOAD_DIRECTORY).mkdir(parents=True, exist_ok=True)
