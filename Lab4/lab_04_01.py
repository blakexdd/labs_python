'''
 * FILE NAME: lab_04_01.py
 * PROGRAMMER: VG6
 * DATE: 29.10.2019
'''

#importing time module
import time

#initializing ticket class
class Ticket:
    #initializing dander method init
    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    #initializing dander method del
    def __del__(self):
        print('Delete ticket: ', time.asctime(self.createDate))

    #initializing display function
    def display(self):
        print('Ticket:')
        print(' createDate: ', time.asctime(self.createDate))
        print(' owner: ', self.owner)
        print(' deadline: ', time.asctime(self.deadline))

#creating ticket object
ticket1 = Ticket(time.localtime(), 'Ivan Ivanov', \
                 time.strptime('17.12.2017', '%d.%m.%Y'))

#display ticket1 info
ticket1.display()

#get atribute value
print('Owner: ', ticket1.owner)
print('Owner(getattr): ', getattr(ticket1, 'owner'))

#check for atribute
print('hasattr: ', hasattr(ticket1, 'owner'))

#setting atribute value
setattr(ticket1, 'owner', 'Alexei Petrov')
print('Owner(setattr): ', ticket1.owner)

#deleting atribute of ticket
delattr(ticket1, 'owner')
#we are trying to print item we've alreay deleted,
#so this ticket has no attribute owner anymore
#print('delattr: ', ticket1.owner)

#deleting object
del ticket1
#we are trying to print object we'va alrady deleted,
#so wo don't have this object anymore. That's why
#python doesn't see it and raises error
#print(ticket1)

#ex4 creating current time variable
ltime = time.localtime()
print('current time: ', time.strftime('%d %b %Y %H:%M:%S', ltime))

#ex5 creating current time from string
stime = time.strptime('17.07.2017 10:53:00', '%d.%m.%Y %H:%M:%S')
print('some time from ex in normal form: ', time.asctime(stime))
