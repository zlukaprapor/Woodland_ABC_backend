from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from app.db.database import Base

class LessonFirstDB(Base):
    """
    Модель таблиці 'lesson' для збереження інформації про урок.

    Атрибути:
        id (int): Унікальний ідентифікатор уроку (PK).
        letter_upper (str): Велика літера, пов'язана з уроком, унікальна.
        letter_lower (str): Мала літера, відповідна до великої.
        description (str): Опис уроку.
        training (str): Текст тренувального матеріалу уроку.
        regulations (str): Правила чи інструкції для уроку.
        letter_image (str): Шлях до зображення великої літери.
        object_image_first (str): Шлях до першого зображення об'єкту.
        object_image_second (str): Шлях до другого зображення об'єкту.
        object_image_third (str): Шлях до третього зображення об'єкту.
        audio_file (str): Шлях до аудіофайлу уроку.
        quiz_file (str): Шлях до файлу з вікториною/тестом.

    Обмеження:
        Унікальність 'letter_upper' забезпечує, що одна велика літера відповідає лише одному уроку.
    """

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
    quiz_file = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint('letter_upper', name='unique_letter_upper'),
    )
