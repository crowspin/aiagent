import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python import schema_run_python_file, run_python_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    applet_verbose = False
    if len(sys.argv) < 2:
        sys.exit(1)

    for arg in sys.argv[2:]:
        if arg == "--verbose":
            applet_verbose = True

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ]
    )

    system_prompt = """
                    You are a helpful AI coding agent.

                    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

                    - List files and directories
                    - Read file contents
                    - Execute Python files with optional arguments
                    - Write or overwrite files

                    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
                    """

    user_prompt = sys.argv[1]
    if applet_verbose: print(f"User prompt: {user_prompt}\n")
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    ret = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        ),
    )
    for function_call_part in ret.function_calls:
        resp = call_function(function_call_part, applet_verbose)
        if not resp.parts[0].function_response.response:
            raise Exception ("fatal exception of some sort")
        elif applet_verbose:
            print(f"-> {resp.parts[0].function_response.response}")
    if ret.text != None:
        print (ret.text)
    if applet_verbose:
        print(f"Prompt tokens: {ret.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {ret.usage_metadata.candidates_token_count}")

def call_function(function_call_part, verbose=False):

    working_directory = "./calculator"

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    match(function_call_part.name):
        case "get_files_info":
            resp = get_files_info(working_directory, **(function_call_part.args))
        case "get_file_content":
            resp = get_file_content(working_directory, **(function_call_part.args))
        case "write_file":
            resp = write_file(working_directory, **(function_call_part.args))
        case "run_python_file":
            resp = run_python_file(working_directory, **(function_call_part.args))
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": resp},
            )
        ],
    )


if __name__ == "__main__":
    main()
