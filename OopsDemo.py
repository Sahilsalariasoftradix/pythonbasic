# Classes are user defined bluprint or prototype
# Sum, multiplication, addition, constant
# methods, class variable s
import calendar


# Self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100

    # default constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("i am now called automatically when object is created ")

    def getData(self):
        print("i am now executing as a method in a class")

    def Summation(self):
        return self.a + self.b


obj = Calculator(2, 5)  # syntax to create objects in python
obj.getData()
print(obj.Summation())
