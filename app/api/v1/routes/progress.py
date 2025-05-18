from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.dependencies import get_current_user
from app.services.progress_service import get_user_progress, update_user_progress
from app.schemas.progress import ProgressUpdate, ProgressResponse

router = APIRouter()

@router.get(
    "/",
    response_model=list[ProgressResponse],
    summary="Отримати прогрес користувача",
    description="Повертає список прогресу для поточного аутентифікованого користувача."
)
def read_progress(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    """Отримання прогресу для поточного користувача"""
    try:
        return get_user_progress(db, user_id=user.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при отриманні прогресу: {str(e)}"
        )

@router.put(
    "/",
    response_model=ProgressResponse,
    summary="Оновити прогрес користувача",
    description="Оновлює інформацію про прогрес проходження уроку для поточного користувача."
)
def update_progress(
    data: ProgressUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    """Оновлення прогресу проходження уроку"""
    try:
        return update_user_progress(db, user_id=user.id, data=data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Помилка при оновленні прогресу: {str(e)}"
        )
