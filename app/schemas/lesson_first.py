from pydantic import BaseModel

class LessonFirstResponse(BaseModel):
    id: int
    letter_upper: str
    letter_lower: str
    description: str
    letter_image: str
    object_image: str
    audio_file: str

    class Config:
        from_attributes = True
