#  higher order function => a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                               (In python, functions are also treated as objects)

"""def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def curse(say):
    text = say("Fuck me!")
    print(text)

curse(loud)"""

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(80))