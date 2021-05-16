class Car:
    color = None

class motorbikes:
    color = None

def change_color(Imports, color):
     Imports.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = motorbikes()
bike_2 = motorbikes()
bike_3 = motorbikes()

change_color(car_1, "black")
change_color(car_2, "red")
change_color(car_3, "blue")

change_color(bike_1, "silver")
change_color(bike_2, "green")
change_color(bike_3, "white")


print(car_1.color)
print(car_2.color)
print(car_3.color+ "\n")

print(bike_1.color)
print(bike_2.color)
print(bike_3.color)
