import os

# Function to calculate the final grade based on the class standing and major exam grade
def calculate_grade(class_standing, major_exam_grade):
    return (0.6 * class_standing) + (0.4 * major_exam_grade)

# Function to display the menu
def show_menu():
    print("\n--- Student Record Management ---")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Add Record")
    print("9. Edit Record")
    print("10. Delete Record")
    print("11. Exit")

# Function to open a file and load the records
def open_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            records = []
            for line in file.readlines():
                student_id, first_name, last_name, class_standing, major_exam_grade = line.strip().split(',')
                records.append((student_id, (first_name, last_name), float(class_standing), float(major_exam_grade)))
            return records
    else:
        print("File not found!")
        return []

# Function to save the student records to a file
def save_file(filename, records):
    with open(filename, 'w') as file:
        for record in records:
            student_id = record[0]
            first_name, last_name = record[1]
            class_standing = record[2]
            major_exam_grade = record[3]
            file.write(f"{student_id},{first_name},{last_name},{class_standing},{major_exam_grade}\n")
    print(f"Records saved to {filename}")

# Function to display all student records
def show_all_records(records):
    if not records:
        print("No records to display.")
        return
    for record in records:
        student_id, name, class_standing, major_exam_grade = record
        full_name = " ".join(name)
        grade = calculate_grade(class_standing, major_exam_grade)
        print(f"ID: {student_id}, Name: {full_name}, Class Standing: {class_standing}, Major Exam Grade: {major_exam_grade}, Final Grade: {grade}")

# Function to order students by last name
def order_by_last_name(records):
    records.sort(key=lambda x: x[1][1])  # Sorting by last name
    show_all_records(records)

# Function to order students by grade
def order_by_grade(records):
    records.sort(key=lambda x: calculate_grade(x[2], x[3]), reverse=True)  # Sorting by grade
    show_all_records(records)

# Function to find and display a student record by ID
def show_student_record(records, student_id):
    for record in records:
        if record[0] == student_id:
            student_id, name, class_standing, major_exam_grade = record
            full_name = " ".join(name)
            grade = calculate_grade(class_standing, major_exam_grade)
            print(f"ID: {student_id}, Name: {full_name}, Class Standing: {class_standing}, Major Exam Grade: {major_exam_grade}, Final Grade: {grade}")
            return
    print("Record not found.")

# Function to add a new student record
def add_record(records):
    student_id = input("Enter Student ID (6 digits): ")
    if len(student_id) != 6 or not student_id.isdigit():
        print("Invalid ID. It must be a 6 digit number.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam_grade = float(input("Enter Major Exam Grade: "))
    records.append((student_id, (first_name, last_name), class_standing, major_exam_grade))
    print("Record added successfully.")

# Function to edit an existing student record
def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            first_name, last_name = record[1]
            class_standing = record[2]
            major_exam_grade = record[3]
            print(f"Current Data - Name: {first_name} {last_name}, Class Standing: {class_standing}, Major Exam Grade: {major_exam_grade}")
            
            first_name = input("Enter New First Name (Leave blank to keep current): ") or first_name
            last_name = input("Enter New Last Name (Leave blank to keep current): ") or last_name
            class_standing = float(input(f"Enter New Class Standing Grade (Leave blank to keep {class_standing}): ") or class_standing)
            major_exam_grade = float(input(f"Enter New Major Exam Grade (Leave blank to keep {major_exam_grade}): ") or major_exam_grade)
            
            records[i] = (student_id, (first_name, last_name), class_standing, major_exam_grade)
            print("Record updated successfully.")
            return
    print("Record not found.")

# Function to delete a student record
def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted successfully.")
            return
    print("Record not found.")

def main():
    records = []
    filename = ""

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename to open: ")
            records = open_file(filename)

        elif choice == "2":
            if filename:
                save_file(filename, records)
            else:
                print("No file to save.")

        elif choice == "3":
            filename = input("Enter the new filename to save as: ")
            save_file(filename, records)

        elif choice == "4":
            show_all_records(records)

        elif choice == "5":
            order_by_last_name(records)

        elif choice == "6":
            order_by_grade(records)

        elif choice == "7":
            student_id = input("Enter Student ID to view: ")
            show_student_record(records, student_id)

        elif choice == "8":
            add_record(records)

        elif choice == "9":
            edit_record(records)

        elif choice == "10":
            delete_record(records)

        elif choice == "11":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()