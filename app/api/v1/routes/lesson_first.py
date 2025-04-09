from fastapi import APIRouter, Depends, Form, UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.lesson_service import create_lesson_with_files
from app.schemas.lesson_first import LessonFirstResponse
from fastapi import Query
from app.models.lesson_first import LessonFirstDB
from app.schemas.lesson_first import LessonFirstResponse
router = APIRouter()

@router.post("/create-with-files", response_model=LessonFirstResponse)
def create_lesson_with_media(
    letter_upper: str = Form(...),
    letter_lower: str = Form(...),
    description: str = Form(...),
    letter_image: UploadFile = Form(...),
    object_image: UploadFile = Form(...),
    audio_file: UploadFile = Form(...),
    db: Session = Depends(get_db),
):
    return create_lesson_with_files(
        db=db,
        letter_upper=letter_upper,
        letter_lower=letter_lower,
        description=description,
        letter_image=letter_image,
        object_image=object_image,
        audio_file=audio_file,
    )
@router.get("/get-by-letter", response_model=LessonFirstResponse)
def get_lesson_by_letter(
    letter_upper: str = Query(..., description="Велика літера"),
    db: Session = Depends(get_db),
):
    lesson = db.query(LessonFirstDB).filter_by(letter_upper=letter_upper).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Літеру не знайдено")
    return lesson
@router.get("/{lesson_id}", response_model=LessonFirstResponse)
def get_lesson_by_id(
    lesson_id: int,
    db: Session = Depends(get_db),
):
    lesson = db.query(LessonFirstDB).get(lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Літеру не знайдено")
    return lesson
