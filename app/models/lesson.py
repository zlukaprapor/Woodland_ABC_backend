from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from app.db.database import Base


class LessonFirstDB(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, index=True)
    letter_upper = Column(String(1), unique=True, nullable=False, index=True)
    letter_lower = Column(String(1), nullable=False)
    description = Column(Text, nullable=False)
    training = Column(Text, nullable=False)
    regulations = Column(Text, nullable=False)
    letter_image = Column(String, nullable=False)
    object_image_first = Column(String, nullable=False)
    object_image_second = Column(String, nullable=False)
    object_image_third = Column(String, nullable=False)
    audio_file = Column(String, nullable=False)

    # Додаємо обмеження, що літера має бути унікальною
    __table_args__ = (
        UniqueConstraint('letter_upper', name='unique_letter_upper'),
    )