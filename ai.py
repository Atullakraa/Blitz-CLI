from google import genai
from google.genai import types
from openai import OpenAI

def create_client(api_choice, config):
    if api_choice == "1":
        return genai.Client(api_key=config["gemini_api_key"])
    elif api_choice == "2":
        return OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=config["openrouter_api_key"]
        )

def get_models(client, api_choice):
    if api_choice == "1":
        return client.models.list()
    elif api_choice == "2":
        return client.models.list() 

def gen_response(api_choice, client, model, max_tokens, user_prompt, system_prompt):

    if api_choice == "1":

        response = client.models.generate_content(
            model=model,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                max_output_tokens=max_tokens
            )
        )
        return response.text, None

    elif api_choice == "2":
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            max_tokens=max_tokens
        )

        token = response.usage.total_tokens
        return response.choices[0].message.content, token    
    
           

    