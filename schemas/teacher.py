from pydantic import BaseModel

class TeacherCreate(BaseModel):
    name: str
    email: str
    department: str

class TeacherUpdate(BaseModel):
    name: str = None
    email: str = None
    department: str = None