#works for lists only

# friends = ["Pawan", "Basanta", "Sudip", "DKC"]
# friends.sort()
# sorted_list = sorted(friends,reverse= True)
# print(sorted_list)

# # for i in friends:
# #     print(i)
# for i in sorted_list:
#     print(i)

friends = [("Pawan","A",1), 
             ("Basanta","C",3),
              ("Sudip", "B",2)]
alpha = lambda alphabets: alphabets[2]
# num = lambda number: number[3]
# friends.sort(key=num)#numbers cannot be assigned directly so a lambda function is used
friends_sort = sorted(friends,key=alpha)
# for i in friends:
#     print(i)
for i in friends_sort:
    print(i)