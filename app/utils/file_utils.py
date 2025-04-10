import os
import uuid
from pathlib import Path
from fastapi import UploadFile
import shutil

UPLOAD_DIRECTORY = "uploads"


def ensure_upload_directory(directory: str) -> str:
    """
    Переконується, що директорія існує, якщо ні - створює її
    """
    full_path = os.path.join(UPLOAD_DIRECTORY, directory)
    Path(full_path).mkdir(parents=True, exist_ok=True)
    return full_path


def save_upload_file(upload_file: UploadFile, directory: str) -> str:
    """
    Зберігає завантажений файл у вказану директорію
    Повертає шлях до збереженого файлу
    """
    # Переконатися, що директорія існує
    upload_dir = ensure_upload_directory(directory)

    # Створити унікальне ім'я файлу
    file_extension = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"

    # Повний шлях до файлу
    file_path = os.path.join(upload_dir, unique_filename)

    # Зберегти файл
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    # Повернути відносний шлях для зберігання в БД
    return os.path.join(directory, unique_filename)


def delete_file_if_exists(file_path: str) -> None:
    """
    Видаляє файл, якщо він існує
    """
    if file_path and os.path.isfile(os.path.join(UPLOAD_DIRECTORY, file_path)):
        os.remove(os.path.join(UPLOAD_DIRECTORY, file_path))