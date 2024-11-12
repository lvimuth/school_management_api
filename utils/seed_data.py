from utils.db import init_db, get_db
from models.student import Student
from models.teacher import Teacher
from models.course import Course
from models.enrollment import Enrollment
from models.payment import Payment
from models.attendance import Attendance

def seed_data():
    init_db()

    with get_db() as db:
        # Students
        student1 = Student(name="John Doe", email="john@example.com", grade=3.8)
        student2 = Student(name="Jane Smith", email="jane@example.com", grade=4.0)
        student3 = Student(name="Bob Johnson", email="bob@example.com", grade=3.2)
        db.add_all([student1, student2, student3])
        db.commit()

        # Teachers
        teacher1 = Teacher(name="Emily Wilson", email="emily@example.com", department="Math")
        teacher2 = Teacher(name="Michael Brown", email="michael@example.com", department="Science")
        db.add_all([teacher1, teacher2])
        db.commit()

        # Courses
        course1 = Course(name="Algebra 101", description="Introduction to Algebra", credits=3, teacher_id=teacher1.id)
        course2 = Course(name="Biology 201", description="Intermediate Biology", credits=4, teacher_id=teacher2.id)
        db.add_all([course1, course2])
        db.commit()

        # Enrollments
        enrollment1 = Enrollment(student_id=student1.id, course_id=course1.id, grade=4.0)
        enrollment2 = Enrollment(student_id=student1.id, course_id=course2.id, grade=3.5)
        enrollment3 = Enrollment(student_id=student2.id, course_id=course1.id, grade=4.0)
        enrollment4 = Enrollment(student_id=student3.id, course_id=course2.id, grade=3.0)
        db.add_all([enrollment1, enrollment2, enrollment3, enrollment4])
        db.commit()

        # Payments
        payment1 = Payment(student_id=student1.id, amount=2500.0, date="2023-05-01")
        payment2 = Payment(student_id=student2.id, amount=2800.0, date="2023-06-15")
        payment3 = Payment(student_id=student3.id, amount=2400.0, date="2023-07-01")
        db.add_all([payment1, payment2, payment3])
        db.commit()

        # Attendance
        attendance1 = Attendance(student_id=student1.id, date="2023-09-01", status="Present")
        attendance2 = Attendance(student_id=student1.id, date="2023-09-02", status="Absent")
        attendance3 = Attendance(student_id=student2.id, date="2023-09-01", status="Present")
        attendance4 = Attendance(student_id=student3.id, date="2023-09-01", status="Late")
        db.add_all([attendance1, attendance2, attendance3, attendance4])
        db.commit()

if __name__ == "__main__":
    seed_data()