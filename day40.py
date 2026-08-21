# OOP: Methods and init

class Car:          #Created a class named Car
    def __init__(self,brand,model):           #used __init__ model a constructor that runs automatically when an object is created
        self.brand = brand                #also used self.brand stores the brand value inside the object
        self.model = model
    def display(self):                  #another display method is created
        print("Brand:", self.brand)           #this print brand and model of the current object
        print("Model:", self.model)
b1=Car("BMW","M5")                       #the object name of brand and model is given
b1.display()                     #called the display()