# Basic LLM

# sentence
words = ['the','cat','sat','because','it','was','tired']

# attentrntion score for words
attention = [0.1,0.7,0.1,0.1,0.0,0.0,0.8]

print('word and attention: ')

for i in range(len(words)):
    print(words[i], '=', attention[i])

# finding word with highest attention
print('\nhigher attention: ')

for i in range(len(words)):
    if attention[i]>=0.7:
        print(words[i], "=" , attention[i])