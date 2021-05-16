# ******************************************
#if __name__ == '__main__'
# *****************************************

# 1. module can be run as a standalone program
# 2. module can be imported and used by other modules


# Python interpreter sets "special variables", one of which is __name__
#then python can be imported and used by other modules
#Python will assign the __name__ variable a value of '__main__' if it's
#the initial module being run


def greeting():
    print("Hi there!")

if __name__ == '__main__':
    greeting()


