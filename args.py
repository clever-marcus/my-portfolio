# *args ==> is a parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments

def add(*addition):
    sum = 0
    addition = list(addition)
    addition[1] = 10
    for i in addition:
        sum += i
    return sum

print(add(1, 7, 8, 8,66, 76))