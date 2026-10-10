# converstaion and chat with LLM
import os


from dotenv import load_dotenv
from google import genai

# loading api key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# chat session
chat = client.chats.create(
    model="gemini-3.6-flash"
)

# chatting started
while True:
    question = input("you: ")

    if question.lower()== "exit":
        print("gemini: goodbye")
        break
    # send msg wirh converstion hisotry
    response = chat.send_message(question)

    print("gemini: ",response.text)