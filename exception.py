try:
    result = 2/0
except ValueError:
    print("You can't divide any number by zero dear\n")
else:
    print(result)
finally:
    print("This will always execute")
# except ZeroDivisionError as e:
#     print("You can't divide any number by zero dear\n")
# except ZeroDivisionError as e:
#     print(e)
# except Exception:
#     print("something went wrong")