from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import NPC
from .npc import generate_raw_npc
from .ai_client import generate_npc_description


app = FastAPI(title="D&D Companion")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "message": "D&D backend is running"}


@app.get("/api/npc/random", response_model=NPC)
def api_random_npc(use_ai: bool = True):
    npc = generate_raw_npc()
    if use_ai:
        try:
            npc.description = generate_npc_description(npc.dict())
        except Exception:
            npc.description = None
    return npc
