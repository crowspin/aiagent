import os, subprocess
from subprocess import TimeoutExpired, CalledProcessError, SubprocessError
from google.genai import types

def run_python_file(working_directory, file_path):
    
    root_directory = os.path.abspath(working_directory)
    selected_file = os.path.abspath(os.path.join(root_directory, file_path))

    if not selected_file.startswith(root_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory\n'
    if not os.path.isfile(selected_file):
        return f'Error: File "{file_path}" not found.\n'
    if not selected_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.\n'
    
    try:
        resp = subprocess.run(["ls", "-l", "/dev/null"], capture_output=True, cwd=os.path.dirname(selected_file), timeout=30)
    except TimeoutExpired:
        return f"Error: Python file '{file_path}' took longer than 30 seconds to execute. Terminated.\n"
    except CalledProcessError:
        return f"Error: The Python file '{file_path}' returned with a non-zero return code\n"
    except ValueError:
        return f"Error: Invalid arguments supplied with '{file_path}'\n"
    except Exception as e:
        return f"Error: executing Python file '{file_path}': {e}\n"
    
    feedback = f"Attempting to run python file '{file_path}': \n\n"

    feedback += f"Process exited with code {resp.returncode}\n"
    if resp.stdout + resp.stderr == "":
        feedback += "No output produced"
    else:
        if resp.stdout:
            feedback += f"STDOUT:\n{resp.stdout}\n\n"
        if resp.stderr:
            feedback += f"STDERR:\n{resp.stderr}\n\n"

    return feedback

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python script from within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the python script file ending in '.py'. Should be relative to the working directory.",
            ),
        },
    ),
)