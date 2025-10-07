import os
import sys
import subprocess
from pathlib import Path

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_dir = Path(working_directory).resolve()
        file_path_obj = Path(file_path)

        if file_path_obj.is_absolute():
            resolved_file_path = file_path_obj
        else:
            resolved_file_path = working_dir / file_path_obj

        try:
            resolved_file_path.relative_to(working_dir)
        except ValueError:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not resolved_file_path.exists():
            return f'Error: File "{file_path}" not found.'

        if not resolved_file_path.suffix == '.py':
            return f'Error: "{file_path}" is not a Python file.'

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

        output_parts = []
        
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        if not output_parts:
            return "No output produced."
        else:
            return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
