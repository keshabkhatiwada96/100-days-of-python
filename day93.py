# Vector Databases: Basic Concept

import chromadb

client = chromadb.Client()

collection = client.create_collection(name="python_notes")

# some text
collection.add(
    ids=["1","2","3"],
    documents= [
            "Python is a programming language.",
            "Machine learning uses data to learn patterns.",
            "Python is useful for AI development."
    ]
)

results = collection.query(
    query_texts=["How can i develop AI using python"],
    n_results=2
)

print(results['documents'])