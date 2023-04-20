from teacher import Teacher
from student import Student
from grade import Grade

print()

grade1 = Grade(90, 89, 95, 87)
grade1.id = '21-41097'
grade1.lastname = 'Quimot'
grade1.firstname = 'Ian'
grade1.middlename = 'Cadangin'
grade1.course = 'BSCS'
grade1.year = 2
grade1.section = 'A'

print(grade1.getName())
print(grade1.getYrCourseSectionSec())
print(grade1.getAverage())