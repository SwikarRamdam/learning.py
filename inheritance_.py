class Ramdam:
    surname = True

    def nationality(self):
        print("Nepali")
    def language(self):
        print("Nepali")
    
class Swikar(Ramdam):
    def relation1(self):
        print("I am the eldest son")
class Sonim(Ramdam):
    def relation(self):
        print("I am the younger one")

son1 = Swikar()
son2 = Sonim()

print(son1.surname)
son2.nationality()
son1.language()
son2.relation()