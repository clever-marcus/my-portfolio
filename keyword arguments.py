#keyword arguments =>   they're arguments preceeded by an identifier when we pass them to a function
#                   => the order of the arguments doesn't matter, unlike positional arguments
#                   => Python knows the names of the arguments that our function receives

#positional arguments
def greetings(first,middle,last):
    print("good morning "+first+" "+middle+ " "+last)

#keyword arguments
greetings(last="developer", middle="smart", first="marcus")