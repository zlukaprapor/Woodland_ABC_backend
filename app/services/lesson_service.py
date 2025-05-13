from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException, status
from typing import Optional, Tuple, List
from app.models.lesson import LessonFirstDB
from app.utils.file_utils import save_upload_file, delete_file_if_exists, validate_file_type
from app.core.config import settings


def create_lesson_with_files(
        db: Session,
        letter_upper: str,
        letter_lower: str,
        description: str,
        training: str,
        regulations: str,
        letter_image: UploadFile,
        object_image_first: UploadFile,
        object_image_second: UploadFile,
        object_image_third: UploadFile,
        audio_file: UploadFile,
        quiz_file: UploadFile,
) -> LessonFirstDB:
    """Створює новий урок з файлами"""
    # Перевірка, чи не існує вже урок з такою літерою
    existing_lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
    if existing_lesson:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Урок з літерою {letter_upper} вже існує"
        )

    # Валідація файлів
    validate_file_type(letter_image, settings.VALID_IMAGE_TYPES)
    validate_file_type(object_image_first, settings.VALID_IMAGE_TYPES)
    validate_file_type(object_image_second, settings.VALID_IMAGE_TYPES)
    validate_file_type(object_image_third, settings.VALID_IMAGE_TYPES)
    validate_file_type(audio_file, settings.VALID_AUDIO_TYPES)
    validate_file_type(quiz_file, settings.VALID_QUIZ_TYPES)

    try:
        # Зберегти файли
        letter_image_path = save_upload_file(
            letter_image, f"{settings.LETTER_SUBDIRECTORY}/{letter_upper}"
        )
        object_image_path_first = save_upload_file(
            object_image_first, f"{settings.OBJECT_SUBDIRECTORY}/{letter_upper}"
        )
        object_image_path_second = save_upload_file(
            object_image_second, f"{settings.OBJECT_SUBDIRECTORY}/{letter_upper}"
        )
        object_image_path_third = save_upload_file(
            object_image_third, f"{settings.OBJECT_SUBDIRECTORY}/{letter_upper}"
        )
        audio_file_path = save_upload_file(
            audio_file, f"{settings.AUDIO_SUBDIRECTORY}/{letter_upper}"
        )
        quiz_file_path = save_upload_file(
            quiz_file, f"{settings.QUIZ_SUBDIRECTORY}/{letter_upper}")

        # Створити запис в БД
        new_lesson = LessonFirstDB(
            letter_upper=letter_upper,
            letter_lower=letter_lower,
            description=description,
            training=training,
            regulations=regulations,
            letter_image=letter_image_path,
            object_image_first=object_image_path_first,
            object_image_second=object_image_path_second,
            object_image_third=object_image_path_third,
            audio_file=audio_file_path,
            quiz_file=quiz_file_path,
        )

        db.add(new_lesson)
        db.commit()
        db.refresh(new_lesson)

        return new_lesson
    except Exception as e:
        delete_file_if_exists(letter_image_path if 'letter_image_path' in locals() else None)
        delete_file_if_exists(object_image_path_first if 'object_image_path_first' in locals() else None)
        delete_file_if_exists(object_image_path_second if 'object_image_path_second' in locals() else None)
        delete_file_if_exists(object_image_path_third if 'object_image_path_third' in locals() else None)
        delete_file_if_exists(audio_file_path if 'audio_file_path' in locals() else None)
        delete_file_if_exists(quiz_file_path if 'quiz_file_path' in locals() else None)

        # Піднімаємо помилку вище
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при створенні уроку: {str(e)}"
        )


def update_lesson_with_files(
        db: Session,
        lesson_id: int,
        letter_upper: Optional[str] = None,
        letter_lower: Optional[str] = None,
        description: Optional[str] = None,
        training: Optional[str] = None,
        regulations: Optional[str] = None,
        letter_image: Optional[UploadFile] = None,
        object_image_first: Optional[UploadFile] = None,
        object_image_second: Optional[UploadFile] = None,
        object_image_third: Optional[UploadFile] = None,
        audio_file: Optional[UploadFile] = None,
        quiz_file: Optional[UploadFile] = None
) -> LessonFirstDB:
    """Оновлює існуючий урок з файлами"""
    # Отримати існуючий урок
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Урок з ID {lesson_id} не знайдено"
        )

    # Перевірка, чи не існує вже урок з такою ж літерою (якщо літера змінюється)
    if letter_upper is not None and letter_upper != lesson.letter_upper:
        existing_lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
        if existing_lesson:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Урок з літерою {letter_upper} вже існує"
            )

    try:
        # Оновити текстові поля, якщо вони надані
        if letter_upper is not None:
            lesson.letter_upper = letter_upper
        if letter_lower is not None:
            lesson.letter_lower = letter_lower
        if description is not None:
            lesson.description = description
        if training is not None:
            lesson.training = training
        if regulations is not None:
            lesson.regulations = regulations
        if letter_image is not None:
            validate_file_type(letter_image, settings.VALID_IMAGE_TYPES)
            delete_file_if_exists(lesson.letter_image)
            lesson.letter_image = save_upload_file(
                letter_image, f"{settings.LETTER_SUBDIRECTORY}/{lesson.letter_upper}"
            )

        if object_image_first is not None:
            validate_file_type(object_image_first, settings.VALID_IMAGE_TYPES)
            delete_file_if_exists(lesson.object_image_first)
            lesson.object_image_first = save_upload_file(
                object_image_first,f"{settings.OBJECT_SUBDIRECTORY}/{lesson.letter_upper}"
            )

        if object_image_second is not None:
            validate_file_type(object_image_second, settings.VALID_IMAGE_TYPES)
            delete_file_if_exists(lesson.object_image_second)
            lesson.object_image_second = save_upload_file(
                object_image_second,f"{settings.OBJECT_SUBDIRECTORY}/{lesson.letter_upper}"
            )

        if object_image_third is not None:
            validate_file_type(object_image_third, settings.VALID_IMAGE_TYPES)
            delete_file_if_exists(lesson.object_image_third)
            lesson.object_image_third = save_upload_file(
                object_image_third,f"{settings.OBJECT_SUBDIRECTORY}/{lesson.letter_upper}"
            )

        if audio_file is not None:
            validate_file_type(audio_file, settings.VALID_AUDIO_TYPES)
            delete_file_if_exists(lesson.audio_file)
            lesson.audio_file = save_upload_file(
                audio_file, f"{settings.AUDIO_SUBDIRECTORY}/{lesson.letter_upper}"
            )

        if quiz_file is not None:
            validate_file_type(quiz_file, settings.VALID_QUIZ_TYPES)
            delete_file_if_exists(lesson.quiz_file)
            lesson.quiz_file = save_upload_file(
                quiz_file, f"{settings.QUIZ_SUBDIRECTORY}/{lesson.letter_upper}"
            )

        db.commit()
        db.refresh(lesson)

        return lesson
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при оновленні уроку: {str(e)}"
        )


def delete_lesson(db: Session, lesson_id: int) -> None:
    """Видаляє урок за ID"""
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Урок з ID {lesson_id} не знайдено"
        )

    try:
        # Видалити файли
        delete_file_if_exists(lesson.letter_image)
        delete_file_if_exists(lesson.object_image_first)
        delete_file_if_exists(lesson.object_image_second)
        delete_file_if_exists(lesson.object_image_third)
        delete_file_if_exists(lesson.audio_file)
        delete_file_if_exists(lesson.quiz_file)

        # Видалити запис з БД
        db.delete(lesson)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при видаленні уроку: {str(e)}"
        )


def get_all_lessons(
        db: Session,
        skip: int = 0,
        limit: int = 10,
        letter_filter: Optional[str] = None
) -> Tuple[List[LessonFirstDB], int]:
    """Отримує список уроків з пагінацією та фільтрацією"""
    query = db.query(LessonFirstDB)

    # Застосувати фільтр за літерою, якщо він наданий
    if letter_filter:
        query = query.filter(LessonFirstDB.letter_upper.contains(letter_filter))

    # Отримати загальну кількість записів
    total = query.count()

    # Застосувати пагінацію
    lessons = query.offset(skip).limit(limit).all()

    return lessons, total


def get_lesson_by_letter(db: Session, letter_upper: str) -> LessonFirstDB:
    """Отримує урок за великою літерою"""
    lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Урок з літерою {letter_upper} не знайдено"
        )
    return lesson


def get_lesson_by_id(db: Session, lesson_id: int) -> LessonFirstDB:
    """Отримує урок за ID"""
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Урок з ID {lesson_id} не знайдено"
        )
    return lesson