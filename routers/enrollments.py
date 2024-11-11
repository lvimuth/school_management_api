from fastapi import APIRouter, HTTPException
from typing import List
from models.course import Course
from schemas.course import CourseCreate, CourseUpdate

router = APIRouter()

# In-memory data storage (replace with a database later)
courses = []

@router.get("/", response_model=List[Course])
def list_courses():
    return courses

@router.get("/{course_id}", response_model=Course)
def get_course(course_id: int):
    course = next((c for c in courses if c.id == course_id), None)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.post("/", response_model=Course)
def create_course(course: CourseCreate):
    new_course = Course(id=len(courses) + 1, **course.dict())
    courses.append(new_course)
    return new_course

@router.put("/{course_id}", response_model=Course)
def update_course(course_id: int, course: CourseUpdate):
    for i, c in enumerate(courses):
        if c.id == course_id:
            courses[i] = Course(id=course_id, **course.dict())
            return courses[i]
    raise HTTPException(status_code=404, detail="Course not found")

@router.delete("/{course_id}")
def delete_course(course_id: int):
    for i, c in enumerate(courses):
        if c.id == course_id:
            del courses[i]
            return
    raise HTTPException(status_code=404, detail="Course not found")
