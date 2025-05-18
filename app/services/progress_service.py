from sqlalchemy.orm import Session
from app.models.progress import ProgressDB
from app.schemas.progress import ProgressCreate, ProgressUpdate

def get_user_progress(db: Session, user_id: int):
    """
    Отримує весь прогрес користувача.

    Args:
        db (Session): Сесія бази даних SQLAlchemy.
        user_id (int): Ідентифікатор користувача.

    Returns:
        List[ProgressDB]: Список записів прогресу користувача.
    """
    return db.query(ProgressDB).filter(ProgressDB.user_id == user_id).all()

def update_user_progress(db: Session, user_id: int, data: ProgressUpdate):
    """
    Оновлює або створює запис прогресу користувача для певного уроку.

    Args:
        db (Session): Сесія бази даних SQLAlchemy.
        user_id (int): Ідентифікатор користувача.
        data (ProgressUpdate): Дані для оновлення або створення прогресу,
                               містять lesson_id та completed (стан завершення уроку).

    Returns:
        ProgressDB: Оновлений або створений запис прогресу.
    """
    progress = db.query(ProgressDB).filter(
        ProgressDB.user_id == user_id,
        ProgressDB.lesson_id == data.lesson_id
    ).first()

    if progress:
        # Оновлення існуючого запису прогресу
        progress.completed = data.completed
    else:
        # Створення нового запису прогресу
        progress = ProgressDB(user_id=user_id, lesson_id=data.lesson_id, completed=data.completed)
        db.add(progress)

    db.commit()
    db.refresh(progress)
    return progress
