import random

class Matrix:

    def __init__(self, rows = 1, columns = 1, type = "zero"):
        if rows < 1 or columns < 1 :
            raise Exception("Rows and columns must be greater than 0.")
        if type == "identity" and rows != columns:
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
        if type == "identity" and rows == columns:
            for row in range(rows):
                for col in range(columns):
                    if row == col:
                        self.matrix[row][col] = 1
            else:
                return None

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



### DO STUFF

# matrix1 = Matrix(3, 3)
# matrix1.randomize()
#
# asdf = Matrix(3, 3)
# asdf.randomize()
#
# matrix1.add_matrix(asdf)

m1 = Matrix(2, 2)
m1.randomize()

m2 = Matrix(3, 2)
m2.randomize()

m1.add_matrix(m2)
