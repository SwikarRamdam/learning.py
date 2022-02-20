class Nepal:

    def city(self):
        print("Dharan is a beautiful city")

class Pokhara(Nepal):

    def city(self):
        print("Pokhara is also a beaitiful city")

place = Pokhara()
place.city()