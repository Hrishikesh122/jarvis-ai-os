# Simple in-memory storage (we'll upgrade later)

chat_history = []

def save_interaction(user_msg, ai_msg):
    chat_history.append({
        "user": user_msg,
        "ai": ai_msg
    })

def get_history():
    return chat_history[-5:]  # last 5 messages only