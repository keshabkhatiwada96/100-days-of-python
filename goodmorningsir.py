from datetime import datetime #FIXME: Import the datetime class to work with the current date and time. 
hour = datetime.now().hour    #FIXME: Get the current hour (0-23)

if 4 <= hour <12:
    print("Good Morning!! ")
elif 12 <= 17:
    print("Good Afternon!! ")
elif 17 <= 21:
    print("Good Evning!! ")
else:
    print("Good Night!!")