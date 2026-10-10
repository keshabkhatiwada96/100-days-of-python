# structured ai response

import os
import json

from dotenv import load_dotenv
from google import genai

# loading api key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



# asking gemini for structured data

name = input("enter student name: ")
skills = input("enter skills (comma separated): ")

prompt = f"""
Create a student profile using the details below.

Name: {name}
Skills: {skills}

Return valid JSON with these fields:
name, skills, course, and level.

Return only valid JSON.
"""

response = client.models.generate_content(

    model="gemini-3.6-flash",
    contents = prompt,
    config = {
        "response_mime_type": "application/json"
    }
)
print(response.text)

# converting json text in python data
data = json.loads(response.text)

print("student name:",data["name"])
print("course:",data["course"])
print("skills:",data["skills"])
print("level:",data["level"])