import os
from dotenv import load_dotenv
from openai import OpenAI

# loading the .env file
load_dotenv(override=True)
api_key = os.getenv("OPEN_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
client = OpenAI(api_key=api_key, base_url=base_url)
messages = [{"role": "developer", "content": "You are a helpful assistant"}]
while True:
    user_input = input("Enter the prompt: ")
    if user_input.lower() == "exit":
        print("Exiting....Goodbye!!!!")
        break

    user_prompt = {"role": "user", "content": user_input}
    messages.append(user_prompt)
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    new_message = {"role": response.choices[0].message.role, "content": response.choices[0].message.content}
    messages.append(new_message)
    print(new_message['content'])
    print("")
    
 
    


