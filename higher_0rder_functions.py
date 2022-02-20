# function that returns function
#accepts functions as arguments
def divisor(x):
    def dividend(y):
        return y/x
    return dividend
    
divide = divisor(12) #program starts here from divisor part which returns dividend 
print(divide(144)) # here dividend is assigned a value and thus printed
# def upper(text):
#     return text.upper()
# def lower(text):
#     return text.lower()
# def hello(func):
#     text = func("Swikar is a good human")#calling function within a function
#     print(text)

# hello(upper)
