import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

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

    user_prompt = sys.argv[1]
    if applet_verbose: print(f"User prompt: {user_prompt}\n")
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    ret = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    print (ret.text)
    if applet_verbose:
        print(f"Prompt tokens: {ret.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {ret.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
