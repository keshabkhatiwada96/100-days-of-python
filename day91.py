# day 91 function calling and tools

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# loading api key
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# creating calculator tool
def calculate(a: int, b: int) -> int:
     print("python calculator tool called")
     return a + b
     

# creating chat session with calculator tool
chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        tools=[calculate]
    )
)

# asking gemini to calculate
question = input("ask gemini: ")

response = chat.send_message(question)

# display response
print("gemini:", response.text)
