import os

def get_file_content(working_directory: str, file_path: str) -> str:
    
    base = os.path.realpath(working_directory)
    target = os.path.realpath(os.path.join(working_directory, file_path))

    # Check integrity of attributes
    if not os.path.isfile(target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        common = os.path.commonpath({base, target})
    except ValueError:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if common != base:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try:
        MAX_CHAR = 10000
        with open(target, "r") as f:
            file_content_string = f.read(MAX_CHAR)

        return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"
    
