class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        return f"{self.name}: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def details(self):
        return f"{super().details()}, {self.department}"

manager = Manager("Ayesha", 80000, "IT")
print(manager.details())
