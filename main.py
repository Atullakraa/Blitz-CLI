import json

from google import genai
from openai import OpenAI

print("┏━━━━━━━━━━━━━━━━━━┓")
print("┃    Blitz-CLI     ┃")
print("┗━━━━━━━━━━━━━━━━━━┛ by Atul 😚")
print("┣━ Type 'exit' to quit the chat.")

print("┣━ Select API: ")
print("┣━ 1. Gemini")
print("┣━ 2. OpenRouter")

api_choice = input("┣━ Enter your choice (1 or 2): ")

with open("config.json", "r") as file:
    data = json.load(file)

gemini_api_key = data["gemini_api_key"]
openrouter_api_key = data["openrouter_api_key"]
max_tokens = data["max-token"]

if api_choice == "1":
    gemini_API_KEY = gemini_api_key  # Replace with your actual Gemini API key
elif api_choice == "2":
    openrouter_API_KEY = openrouter_api_key  # Replace with your openrouter API key

if api_choice == "1":
    client = genai.Client(api_key=gemini_API_KEY)
elif api_choice == "2":
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_API_KEY
    )
print("┣━ 1. Checking available models...")
print("┣━ 2. Set Model for the chat...")
option = input("┣━ Select an option (1 or 2): ")

if option == "1":
    for model in client.models.list():
        print(f"┃ {model.name}")
    model_input = input("┣━ Enter the model name you want to use: ")

elif option == "2":
    model_input = input("┣━ Enter the model name you want to use: ")  

SYSTEM_PROMPT = """
You are Blitz, an AI assistant created by Atul.
Be helpful, concise, and friendly.
"""
while True:
    user_input = input("┣━ You: ")

    # user_input = open("dev_prompt.txt", "r").read().strip()  # Read the user name from the file

    if user_input.lower() == "exit":
        print("┃ Exiting the chat. Goodbye!")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        break
    

    if api_choice == "1":
        response = client.models.generate_content(
            model=model_input,
            contents=user_input,
        )
        print(f"┣━ Blitz: {response.text}", flush=True)    
    elif api_choice == "2":
        response = client.chat.completions.create(
            model=model_input,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            max_tokens=max_tokens
        )      
        total = response.usage.total_tokens
        print(f"┣━ Blitz: {response.choices[0].message.content}")
        print(f"┣━ Token Used: {total}")