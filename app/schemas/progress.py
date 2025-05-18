from pydantic import BaseModel, Field

class ProgressBase(BaseModel):
    """
    Базова схема для прогресу користувача по уроку.
    """
    lesson_id: int = Field(..., description="Ідентифікатор уроку")
    completed: bool = Field(..., description="Статус завершення уроку")

class ProgressCreate(ProgressBase):
    """
    Схема для створення нового запису прогресу.
    Наслідує всі поля базової схеми.
    """
    pass

class ProgressUpdate(ProgressBase):
    """
    Схема для оновлення існуючого прогресу.
    Наслідує всі поля базової схеми.
    """
    pass

class ProgressResponse(ProgressBase):
    """
    Схема відповіді з прогресом, включає ID користувача.
    """
    user_id: int = Field(..., description="Ідентифікатор користувача")

    class Config:
        from_attributes = True  # Підтримка ORM моделей для автоконвертації
