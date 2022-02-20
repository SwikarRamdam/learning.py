# to access parent members
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__(self , length,width,height):
        super().__init__(length, width)      
        self.height = height
    def volume(self):
        return self.length * self.height * self.width


sq = Square(3, 3)
cu = Cube(3, 3, 3)

print(sq.area())
print(cu.volume())