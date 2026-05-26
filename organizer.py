from pathlib import Path
from rules import file_category
import shutil


def organize_files(source_folder):

    source_path = Path(source_folder)

    # Take snapshot of files before moving
    for file in list(source_path.iterdir()):

        # Ignore folders
        if file.is_file():

            moved = False

            # Check categories
            for category, extensions in file_category.items():

                if file.suffix.lower() in extensions:

                    destination_folder = source_path / category
                    destination_folder.mkdir(exist_ok=True)

                    shutil.move(
                        str(file),
                        str(destination_folder / file.name)
                    )

                    print(f"Moved {file.name} to {destination_folder}")

                    moved = True
                    break

            # If no category matched
            if not moved:

                others_folder = source_path / "Others"
                others_folder.mkdir(exist_ok=True)

                shutil.move(
                    str(file),
                    str(others_folder / file.name)
                )

                print(f"Moved {file.name} to {others_folder}")