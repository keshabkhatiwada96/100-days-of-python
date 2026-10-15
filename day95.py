# simple rag system

import chromadb

client = chromadb.Client()

collection = client.create_collection(name="rag_demo")

collection.add(
    ids=["1","2",'3'],
    documents=[
              "Python is a programming language.",
             "Java is an object-oriented programming language.",
             "Machine learning uses data to learn patterns."
    ]
)

question = "what is python?"

results = collection.query(
    query_texts=[question],
    n_results=1
)

context = results["documents"][0][0]

print("quesstion = ",question)
print("retrived context = ",context)