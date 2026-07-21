# Strings in Python

# A string is a sequence of characters enclosed in single (''),
# double ("") or triple quotes (''' ''' or """ """).
name = "Jonas"
print(name)

# multiline string 
message = """
 sic mundus creatus est 
 the beginning is the end
 and
 the end is the beginning
  """
print(message)

# Accessing Characters of a String
# Strings use indexing. Index starts from 0.

text = "DARK"

print(text[0])    
print(text[1])    
print(text[2])   
print(text[3])    


# Looping Through a String
# Each character is accessed one by one.
print("Looping Through a String")
word = "Winden"

for letter in word:
    print(letter)

print("Length of a string")

    # Length of a String
word = 'GERMANY'
print(len(word))