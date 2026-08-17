# File Handling in python
# In py file handling allow us to read and write to files

with open("example.txt", "r") as file:
    print(file.read())    #read mode




file = open("example2.txt","w")    #write file

file.write("hello keshab , im good wbu, system32")
file.close()



file = open("example2.txt","a")    #append file

file.write("\nhello keshab \nhey im good \n wbu?? ")
file.close()

