import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from pydantic import BaseModel
from models.llm import query_llm

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "JARVIS AI backend running"}

@app.post("/chat")
def chat(req: ChatRequest):
    reply = query_llm(req.message)
    return {
        "reply": reply,
        "confidence": 0.9,
        "actions": []
    }