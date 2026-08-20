# OOP Basics: Classes and Objects

class Book:

    # __init__() is a constructor that runs automatically when an object is created
    # name and author are values passed when creating the object
    def __init__(self, name, author):

        # self refers to the current object
        # store the name value inside the object name attribute
        self.name = name
        
        # store the author value inside the object's author attribute
        self.author = author


# creating an object of the Book class
# "Python" is passed to name and "Keshab" is passed to author
# since self.name is before the first value python become and and 2nd value keshab become author
b1 = Book("Python", "Keshab")


#printing the object attribute
print("Name of author is", b1.author)
print("Name of book is", b1.name)