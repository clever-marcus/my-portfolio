"""lambda function => function written in 1 line using lambda keyword
    accepts any number of arguments, but only has one expression
    (think of it as a shortcut)
    (useful if needed for a short period of time, throw-away)"""

#syntax
#lambda parameters: expression

#def double(x):
 #   return x * 2

#print(double(8))

double = lambda x: x * 2
print(double(9))

"""for double parameters"""
multiply = lambda x, y: x * y
print(multiply(6, 8))

add = lambda x, y, z: x + y + z
print(add(4, 5, 10))

names = lambda first_name, last_name: first_name + " " + last_name
print(names("marcus", "ogutu"))

age_check = lambda age:True if age >= 18 else False
print(age_check(21))