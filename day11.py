# FIXME: String Methods in Python

a = "Arthur Morgan +++"

print(len(a))  #FIXME:"len() counts length of given string"
print(a)
print(a.upper())  #FIXME:"upper() make all charcater in uppercase"
print(a.lower())   #FIXME:"lower() make all charcater in lowercase"
print(a.rstrip('+')) #FIXME: "rstrip() is a Python string method that removes characters from the right (end) of a string. "
print(a.replace("Arthur Morgan", "John Marston")) #FIXME: "replace() it replaces the occurance of the string with another string"
print(a.split(" "))  #FIXME: "split() method splits given string at the specialized instance and retuns the seperated  string as list items"
b = "hello my name is Arthur Morgan"
print(b.capitalize())  #FIXME: "the capitalize() convert only the first character to upper case if it is already in upper case no changes are made"
print(a.center(50))  # FIXME: "center() places the string in the center of the specified width by adding spaces on both sides."
print(a.endswith("+++"))  # FIXME: "endswith() returns True if the string ends with the specified value otherwise it returns False."
#FIXME: Arthur Morgan
print(a.find("Morgan"))  # FIXME: "find() searches for the specified value and returns its first index. If not found, it returns -1."
c  = "wildwest"
print(c.isalnum())  # FIXME: "isalnum() checks whether all characters are alphabets or numbers and returns True or False."
print(c.isalpha())  # FIXME: "isalpha() returns True if all characters in the string are alphabets. Otherwise, it returns False."
print(c.islower())  # FIXME: "islower() returns True if all alphabetic characters in the string are lowercase. Otherwise, it returns False."
d = "hello ich libe dich \n"
print(d.isprintable())
# FIXME: the d string shows false because \n is not printable if \n was not there the output will be true.
print(b.isspace())  # FIXME: "isspace() returns True if all characters in the string are whitespace characters such as ' ', '\t', or '\n'. Otherwise, it returns False."
print(b.istitle())  # FIXME: "istitle() returns True if the first letter of every word is uppercase and the remaining letters are lowercase. Otherwise, it returns False."
print(c.swapcase())  # FIXME: "swapcase() converts all uppercase letters to lowercase and all lowercase letters to uppercase."
print(b.title())  # FIXME: "title() converts the first letter of every word to uppercase and the remaining letters to lowercase."


