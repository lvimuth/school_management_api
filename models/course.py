from pydantic import BaseModel

class Course(BaseModel):
    id: int
    name: str
    description: str
    credits: int