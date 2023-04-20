
class Person:
    def __init__(self, id, lastname, firstname, middlename, type) -> None:
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.type = type

    def __str__(self) -> str:
        return f'{self.type} - {self.id} {self.lastname}, {self.firstname} {self.middlename}'
    
    def getName(self):
        return f'{self.lastname}, {self.firstname} {self.middlename}'