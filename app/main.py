import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Expected: 'mv <source> <destination>'")

    source_file = parts[1]
    dest_file = parts[2]

    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"Source file '{source_file}' does not exist.")

    if dest_file.endswith("/") or os.path.isdir(dest_file):
        target_dir = dest_file
        target_file = os.path.join(dest_file, os.path.basename(source_file))
    else:
        target_dir = os.path.dirname(dest_file)
        target_file = dest_file

    # create destination directories if path is not empty
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    # copy contents to target and clean up source file
    shutil.copyfile(source_file, target_file)
    os.remove(source_file)
