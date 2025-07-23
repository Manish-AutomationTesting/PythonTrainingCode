class Car:
    # class variables
    wheels = 4

    # constructor of this class:
    def __init__(self, color):
        print("car class const")
        self.color = color

    def __int__(self):
        print("default const")

    def test(self):
        print("test method")

    # if any var is declared inside the method or constructor: instance variable
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price


# how to create an object of this class:
c1 = Car(color="red")
c1 = Car("Black")
print(c1.wheels)
print(Car.wheels)
c1.test()
c1.setPrice(1000)
print(c1.getPrice())

c2=Car("Golden")
c2.setPrice(3000)
print(c2.getPrice())

class Test:
    a=10

#Blank class:
class Pop:
    pass

P1=Pop()

