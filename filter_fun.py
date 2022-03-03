#filter fun--> creates a collection of elements from iterable for which function returns



Twenty_Qualifiers = [("Nepal",4),
                    ("Canada",3), 
                    ("Oman",2)]

rate = lambda rate:(rate[1]>=3)

filtered = list(filter(rate, Twenty_Qualifiers))
for i in filtered:
    print(i)