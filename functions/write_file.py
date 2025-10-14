import os

def write_file(working_directory: str, file_path: str, content: str) -> str:

    base = os.path.realpath(working_directory)
    target = os.path.realpath(os.path.join(working_directory, file_path))

    # Check integrity of attributes
    if not os.path.exists(target):
        try:
            common = os.path.commonpath({base, target})
        except ValueError:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if common != base:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        try:
            os.makedirs(os.path.dirname(target), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
        
    if os.path.exists(target) and os.path.isdir(target):
        return f'Error: "{file_path}" is a directory, not a file'
    
    try:
        with open(target, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"