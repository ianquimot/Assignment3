from teacher import Teacher

class Load(Teacher):
    def __init__(self, subjects) -> None:
        self.subject = subjects

    def getSubjects(self):
        return self.subject

