from config import load_config
from ai import create_client, get_models, gen_response
from prompts import mode_prompt

print("┏━━━━━━━━━━━━━━━━━━┓")
print("┃    Blitz-CLI     ┃")
print("┗━━━━━━━━━━━━━━━━━━┛ by Atul 😚")
print("┣━ Type 'exit' to quit the chat.")

config = load_config()

print("┣━ Select API: ")
print("┣━ 1. Gemini")
print("┣━ 2. OpenRouter")

api_choice = input("┣━ Enter your choice (1 or 2): ")

client = create_client(api_choice, config)

print("┣━ 1. Checking available models...")
print("┣━ 2. Set Model manually...")
option = input("┣━ Select an option (1 or 2): ")

if option == "1":

    print("┃ Listing available models:")
    models = get_models(client, api_choice)

    for model in models:

        name = model.name

        if "/" in name:
            name =name.split("/")[-1]
        print(f"┃ {name}")
    model_input = input("┣━ Enter the model name: ")    
elif option == "2":
    model_input = input("┣━ Enter the model name: ")

print("┣━ Select Mode:")
print("┣━ 1. Dev Mode")
print("┣━ 2. jailbreak_lite Mode")
print("┣━ 3. jailbreak_adv Mode")
mode_input = input("┣━ Enter your choice (1, 2, or 3): ")

system_prompt = mode_prompt(mode_input)

max_tokens = config["max-token"]

while True:
    user_input = input("┣━ You: ")

    if user_input.lower() == "exit":
        print("┣━ Exiting the chat. GoodBye!")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        break

    response, token = gen_response(
        api_choice,
        client,
        model_input,
        max_tokens,
        user_input,
        system_prompt
    )
    print(f"┣━ Blitz: {response}")

    if token is not None:
        print(f"Token used: {token}")



        


