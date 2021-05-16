#Logical operators (AND, OR) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

if not(temp >=0 and temp <=30):
    print("the temperature is bad today")
    print("Please stay at home!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today")
    print("Go outside!")