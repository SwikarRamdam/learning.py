#map()--> applies a functions to each of the iterables (list, tuples, etc)
# map(function, iterables)

Twenty_Qualifiers = [("Nepal",4),
                            ("Canada",3), 
                            ("Oman",2)  ]
ranking = lambda rank: (rank[0],rank[1]*2)

holder = list(map(ranking,Twenty_Qualifiers)) #casting into list and storing in a holder
for i in holder:
    print(i)