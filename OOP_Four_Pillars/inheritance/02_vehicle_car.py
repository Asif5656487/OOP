class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} vehicle started"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def description(self):
        return f"{self.brand} car has {self.doors} doors"

car = Car("Toyota", 4)
print(car.start())
print(car.description())
