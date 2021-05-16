#Prevents a user from creating an object of that class
# it compiles a user to override abstract methods in a child class

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod


class vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(vehicle):
    def go(self):
        print("you drive the car")

    def stop(self):
        print("the car stopped")

class motorbike(vehicle):
    def go(self):
        print("you ride the motorbike")

    def stop(self):
        print("the motorbike stopped")

#vehicle = vehicle()
car = Car()
motorbike = motorbike()


#vehicle.go()
car.go()
motorbike.go()

car.stop()
motorbike.stop()