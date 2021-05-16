#if statements => is a block of code that will execute if its condition is true

age = int(input("How old are you? "))
if age == 100:
    print("You're a very old human being!")
elif age >= 18:
    print("You're are an Adult!")
elif age < 0 :
    print("You haven't been born yet!")
else:
    print("You're a child!")