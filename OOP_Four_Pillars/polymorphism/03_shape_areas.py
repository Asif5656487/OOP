from math import pi

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

for shape in [Rectangle(3, 4), Circle(2)]:
    print(type(shape).__name__, round(shape.area(), 2))
