from OOP_car import Car

car_1 = Car("Ford","green","20,000") # car = object, Car= class-constructor, ford,green,20000= values
car_2 = Car("Tesla","Black","20000") #here

print(car_1.brand)
print(car_1.colour)
print(car_1.price)

print(car_2.colour)

car_1.drive()
car_1.stop()


car_1.tyres = 4
print(car_1.tyres)  #changes value for car_1
print(car_2.tyres) #calls default value

Car.tyres = 1

print(car_1.tyres) #first local,then semi-global and global
print(car_2.tyres)