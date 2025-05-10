from pydantic import BaseModel

class ProgressBase(BaseModel):
    lesson_id: int
    completed: bool

class ProgressCreate(ProgressBase):
    pass

class ProgressUpdate(ProgressBase):
    pass

class ProgressResponse(ProgressBase):
    user_id: int

    class Config:
        from_attributes = True
