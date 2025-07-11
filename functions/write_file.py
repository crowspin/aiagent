import os

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