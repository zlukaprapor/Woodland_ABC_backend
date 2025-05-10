from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.dependencies import get_current_user
from app.services.progress_service import get_user_progress, update_user_progress
from app.schemas.progress import ProgressUpdate, ProgressResponse

router = APIRouter()

@router.get("/", response_model=list[ProgressResponse])
def read_progress(db: Session = Depends(get_db), user=Depends(get_current_user)):
    """Отримання прогресу для поточного користувача"""
    return get_user_progress(db, user_id=user.id)

@router.put("/", response_model=ProgressResponse)
def update_progress(
    data: ProgressUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    """Оновлення прогресу проходження уроку"""
    return update_user_progress(db, user_id=user.id, data=data)
