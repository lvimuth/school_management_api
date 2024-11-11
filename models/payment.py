from pydantic import BaseModel

class Payment(BaseModel):
    id: int
    student_id: int
    amount: float
    date: str