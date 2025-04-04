from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserLogin(BaseModel):
        email: str
        password: str

class Config:
        from_attributes = True

