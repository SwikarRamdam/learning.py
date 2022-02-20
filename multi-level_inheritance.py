class Humans:
    alive = True
class good(Humans):
    def nature(self):
        print("They have good nature")
    
class happy(good):
    def mood(self):
        print("They have good mood")

swikar = happy()

swikar.nature()
swikar.mood()