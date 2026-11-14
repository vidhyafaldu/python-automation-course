
# Student Record Automation

file_path = "practice_files/students.txt"

name = input("Enter student name: ")
course = input("Enter course name: ")

with open(file_path, "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Course: {course}\n")
    file.write("-------------------\n")

print("\nStudent record saved!")

with open(file_path, "r") as file:
    print("\nAll Student Records:")
    print(file.read())
