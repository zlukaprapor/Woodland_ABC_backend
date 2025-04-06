from pydantic import BaseModel

class LessonFirst(BaseModel):
    letter_upper: str
    letter_lower: str
    description: str
    image_url: str

    class Config:
        from_attributes = True
