# Connecting gemini ai with python and running in terminal
# first used pip install google-genai cmd to install the pacakage

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

while True:
    question = input("You: ")
    if question.lower() == "exit":break

    
      
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )


    print("Gemini: ",response.text)

