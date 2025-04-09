import os
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.models.lesson_first import LessonFirstDB
from uuid import uuid4
from pathlib import Path
from app.core.config import LETTER_IMG_SUBDIR, OBJECT_IMG_SUBDIR, AUDIO_SUBDIR
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

UPLOAD_DIR = "media/lessons_first"

def save_file(file: UploadFile, subfolder: str = "") -> str:
    Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
    ext = file.filename.split('.')[-1]
    filename = f"{uuid4()}.{ext}"
    file_path = os.path.join(UPLOAD_DIR, subfolder, filename)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path.replace("\\", "/")  # for Windows compatibility

def create_lesson_with_files(
    db: Session,
    letter_upper: str,
    letter_lower: str,
    description: str,
    letter_image: UploadFile,
    object_image: UploadFile,
    audio_file: UploadFile,
) -> LessonFirstDB:
    lesson = LessonFirstDB(
        letter_upper=letter_upper,
        letter_lower=letter_lower,
        description=description,
        letter_image=save_file(letter_image, LETTER_IMG_SUBDIR),
        object_image=save_file(object_image, OBJECT_IMG_SUBDIR),
        audio_file=save_file(audio_file, AUDIO_SUBDIR),
    )
    db.add(lesson)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Урок з великою літерою '{letter_upper}' вже існує."
        )
    db.refresh(lesson)
    return lesson
