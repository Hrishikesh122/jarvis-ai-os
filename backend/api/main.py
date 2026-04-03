import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from orchestrator.engine import orchestrate
from fastapi import FastAPI
from pydantic import BaseModel
from models.llm import query_llm
from security.filter import is_safe
from security.risk import risk_score

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "JARVIS AI backend running"}

@app.post("/chat")
def chat(req: ChatRequest):
    if not is_safe(req.message):
        return {
            "reply": "Request blocked due to security policy.",
            "confidence": 1.0,
            "actions": ["blocked"]
        }

    risk = risk_score(req.message)

    response = orchestrate(req.message)
    response["risk"] = risk

    return response