class Thermostat:
    def __init__(self, celsius):
        self.__celsius = 0
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self.__celsius = value

    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

room = Thermostat(25)
room.celsius = 30
print(room.celsius, room.fahrenheit())
