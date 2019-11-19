'''
 * FILE NAME: lab_04_05.py
 * PROGRAMMER: VG6
 * DATE: 29.10.2019
'''

#creating class Person with his name, surname
#age and method display
class Person:
    '''This class represents info about unique person'''

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print('Name: ', self.firstname)
        print('Surname: ', self.lastname)
        print('Age: ', self.age)

#creating student class as an inherited class from class Person
class Student(Person):
    '''This class represents info about student'''
    studentID = 0

    def __init__(self, firstname, lastname, age, recordBook):
        Person.__init__(self, firstname, lastname, age)
        self.studentID = Student.studentID
        self.recordBook = recordBook
        Student.studentID += 1

    def display(self):
        Person.display(self)
        print("Student's id: ", self.studentID)
        print("Amount 5 marks: ", self.recordBook)

#creating Professor class with his degree and prefessorID
class Professor(Person):
    '''This class represents info about professor'''
    professorID = 0

    def __init__(self, firstname, lastname, age, degree):
        Person.__init__(self, firstname, lastname, age)
        self.professorID = Professor.professorID
        self.degree = degree
        Professor.professorID += 1

    def display(self):
        Person.display(self)
        print("Professor's id: ", self.professorID)
        print("Professor's degree: ", self.degree)

#creating 3 students and 3 professors
firsts = Student('Vladimir', 'Gololobov', 18, 6)
seconds = Student('Imshennik', 'Michael', 18, 8)
firds = Student('Alyona', 'Rychalina', 18, 7)
firstp = Professor('Andreev', 'Vitaliy', 47, 'best')
secondp = Professor('Ivanov', 'Gleb', 50, 'good')
firdp = Professor('Petrov', 'Ivan', 65, 'very good')

#displaying students and professors info
firsts.display()
print('=========')
seconds.display()
print('=========')
firds.display()
print('=========')
firstp.display()
print('=========')
secondp.display()
print('=========')
firdp.display()



