from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class LessonFirstDB(Base):
    __tablename__ = "lesson_first"

    id = Column(Integer, primary_key=True, index=True)
    letter_upper = Column(String, unique=True, nullable=False)  # Наприклад, "А"
    letter_lower = Column(String, nullable=False)            # Наприклад, "а"
    description = Column(Text)                            # Текст опису або вимови
    image_url = Column(String)                            # URL до зображення або анімації
