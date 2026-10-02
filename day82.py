# Tokens, Context and Parameters

sentence = "my name is keshab"

# tokenization
tokens = sentence.split()
print("Sentence :")
print(sentence)

print("tokenized sentence: ")
print(tokens)


# tokens id
tokens_ids = {
  "my" : 101,
  "name" : 205,
  "is" : 312,
  "keshab" : 450
}

for token in tokens:
    print(token, "=", tokens_ids[token])

# token id list 
ids = []

for token in tokens:
    ids.append(tokens_ids[token])

print("tokenn ids:")
print(ids)

