import random

class Vehicle:
    def __init__(self, name, speed=100, reliability=8, distance=1000):
        self.name = name
        self.speed = speed
        self.reliability = reliability
        self.distance = distance

    def move(self):
        self.distance -= self.speed
        print(self.name, self.distance)

    def breakdown(self):
        r = random.randint(1,10)
        if r < self.reliability:
            self.move()
        else:
            print(self.name, " broke down!")

    def check_distance(self):
        if(self.distance > 0):
            return True

    def __str__(self):
        return f'{self.name} {self.speed} {self.reliability}'

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
  

class Motorcycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.speed += 5
        self.reliability -=1 


class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.reliability -= 2
        self.speed += 10


def race(v1, v2, v3):
    while (v1.check_distance() and v2.check_distance() and v3.check_distance()):
        v1.breakdown()
        v2.breakdown()
        v3.breakdown()
        print("\n")
        if not (v1.check_distance()):
            print(v1.name, " wins!")
            break
        elif not v2.check_distance():
            print(v2.name, " wins!")
            break
        elif not v3.check_distance():
            print(v3.name, " wins!")
            break


car = Car("car")
moto = Motorcycle("motorcycle")
truck = Truck("truck")
race(car, moto, truck)
