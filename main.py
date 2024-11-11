from fastapi import FastAPI
from routers import students, teachers, courses, enrollments, payments, attendance

app = FastAPI()

app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(teachers.router, prefix="/teachers", tags=["teachers"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["enrollments"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(attendance.router, prefix="/attendance", tags=["attendance"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)