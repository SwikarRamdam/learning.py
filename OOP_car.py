class Car:
    tyres = 3 #class variables
    def __init__(self,brand,colour,price): #works as a constructor
        self.brand = brand
        self.colour = colour
        self.price = price

    def drive(self):
        print("This "+self.brand+self.colour+" is driving")

    def stop(self):
        print("The car has stopped")