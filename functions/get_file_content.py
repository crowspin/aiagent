import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):

    root_directory = os.path.abspath(working_directory)
    selected_file = os.path.abspath(os.path.join(root_directory, file_path))

    if not selected_file.startswith(root_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory\n'
    if not os.path.isfile(selected_file):
        return f'Error: File not found or is not a regular file: "{file_path}"\n'
    
    try:
        with open(selected_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string + "\n\n"
    except FileNotFoundError:
        return f"Error: File not found: '{file_path}'"
    except PermissionError:
        return f"Error: Insufficient privileges: '{file_path}'"
    except ValueError:
        return f"Error: Invalid data format: '{file_path}'"
    except OSError:
        return f"Error: An error occurred while opening the file: '{file_path}'"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Returns the content of a specified file within the working directory up to a maximum of {MAX_CHARS} characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file name to read from, relative to the working directory.",
            ),
        },
    ),
)