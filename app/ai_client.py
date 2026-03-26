import os
import requests
from dotenv import load_dotenv

load_dotenv()

AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def generate_npc_description(npc_data: dict) -> str:
    """
    npc_data: dict with fields name, race, role, personality, goal, flaw
    """
    if AI_PROVIDER != "ollama":
        raise RuntimeError(f"Unsupported AI_PROVIDER: {AI_PROVIDER}")

    prompt = (
        "You are an assistant helping a Dungeon Master in a fantasy tabletop RPG.\n"
        "Write 2–4 sentences of atmospheric, narrative description of this NPC in English.\n"
        "Do not mention game rules or numbers, focus only on mood, personality and hints of backstory.\n\n"
        f"Name: {npc_data['name']}\n"
        f"Race: {npc_data['race']}\n"
        f"Role: {npc_data['role']}\n"
        f"Personality: {npc_data['personality']}\n"
        f"Goal: {npc_data['goal']}\n"
        f"Flaw: {npc_data['flaw']}\n\n"
        "Answer with one coherent paragraph in English."
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
