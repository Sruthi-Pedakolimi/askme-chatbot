import os
from dotenv import load_dotenv
from openai import OpenAI

# loading the .env file
load_dotenv(override=True)
api_key = os.getenv("OPEN_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
client = OpenAI(api_key=api_key, base_url=base_url)
messages = [{"role": "developer", "content": "You are a helpful assistant"}]

conversation = client.conversations.create()
while True:
    user_prompt = input("Enter your prompt: ")
    if user_prompt.lower() == "exit":
        print("Exiting....Goodbye!!!")
        break 

    response = client.responses.create(
        model="gpt-4.1",
        input=[{"role": "user", "content": user_prompt}],
        conversation=conversation.id,
        stream=True
        )
    for event in response:
        if event.type == "response.output_text.delta":
            print(event.delta, end=" ", flush=True)
    print()

    
