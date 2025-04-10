from pydantic import BaseModel
from typing import List, Optional

class LessonFirstResponse(BaseModel):
    id: int
    letter_upper: str
    letter_lower: str
    description: str
    letter_image: str
    object_image: str
    audio_file: str

    model_config = {
        "from_attributes": True
    }

class LessonFirstListResponse(BaseModel):
    items: List[LessonFirstResponse]
    total: int
    skip: int
    limit: int