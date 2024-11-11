from fastapi import APIRouter, HTTPException
from typing import List
from models.teacher import Teacher
from schemas.teacher import TeacherCreate, TeacherUpdate

router = APIRouter()

# In-memory data storage (replace with a database later)
teachers = []

@router.get("/", response_model=List[Teacher])
def list_teachers():
    return teachers

@router.get("/{teacher_id}", response_model=Teacher)
def get_teacher(teacher_id: int):
    teacher = next((t for t in teachers if t.id == teacher_id), None)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.post("/", response_model=Teacher)
def create_teacher(teacher: TeacherCreate):
    new_teacher = Teacher(id=len(teachers) + 1, **teacher.dict())
    teachers.append(new_teacher)
    return new_teacher

@router.put("/{teacher_id}", response_model=Teacher)
def update_teacher(teacher_id: int, teacher: TeacherUpdate):
    for i, t in enumerate(teachers):
        if t.id == teacher_id:
            teachers[i] = Teacher(id=teacher_id, **teacher.dict())
            return teachers[i]
    raise HTTPException(status_code=404, detail="Teacher not found")

@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int):
    for i, t in enumerate(teachers):
        if t.id == teacher_id:
            del teachers[i]
            return
    raise HTTPException(status_code=404, detail="Teacher not found")
