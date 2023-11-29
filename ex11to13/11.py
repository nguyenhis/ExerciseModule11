#1
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(self.name, end=" ")

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        super().print_information()
        print("(author: " + self.author + ", " + str(self.pages) + " pages)")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        super().print_information()
        print("(chief editor: " + self.editor + ")")

pubs = []
pubs.append(Magazine("Donald Duck", "Aki Hyyppä"))
pubs.append(Book("Compartment 6", "Rosa Liksom", 192))

for pub in pubs:
    pub.print_information()

#2
import random

class Car:
    def __init__(self, regPlate, maxSpeed):
        self.regPlate = regPlate
        self.maxSpeed = maxSpeed
        self.speed = 0
        self.odometer = 0

    def accelerate(self, acceleration):
        self.speed = min(max(self.speed + acceleration, 0), self.maxSpeed)

    def drive(self, time):
        self.odometer += self.speed * time

class ElectricCar(Car):
    def __init__(self, regPlate, maxSpeed, battery_capacity):
        super().__init__(regPlate, maxSpeed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, regPlate, maxSpeed, tank_volume):
        super().__init__(regPlate, maxSpeed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)

gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(20)
gasoline_car.accelerate(15)

for _ in range(3):
    electric_car.drive(1)
    gasoline_car.drive(1)

print(f"Electric Car Odometer: {electric_car.odometer} km")
print(f"Gasoline Car Odometer: {gasoline_car.odometer} km")
