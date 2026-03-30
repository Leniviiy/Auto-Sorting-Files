import os
import shutil
from pathlib import Path

SOURCE_DIR = "C:/Users/YourUser/Downloads"

DEST_DIRS = {
    "Video": "D:/Video",
    "Photo": "D:/Photo",
    "Music": "D:/Music",
    "Archives": "D:/Archives"
}

FILE_TYPES = {
    ".mp4": "Video", ".mov": "Video", ".mkv": "Video", ".avi": "Video", ".gif": "Video",
    ".jpg": "Photo", ".jpeg": "Photo", ".png": "Photo", ".webp": "Photo",
    ".avif": "Photo",  
    ".mp3": "Music", ".wav": "Music", ".flac": "Music",
    ".zip": "Archives", "Archives": "Archives", ".7z": "Archives"
}


def sort_my_files():
    print(f"Scanning a folder: {SOURCE_DIR}...")

    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Folder {SOURCE_DIR} not found!")
        return

    for folder_path in DEST_DIRS.values():
        os.makedirs(folder_path, exist_ok=True)

    files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]
    print(f"Files found for verification: {len(files)}")
    
    count = 0
    for file_name in files:
        extension = os.path.splitext(file_name)[1].lower()
        
        if extension in FILE_TYPES:
            category = FILE_TYPES[extension]
            target_folder = DEST_DIRS[category]
            
            path_from = os.path.join(SOURCE_DIR, file_name)
            path_to = os.path.join(target_folder, file_name)

            try:
                if not os.path.exists(path_to):
                    shutil.move(path_from, path_to)
                    print(f"[OK] {file_name} -> {category}")
                    count += 1
                else:
                    print(f"[MISSING] File {file_name} already exists in {category}")
            except Exception as e:
                print(f"[ERROR] Failed to move {file_name}: {e}")

    print(f"\n--- Job completed! Files moved: {count} ---")

if __name__ == "__main__":
    sort_my_files()