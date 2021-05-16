class Animal:
    alive = True

    def eat(self):
        print("The animal eats")

    def sleep(self):
        print("The animal sleeps")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This Fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This Hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()