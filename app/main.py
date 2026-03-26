from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import NPC
from .npc import generate_raw_npc
from .ai_client import generate_npc_description
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import pathlib


app = FastAPI(title="D&D Companion")
BASE_DIR = pathlib.Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/ui", response_class=HTMLResponse)
def ui_root():
    with open(BASE_DIR / "static" / "index.html", "r", encoding="utf-8") as f:
        return f.read()

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
