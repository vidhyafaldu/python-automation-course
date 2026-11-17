import csv

input_file = "data/student.csv"
output_file = "reports/student_results.csv"

# Read student records and generate result report
with open(input_file, "r", newline="") as file:
    reader = csv.DictReader(file)

    with open(output_file, "w", newline="") as report:
        fieldnames = ["Name", "Age", "Course", "Marks", "Result"]

        writer = csv.DictWriter(report, fieldnames=fieldnames)

        # Write column headings
        writer.writeheader()

        for student in reader:
            marks = int(student["Marks"])

            if marks >= 35:
                result = "Pass"
            else:
                result = "Fail"

            writer.writerow({
                "Name": student["Name"],
                "Age": student["Age"],
                "Course": student["Course"],
                "Marks": marks,
                "Result": result
            })

print("Student result report generated successfully!")

file_path = "data/student.csv"

total_marks = 0
student_count = 0

# Read student records
with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for student in reader:
        marks = int(student["Marks"])

        total_marks += marks
        student_count += 1

# Calculate average
if student_count > 0:
    average = total_marks / student_count

    print("Total Students:", student_count)
    print("Total Marks:", total_marks)
    print("Average Marks:", round(average, 2))
else:
    print("No student records found!")

file_path = "data/student.csv"

# Get student name from user
search_name = input("Enter student name to search: ").strip()

found = False

# Search student in CSV
with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for student in reader:
        if student["Name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])

            found = True
            break

if not found:
    print("Student not found!")
file_path = "data/student.csv"

# Add a new student
with open(file_path, "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Neha", 22, "MCA", 88])

print("New student record added successfully!")

file_path = "data/student.csv"

# Read CSV using DictReader
with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Course:", student["Course"])
        print("Marks:", student["Marks"])
        print("----------------------")
 
file_path = "data/student.csv"

# Read student records
with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
# Create student CSV file

file_path = "data/student.csv"

with open(file_path, "w", newline="") as file:

    writer = csv.writer(file)

    # Add header
    writer.writerow(["Name", "Age", "Course", "Marks"])

    # Add student records
    writer.writerow(["Vidya", 22, "BCA", 85])
    writer.writerow(["Rahul", 21, "MCA", 90])
    writer.writerow(["Priya", 22, "BCA", 78])
    writer.writerow(["Amit", 23, "MCA", 92])

print("Student CSV file created successfully!")
