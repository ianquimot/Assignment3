
from person import Person

class Student(Person):
    def __init__(self, id, lastname, firstname, middlename, type, year, course, section) -> None:
        self.year = year
        self.course = course
        self.section = section

        Person.__init__(id, lastname, firstname, middlename, type)

    def __str__(self) -> str:
        return super().__str__()
    
    def getYrCourseSectionSec(self):
        return f'{self.year}/{self.course}/{self.section}'