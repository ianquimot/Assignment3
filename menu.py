from grade import Grade
from teacher import Teacher
from load import Load
# from person import Person

students = []
teachers = []

def addStudents():
    while True:
        print()
        print('Enter Student Information')
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        course = input('Enter Course: ')
        year = input('Enter year: ')
        section = input('Enter section: ')
        print('----------------------------')
        filipino = input('Grade Filipino: ')
        math = input('Grade Math: ')
        science = input('Grade Science: ')
        english = input('Grade English: ')

        stud = Grade(filipino, math, science, english)
        stud.id = id
        stud.lastname = lastName
        stud.firstname = firstName
        stud.middlename = middleName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()

def addTeacher():
    while True:
        print()
        print('Enter Teacher Information')
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        department = input('Enter department: ')
        position = input('Enter position: ')
        print('----------------------------')
        subject = input('Enter subject: ')

        teach = Load(subject)
        teach.id = id
        teach.lastname = lastName
        teach.firstname = firstName
        teach.middlename = middleName
        teach.type = type
        teach.department = department
        teach.position = position

        teachers.append(teach)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()

def deleteStudent():
    i = int(input('Enter Index: '))
    students.pop(i)
    print(f'Index {i} been deleted sucessfully!')

    menu()

def deleteTeacher():
    i = int(input('Enter Index: '))
    teachers.pop(i)
    print(f'Index {i} been deleted sucessfully!')

    menu()

def deleteAll():
    students.clear()
    teachers.clear()
    print('All records has been deleted!')

    menu()

def searchStudent():
    i = int(input('Enter Index: '))
    print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCourseSectionSec()} \t | {students[i].getAverage()}')

    menu()

def searchTeacher():
    i = int(input('Enter Index: '))
    print(f'{i} \t {teachers[i].getName()} \t | {teachers[i].getDepartment()} \t | {teachers[i].getPosition()}')

    menu()

def displayStudent():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSectionSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def displayTeacher():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def displayAll():
    print()
    print('List of Students')
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSectionSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    print()
    print('List of Teachers')
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')


    menu()

def menu():
    print()
    print()
    print(':: Menu ::')
    print('D - Delete Student       S - Search Student')
    print('A - Add Student          M - Display Student')
    print('F - Add Teacher          N - Display Teacher')
    print('G - Delete Teacher       X - Display All')
    print('C - Search Teacher       Z - Delete All')
    print()

    c = input('Enter a Function: ')
    choice = c.upper()

    if (choice == 'D'):
        deleteStudent()
    elif (choice == 'S'):
        searchStudent()
    elif (choice == 'A'):
        addStudents()
    elif (choice == 'M'):
        displayStudent()
    elif (choice == 'F'):
        addTeacher()
    elif (choice == 'N'):
        displayTeacher()
    elif (choice == 'G'):
        deleteTeacher()
    elif (choice == 'X'):
        displayAll()
    elif (choice == 'C'):
        searchTeacher()
    elif (choice == 'Z'):
        deleteAll()
    else:
        print('Unknown Input, Please try again')

    print()


menu()