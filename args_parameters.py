# *args --> parameter that packs all arguments into tuple
# no multiple arguments are needed for multiple operands

def give_sum(*num):
    sum = 0
    num = list(num)
    num[2] = 5
    for i in num:
        sum = sum + i
    return sum
print(give_sum(1.4,2,3,4,4,5,6))
