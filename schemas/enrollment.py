from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    grade: float

class EnrollmentUpdate(BaseModel):
    student_id: int = None
    course_id: int = None
    grade: float = None