"""List comprehension  => is a way to create a new list with less syntax
    it can mimic certain lambda functions, easier to read
    list = [expression (if/else) for item in iterable if conditional]"""

square = []                 #create an empty list
for i in range (1, 11):     #create a For Loop
    square.append(i * i)    #define what each loop iteration should do
#print(square)

square = [i * i for i in range(1, 11)]
print(square)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
#passed_students = list(filter(lambda x: x >= 60, students))

#passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "Failed!" for i in students ]

print(passed_students)


