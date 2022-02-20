# strformat
name = "Swikar"
surname = "Ramdam"
print("My name is {2} {0} from {1}".format(name,surname,"Dharan"))

# adding padding

name = "Swikar"
surname = "Ramdam"
print("My name is {} {} from Dh....{:>10}".format(name,surname,"Dharan"))

# number format
num = 1000

print("The number is {}".format(num))
print("The number is {:.3f}".format(num))
print("The number is {:,}".format(num)) #coolest
print("The number is {:b}".format(num)) #useful
print("The number is {:X}".format(num)) #useful
print("The number is {:x}".format(num)) #useful
print("The number is {:e}".format(num)) #useful
print("The number is {:E}".format(num)) #useful