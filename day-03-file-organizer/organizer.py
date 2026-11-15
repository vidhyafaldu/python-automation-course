 
from pathlib import Path

folder = Path("sample_files")

for file in folder.iterdir():

    if file.is_file():
        print(file.name, "->", file.suffix)



from pathlib import Path

folder = Path("sample_files")

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Text": [".txt"],
    "Spreadsheets": [".csv", ".xlsx"],
    "Documents": [".docx", ".doc"],
    "Python": [".py"]
}

for category in categories:
    folder_path = Path("organized_files") / category

    folder_path.mkdir(parents=True, exist_ok=True)

    print("Created:", category)

print("All folders created!")



import shutil
from collections import Counter

# Input and output folders
source_folder = Path("sample_files")
destination_folder = Path("organized_files")

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Text": [".txt"],
    "Spreadsheets": [".csv", ".xlsx"],
    "Documents": [".docx", ".doc"],
    "Python": [".py"]
}

# Check input folder
if not source_folder.exists():
    print("Source folder does not exist!")
    exit()

# Create output folder
destination_folder.mkdir(exist_ok=True)

# Count organized files
summary = Counter()

# Process files
for file in source_folder.iterdir():

    if not file.is_file():
        continue

    extension = file.suffix.lower()

    category = "Others"

    # Identify category
    for folder, extensions in categories.items():

        if extension in extensions:
            category = folder
            break

    # Create category folder
    target_folder = destination_folder / category
    target_folder.mkdir(parents=True, exist_ok=True)

    # Avoid overwriting duplicate filenames
    target_file = target_folder / file.name
    count = 1

    while target_file.exists():
        target_file = target_folder / f"{file.stem}_{count}{file.suffix}"
        count += 1

    # Move file
    shutil.move(str(file), str(target_file))

    summary[category] += 1

    print(f"Moved: {file.name} -> {category}")

# Final report
print("\n--- ORGANIZATION SUMMARY ---")

for category, total in summary.items():
    print(f"{category}: {total} files")

print("\nFile organization completed!")
