from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.lesson_first import LessonFirst
from app.services.lesson_service import create_lesson, get_lesson_by_letter

router = APIRouter()

@router.post("/create")
def create_lesson_intro(lesson: LessonFirst, db: Session = Depends(get_db)):
    return create_lesson(db, lesson)

@router.get("/first/{letter}")
def read_lesson(letter: str, db: Session = Depends(get_db)):
    lesson = get_lesson_by_letter(db, letter)
    if not lesson:
        raise HTTPException(status_code=404, detail="Letter not found")
    return lesson
