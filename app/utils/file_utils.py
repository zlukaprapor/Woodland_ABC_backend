import os
import uuid
from pathlib import Path
from fastapi import UploadFile, HTTPException, status
import shutil
from typing import List
from app.core.config import settings


def validate_file_type(file: UploadFile, allowed_types: List[str]) -> None:
    """Перевірка типу файлу"""
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Непідтримуваний тип файлу. Допустимі типи: {', '.join(allowed_types)}"
        )


def ensure_upload_directory(directory: str) -> str:
    """Переконується, що директорія існує, якщо ні - створює її"""
    full_path = os.path.join(settings.UPLOAD_DIRECTORY, directory)
    Path(full_path).mkdir(parents=True, exist_ok=True)
    return full_path


def save_upload_file(upload_file: UploadFile, directory: str) -> str:
    """Зберігає завантажений файл у вказану директорію"""
    # Переконатися, що директорія існує
    upload_dir = ensure_upload_directory(directory)

    # Створити унікальне ім'я файлу
    file_extension = os.path.splitext(upload_file.filename)[1].lower()
    unique_filename = f"{uuid.uuid4()}{file_extension}"

    # Повний шлях до файлу
    file_path = os.path.join(upload_dir, unique_filename)

    # Зберегти файл
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при збереженні файлу: {str(e)}"
        )

    # Повернути відносний шлях для зберігання в БД
    return os.path.join(directory, unique_filename)


def delete_file_if_exists(file_path: str) -> None:
    """Видаляє файл, якщо він існує"""
    if not file_path:
        return

    full_path = os.path.join(settings.UPLOAD_DIRECTORY, file_path)
    if os.path.isfile(full_path):
        try:
            os.remove(full_path)
        except Exception as e:
            # Логуємо помилку, але не викидаємо виняток
            print(f"Помилка при видаленні файлу {full_path}: {str(e)}")