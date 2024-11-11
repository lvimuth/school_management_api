# routers/students.py
from fastapi import APIRouter, HTTPException
from typing import List
from models.student import Student
from schemas.student import StudentCreate, StudentUpdate

router = APIRouter()

# In-memory data storage (replace with a database later)
students = []

@router.get("/", response_model=List[Student])
def list_students():
    return students

@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = next((s for s in students if s.id == student_id), None)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/", response_model=Student)
def create_student(student: StudentCreate):
    new_student = Student(id=len(students) + 1, **student.dict())
    students.append(new_student)
    return new_student

@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentUpdate):
    for i, s in enumerate(students):
        if s.id == student_id:
            students[i] = Student(id=student_id, **student.dict())
            return students[i]
    raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{student_id}")
def delete_student(student_id: int):
    for i, s in enumerate(students):
        if s.id == student_id:
            del students[i]
            return
    raise HTTPException(status_code=404, detail="Student not found")
