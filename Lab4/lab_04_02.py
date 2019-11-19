'''
 * FILE NAME: lab_04_02.py
 * PROGRAMMER: VG6
 * DATE: 29.10.2019
'''

class Worker:
    '''doc class Worker'''
    count = 0

    #initialing dander method init
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    #initializing display function
    def display(self):
        print('Worker:')
        print('{} {}',format(self.name, self.surname))

#doint something with our new class
w1 = Worker('Ivan', "Ivanov")
print('w1.count: ', w1.count)
w2 = Worker('Alexei', 'Petrov')
print('w2 count: ', w2.count)
print('w1 count: ', w1.count)
print('Worker.count: {0}\n'.format(Worker.count))
print('Worker.__name__: ', Worker.__name__)
print('Worker.__dict__: ', Worker.__dict__)
print('Worker.__doc__: ', Worker.__doc__)
print('Worker.__bases__: ', Worker.__bases__)

#ex7 creating new class
class Animal:
    '''This is an anminal class'''
    count = 0

    #initialing dander method init
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = Animal.count
        Animal.count += 1

    #initializing display function
    def display(self):
        print('Animal id: ', self.id)
        print('Name: ', self.name)
        print('Age: ', self.age)

#creatin animals
dog = Animal('Akiro', 2)
cat = Animal('Pushok', 3)
rabbit = Animal('Push', 5)

#printing info about animals
#id variable common for all aniaml
#so as we create new animal, id of all
#animals incrising by 1. We have got 3
#animals, so id = 3 after all
dog.display()
cat.display()
rabbit.display()

