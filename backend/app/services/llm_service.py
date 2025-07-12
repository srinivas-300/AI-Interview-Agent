import os
from openai import OpenAI



api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def ask_llm(prompt: str, model: str = "gpt-4.1-nano-2025-04-14") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300  
    )
    return response.choices[0].message.content.strip()