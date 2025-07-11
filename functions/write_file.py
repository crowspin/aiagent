import os
from google.genai import types

def write_file(working_directory, file_path, content):
    
    root_directory = os.path.abspath(working_directory)
    selected_file = os.path.abspath(os.path.join(root_directory, file_path))

    if not selected_file.startswith(root_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory\n'
    
    if not os.path.exists(selected_file):
        os.makedirs(os.path.dirname(selected_file), 511, True)

    with open(selected_file, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)\n'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrite a file in the working directory with the data you supply. If the file does not exist, it will be created. If the directory structure does not exist, it will be created.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="A path to the file you want overwritten, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The data you want the file to be overwritten with.",
            )
        },
    ),
)