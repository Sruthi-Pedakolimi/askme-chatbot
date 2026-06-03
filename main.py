import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

def error_handling(e):
    message = None
    if isinstance(e.body, dict):
        message = e.body.get("message", e)
    else:
        message = e
    return message

# loading the .env file
load_dotenv(override=True)
api_key = os.getenv("OPEN_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
client = OpenAI(api_key=api_key, base_url=base_url)
try:
    conversation = client.conversations.create()
    while True:
        user_prompt = input("Enter your prompt: ")
        if user_prompt.lower() == "exit":
            print("Exiting....Goodbye!!!")
            break 
        if user_prompt.strip() == "":
            print("Please enter the input")
            continue
        response = client.responses.create(
            model="gpt-4.1",
            input=[{"role": "user", "content": user_prompt}],
            conversation=conversation.id,
            stream=True
            )
        for event in response:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
        print()
except openai.AuthenticationError as e:
    message = error_handling(e)
    print(f"Authentication failed: {message}")

except openai.RateLimitError as e:
     message = error_handling(e)
     print(f"OpenAI API request exceeded rate limit: {message}")

except openai.APITimeoutError as e:
    message = error_handling(e)
    print(f"Timeout error please try after sometime: {message}")

except openai.APIConnectionError as e:
    message = error_handling(e)
    print(f"Network error please check and try again: {message}")
except Exception as e:
    print(f"An error occured {e}")