from fastapi import FastAPI

app = FastAPI(title="D&D Companion")

@app.get("/")
def root():
    return {"status": "ok", "message": "D&D backend is running"}

@app.get("/hello")
def hello():
    return {"message": "Hello, DnD!"}
