import random

class Matrix:

    def __init__(self, rows = 1, columns = 1):
        # Set amount of rows and columns
        self.matrix = []
        self.rows = rows
        self.columns = columns
        # Create rows
        for i in range(rows):
            self.matrix.append([])
        # Fill rows with 0s
        for i in self.matrix:
            for ii in range(columns):
                i.append(0)

    def showSelf(self):
        for row in self.matrix:
            print row

    def getSize(self):
        return (self.rows, self.columns)

    def randomize(self):
        #print random.randint(0, 9)
        for row in range(self.rows):
            for entry in range(self.columns):
                self.matrix[row][entry] = random.randint(0, 9)

    def addMatrix(self, otherMatrix):
        print "Adding"
        self.showSelf()
        print "and"
        otherMatrix.showSelf()
        print "Result = "
        resultMatrix = Matrix(self.rows, self.columns)

        for row in range(resultMatrix.rows):
            for col in range(resultMatrix.columns):
                resultMatrix.matrix[row][col] = self.matrix[row][col] + otherMatrix.matrix[row][col]

        resultMatrix.showSelf()


### DO STUFF

matrix1 = Matrix(3, 3)
matrix1.randomize()

asdf = Matrix(3, 3)
asdf.randomize()

# print "Matrix 1: "
# matrix1.showSelf()
# print "\nMatrix 2:"
# asdf.showSelf()

matrix1.addMatrix(asdf)
