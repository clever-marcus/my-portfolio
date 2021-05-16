#str.format() => is an optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

#print("the "+animal+ " jumped over the "+ item)
#print("The {} jumped over the {}". format(animal, item) )
#print("The {1} jumped over the {0}". format(animal, item) )   #positional argument
#print("The {animal} jumped over the {item}". format(animal="cow", item="moon") )   #keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal, item))

#name = "marcus"

#print("Good morning, {}".format(name))
#print("Good morning, {:5}. Nice to meet you".format(name))


number = 1000
print("the number pie is {:.2f}".format(number))    #this will display the number of digits after the decimal point
print("the number  is {:,}".format(number)) #this will add a comma to the digit
print("the number is {:b}".format(number))  #this will display a binary
print("the number is {:x}".format(number))  #this display the number in hexidecimal
print("the number pie is {:e}".format(number)) #this will display the number in scientific notation