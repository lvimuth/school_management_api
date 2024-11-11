from pydantic import BaseModel

class PaymentCreate(BaseModel):
    student_id: int
    amount: float
    date: str

class PaymentUpdate(BaseModel):
    student_id: int = None
    amount: float = None
    date: str = None