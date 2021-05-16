#filter() => creates a collection of elements from an iterable for which a function returns true

#filter(function, iterable)

friends = [("Dan", 21),
           ("Pato", 25),
           ("Zena", 19),
           ("jared", 23),
           ("Josie", 20),
           ("Betty", 19),
           ("Doti", 17),
           ("Najma", 17),
           ("Moraa", 15)]

age = lambda data:data[1] >= 18

allowed_drinking_friends = list(filter(age, friends))

for i in allowed_drinking_friends:
    print(i)