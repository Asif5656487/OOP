from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

class FullTimeWorker(Worker):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

class PartTimeWorker(Worker):
    def __init__(self, hours, hourly_rate):
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours * self.hourly_rate

for worker in [FullTimeWorker(50000), PartTimeWorker(40, 500)]:
    print(type(worker).__name__, worker.calculate_pay())
