# Day 96; Connecting RAG with Gemini API
import os
import chromadb
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Createing vector database
db_client = chromadb.Client()
collection = db_client.create_collection(name="rag_demo")

# Storing documents
collection.add(
    ids=["1", "2", "3"],
    documents=[
        "Python is a programming language.",
        "Java is an object-oriented programming language.",
        "Machine learning uses data to learn patterns."
    ]
)

# Asking a question
question = "Is Python a programming language?"

# Retrieve relevant context
results = collection.query(
    query_texts=[question],
    n_results=1
)

context = results["documents"][0][0]

prompt = f"""
Answer the question using the context below.
If the answer is not in the context, say you don't know
based on the provided context.

Context:
{context}

Question:
{question}
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print("Question:", question)
print("Retrieved Context:", context)
print("AI Answer:", response.text)