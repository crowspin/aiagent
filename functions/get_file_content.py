import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):

    root_directory = os.path.abspath(working_directory)
    selected_file = os.path.abspath(os.path.join(root_directory, file_path))

    if not selected_file.startswith(root_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory\n'
    if not os.path.isfile(selected_file):
        return f'Error: File not found or is not a regular file: "{file_path}"\n'
    
    with open(selected_file, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    return file_content_string

#Catch errors