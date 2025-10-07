import os
import sys
from pathlib import Path

def write_file(working_directory, file_path, content):
    """
    Write content to a file with proper error handling and security checks.

    Args:
        working_directory (str): The working directory path
        file_path (str): The file path to write to
        content (str): The content to write to the file

    Returns:
        str: Success message or error message
    """
    try:
        # Convert to Path objects for easier manipulation
        working_dir = Path(working_directory).resolve()
        file_path_obj = Path(file_path)

        # Resolve the file path relative to working directory
        if file_path_obj.is_absolute():
            resolved_file_path = file_path_obj
        else:
            resolved_file_path = working_dir / file_path_obj

        # Check if file path is outside working directory
        try:
            resolved_file_path.relative_to(working_dir)
        except ValueError:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Create parent directories if they don't exist
        resolved_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write content to file
        with open(resolved_file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        # Return success message
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {str(e)}'
