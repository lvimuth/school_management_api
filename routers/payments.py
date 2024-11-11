from fastapi import APIRouter, HTTPException
from typing import List
from models.payment import Payment
from schemas.payment import PaymentCreate, PaymentUpdate

router = APIRouter()

# In-memory data storage (replace with a database later)
payments = []

@router.get("/", response_model=List[Payment])
def list_payments():
    return payments

@router.get("/{payment_id}", response_model=Payment)
def get_payment(payment_id: int):
    payment = next((p for p in payments if p.id == payment_id), None)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.post("/", response_model=Payment)
def create_payment(payment: PaymentCreate):
    new_payment = Payment(id=len(payments) + 1, **payment.dict())
    payments.append(new_payment)
    return new_payment

@router.put("/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payment: PaymentUpdate):
    for i, p in enumerate(payments):
        if p.id == payment_id:
            payments[i] = Payment(id=payment_id, **payment.dict())
            return payments[i]
    raise HTTPException(status_code=404, detail="Payment not found")

@router.delete("/{payment_id}")
def delete_payment(payment_id: int):
    for i, p in enumerate(payments):
        if p.id == payment_id:
            del payments[i]
            return
    raise HTTPException(status_code=404, detail="Payment not found")
