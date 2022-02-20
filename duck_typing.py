class Duck:
     def walk(self):
         print("Duck is walking")
class Chicken:
     def walk(self):
         print("Chicken is walking")
class Person:
    def catch(self,duck):
        duck.walk()
        # chicken.walk()
        # print("Person is walking")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken) #duck and chicken are just the parameters
person.catch(duck) #duck and chicken are just the parameters

# same function names like walk. Both chicken and duck can walk so this method is just trying to teach that if two classes have similar properties any of the one can be used in the absence of the other. 
#if it walks like a duck, quacks like a duck then it must be a duck

