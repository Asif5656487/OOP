class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"I am {self.name}, age {self.age}"

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def introduce(self):
        return f"{super().introduce()}, roll {self.roll_number}"

student = Student("Abdullah", 21, "CS-07")
print(student.introduce())
