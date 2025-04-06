from sqlalchemy.orm import Session
from app.models.lesson_first import LessonFirstDB
from app.schemas.lesson_first import LessonFirst

def create_lesson(db: Session, lesson_data: LessonFirst):
    lesson = LessonFirstDB(
        letter_upper=lesson_data.letter_upper,
        letter_lower=lesson_data.letter_lower,
        description=lesson_data.description,
        image_url=lesson_data.image_url
    )
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson

def get_lesson_by_letter(db: Session, letter: str):
    return db.query(LessonFirstDB).filter(LessonFirstDB.letter_upper == letter.upper()).first()
