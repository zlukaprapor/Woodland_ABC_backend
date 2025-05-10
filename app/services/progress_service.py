from sqlalchemy.orm import Session
from app.models.progress import ProgressDB
from app.schemas.progress import ProgressCreate, ProgressUpdate

def get_user_progress(db: Session, user_id: int):
    return db.query(ProgressDB).filter(ProgressDB.user_id == user_id).all()

def update_user_progress(db: Session, user_id: int, data: ProgressUpdate):
    progress = db.query(ProgressDB).filter(
        ProgressDB.user_id == user_id,
        ProgressDB.lesson_id == data.lesson_id
    ).first()

    if progress:
        progress.completed = data.completed
    else:
        progress = ProgressDB(user_id=user_id, lesson_id=data.lesson_id, completed=data.completed)
        db.add(progress)

    db.commit()
    db.refresh(progress)
    return progress
