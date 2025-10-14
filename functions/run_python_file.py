import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args=[]):

    base = os.path.realpath(working_directory)
    target = os.path.realpath(os.path.join(working_directory, file_path))

    # Check integrity of attributes
    if not os.path.exists(target):
        return f'Error: File "{file_path}" not found.'
    
    try:
        common = os.path.commonpath({base, target})
    except ValueError:
        return f'Error: Cannot execute "{file_path}" as it is outside'
    if common != base:
        return f'Error: Cannot execute "{file_path}" as it is outside'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(
            ["python", target, *args],
            capture_output=True,
            text=True,
            cwd=base,
            timeout=30
        )

        stdout = completed_process.stdout.strip()
        stderr = completed_process.stderr.strip()
        code = completed_process.returncode

        # Build the output message
        output_parts = []
        if stdout:
            output_parts.append(f"STDOUT:\n{stdout}")
        if stderr:
            output_parts.append(f"STDERR:\n{stderr}")
        if code != 0:
            output_parts.append(f"Process exited with code {code}")

        # If there’s no output at all
        if not output_parts:
            return "No output produced."

        return "\n\n".join(output_parts)


    except subprocess.TimeoutExpired:
        return f'Error: execution of "{file_path}" timed out after 30 seconds.'
    except Exception as e:
        return f"Error: executing Python file: {e}"



