class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber
obj = Student()
obj.setName("Shoyab")
obj.setRollNumber("313")
name = obj.getName()
rollNumber = obj.getRollNumber()
print("Name:", name)
print("Roll Number:", rollNumber)
