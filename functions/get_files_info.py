import os
from google.genai import types

def get_files_info(working_directory, directory=None):

    root_directory = os.path.abspath(working_directory)
    operating_directory = os.path.abspath(os.path.join(root_directory, directory))

    if not operating_directory.startswith(root_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
    if not os.path.isdir(operating_directory):
        return f'Error: "{directory}" is not a directory\n'
    
    file_list = ""

    if directory == ".":
        file_list += "Results for current directory:\n"
    else:
        file_list += f"Results for '{directory}' directory:\n"

    for obj in os.listdir(operating_directory):
        try:
            abso = os.path.join(operating_directory, obj)
            file_list += f"- {obj}: file_size={os.path.getsize(abso)} bytes, is_dir={os.path.isdir(abso)}\n"
        except OSError:
            return f"Error: An error occurred while listing files in '{directory}'"
    
    return file_list

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)