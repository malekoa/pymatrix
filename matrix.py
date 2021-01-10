import random
import datetime

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
        return self.add_matrix(otherMatrix)

    def __sub__(self, otherMatrix):
        return self.subtract_matrix(otherMatrix)

    def __mul__(self, otherMatrix):
        return self.multiply_matrix(otherMatrix)

    # returns true if same size, false otherwise
    def is_same_size(self, otherMatrix):
        if self.rows == otherMatrix.rows and self.columns == otherMatrix.columns:
            return True
        return False

    # prints the matrix instance to the console
    def show_self(self):
        for row in self.matrix:
            print row

    # returns a tuple that contains the size of the matrix instance (rows, columns)
    def get_size(self):
        return (self.rows, self.columns)

    ### REMEMBER TO CHANGE BACK TO 0!!!!!!!!

    # sets all entries in a matrix instance to a random int between 0 and 9
    def randomize(self):
        for row in range(self.rows):
            for entry in range(self.columns):
                self.matrix[row][entry] = random.randint(0, 9)

    # returns a matrix instance that is the transpose of the given matrix
    def transpose(self):
        # get all columns in matrix
        columns = []
        for col in range(self.columns):
            columns.append(self.getColumn(col))

        # transposed matrix has rows and columns switched
        transposed_matrix = Matrix(self.columns, self.rows)
        # loop through rows in transposed_matrix and place the columns in
        transposed_matrix.matrix = columns
        #transposed_matrix.show_self()

        return transposed_matrix

    # returns the specified column of a matrix
    def getColumn(self, col):
        column = []
        for row in self.matrix:
            column.append(row[col])

        return column

    # returns a matrix instance that is the sum of two matrix instances
    def add_matrix(self, otherMatrix):
        if(self.is_same_size(otherMatrix) == False):
            raise Exception("Matrices must be of the same size for addition.")

        resultMatrix = Matrix(self.rows, self.columns)

        for row in range(resultMatrix.rows):
            for col in range(resultMatrix.columns):
                resultMatrix.matrix[row][col] = self.matrix[row][col] + otherMatrix.matrix[row][col]

        return resultMatrix

    # returns a matrix instance that is the difference of two matrix instances
    def subtract_matrix(self, otherMatrix):
        if(self.is_same_size(otherMatrix) == False):
            raise Exception("Matrices must be of the same size for subtraction.")

        resultMatrix = Matrix(self.rows, self.columns)

        for row in range(resultMatrix.rows):
            for col in range(resultMatrix.columns):
                resultMatrix.matrix[row][col] = self.matrix[row][col] - otherMatrix.matrix[row][col]

        return resultMatrix

    # returns a matrix instance that is a scaled to a scalar
    def scale(self, scalar):
        scaled_matrix = Matrix(self.rows, self.columns)

        for row in range(self.rows):
            for col in range(self.columns):
                scaled_matrix.matrix[row][col] = self.matrix[row][col] * scalar

        return scaled_matrix

    # sets a specific entry in a matrix instance to new_entry. takes a tuple for
    # entry_position
    def set_entry(self, entry_position, new_entry):
        row, col = entry_position
        self.matrix[row][col] = new_entry

    def get_entry(self, entry_position):
        row, column = entry_position
        return self.matrix[row][column]

    # returns a matrix instance that is the product of two matrices
    def multiply_matrix(self, otherMatrix):
        resultMatrix = Matrix(self.rows, otherMatrix.columns)

        for row in range(self.rows):
            for col in range(otherMatrix.columns):
                sum = 0
                for entry in range(len(self.matrix[row])):
                    product = self.matrix[row][entry] * otherMatrix.getColumn(col)[entry]
                    sum += product

                resultMatrix.set_entry((row, col), sum)

        return resultMatrix

    # switches the positions of row1 and row2 in a matrix instance
    def switch_row(self, row1, row2):
        r1 = self.matrix[row1]
        r2 = self.matrix[row2]
        self.matrix[row1] = r2
        self.matrix[row2] = r1


    def fetch_minor_matrix(self, position):
        r, c = position
        values = []

        # get values from self.matrix that aren't in the row or column given in position
        for row in range(self.rows):
            for col in range(self.columns):
                if row != r and col != c:
                    values.append(self.matrix[row][col])

        # create minor matrix and fill with values
        minor = Matrix(self.rows - 1, self.columns - 1)
        pos = 0
        for row in range(minor.rows):
            for col in range(minor.columns):
                minor.matrix[row][col] = values[pos]
                pos += 1

        return minor.determinant()


    # returns the determinant of the matrix instance
    def determinant(self):
        rows, cols = self.get_size()
        if rows == 2 and rows == cols:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

        result = 0
        if rows >= 3 and rows == cols:
            for row in range(self.rows):
                det = self.fetch_minor_matrix((row, 0))
                if row % 2 == 0:
                    result += self.matrix[row][0] * det
                else:
                    result += -1 * (self.matrix[row][0] * det)

        return result

### TG

m1 = Matrix(5, 5)
m1.randomize()

m1.show_self()
print "\n---\n"
start = datetime.datetime.now()
det = m1.determinant()
end = datetime.datetime.now()
time = end - start
print "determinant: " + str(det)
print "time elapsed (ms): " + str(time.total_seconds() * 1000)
