# := --> assigns values to the variables as a part of larger expression

Happy = True
print(Happy)

# print(Happy = True)
print(Happy := True) #walrus operator

foods= list()
while food := input("Are you fed up ?(y/n)") != "quit":
    foods.append(food)
