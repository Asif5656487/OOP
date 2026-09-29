from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def fare(self, distance):
        pass

class Bus(Transport):
    def fare(self, distance):
        return distance * 10

class Taxi(Transport):
    def fare(self, distance):
        return 100 + distance * 25

for transport in [Bus(), Taxi()]:
    print(type(transport).__name__, transport.fare(5))
