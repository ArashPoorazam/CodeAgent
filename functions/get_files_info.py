import os


def get_files_info(working_directory: str, directory: str = '.') -> str:

    # Resolve to absolute, canonical paths (resolve symlinks)
    base = os.path.realpath(working_directory)
    target = os.path.realpath(os.path.join(working_directory, directory))

    # Prevent access outside base using commonpath check
    try:
        common = os.path.commonpath([base, target])
    except ValueError:
        return f'Error: Cannot access "{directory}" — target is outside the permitted working directory'
    if common != base:
        return f'Error: Cannot access "{directory}" — target is outside the permitted working directory'

    # Now attempt to list directory contents
    try:
        entries = os.listdir(target)
    except Exception as e:
        return f'Error: Unable to access "{directory}". {str(e)}'
    if not entries:
        return 'No files found.'

    # Gather file info
    lines = []
    for entry in sorted(entries):
        entry_path = os.path.join(target, entry)
        try:
            size = os.path.getsize(entry_path)
        except OSError:
            size = 'unknown'
        is_dir = os.path.isdir(entry_path)
        lines.append(f"{entry}: file_size={size} bytes, is_dir={is_dir}")

    return "\n".join(lines)

