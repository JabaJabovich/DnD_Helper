from pydantic import BaseModel


class NPC(BaseModel):
    id: int | None = None
    name: str
    race: str
    role: str
    personality: str
    goal: str
    flaw: str
    description: str | None = None
