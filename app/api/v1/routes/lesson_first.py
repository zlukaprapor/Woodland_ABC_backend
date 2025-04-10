from fastapi import APIRouter, Depends, Form, UploadFile, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.services.lesson_service import (
    create_lesson_with_files,
    update_lesson_with_files,
    delete_lesson,
    get_all_lessons
)
from app.schemas.lesson_first import LessonFirstResponse, LessonFirstListResponse
from app.models.lesson_first import LessonFirstDB

router = APIRouter()


@router.post("/create-with-files", response_model=LessonFirstResponse, status_code=status.HTTP_201_CREATED)
def create_lesson_with_media(
        letter_upper: str = Form(...),
        letter_lower: str = Form(...),
        description: str = Form(...),
        letter_image: UploadFile = Form(...),
        object_image: UploadFile = Form(...),
        audio_file: UploadFile = Form(...),
        db: Session = Depends(get_db),
):
    """Створення нового уроку з файлами"""
    # Валідація букв
    if len(letter_upper) != 1 or len(letter_lower) != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Літери повинні бути одиночними символами"
        )

    # Валідація розширень файлів
    valid_image_types = ["image/jpeg", "image/png", "image/webp"]
    valid_audio_types = ["audio/mpeg", "audio/mp3", "audio/wav"]

    if letter_image.content_type not in valid_image_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Зображення літери повинно бути в форматі JPEG, PNG або WEBP"
        )

    if object_image.content_type not in valid_image_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Зображення об'єкта повинно бути в форматі JPEG, PNG або WEBP"
        )

    if audio_file.content_type not in valid_audio_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Аудіо файл повинен бути в форматі MP3 або WAV"
        )

    try:
        return create_lesson_with_files(
            db=db,
            letter_upper=letter_upper,
            letter_lower=letter_lower,
            description=description,
            letter_image=letter_image,
            object_image=object_image,
            audio_file=audio_file,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при створенні уроку: {str(e)}"
        )


@router.put("/{lesson_id}", response_model=LessonFirstResponse)
def update_lesson(
        lesson_id: int,
        letter_upper: Optional[str] = Form(None),
        letter_lower: Optional[str] = Form(None),
        description: Optional[str] = Form(None),
        letter_image: Optional[UploadFile] = Form(None),
        object_image: Optional[UploadFile] = Form(None),
        audio_file: Optional[UploadFile] = Form(None),
        db: Session = Depends(get_db),
):
    """Оновлення існуючого уроку"""
    # Перевіряємо, чи існує урок
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Урок не знайдено"
        )

    # Валідація букв, якщо вони передані
    if letter_upper is not None and len(letter_upper) != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Велика літера повинна бути одиночним символом"
        )

    if letter_lower is not None and len(letter_lower) != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Мала літера повинна бути одиночним символом"
        )

    # Валідація файлів, якщо вони передані
    if letter_image is not None:
        valid_image_types = ["image/jpeg", "image/png", "image/webp"]
        if letter_image.content_type not in valid_image_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Зображення літери повинно бути в форматі JPEG, PNG або WEBP"
            )

    if object_image is not None:
        valid_image_types = ["image/jpeg", "image/png", "image/webp"]
        if object_image.content_type not in valid_image_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Зображення об'єкта повинно бути в форматі JPEG, PNG або WEBP"
            )

    if audio_file is not None:
        valid_audio_types = ["audio/mpeg", "audio/mp3", "audio/wav"]
        if audio_file.content_type not in valid_audio_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Аудіо файл повинен бути в форматі MP3 або WAV"
            )

    try:
        return update_lesson_with_files(
            db=db,
            lesson_id=lesson_id,
            letter_upper=letter_upper,
            letter_lower=letter_lower,
            description=description,
            letter_image=letter_image,
            object_image=object_image,
            audio_file=audio_file,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при оновленні уроку: {str(e)}"
        )


@router.delete("/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_lesson(
        lesson_id: int,
        db: Session = Depends(get_db),
):
    """Видалення уроку за ID"""
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Урок не знайдено"
        )

    try:
        delete_lesson(db=db, lesson_id=lesson_id)
        return {"message": "Урок успішно видалено"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при видаленні уроку: {str(e)}"
        )


@router.get("/", response_model=LessonFirstListResponse)
def list_lessons(
        skip: int = Query(0, ge=0, description="Кількість записів для пропуску (пагінація)"),
        limit: int = Query(10, ge=1, le=100, description="Кількість записів для отримання (пагінація)"),
        letter_filter: Optional[str] = Query(None, description="Фільтр за літерою"),
        db: Session = Depends(get_db)
):
    """Отримання списку всіх уроків з можливістю пагінації та фільтрації"""
    try:
        lessons, total = get_all_lessons(
            db=db,
            skip=skip,
            limit=limit,
            letter_filter=letter_filter
        )
        return {
            "items": lessons,
            "total": total,
            "skip": skip,
            "limit": limit
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при отриманні списку уроків: {str(e)}"
        )


@router.get("/get-by-letter", response_model=LessonFirstResponse)
def get_lesson_by_letter(
        letter_upper: str = Query(..., description="Велика літера"),
        db: Session = Depends(get_db),
):
    """Отримання уроку за великою літерою"""
    if len(letter_upper) != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Літера повинна бути одиночним символом"
        )

    lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Літеру не знайдено"
        )
    return lesson


@router.get("/{lesson_id}", response_model=LessonFirstResponse)
def get_lesson_by_id(
        lesson_id: int,
        db: Session = Depends(get_db),
):
    """Отримання уроку за ID"""
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Урок не знайдено"
        )
    return lesson