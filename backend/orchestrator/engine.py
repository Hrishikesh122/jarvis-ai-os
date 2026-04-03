from models.llm import query_llm
from tools.calculator import calculate
from memory.store import save_interaction, get_history

def orchestrate(user_input: str):
    user_input_lower = user_input.lower()

    # TOOL: Calculator
    if "calculate" in user_input_lower:
        expression = user_input_lower.replace("calculate", "").strip()
        result = calculate(expression)

        save_interaction(user_input, result)

        return {
            "reply": result,
            "confidence": 0.95,
            "actions": ["calculator"]
        }

    # MEMORY: Get past context
    history = get_history()

    context = ""
    for h in history:
        context += f"User: {h['user']}\nAI: {h['ai']}\n"

    prompt = context + f"User: {user_input}\nAI:"

    reply = query_llm(prompt)

    # SAVE interaction
    save_interaction(user_input, reply)

    return {
        "reply": reply,
        "confidence": 0.9,
        "actions": ["llm", "memory"]
    }