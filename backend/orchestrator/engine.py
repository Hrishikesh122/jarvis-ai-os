from models.llm import query_llm
from tools.calculator import calculate

def orchestrate(user_input: str):
    user_input_lower = user_input.lower()

    # TOOL DECISION: Calculator
    if "calculate" in user_input_lower:
        expression = user_input_lower.replace("calculate", "").strip()
        return {
            "reply": calculate(expression),
            "confidence": 0.95,
            "actions": ["calculator"]
        }

    # DEFAULT: LLM
    reply = query_llm(user_input)
    return {
        "reply": reply,
        "confidence": 0.9,
        "actions": ["llm"]
    }