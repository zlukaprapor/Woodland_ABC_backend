# app/models/progress.py
from sqlalchemy import Column, Integer, ForeignKey, Boolean, UniqueConstraint
from app.db.database import Base

class ProgressDB(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lesson.id"), nullable=False)
    completed = Column(Boolean, default=False, nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "lesson_id", name="unique_user_lesson"),
    )
