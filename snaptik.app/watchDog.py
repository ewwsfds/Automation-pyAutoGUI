import os
import time

files = []

while True:
    root = os.path.dirname(os.path.abspath(__file__))

    # Remove files from list that no longer exist
    files = [
        f for f in files
        if os.path.exists(os.path.join(root, f))
    ]

    # Get all mp4 files in the same folder
    current_files = [
        f for f in os.listdir(root)
        if f.lower().endswith(".mp4")
    ]

    # Check for new files not in our list
    for file in current_files:
        if file not in files:
            new_name = f"video{len(files)}.mp4"

            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_name)

            # Avoid renaming if already has the target name
            if file != new_name:
                os.rename(old_path, new_path)
                file = new_name

            files.append(file)

    time.sleep(2)