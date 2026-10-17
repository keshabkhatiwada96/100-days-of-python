# AI Agents: What They Are

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def calculator (a:int, b:int) -> int:
    return a+b


chat = client.chats.create(
    model = "gemini-3.6-flash",
    config={
        "tools":[calculator]
    }
)

question = "what is 25 + 35? use the calculator"

response = chat.send_message(question)

print("question :",question)
print("answer",response.text)