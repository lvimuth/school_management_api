import os

# Define the folder structure
folders = [
    "school_management_api",
    "school_management_api/routers",
    "school_management_api/models",
    "school_management_api/schemas",
    "school_management_api/utils"
]

# Define files to be created in each folder
files = {
    "school_management_api": ["main.py"],
    "school_management_api/routers": [
        "students.py", "teachers.py", "courses.py", "enrollments.py", "payments.py", "attendance.py"
    ],
    "school_management_api/models": [
        "student.py", "teacher.py", "course.py", "enrollment.py", "payment.py", "attendance.py"
    ],
    "school_management_api/schemas": [
        "student.py", "teacher.py", "course.py", "enrollment.py", "payment.py", "attendance.py"
    ],
    "school_management_api/utils": ["db.py"]
}

# Create folders and files
for folder in folders:
    os.makedirs(folder, exist_ok=True)  # Create folders if they don't exist
    for file in files.get(folder, []):
        file_path = os.path.join(folder, file)
        with open(file_path, 'w') as f:  # Create each file
            f.write("")  # Create an empty file

print("Directory structure created successfully.")
