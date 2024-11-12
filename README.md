# FastAPI School Management API

This project is a simple **School Management API** built using **FastAPI**. It includes various endpoints to manage students, teachers, courses, enrollments, payments, and attendance, structured as RESTful services for easy integration.

## Project Structure

The code is organized as follows:

- **main.py**: This file initializes the FastAPI application and registers routers for different functionalities.
- **routers**: Each router file (students, teachers, courses, enrollments, payments, attendance) defines endpoints for the respective entity's CRUD operations.
- **models**: Defines the data models for entities like `Student`, `Teacher`, etc., using Pydantic.
- **schemas**: Contains schema classes for creating and updating data, ensuring data validation on incoming requests.

## Functionality Overview

### main.py

- Initializes the FastAPI app.
- Registers routers with prefixes and tags for organized and modular endpoints.
- Runs the app with Uvicorn server when executed as the main module.

### Routers

Each router (e.g., `students.py`, `teachers.py`) defines:

1. **GET Requests**: To retrieve a list of records or a specific record by ID.
2. **POST Requests**: To create a new record.
3. **PUT Requests**: To update an existing record by ID.
4. **DELETE Requests**: To delete a record by ID.

### Data Storage

Currently, each router uses in-memory lists to store data. This can be replaced with a database for production use.

### Models and Schemas

- **Models**: Define the structure of each entity (Student, Teacher, Course, etc.) for consistent data representation.
- **Schemas**: Provide data validation and ensure that incoming data conforms to the expected format.

## API Endpoints

### Students

- **GET /students**: List all students.
- **GET /students/{student_id}**: Retrieve a student by ID.
- **POST /students**: Create a new student.
- **PUT /students/{student_id}**: Update an existing student.
- **DELETE /students/{student_id}**: Delete a student by ID.

### Teachers

- **GET /teachers**: List all teachers.
- **GET /teachers/{teacher_id}**: Retrieve a teacher by ID.
- **POST /teachers**: Create a new teacher.
- **PUT /teachers/{teacher_id}**: Update an existing teacher.
- **DELETE /teachers/{teacher_id}**: Delete a teacher by ID.

### Courses

- **GET /courses**: List all courses.
- **GET /courses/{course_id}**: Retrieve a course by ID.
- **POST /courses**: Create a new course.
- **PUT /courses/{course_id}**: Update an existing course.
- **DELETE /courses/{course_id}**: Delete a course by ID.

### Enrollments

- **GET /enrollments**: List all enrollments.
- **GET /enrollments/{enrollment_id}**: Retrieve an enrollment by ID.
- **POST /enrollments**: Create a new enrollment.
- **PUT /enrollments/{enrollment_id}**: Update an existing enrollment.
- **DELETE /enrollments/{enrollment_id}**: Delete an enrollment by ID.

### Payments

- **GET /payments**: List all payments.
- **GET /payments/{payment_id}**: Retrieve a payment by ID.
- **POST /payments**: Create a new payment.
- **PUT /payments/{payment_id}**: Update an existing payment.
- **DELETE /payments/{payment_id}**: Delete a payment by ID.

### Attendance

- **GET /attendance**: List all attendance records.
- **GET /attendance/{attendance_id}**: Retrieve an attendance record by ID.
- **POST /attendance**: Create a new attendance record.
- **PUT /attendance/{attendance_id}**: Update an existing attendance record.
- **DELETE /attendance/{attendance_id}**: Delete an attendance record by ID.

## Running the Application

Run the app with Uvicorn:

```bash
uvicorn main:app --reload
```

Access the interactive API documentation at `http://127.0.0.1:8000/docs` for easy testing and exploration.

## Future Improvements

- Integrate a database for persistent data storage.
- Implement authentication and authorization for secure access.
- Add more validation and error handling.

## Conclusion

This API provides a modular, RESTful structure for managing school data. It demonstrates the flexibility and power of FastAPI for building scalable and performant APIs. Replace in-memory storage with a database for production use, and explore FastAPI's extensive documentation to add more features.
