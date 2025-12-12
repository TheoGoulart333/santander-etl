import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4")

def generate_marketing_message(profile: dict) -> str:
    name = profile.get("name", "cliente")

    messages = [
        {"role": "system", "content": "Você é um gerador de mensagens de marketing."},
        {"role": "user", "content": f"Crie um texto de marketing curto para o usuário {name} com base nos dados: {profile}"}
    ]

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        max_tokens=120
    )

    return response.choices[0].message["content"]
