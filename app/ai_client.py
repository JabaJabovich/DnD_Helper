import os
import requests
from dotenv import load_dotenv

load_dotenv()

AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def generate_npc_description(npc_data: dict) -> str:
    """
    npc_data: dict с полями name, race, role, personality, goal, flaw
    """
    if AI_PROVIDER != "ollama":
        raise RuntimeError(f"Unsupported AI_PROVIDER: {AI_PROVIDER}")

    prompt = (
        "Ты помощник ведущего Dungeons & Dragons. "
        "ВСЕГДА отвечай ТОЛЬКО на русском языке. "
        "Напиши 2–4 предложения атмосферного описания этого NPC, "
        "без игровых правил и чисел, только художественный текст.\n\n"
        f"Имя: {npc_data['name']}\n"
        f"Раса: {npc_data['race']}\n"
        f"Роль: {npc_data['role']}\n"
        f"Характер: {npc_data['personality']}\n"
        f"Цель: {npc_data['goal']}\n"
        f"Изъян: {npc_data['flaw']}"
    )

    url = f"{OLLAMA_BASE_URL}/v1/chat/completions"

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
    }

    resp = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()
