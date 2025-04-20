from pydantic import BaseModel, Field
from typing import List

class LessonFirstBase(BaseModel):
    letter_upper: str = Field(..., min_length=1, max_length=1)
    letter_lower: str = Field(..., min_length=1, max_length=1)
    description: str

class LessonFirstCreate(LessonFirstBase):
    pass

class LessonFirstUpdate(BaseModel):
    letter_upper: str = Field(None, min_length=1, max_length=1)
    letter_lower: str = Field(None, min_length=1, max_length=1)
    description: str = None

class LessonFirstResponse(LessonFirstBase):
    id: int
    letter_image: str
    object_image: str
    audio_file: str

    class Config:
        from_attributes = True

class LessonFirstListResponse(BaseModel):
    items: List[LessonFirstResponse]
    total: int
    skip: int
    limit: int