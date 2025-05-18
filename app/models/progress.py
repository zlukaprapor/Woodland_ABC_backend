# app/models/progress.py
from sqlalchemy import Column, Integer, ForeignKey, Boolean, UniqueConstraint
from app.db.database import Base

class ProgressDB(Base):
    """
    Модель таблиці 'progress' для збереження прогресу користувача у проходженні уроків.

    Атрибути:
        id (int): Унікальний ідентифікатор запису прогресу (PK).
        user_id (int): Ідентифікатор користувача (FK до таблиці users).
        lesson_id (int): Ідентифікатор уроку (FK до таблиці lesson).
        completed (bool): Статус завершення уроку користувачем (True, якщо завершено).

    Обмеження:
        Унікальність комбінації (user_id, lesson_id) забезпечує, що для кожного користувача
        і уроку існує лише один запис прогресу.
    """

    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lesson.id"), nullable=False)
    completed = Column(Boolean, default=False, nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "lesson_id", name="unique_user_lesson"),
    )
