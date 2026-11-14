from pathlib import Path
import shutil

folder = Path("test_files")

for file in folder.iterdir():

    if file.is_file():

        extension = file.suffix.lower().replace(".", "")

        if not extension:
            extension = "others"

        target = folder / extension
        target.mkdir(exist_ok=True)

        shutil.move(str(file), str(target / file.name))

print("Files organized successfully!")