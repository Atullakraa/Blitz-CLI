from google import genai
from openai import OpenAI

print("┏━━━━━━━━━━━━━━━━━━┓")
print("┃    Blitz-CLI     ┃")
print("┗━━━━━━━━━━━━━━━━━━┛ by Atullakra 😚")
print("┣━ Type 'exit' to quit the chat.")

print("┣━ Select API: ")
print("┣━ 1. Gemini")
print("┣━ 2. OpenRouter")

api_choice = input("┣━ Enter your choice (1 or 2): ")


if api_choice == "1":
    gemini_API_KEY = "Your_Gemini_API_Key"  # Replace with your actual Gemini API key
elif api_choice == "2":
    openrouter_API_KEY = "Your_OpenRouter_API_Key"  # Replace with your openrouter API key

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

while True:
    user_input = input("┣━ You: ")

    # user_input = open("dev_guy.txt", "r").read().strip()  # Read the user name from the file

    if user_input.lower() == "exit":
        print("┃ Exiting the chat. Goodbye!")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        break
    

    if api_choice == "1":
        response = client.models.generate_content(
            model=model_input,
            contents=user_input
        )
        print(f"┣━ Blitz: {response.text}", flush=True)    
    elif api_choice == "2":
        response = client.chat.completions.create(
            model=model_input,
            messages=[
                {"role": "user", "content": user_input}
            ],
            max_tokens=1000
        )      
        total = response.usage.total_tokens
        print(f"┣━ Blitz: {response.choices[0].message.content}")
        print(f"┣━ Token Used: {total}")