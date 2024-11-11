from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    description: str
    credits: int

class CourseUpdate(BaseModel):
    name: str = None
    description: str = None
    credits: int = None