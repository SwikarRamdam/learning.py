# module --> file containing python codes

# import for_module_test 
# for_module_test.hello()
# for_module_test.bye()

# import for_module_test as test
# test.hello()
# test.bye()

# from for_module_test import hello, bye
# hello()
# bye()

from for_module_test import * #imports everything, suitable for small programs

help("modules")

print("My name is",end=" ") #use end to print in the same line
print("Swikar Ramdam")

print("My name is") #prints in two different line
print("Swikar Ramdam")