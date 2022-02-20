
class boy:
    def handsome(self):
        print("boys are handsome")
class girl:
    def beautiful(self):
        print("girls are beautiful")

class Ram(boy):
    pass
class Sita(girl):
    pass
class House(boy,girl):
    pass

ram = Ram()
sita = Sita()
house = House()

house.beautiful()
house.handsome()
ram.handsome()
sita.beautiful()
# ram.beautiful()