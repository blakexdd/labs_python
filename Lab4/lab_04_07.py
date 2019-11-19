'''
 * FILE NAME: lab_04_07.py
 * PROGRAMMER: VG6
 * DATE: 29.10.2019
'''

#crating Row calss with id, collection and value
class Row:
    '''This class represents rows'''
    id = 0

    def __init__(self, collection, value):
        self.collection = collection
        self.value = value
        self.id = Row.id
        Row.id += 1

#creating Table class
class Table(Row):
    '''This class represents table'''
    rows = []

    def __init__(self, rowsNum):
        self.rowsNum = rowsNum

    def addRow(self, row):
        Table.rows += [((row.collection), row.value)]


    def setRow(self, row):
        if row.id <= self.rowsNum:
            Table.rows[row.id][0] = row.collection
            Table.rows[row.id][1] = row.value

    def getRow(self, rowId):
        return Table.rows[rowId]

    def display(self):
        print('id  x1  x2   f(x1, x2)')
        for i in range(self.rowsNum):
            print(i, ' ', self.getRow(i)[0][0], ' ', self.getRow(i)[0][0], ' |    ',
                  self.getRow(i)[1])

#creating LogicFunction class
class LogicFunction(Table):
    '''This class represents logicfunction'''

    def __init__(self, variablesNum, table):
        self.variablesNum = variablesNum
        self.table = table

    def getExpression(self):
        pass

    def getTable(self):
        pass

    def printTable(self):
        pass

#creating new table with 3 rows
newT = Table(3)
newT.addRow(Row([1, 2], 3))
newT.addRow(Row([4, 5], 6))
newT.addRow(Row([7, 8], 9))
newT.display()