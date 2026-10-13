# simple rag demonstration
question = "What is Python?"

documents = [
    "Python is a programming language.",
    "Java is an object-oriented programming language.",
    "Machine learning uses data to learn patterns."
]

# imagine this retrieves the most relevant document
context = "Python is a programming language."

prompt = f"""
Answer the question using the context below.

Context: {context}
Question: {question}
"""

print(prompt)