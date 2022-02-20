from abc import ABC, abstractmethod
class Smartphones:
    @abstractmethod
    def android(self):
        print("I am android")
    @abstractmethod 
    def ios(self):
        print("I am ios")

class Samsung(Smartphones):
    pass
class Apple(Smartphones):
    pass

sam = Samsung()
app = Apple()

sam.android()
app.ios()

#hasn't worked