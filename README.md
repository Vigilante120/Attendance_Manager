# Attendance_Manager
"Smart Attendance Manager for Class"

Features of the Project:
Add Students:
Allows you to add new students to the PGDCA class.
Each student is identified by a unique roll number, name, and optional email address.
Prevents duplicate entries by checking for existing roll numbers.
Take Attendance:
Records attendance for the PGDCA class on a specific date.
Marks students as present or absent based on user input.
Ensures attendance is not overwritten if already taken for the day.
View Attendance:
Displays attendance records for a specific date.
Shows the names and roll numbers of students who were present on that date.
Notifies if no attendance record exists for the selected date.
View Students:
Lists all students in the PGDCA class.
Displays their roll numbers, names, and email addresses (if provided).
Automatically sorts students alphabetically by their names for better readability.
Delete Students:
Allows you to delete a student from the PGDCA class using their roll number.
Displays the full list of students before deletion for easy selection.
Asks for confirmation before permanently removing a student.
Persistent Data Storage:
All data (students and attendance records) is stored in a JSON file (data.json).
Ensures data is saved persistently and can be accessed even after restarting the program.
User-Friendly Interface:
Simple command-line interface (CLI) with numbered menu options.
Provides clear instructions and feedback for each operation.
Error Handling:
Handles invalid inputs gracefully (e.g., non-numeric roll numbers).
Prevents accidental overwrites or deletions with confirmation prompts.
Scalable Design:
Designed to manage a single class (PGDCA) but can be extended to support multiple classes in the future.
