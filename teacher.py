
from person import Person

class Teacher(Person):
    def __init__(self, id, lastname, firstname, middlename, type, department, position) -> None:
        self.department = department
        self.position = position

        Person().__init__(id, lastname, firstname, middlename, type)

    def __str__(self) -> str:
        return super().__str__()
    
    def getDepartment(self):
        return self.department
    
    def getPosition(self):
        return self.position