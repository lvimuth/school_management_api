from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str
    grade: float

class StudentUpdate(BaseModel):
    name: str = None
    email: str = None
    grade: float = None