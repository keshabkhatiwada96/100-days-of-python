# Simple agent workflow with memory

memory = {}

def calculator(a, b):
    return a + b

def agent(question, a, b):
    result = calculator(a, b)

    memory["last-question"] = question
    memory["last-result"] = result

    return result

question = "what is 25 + 35?"

answer = agent(question, 25, 35)

print("question:", question)
print("answer:", answer)
print("agent Memory:", memory)