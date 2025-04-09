from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class LessonFirstDB(Base):
    __tablename__ = "lesson_first"

    id = Column(Integer, primary_key=True, index=True)
    letter_upper = Column(String, unique=True, nullable=False)
    letter_lower = Column(String, nullable=False)
    description = Column(Text)
    letter_image = Column(String)
    object_image = Column(String)
    audio_file = Column(String)
