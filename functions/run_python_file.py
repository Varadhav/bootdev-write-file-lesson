import os
import sys
import subprocess
from pathlib import Path

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_dir = Path(working_directory).resolve()
        file_path_obj = Path(file_path)

        # Resolve the file path relative to working directory
        if file_path_obj.is_absolute():
            resolved_file_path = file_path_obj
        else:
            resolved_file_path = (working_dir / file_path_obj).resolve()

        # Check if file path is outside working directory (using normalized paths)
        try:
            resolved_file_path.relative_to(working_dir)
        except ValueError:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if file exists
        if not resolved_file_path.exists():
            return f'Error: File "{file_path}" not found.'

        # Check if file is a Python file
        if not resolved_file_path.suffix == '.py':
            return f'Error: "{file_path}" is not a Python file.'

        # Execute the Python file using subprocess.run
        try:
            result = subprocess.run(
                [sys.executable, str(resolved_file_path)] + args,
                cwd=str(working_dir),
                capture_output=True,
                text=True,
                timeout=30
            )
        except subprocess.TimeoutExpired:
            return "Error: Process timed out after 30 seconds"

        # Format the output - ALWAYS include STDOUT and STDERR sections
        output_parts = []
        
        # Always add STDOUT section
        stdout_content = result.stdout if result.stdout else ""
        output_parts.append(f"STDOUT:\n{stdout_content}")
        
        # Always add STDERR section  
        stderr_content = result.stderr if result.stderr else ""
        output_parts.append(f"STDERR:\n{stderr_content}")
        
        # Add exit code if non-zero
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        # Check if both stdout and stderr are empty
        if not result.stdout and not result.stderr:
            return "No output produced."
        else:
            return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
