class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow"

animals = [Dog("Buddy"), Cat("Misty")]
for animal in animals:
    print(animal.name, animal.speak())
