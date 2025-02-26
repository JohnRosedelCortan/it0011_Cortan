import json
import os

class StudentRecordManager:
    def __init__(self):
        self.records = []
        self.file_path = None

    def load_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.records = json.load(file)
                self.file_path = file_path
                print("File loaded successfully.")
        else:
            print("File does not exist.")

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                json.dump(self.records, file, indent=4)
                print("File saved successfully.")
        else:
            print("No file opened. Use 'Save As' to specify a file.")

    def save_as_file(self, file_path):
        self.file_path = file_path
        self.save_file()

    def show_all_records(self):
        if not self.records:
            print("No records available.")
        else:
            for record in self.records:
                print(record)

    def order_by_last_name(self):
        self.records.sort(key=lambda x: x[1][1])
        print("Records sorted by last name.")

    def order_by_grade(self):
        self.records.sort(key=lambda x: x[2] * 0.6 + x[3] * 0.4, reverse=True)
        print("Records sorted by grade.")

    def show_student_record(self, student_id):
        record = next((r for r in self.records if r[0] == student_id), None)
        print(record if record else "Student not found.")

    def add_record(self, student_id, first_name, last_name, class_standing, major_exam):
        self.records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")

    def edit_record(self, student_id, new_first_name=None, new_last_name=None, new_class_standing=None, new_major_exam=None):
        for i, record in enumerate(self.records):
            if record[0] == student_id:
                updated_record = (
                    student_id,
                    (new_first_name or record[1][0], new_last_name or record[1][1]),
                    new_class_standing if new_class_standing is not None else record[2],
                    new_major_exam if new_major_exam is not None else record[3],
                )
                self.records[i] = updated_record
                print("Record updated successfully.")
                return
        print("Student not found.")

    def delete_record(self, student_id):
        self.records = [r for r in self.records if r[0] != student_id]
        print("Record deleted if it existed.")


def main():
    manager = StudentRecordManager()
    
    while True:
        print("""
        1. Open File
        2. Save File
        3. Save As File
        4. Show All Students Record
        5. Order by Last Name
        6. Order by Grade
        7. Show Student Record
        8. Add Record
        9. Edit Record
        10. Delete Record
        11. Exit
        """)
        choice = input("Enter your choice: ")
        
        if choice == '1':
            path = input("Enter file path: ")
            manager.load_file(path)
        elif choice == '2':
            manager.save_file()
        elif choice == '3':
            path = input("Enter new file path: ")
            manager.save_as_file(path)
        elif choice == '4':
            manager.show_all_records()
        elif choice == '5':
            manager.order_by_last_name()
        elif choice == '6':
            manager.order_by_grade()
        elif choice == '7':
            student_id = input("Enter Student ID: ")
            manager.show_student_record(student_id)
        elif choice == '8':
            student_id = input("Enter Student ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            manager.add_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == '9':
            student_id = input("Enter Student ID to edit: ")
            first_name = input("Enter new First Name (or press Enter to keep unchanged): ") or None
            last_name = input("Enter new Last Name (or press Enter to keep unchanged): ") or None
            class_standing = input("Enter new Class Standing Grade (or press Enter to keep unchanged): ")
            major_exam = input("Enter new Major Exam Grade (or press Enter to keep unchanged): ")
            manager.edit_record(student_id, first_name, last_name,
                               float(class_standing) if class_standing else None,
                               float(major_exam) if major_exam else None)
        elif choice == '10':
            student_id = input("Enter Student ID to delete: ")
            manager.delete_record(student_id)
        elif choice == '11':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
