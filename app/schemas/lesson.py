from pydantic import BaseModel, Field
from typing import List, Optional

class LessonFirstBase(BaseModel):
    """
    Базова схема для уроку з основними текстовими полями.
    """
    letter_upper: str = Field(..., min_length=1, max_length=1, description="Велика літера (один символ)")
    letter_lower: str = Field(..., min_length=1, max_length=1, description="Мала літера (один символ)")
    description: str = Field(..., description="Опис уроку")
    training: str = Field(..., description="Текст тренування")
    regulations: str = Field(..., description="Регламенти уроку")

class LessonFirstCreate(LessonFirstBase):
    """
    Схема для створення нового уроку.
    Наслідує всі поля базової схеми.
    """
    pass

class LessonFirstUpdate(BaseModel):
    """
    Схема для оновлення уроку.
    Всі поля необов’язкові, можна оновлювати частково.
    """
    letter_upper: Optional[str] = Field(None, min_length=1, max_length=1, description="Велика літера (один символ)")
    letter_lower: Optional[str] = Field(None, min_length=1, max_length=1, description="Мала літера (один символ)")
    description: Optional[str] = Field(None, description="Опис уроку")
    training: Optional[str] = Field(None, description="Текст тренування")
    regulations: Optional[str] = Field(None, description="Регламенти уроку")

class LessonFirstResponse(LessonFirstBase):
    """
    Схема відповіді для уроку з додатковими полями файлів і ID.
    """
    id: int = Field(..., description="Унікальний ідентифікатор уроку")
    letter_image: Optional[str] = Field(None, description="Шлях або URL до зображення великої літери")
    object_image_first: Optional[str] = Field(None, description="Шлях або URL до першого об’єктного зображення")
    object_image_second: Optional[str] = Field(None, description="Шлях або URL до другого об’єктного зображення")
    object_image_third: Optional[str] = Field(None, description="Шлях або URL до третього об’єктного зображення")
    audio_file: Optional[str] = Field(None, description="Шлях або URL до аудіофайлу")
    quiz_file: Optional[str] = Field(None, description="Шлях або URL до файлу з вікториною")

    class Config:
        from_attributes = True  # Дозволяє створювати схему із ORM моделей

class LessonFirstListResponse(BaseModel):
    """
    Схема для відповіді зі списком уроків з пагінацією.
    """
    items: List[LessonFirstResponse] = Field(..., description="Список уроків")
    total: int = Field(..., description="Загальна кількість уроків")
    skip: int = Field(..., description="Кількість пропущених записів (offset)")
    limit: int = Field(..., description="Ліміт записів на сторінку")
