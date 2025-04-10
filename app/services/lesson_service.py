from sqlalchemy.orm import Session
from fastapi import UploadFile
from typing import Optional, Tuple, List
import os
from app.models.lesson_first import LessonFirstDB
from app.utils.file_utils import save_upload_file, delete_file_if_exists


def create_lesson_with_files(
        db: Session,
        letter_upper: str,
        letter_lower: str,
        description: str,
        letter_image: UploadFile,
        object_image: UploadFile,
        audio_file: UploadFile,
) -> LessonFirstDB:
    """
    Створює новий урок з файлами
    """
    # Перевірка, чи не існує вже урок з такою літерою
    existing_lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
    if existing_lesson:
        raise ValueError(f"Урок з літерою {letter_upper} вже існує")

    # Зберегти файли
    letter_image = save_upload_file(letter_image, f"letters/{letter_upper}")
    object_image = save_upload_file(object_image, f"objects/{letter_upper}")
    audio_file = save_upload_file(audio_file, f"audio/{letter_upper}")

    # Створити запис в БД
    new_lesson = LessonFirstDB(
        letter_upper=letter_upper,
        letter_lower=letter_lower,
        description=description,
        letter_image=letter_image,
        object_image=object_image,
        audio_file=audio_file
    )

    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)

    return new_lesson


def update_lesson_with_files(
        db: Session,
        lesson_id: int,
        letter_upper: Optional[str] = None,
        letter_lower: Optional[str] = None,
        description: Optional[str] = None,
        letter_image: Optional[UploadFile] = None,
        object_image: Optional[UploadFile] = None,
        audio_file: Optional[UploadFile] = None,
) -> LessonFirstDB:
    """
    Оновлює існуючий урок з файлами
    """
    # Отримати існуючий урок
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise ValueError(f"Урок з ID {lesson_id} не знайдено")

    # Перевірка, чи не існує вже урок з такою ж літерою (якщо літера змінюється)
    if letter_upper is not None and letter_upper != lesson.letter_upper:
        existing_lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
        if existing_lesson:
            raise ValueError(f"Урок з літерою {letter_upper} вже існує")

    # Оновити текстові поля, якщо вони надані
    if letter_upper is not None:
        lesson.letter_upper = letter_upper
    if letter_lower is not None:
        lesson.letter_lower = letter_lower
    if description is not None:
        lesson.description = description

    # Оновити файли, якщо вони надані
    if letter_image is not None:
        # Видалити старий файл
        delete_file_if_exists(lesson.letter_image)
        # Зберегти новий файл
        lesson.letter_image = save_upload_file(letter_image, f"letters/{lesson.letter_upper}")

    if object_image is not None:
        delete_file_if_exists(lesson.object_image)
        lesson.object_image = save_upload_file(object_image, f"objects/{lesson.letter_upper}")

    if audio_file is not None:
        delete_file_if_exists(lesson.audio_file)
        lesson.audio_file = save_upload_file(audio_file, f"audio/{lesson.letter_upper}")

    db.commit()
    db.refresh(lesson)

    return lesson


def delete_lesson(db: Session, lesson_id: int) -> None:
    """
    Видаляє урок за ID
    """
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise ValueError(f"Урок з ID {lesson_id} не знайдено")

    # Видалити файли
    delete_file_if_exists(lesson.letter_image)
    delete_file_if_exists(lesson.object_image)
    delete_file_if_exists(lesson.audio_file)

    # Видалити запис з БД
    db.delete(lesson)
    db.commit()


def get_all_lessons(
        db: Session,
        skip: int = 0,
        limit: int = 10,
        letter_filter: Optional[str] = None
) -> Tuple[List[LessonFirstDB], int]:
    """
    Отримує список уроків з пагінацією та фільтрацією
    """
    query = db.query(LessonFirstDB)

    # Застосувати фільтр за літерою, якщо він наданий
    if letter_filter:
        query = query.filter(LessonFirstDB.letter_upper.contains(letter_filter))

    # Отримати загальну кількість записів
    total = query.count()

    # Застосувати пагінацію
    lessons = query.offset(skip).limit(limit).all()

    return lessons, total