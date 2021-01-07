import random

class Matrix:

    def __init__(self, rows = 1, columns = 1, matrixType = "zero"):
        if rows < 1 or columns < 1 :
            raise Exception("Rows and columns must be greater than 0.")
        if matrixType == "identity" and rows != columns:
            raise Exception("Identity matrices must be square.")
        # Set amount of rows and columns
        self.matrix = []
        self.rows = rows
        self.columns = columns
        # Create rows
        for i in range(rows):
            self.matrix.append([])

        # Makes zero matrix
        for i in self.matrix:
            for ii in range(columns):
                i.append(0)

        # Makes identity matrix
        if matrixType == "identity" and rows == columns:
            for row in range(rows):
                for col in range(columns):
                    if row == col:
                        self.matrix[row][col] = 1
            else:
                return None

    def __add__(self, otherMatrix):
        self.add_matrix(otherMatrix)

    def __sub__(self, otherMatrix):
        self.subtract_matrix(otherMatrix)

    # returns true if same size, false otherwise
    def is_same_size(self, otherMatrix):
        if self.rows == otherMatrix.rows and self.columns == otherMatrix.columns:
            return True
        return False

    def show_self(self):
        for row in self.matrix:
            print row

    def get_size(self):
        return (self.rows, self.columns)

    def randomize(self):
        for row in range(self.rows):
            for entry in range(self.columns):
                self.matrix[row][entry] = random.randint(0, 9)

    def transpose(self):
        self.show_self()
        print ""

        # get all columns in matrix
        columns = []
        for col in range(self.columns):
            columns.append(self.getColumn(col))

        # create matrix with columns and rows switched to hold the transpose
        transposed_matrix = Matrix(self.columns, self.rows)

        # loop through rows in transposed_matrix and place the columns in
        transposed_matrix.matrix = columns

        transposed_matrix.show_self()

        return transposed_matrix

    # pass a matrix and the column you wish to get
    def getColumn(self, col):
        #self.show_self()

        column = []
        for row in self.matrix:
            column.append(row[col])

        return column
        #print column

    def add_matrix(self, otherMatrix):
        # if matrices aren't the same size
        if(self.is_same_size(otherMatrix) == False):
            raise Exception("Matrices must be of the same size for addition.")

        self.show_self()
        print "+"
        otherMatrix.show_self()
        print "="
        resultMatrix = Matrix(self.rows, self.columns)

        for row in range(resultMatrix.rows):
            for col in range(resultMatrix.columns):
                resultMatrix.matrix[row][col] = self.matrix[row][col] + otherMatrix.matrix[row][col]

        resultMatrix.show_self()

    def subtract_matrix(self, otherMatrix):
        # if matrices aren't the same size
        if(self.is_same_size(otherMatrix) == False):
            raise Exception("Matrices must be of the same size for subtraction.")

        self.show_self()
        print "-"
        otherMatrix.show_self()
        print "="
        resultMatrix = Matrix(self.rows, self.columns)

        for row in range(resultMatrix.rows):
            for col in range(resultMatrix.columns):
                resultMatrix.matrix[row][col] = self.matrix[row][col] - otherMatrix.matrix[row][col]

        resultMatrix.show_self()

    def scale(self, scalar):
        self.show_self()
        print "*"
        print scalar
        print "="
        scaled_matrix = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for col in range(self.columns):
                scaled_matrix.matrix[row][col] = self.matrix[row][col] * scalar
        scaled_matrix.show_self()
        return scaled_matrix


### DO STUFF

matrix = Matrix(2, 2)
matrix.randomize()
matrix.scale(1.0/3.0)
