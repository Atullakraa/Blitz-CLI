BASE_SYSTE_PROMPTS="""
You are Blitz, an AI assistant created by Atul.
Be helpful, concise, and friendly.
"""

def mode_prompt(modes):
    files = {
        "1": 'prompt/dev_prompt.txt',
        "2": 'prompt/bypass1_prompt.txt',
        "3": 'prompt/bypass2_prompt.txt'
    }
    if modes not in files:
        return BASE_SYSTE_PROMPTS

    try:
        with open(files[modes], 'r', encoding='utf-8') as file:
            mode_prompt = file.read().strip()
        return f"{BASE_SYSTE_PROMPTS}\n{mode_prompt}"

    except FileNotFoundError:
        print("┃ Prompt file not found.")
        return BASE_SYSTE_PROMPTS