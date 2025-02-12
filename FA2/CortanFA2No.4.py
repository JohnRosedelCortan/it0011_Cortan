print("Reading Student Information:\n")
try:
    with open("students.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: 'students.txt' file not found. Please save student data first.")