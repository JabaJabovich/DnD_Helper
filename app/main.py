from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import NPC
from .npc import generate_raw_npc

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
def api_random_npc():
    npc = generate_raw_npc()
    return npc
