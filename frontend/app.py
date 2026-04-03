import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/chat"

def chat_with_ai(user_input):
    try:
        response = requests.post(
            API_URL,
            json={"message": user_input}
        )
        data = response.json()

        reply = data.get("reply", "")
        confidence = data.get("confidence", "")
        actions = data.get("actions", [])
        risk = data.get("risk", "")

        return f"""
🤖 Reply: {reply}

📊 Confidence: {confidence}
⚙️ Actions: {actions}
🛡️ Risk: {risk}
"""
    except Exception as e:
        return f"Error: {str(e)}"

iface = gr.Interface(
    fn=chat_with_ai,
    inputs=gr.Textbox(placeholder="Ask JARVIS..."),
    outputs="text",
    title="JARVIS AI OS",
    description="Offline AI Assistant with Memory, Tools, and Security"
)

if __name__ == "__main__":
    iface.launch()