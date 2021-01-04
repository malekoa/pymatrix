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

    def show_self(self):
        for row in self.matrix:
            print row

    def get_size(self):
        return (self.rows, self.columns)

    def randomize(self):
        for row in range(self.rows):
            for entry in range(self.columns):
                self.matrix[row][entry] = random.randint(0, 9)

    def add_matrix(self, otherMatrix):
        print "Adding"
        self.show_self()
        print "and"
        otherMatrix.show_self()
        print "Result = "
        resultMatrix = Matrix(self.rows, self.columns)

        for row in range(resultMatrix.rows):
            for col in range(resultMatrix.columns):
                resultMatrix.matrix[row][col] = self.matrix[row][col] + otherMatrix.matrix[row][col]

        resultMatrix.show_self()


### DO STUFF

matrix1 = Matrix(3, 3)
matrix1.randomize()

asdf = Matrix(3, 3)
asdf.randomize()

matrix1.add_matrix(asdf)
