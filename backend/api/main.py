from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "JARVIS AI backend running"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "reply": f"Received: {req.message}",
        "confidence": 0.5,
        "actions": []
    }