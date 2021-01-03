class Matrix:

    matrix = []
    rows = 0
    columns = 0

    def __init__(self, rows = 1, columns = 1):
        # Set amount of rows and columns
        self.rows = rows
        self.columns = columns
        # Create rows
        for i in range(rows):
            self.matrix.append([])
        # Fill rows with 0s
        for i in self.matrix:
            for ii in range(columns):
                i.append(0)

    def getSize(self):
        return (self.rows, self.columns)

    def showSelf(self):
        for i in self.matrix:
            print i

    def addRows(self, amount = 1):
        for i in range(amount):
            self.matrix.append([])

    def addEntry(self, row, column, value):
        self.matrix[row][column] = value


### DO STUFF

matrix1 = Matrix(4, 4)

matrix1.addEntry(1, 1, 2)

matrix1.showSelf()
