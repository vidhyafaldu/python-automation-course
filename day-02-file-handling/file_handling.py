
import shutil
import os

source = "practice_files/student.txt"
destination = "practice_files/student_backup.txt"

# Copy file
shutil.copy(source, destination)

print("File copied successfully!")

# Rename copied file
os.rename(destination, "practice_files/student_details.txt")

print("File renamed successfully!")


import os

file_path = "practice_files/student.txt"

if os.path.exists(file_path):
    print("File exists!")
else:
    print("File does not exist!")

# Append new information

with open("practice_files/student.txt", "a") as file:
    file.write("Skill: Python\n")
    file.write("Status: Learning\n")

print("New information added!")

# Read the student file

with open("practice_files/student.txt", "r") as file:
    content = file.read()

print("Student Details:")
print(content)

# Day 02 - Practical 1
# Create and write a text file

file_path = "practice_files/student.txt"

with open(file_path, "w") as file:
    file.write("Name: Vidya\n")
    file.write("Course: Python Automation\n")
    file.write("Day: 02\n")

print("File created successfully!")

try:
    with open("practice_files/studentunknow.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")
