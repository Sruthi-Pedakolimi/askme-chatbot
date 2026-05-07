import os
from dotenv import load_dotenv
from openai import OpenAI

# loading the .env file
load_dotenv(override=True)
api_key = os.getenv("OPEN_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
client = OpenAI(api_key=api_key, base_url=base_url)


response = client.chat.completions.create(model="gpt-4o-mini", 
                                          messages=[
                                              {"role": "developer", "content": "You are a hepful assistant"},
                                              {"role": "user", "content": "Can you tell me a one sentence story on unicorn"}])
print(response.choices[0].message.content)