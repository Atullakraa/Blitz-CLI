from google import genai

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key

client = genai.Client(api_key=API_KEY)

print("┏━━━━━━━━━━━━━━━━━━┓")
print("┃    Blitz-CLI     ┃")
print("┗━━━━━━━━━━━━━━━━━━┛ by Atullakra 😚")
print("┣━ Type 'exit' to quit the chat.")

print("┣━ 1. Checking available models...")
print("┣━ 2. Set Model for the chat...")
option = input("┣━ Select an option (1 or 2): ")

if option == "1":
    for model in client.models.list():
        print(f"┃ {model.name}")
if option == "2":
    model_input = input("┣━ Enter the model name you want to use: ")  

while True:
    user_input = input("┣ You: ")

    if user_input.lower() == "exit":
        print("┃ Exiting the chat. Goodbye!")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        break

    response = client.models.generate_content(
        model=model_input,
        contents=user_input
    )

    print(f"┣━ Blitz: {response.text}")

    