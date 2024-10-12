import os
import glob

def delete_files_by_extension(folder_path, file_extension):
    # Create the search pattern for the specified file type
    search_pattern = os.path.join(folder_path, f"*{file_extension}")

    # Loop through all files that match the pattern
    for file_path in glob.glob(search_pattern):
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")

# Example usage:
folder_path = "D:/DCIM/100CANON"
file_extension = '.CR3'  # Replace with the file type you want to delete

delete_files_by_extension(folder_path, file_extension)
