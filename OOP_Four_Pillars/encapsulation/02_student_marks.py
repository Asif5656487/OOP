class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Marks must be from 0 to 100")
        self.__marks = value

student = Student("Abdullah")
student.marks = 87
print(student.name, student.marks)
