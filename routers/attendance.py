from fastapi import APIRouter, HTTPException
from typing import List
from models.attendance import Attendance
from schemas.attendance import AttendanceCreate, AttendanceUpdate

router = APIRouter()

# In-memory data storage (replace with a database later)
attendance_records = []

@router.get("/", response_model=List[Attendance])
def list_attendance():
    return attendance_records

@router.get("/{attendance_id}", response_model=Attendance)
def get_attendance(attendance_id: int):
    attendance_record = next((a for a in attendance_records if a.id == attendance_id), None)
    if not attendance_record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance_record

@router.post("/", response_model=Attendance)
def create_attendance(attendance: AttendanceCreate):
    new_attendance = Attendance(id=len(attendance_records) + 1, **attendance.dict())
    attendance_records.append(new_attendance)
    return new_attendance

@router.put("/{attendance_id}", response_model=Attendance)
def update_attendance(attendance_id: int, attendance: AttendanceUpdate):
    for i, a in enumerate(attendance_records):
        if a.id == attendance_id:
            attendance_records[i] = Attendance(id=attendance_id, **attendance.dict())
            return attendance_records[i]
    raise HTTPException(status_code=404, detail="Attendance record not found")

@router.delete("/{attendance_id}")
def delete_attendance(attendance_id: int):
    for i, a in enumerate(attendance_records):
        if a.id == attendance_id:
            del attendance_records[i]
            return
    raise HTTPException(status_code=404, detail="Attendance record not found")
