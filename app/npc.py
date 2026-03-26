import random
from .models import NPC

RACES = ["человек", "эльф", "дварф", "полурослик", "тифлинг"]
ROLES = [
    "тавернщик",
    "городской стражник",
    "мелкий дворянин",
    "жрица храма",
    "контрабандист",
]
PERSONALITIES = [
    "доброжелательный и немного наивный",
    "язвительный, но справедливый",
    "угрюмый и подозрительный",
    "чрезмерно вежливый и льстивый",
]
GOALS = [
    "разбогатеть любой ценой",
    "защитить свою семью",
    "искупить старую вину",
    "сбежать из города",
]
FLAWS = [
    "не умеет держать язык за зубами",
    "страдает от жадности",
    "не доверяет авантюристам",
    "пьёт больше, чем следует",
]


def generate_raw_npc() -> NPC:
    return NPC(
        name=random.choice(["Элдрин", "Мира", "Боромир", "Лиара", "Гундрик"]),
        race=random.choice(RACES),
        role=random.choice(ROLES),
        personality=random.choice(PERSONALITIES),
        goal=random.choice(GOALS),
        flaw=random.choice(FLAWS),
    )
