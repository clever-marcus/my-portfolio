# **kwargs = > is a parameter that will pack all arguments into a dictionary
#           = > it is useful so that a function can accept a varying amount of keyword arguments

def greetings(**myNames):
    #print("Hello "+ kwargs['first']+ " "+ kwargs['last'])
    print("hey ", end=" ")
    for key,value in myNames.items():
        print(value, end=" ")
greetings(title='Mr.', first='marcus', middle='smart', last='developer')