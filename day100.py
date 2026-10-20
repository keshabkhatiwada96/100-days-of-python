# DAY-100 simple AI QNA system

import os
import chromadb
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

db = chromadb.Client()
collection = db.create_collection(name="day100_notes")

collection.add(

ids=['1','2','3'],
documents = [
    "Python is a programming language.",
    "Machine learning uses data to learn patterns.",
    "RAG retrieves relevant information before generating an AI answer."
]
)

question = "What is RAG?"

results = collection.query(
    query_texts=[question],
    n_results=1
)
context = results["documents"][0][0]

prompt = f"""
Answer the question using the provided context

Context:{context}

Question:{question}
"""
response = client.models.generate_content(
model = "gemini-3.6-flash",
contents = prompt
)

print("question:",question)
print("retrieved context:",context)
print("Ai answer:",response.text)