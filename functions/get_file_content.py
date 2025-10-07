import os
import sys
from pathlib import Path

# Add the parent directory to the path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import MAX_FILE_SIZE

def get_file_content(working_directory, file_path):
    """
    Read file content and return as string, with error handling and truncation.
    
    Args:
        working_directory (str): The working directory path
        file_path (str): The file path to read
        
    Returns:
        str: File content or error message
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
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if file exists and is a regular file
        if not resolved_file_path.exists():
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        if not resolved_file_path.is_file():
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read file content
        with open(resolved_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Truncate if necessary
        if len(content) > MAX_FILE_SIZE:
            content = content[:MAX_FILE_SIZE]
            content += f'[...File "{file_path}" truncated at {MAX_FILE_SIZE} characters]'
        
        return content
        
    except Exception as e:
        return f'Error: {str(e)}'