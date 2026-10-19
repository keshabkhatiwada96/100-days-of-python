# Day 99: Simple LLM Application Evaluation demonstartion

def evluate_answer(expected, actual):
 if expected.lower() == actual.lower():
    return "PASS"
 else:
    return "FAIL"

expected_answer = "Python is a programming language."
actual_answer = "Python is a programming language."


result = evluate_answer(expected_answer,actual_answer)
print("Expected:", expected_answer)
print("Actual:", actual_answer)
print("Evaluation:", result)