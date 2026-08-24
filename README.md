**Blitz-CLI**\n
Blitz-CLI is a Python command-line AI assistant that supports ai models, with configurable system prompts and model selection.
Currently Supports Ai models:
1.gemini api key https://aistudio.google.com/apikey?utm_source=chatgpt.com
2.openrouter api key https://openrouter.ai/?utm_source=chatgpt.com

**How to Install**
```
git clone https://github.com/Atullakraa/Blitz-CLI.git
cd Blitz-CLI
pip install -r requirements.txt
python Blitz-CLI
```
**config.json**
```
{
    "gemini_api_key": "your_gemini_api_key_here",
    "openrouter_api_key": "your_openrouter_api_key_here",
    "max-token": 1000
}
```
gemini api key https://aistudio.google.com/apikey?utm_source=chatgpt.com
openrouter api key https://openrouter.ai/?utm_source=chatgpt.com

***genai client***
```
client = genai.Client(api_key=gemini_API_KEY)
```

***genai response***
```
response = client.models.generate_content(
            model=model_input,
            contents=user_input
        )
```        

***Openrouter client***
```
client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_API_KEY
    )
```
***Openrouter response***

```
response = client.chat.completions.create(
            model=model_input,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            max_tokens=1000
        )  
```
