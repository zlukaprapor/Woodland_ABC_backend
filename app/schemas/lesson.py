from pydantic import BaseModel, Field
from typing import List, Optional

class LessonFirstBase(BaseModel):
    letter_upper: str = Field(..., min_length=1, max_length=1)
    letter_lower: str = Field(..., min_length=1, max_length=1)
    description: str
    training: str
    regulations: str

class LessonFirstCreate(LessonFirstBase):
    pass

class LessonFirstUpdate(BaseModel):
    letter_upper: Optional[str] = Field(None, min_length=1, max_length=1)
    letter_lower: Optional[str] = Field(None, min_length=1, max_length=1)
    description: Optional[str] = None
    training: Optional[str] = None
    regulations: Optional[str] = None

class LessonFirstResponse(LessonFirstBase):
    id: int
    letter_image: Optional[str] = None
    object_image_first: Optional[str] = None
    object_image_second: Optional[str] = None
    object_image_third: Optional[str] = None
    audio_file: Optional[str] = None
    quiz_file: Optional[str] = None

    class Config:
        from_attributes = True

class LessonFirstListResponse(BaseModel):
    items: List[LessonFirstResponse]
    total: int
    skip: int
    limit: int
