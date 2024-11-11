from fastapi import APIRouter, HTTPException
from typing import List
from models.enrollment import Enrollment
from schemas.enrollment import EnrollmentCreate, EnrollmentUpdate

router = APIRouter()

# In-memory data storage (replace with a database later)
enrollments = []

@router.get("/", response_model=List[Enrollment])
def list_enrollments():
    return enrollments

@router.get("/{enrollment_id}", response_model=Enrollment)
def get_enrollment(enrollment_id: int):
    enrollment = next((e for e in enrollments if e.id == enrollment_id), None)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@router.post("/", response_model=Enrollment)
def create_enrollment(enrollment: EnrollmentCreate):
    new_enrollment = Enrollment(id=len(enrollments) + 1, **enrollment.dict())
    enrollments.append(new_enrollment)
    return new_enrollment

@router.put("/{enrollment_id}", response_model=Enrollment)
def update_enrollment(enrollment_id: int, enrollment: EnrollmentUpdate):
    for i, e in enumerate(enrollments):
        if e.id == enrollment_id:
            enrollments[i] = Enrollment(id=enrollment_id, **enrollment.dict())
            return enrollments[i]
    raise HTTPException(status_code=404, detail="Enrollment not found")

@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int):
    for i, e in enumerate(enrollments):
        if e.id == enrollment_id:
            del enrollments[i]
            return
    raise HTTPException(status_code=404, detail="Enrollment not found")