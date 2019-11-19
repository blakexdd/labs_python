'''
 * FILE NAME: lab_04_03.py
 * PROGRAMMER: VG6
 * DATE: 29.10.2019
'''

import math

#creating geometric class
class Geometric:
    def calculateArea(self):
        print('Calculating area')

#creting square class
class Square(Geometric):
    def __init__(self, a):
        self.side = a
    def _perimeter(self):
        print('Perimeter of Square {}: {}\n'.format(\
            self.side, self.side * 4))
    def calculateArea(self):
        print('Area of Square {}: {}\n'.format(self.side,
                                               pow(self.side, 2)))

#creating object of Geometric class
geom = Geometric()
geom.calculateArea()

#creating object of Square class
sq = Square(5)
sq.calculateArea()
sq._perimeter()

#checking relationships between classes
print('Check subclass: ', issubclass(Square, Geometric))
print('Check instance sq->Square: ', isinstance(sq, Square))
print('Check instance sq->Geometric: ',
      isinstance(sq, Geometric))
print('Check instance sq->dict: ', isinstance(sq, dict))
print('Geometric.__bases__: ', Geometric.__bases__)
print('Square.__bases__: ', Square.__bases__)

#creating circle class
class Circle(Geometric):
    def __init__(self, radius):
        self.__radius = radius

    def calculateArea(self):
        print('Square of triangle: ',
              math.pi * pow(self.__radius, 2))

c = Circle(10)
c.calculateArea()

