**Blitz-CLI**
Currently Supports:
1.gemini api key https://aistudio.google.com/apikey?utm_source=chatgpt.com
2.openrouter api key https://openrouter.ai/?utm_source=chatgpt.com

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
