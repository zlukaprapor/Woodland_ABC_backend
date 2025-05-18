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
    """
    Створює новий урок з повним набором файлів та зберігає його у базу даних.

    Перевіряє унікальність літери, валідовує типи файлів, зберігає файли на диск,
    створює запис уроку та повертає об'єкт уроку.

    Аргументи:
        db (Session): сесія бази даних.
        letter_upper (str): велика літера уроку (унікальний ідентифікатор).
        letter_lower (str): мала літера.
        description (str): опис уроку.
        training (str): текст тренування.
        regulations (str): правила уроку.
        letter_image (UploadFile): зображення літери.
        object_image_first (UploadFile): перше зображення об’єкта.
        object_image_second (UploadFile): друге зображення об’єкта.
        object_image_third (UploadFile): третє зображення об’єкта.
        audio_file (UploadFile): аудіофайл уроку.
        quiz_file (UploadFile): файл з тестом.

    Повертає:
        LessonFirstDB: створений об'єкт уроку.

    Викидає:
        HTTPException(400) - якщо урок з такою літерою вже існує.
        HTTPException(500) - якщо сталася помилка при збереженні уроку або файлів.
    """
    # Перевірка, чи урок з такою великою літерою вже існує
    existing_lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
    if existing_lesson:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Урок з літерою {letter_upper} вже існує"
        )

    # Валідація типів усіх отриманих файлів
    validate_file_type(letter_image, settings.VALID_IMAGE_TYPES)
    validate_file_type(object_image_first, settings.VALID_IMAGE_TYPES)
    validate_file_type(object_image_second, settings.VALID_IMAGE_TYPES)
    validate_file_type(object_image_third, settings.VALID_IMAGE_TYPES)
    validate_file_type(audio_file, settings.VALID_AUDIO_TYPES)
    validate_file_type(quiz_file, settings.VALID_QUIZ_TYPES)

    try:
        # Збереження файлів у відповідних директоріях
        letter_image_path = save_upload_file(letter_image, f"{settings.LETTER_SUBDIRECTORY}/{letter_upper}")
        object_image_path_first = save_upload_file(object_image_first, f"{settings.OBJECT_SUBDIRECTORY}/{letter_upper}")
        object_image_path_second = save_upload_file(object_image_second, f"{settings.OBJECT_SUBDIRECTORY}/{letter_upper}")
        object_image_path_third = save_upload_file(object_image_third, f"{settings.OBJECT_SUBDIRECTORY}/{letter_upper}")
        audio_file_path = save_upload_file(audio_file, f"{settings.AUDIO_SUBDIRECTORY}/{letter_upper}")
        quiz_file_path = save_upload_file(quiz_file, f"{settings.QUIZ_SUBDIRECTORY}/{letter_upper}")

        # Створення нового уроку в базі даних
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
        # При помилці видаляємо вже збережені файли, щоб не лишати сміття
        delete_file_if_exists(letter_image_path if 'letter_image_path' in locals() else None)
        delete_file_if_exists(object_image_path_first if 'object_image_path_first' in locals() else None)
        delete_file_if_exists(object_image_path_second if 'object_image_path_second' in locals() else None)
        delete_file_if_exists(object_image_path_third if 'object_image_path_third' in locals() else None)
        delete_file_if_exists(audio_file_path if 'audio_file_path' in locals() else None)
        delete_file_if_exists(quiz_file_path if 'quiz_file_path' in locals() else None)

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
    """
    Оновлює існуючий урок, оновлюючи поля та/або файли.

    Підтримує часткове оновлення — можна оновити лише деякі поля або файли.

    Аргументи:
        db (Session): сесія бази даних.
        lesson_id (int): ID уроку для оновлення.
        letter_upper (Optional[str]): нова велика літера (унікальна).
        letter_lower (Optional[str]): нова мала літера.
        description (Optional[str]): новий опис.
        training (Optional[str]): новий текст тренування.
        regulations (Optional[str]): нові правила.
        letter_image (Optional[UploadFile]): нове зображення літери.
        object_image_first (Optional[UploadFile]): нове перше зображення об’єкта.
        object_image_second (Optional[UploadFile]): нове друге зображення об’єкта.
        object_image_third (Optional[UploadFile]): нове третє зображення об’єкта.
        audio_file (Optional[UploadFile]): новий аудіофайл.
        quiz_file (Optional[UploadFile]): новий файл з тестом.

    Повертає:
        LessonFirstDB: оновлений об'єкт уроку.

    Викидає:
        HTTPException(404) - якщо урок не знайдено.
        HTTPException(400) - якщо нова велика літера вже існує у іншого уроку.
        HTTPException(500) - при помилці оновлення.
    """
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Урок з ID {lesson_id} не знайдено"
        )

    # Якщо змінюємо велику літеру, перевіряємо унікальність
    if letter_upper is not None and letter_upper != lesson.letter_upper:
        existing_lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
        if existing_lesson:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Урок з літерою {letter_upper} вже існує"
            )

    try:
        # Оновлення текстових полів, якщо передані
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

        # Оновлення файлів — валідовуємо, видаляємо старі, зберігаємо нові
        if letter_image is not None:
            validate_file_type(letter_image, settings.VALID_IMAGE_TYPES)
            delete_file_if_exists(lesson.letter_image)
            lesson.letter_image = save_upload_file(letter_image, f"{settings.LETTER_SUBDIRECTORY}/{lesson.letter_upper}")

        if object_image_first is not None:
            validate_file_type(object_image_first, settings.VALID_IMAGE_TYPES)
            delete_file_if_exists(lesson.object_image_first)
            lesson.object_image_first = save_upload_file(object_image_first, f"{settings.OBJECT_SUBDIRECTORY}/{lesson.letter_upper}")

        if object_image_second is not None:
            validate_file_type(object_image_second, settings.VALID_IMAGE_TYPES)
            delete_file_if_exists(lesson.object_image_second)
            lesson.object_image_second = save_upload_file(object_image_second, f"{settings.OBJECT_SUBDIRECTORY}/{lesson.letter_upper}")

        if object_image_third is not None:
            validate_file_type(object_image_third, settings.VALID_IMAGE_TYPES)
            delete_file_if_exists(lesson.object_image_third)
            lesson.object_image_third = save_upload_file(object_image_third, f"{settings.OBJECT_SUBDIRECTORY}/{lesson.letter_upper}")

        if audio_file is not None:
            validate_file_type(audio_file, settings.VALID_AUDIO_TYPES)
            delete_file_if_exists(lesson.audio_file)
            lesson.audio_file = save_upload_file(audio_file, f"{settings.AUDIO_SUBDIRECTORY}/{lesson.letter_upper}")

        if quiz_file is not None:
            validate_file_type(quiz_file, settings.VALID_QUIZ_TYPES)
            delete_file_if_exists(lesson.quiz_file)
            lesson.quiz_file = save_upload_file(quiz_file, f"{settings.QUIZ_SUBDIRECTORY}/{lesson.letter_upper}")

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
    """
    Видаляє урок та пов’язані з ним файли за заданим ID.

    Аргументи:
        db (Session): сесія бази даних.
        lesson_id (int): ID уроку для видалення.

    Викидає:
        HTTPException(404) - якщо урок не знайдено.
        HTTPException(500) - при помилці видалення.
    """
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Урок з ID {lesson_id} не знайдено"
        )

    try:
        # Видалення всіх пов'язаних файлів
        delete_file_if_exists(lesson.letter_image)
        delete_file_if_exists(lesson.object_image_first)
        delete_file_if_exists(lesson.object_image_second)
        delete_file_if_exists(lesson.object_image_third)
        delete_file_if_exists(lesson.audio_file)
        delete_file_if_exists(lesson.quiz_file)

        # Видалення запису з БД
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
    """
    Повертає список уроків з підтримкою пагінації та фільтрації за літерою.

    Аргументи:
        db (Session): сесія бази даних.
        skip (int): кількість записів для пропуску (для пагінації).
        limit (int): максимальна кількість записів для вибірки.
        letter_filter (Optional[str]): фільтр за великою літерою (часткова співпадінність).

    Повертає:
        Tuple[List[LessonFirstDB], int]: кортеж зі списком уроків і загальною кількістю уроків, що відповідають фільтру.
    """
    query = db.query(LessonFirstDB)

    if letter_filter:
        query = query.filter(LessonFirstDB.letter_upper.contains(letter_filter))

    total = query.count()

    lessons = query.offset(skip).limit(limit).all()

    return lessons, total


def get_lesson_by_letter(db: Session, letter_upper: str) -> LessonFirstDB:
    """
    Повертає урок за великою літерою.

    Аргументи:
        db (Session): сесія бази даних.
        letter_upper (str): велика літера уроку.

    Повертає:
        LessonFirstDB: об'єкт уроку.

    Викидає:
        HTTPException(404) - якщо урок не знайдено.
    """
    lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Урок з літерою {letter_upper} не знайдено"
        )
    return lesson


def get_lesson_by_id(db: Session, lesson_id: int) -> LessonFirstDB:
    """
    Повертає урок за ID.

    Аргументи:
        db (Session): сесія бази даних.
        lesson_id (int): ID уроку.

    Повертає:
        LessonFirstDB: об'єкт уроку.

    Викидає:
        HTTPException(404) - якщо урок не знайдено.
    """
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Урок з ID {lesson_id} не знайдено"
        )
    return lesson
