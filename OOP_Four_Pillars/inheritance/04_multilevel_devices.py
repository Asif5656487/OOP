class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        return f"{self.brand} is on"

class Computer(Device):
    def __init__(self, brand, ram):
        super().__init__(brand)
        self.ram = ram

class Laptop(Computer):
    def details(self):
        return f"{self.brand} laptop, {self.ram} GB RAM"

laptop = Laptop("Dell", 16)
print(laptop.power_on())
print(laptop.details())
