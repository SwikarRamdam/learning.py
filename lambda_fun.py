#one line function (like inline function of cpp)
#only one expression is allowed


# def double(x):
#     return x*2
# print(double(30))

# doubler = lambda x : x*2 
# print(doubler(45))

# doubler = lambda x,y: x*y
# print(doubler(3,4))

full_name = lambda first_name, mid_name, last_name : first_name+ " "+ mid_name +" "+ last_name
print(full_name("Prem","Bahadur","Bishwakarma"))

age_check = lambda age: True if age>=18 else False
print(age_check(20))