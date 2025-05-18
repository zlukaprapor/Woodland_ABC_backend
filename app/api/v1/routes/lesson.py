from fastapi import APIRouter, Depends, Form, UploadFile, HTTPException, Query, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Optional

from app.db.database import get_db
from app.core.dependencies import get_current_admin_user
from app.services.lesson_service import (
    create_lesson_with_files,
    update_lesson_with_files,
    delete_lesson,
    get_all_lessons,
    get_lesson_by_letter,
    get_lesson_by_id
)
from app.schemas.lesson import LessonFirstResponse, LessonFirstListResponse


router = APIRouter()

@router.post(
    "/create-with-files",
    response_model=LessonFirstResponse,
    status_code=status.HTTP_201_CREATED,
    #dependencies=[Depends(get_current_admin_user)],
    summary="Створити урок з файлами",
    description=(
        "Створює новий урок з повним набором медіафайлів:\n"
        "- верхня та нижня літери\n"
        "- опис, тренування, регламенти\n"
        "- зображення (літера, три об'єкти)\n"
        "- аудіо та файл тесту\n\n"
        "Параметри приймаються як multipart/form-data."
    )
)
def create_lesson_with_media(
        letter_upper: str = Form(..., min_length=1, max_length=1, description="Верхня літера"),
        letter_lower: str = Form(..., min_length=1, max_length=1, description="Нижня літера"),
        description: str = Form(..., description="Опис уроку"),
        training: str = Form(..., description="Матеріали для тренування"),
        regulations: str = Form(..., description="Правила"),
        letter_image: UploadFile = Form(..., description="Зображення літери"),
        object_image_first: UploadFile = Form(..., description="Зображення першого об'єкта"),
        object_image_second: UploadFile = Form(..., description="Зображення другого об'єкта"),
        object_image_third: UploadFile = Form(..., description="Зображення третього об'єкта"),
        audio_file: UploadFile = Form(..., description="Аудіофайл"),
        quiz_file: UploadFile = Form(..., description="Файл тесту"),
        db: Session = Depends(get_db),
):
    try:
        return create_lesson_with_files(
            db=db,
            letter_upper=letter_upper,
            letter_lower=letter_lower,
            description=description,
            training=training,
            regulations=regulations,
            letter_image=letter_image,
            object_image_first=object_image_first,
            object_image_second=object_image_second,
            object_image_third=object_image_third,
            audio_file=audio_file,
            quiz_file=quiz_file,
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при створенні уроку: {str(e)}"
        )


@router.put(
    "/{lesson_id}",
    response_model=LessonFirstResponse,
    dependencies=[Depends(get_current_admin_user)],
    summary="Оновити урок",
    description=(
        "Оновлює існуючий урок за ID.\n"
        "Підтримується часткове оновлення: можна передати будь-які поля або файли."
    )
)
def update_lesson(
        lesson_id: int,
        letter_upper: Optional[str] = Form(None, min_length=1, max_length=1, description="Верхня літера"),
        letter_lower: Optional[str] = Form(None, min_length=1, max_length=1, description="Нижня літера"),
        description: Optional[str] = Form(None, description="Опис уроку"),
        training: Optional[str] = Form(None, description="Матеріали для тренування"),
        regulations: Optional[str] = Form(None, description="Правила"),
        letter_image: Optional[UploadFile] = Form(None, description="Зображення літери"),
        object_image_first: Optional[UploadFile] = Form(None, description="Зображення першого об'єкта"),
        object_image_second: Optional[UploadFile] = Form(None, description="Зображення другого об'єкта"),
        object_image_third: Optional[UploadFile] = Form(None, description="Зображення третього об'єкта"),
        audio_file: Optional[UploadFile] = Form(None, description="Аудіофайл"),
        quiz_file: Optional[UploadFile] = Form(None, description="Файл тесту"),
        db: Session = Depends(get_db),
):
    try:
        return update_lesson_with_files(
            db=db,
            lesson_id=lesson_id,
            letter_upper=letter_upper,
            letter_lower=letter_lower,
            description=description,
            training=training,
            regulations=regulations,
            letter_image=letter_image,
            object_image_first=object_image_first,
            object_image_second=object_image_second,
            object_image_third=object_image_third,
            audio_file=audio_file,
            quiz_file=quiz_file,
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при оновленні уроку: {str(e)}"
        )


@router.delete(
    "/{lesson_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_current_admin_user)],
    summary="Видалити урок",
    description="Видаляє урок за заданим ID."
)
def remove_lesson(
        lesson_id: int,
        db: Session = Depends(get_db),
):
    try:
        delete_lesson(db=db, lesson_id=lesson_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Урок успішно видалено"}
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при видаленні уроку: {str(e)}"
        )


@router.get(
    "/",
    response_model=LessonFirstListResponse,
    summary="Список уроків",
    description="Отримання списку уроків з підтримкою пагінації та фільтрації за літерою."
)
def list_lessons(
        skip: int = Query(0, ge=0, description="Кількість записів для пропуску (пагінація)"),
        limit: int = Query(10, ge=1, le=100, description="Кількість записів для отримання (пагінація)"),
        letter_filter: Optional[str] = Query(None, description="Фільтр за літерою"),
        db: Session = Depends(get_db)
):
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
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при отриманні списку уроків: {str(e)}"
        )


@router.get(
    "/get-by-letter",
    response_model=LessonFirstResponse,
    summary="Отримати урок за літерою",
    description="Повертає урок за великою літерою."
)
def get_lesson_by_letter_route(
        letter_upper: str = Query(..., min_length=1, max_length=1, description="Велика літера"),
        db: Session = Depends(get_db),
):
    try:
        return get_lesson_by_letter(db, letter_upper)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при отриманні уроку за літерою: {str(e)}"
        )


@router.get(
    "/{lesson_id}",
    response_model=LessonFirstResponse,
    summary="Отримати урок за ID",
    description="Повертає урок за його унікальним ID."
)
def get_lesson_by_id_route(
        lesson_id: int,
        db: Session = Depends(get_db),
):
    try:
        return get_lesson_by_id(db, lesson_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при отриманні уроку за ID: {str(e)}"
        )
