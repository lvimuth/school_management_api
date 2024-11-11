from pydantic import BaseModel

class AttendanceCreate(BaseModel):
    student_id: int
    date: str
    status: str

class AttendanceUpdate(BaseModel):
    student_id: int = None
    date: str = None
    status: str = None