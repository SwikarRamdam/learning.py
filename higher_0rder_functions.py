# function as arguments
def upper(text):
    return text.upper()
def lower(text):
    return text.lower()
def hello(func):
    text = func("Swikar is a good human")#calling function within a function
    print(text)

hello(upper)