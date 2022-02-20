class Shirt:
    pass
#     colour = None
def assign_colour(object,colour):
    object.colour = colour
    
shirt_1 = Shirt()
shirt_2 = Shirt()
shirt_3 = Shirt()

assign_colour(shirt_1,"black")#the colours are assigned here
assign_colour(shirt_2,"blue")
assign_colour(shirt_3,"red")

print(shirt_1.colour) #4th row is printed here - simple
print(shirt_2.colour)
print(shirt_3.colour)