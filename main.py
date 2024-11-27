import json
import os
from datetime import datetime

DATA = "data.json"


def load_data():
    if not os.path.exists(DATA):
        return {}
    with open(DATA, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA, "w") as file:
        json.dump(data, file, indent=4)


CLASS_NAME = "PGDCA"


def add_student(roll_no, name, email=""):
    """
    Adds a student to the PGDCA class.

    :param roll_no: Roll number of the student
    :param name: Name of the student
    :param email: Email of the student (optional)
    """
    data = load_data()

    if CLASS_NAME not in data:
        data[CLASS_NAME] = {"students": [], "attendance": {}}

    for student in data[CLASS_NAME]["students"]:
        if student["roll_no"] == roll_no:
            print(f"Student with roll no '{roll_no}' already exists.")
            return

    data[CLASS_NAME]["students"].append({"roll_no": roll_no, "name": name, "email": email})
    save_data(data)
    print(f"Student '{name}' added successfully to PGDCA.")


def take_attendance():
    data = load_data()
    if CLASS_NAME not in data:
        print(f"Class '{CLASS_NAME} does not exist.")
        return

    today_date = datetime.now().strftime("%d-%m-%Y")

    if today_date in data[CLASS_NAME]["attendance"]:
        print(f"Attendance for {today_date} has already been taken")
        return

    print(f"Taking Attendance for {CLASS_NAME} on {today_date}.")

    present_students =[]

    for student in data[CLASS_NAME]["students"]:
        roll_no = student["roll_no"]
        name = student["name"]
        status = input(f"Is {name} (Roll No: {roll_no}) present ? (y/n): ".strip().lower())
        if status == 'y':
            present_students.append(roll_no)

    if CLASS_NAME not in data:
        data[CLASS_NAME] = {"student": [], "attendance": {}}
    data[CLASS_NAME]["attendance"][today_date] = present_students
    save_data(data)
    print(f"Attendance recorded successfully for {today_date}.")


def view_attendance(date):
    """
    Displays attendance for a specific date in PGDCA.
    """
    data = load_data()

    if CLASS_NAME not in data:
        print(f"Class {CLASS_NAME} does not exist.")
        return

    if date not in data[CLASS_NAME]["attendance"]:
        print(f"No attendance record found for {date} in {CLASS_NAME}.")
        return

    print(f"Attendance for {CLASS_NAME} on {date}:")

    present_students = data[CLASS_NAME]["attendance"][date]

    for roll_no in present_students:
        student = next((s for s in data[CLASS_NAME]["students"] if s["roll_no"] == roll_no), None)
        if student:
            print(f"- {student['name']} (Roll No: {roll_no})")

def view_students():
    """
    Displays the list of all students in the PGDCA class, sorted alphabetically by name.
    """
    data = load_data()

    if CLASS_NAME not in data or not data[CLASS_NAME]["students"]:
        print(f"No students found in the {CLASS_NAME} class.")
        return

    # Sort students alphabetically by name
    sorted_students = sorted(data[CLASS_NAME]["students"], key=lambda s: s["name"].lower())

    print(f"\nList of students in {CLASS_NAME} (sorted alphabetically):")
    for student in sorted_students:
        print(f"- Roll No: {student['roll_no']}, Name: {student['name']} | Email: {student['email'] or 'N/A'}")


def delete_student():
    """
    Deletes a student from the PGDCA class by roll number.
    """
    data = load_data()

    if CLASS_NAME not in data or not data[CLASS_NAME]["students"]:
        print(f"No students found in the {CLASS_NAME} class.")
        return

    view_students()

    try:
        roll_no = int(input("\nEnter the roll number of the student to delete: ").strip())
    except ValueError:
        print("Invalid roll number! Please enter a valid numeric roll number.")
        return

    student_to_delete = next((s for s in data[CLASS_NAME]["students"] if int(s["roll_no"]) == roll_no), None)

    if not student_to_delete:
        print(f"No student found with Roll No: {roll_no}.")
        return

    confirm = input(f"Are you sure you want to delete {student_to_delete['name']} (Roll No: {roll_no})? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return

    data[CLASS_NAME]["students"] = [s for s in data[CLASS_NAME]["students"] if int(s["roll_no"]) != roll_no]

    save_data(data)
    print(f"Student with Roll No: {roll_no} has been deleted successfully.")

def main():
    while True:
        print("\n--- Attendance System (PGDCA) ---")
        print("1. Add Student")
        print("2. Take Attendance")
        print("3. View Attendance")
        print("4. View Students")
        print("5. Delete Student")  # New Option
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            roll_no = input("Enter roll number: ").strip()
            name = input("Enter student name: ").strip()
            email = input("Enter student email (optional): ").strip()
            add_student(roll_no, name, email)

        elif choice == '2':
            take_attendance()

        elif choice == '3':
            date = input("Enter date (DD-MM-YYYY): ").strip()
            view_attendance(date)

        elif choice == '4':
            view_students()

        elif choice == '5':  # New Option to Delete Students
            delete_student()

        elif choice == '6':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

main()