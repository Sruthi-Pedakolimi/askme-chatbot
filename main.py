import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

# get the error message from the error object
def get_error_message(e):
    message = None
    if isinstance(e.body, dict):
        message = e.body.get("message", e)
    else:
        message = e
    return message

# loading the .env file
# override the global keys if needed
load_dotenv(override=True)
api_key = os.getenv("OPEN_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
system_prompt = os.getenv("SYSTEM_PROMPT")

# creating open AI object
client = OpenAI(api_key=api_key, base_url=base_url)
try:
    # creating the conversation with the system prompt
    conversation = client.conversations.create(
         items=[
             {"type": "message", "role": "system", "content": system_prompt}
            ]
    )
    # handling the conversation loop until user exit
    while True:
        user_prompt = input("Enter your prompt: ")

        # handling exit condition
        if user_prompt.lower() == "exit":
            print("Exiting....Goodbye!!!")
            break 

        # handling user empty input condition
        if user_prompt.strip() == "":
            print("Please enter the input")
            continue

        # call response API with conversation id
        response = client.responses.create(
            model="gpt-4.1",
            input=[{"role": "user", "content": user_prompt}],
            conversation=conversation.id,
            stream=True
            )
        
        # print stream message
        for event in response:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
        print()

# handling exceptions
except openai.AuthenticationError as e:
    message = get_error_message(e)
    print(f"Authentication failed: {message}")

except openai.RateLimitError as e:
     message = get_error_message(e)
     print(f"OpenAI API request exceeded rate limit: {message}")

except openai.APITimeoutError as e:
    message = get_error_message(e)
    print(f"Timeout error please try after sometime: {message}")

except openai.APIConnectionError as e:
    message = get_error_message(e)
    print(f"Network error please check and try again: {message}")
except Exception as e:
    print(f"An error occured {e}")