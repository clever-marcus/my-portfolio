"""map() ==> applies a function to each item in an iterable(list, tuple, e.t.c)"""

#map(function, iterable)


store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_kshs = lambda data: (data[0], data[1]*100)

store_kshs = list(map(to_kshs, store))

for i in store_kshs:
    print(i)