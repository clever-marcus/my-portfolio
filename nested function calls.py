#nested functions calss => function calls inside other function calls
#                        => innermost function calls are resolved first
#                       => returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

"""we can rewrite the above code using nested functions containing less lines of code"""

print(round(abs(float(input("Enter a whole positive number: ")))))