# JARVIS AI OS - Architecture Contract

## Backend API

POST /chat
Request:
{
  "message": "string"
}

Response:
{
  "reply": "string",
  "confidence": "float",
  "actions": []
}

---

## Tool Interface

run(input: dict) -> dict

---

## Memory Interface

save(message: str)
retrieve(query: str)

---

## Security Layer

is_safe(input: str) -> bool

---

## Orchestrator Flow

Input → Security → Memory → Tool/LLM → Response → Store

---

## Frontend Contract

Frontend must:
- Call POST /chat
- Display reply
- Show system status