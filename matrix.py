import random
import datetime
from fractions import Fraction as frac

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
        strmat = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for col in range(self.columns):
                strmat.matrix[row][col] = str(self.matrix[row][col])
        for row in strmat.matrix:
            print(row)


    # returns a tuple that contains the size of the matrix instance (rows, columns)
    def get_size(self):
        return (self.rows, self.columns)

    ### REMEMBER TO CHANGE BACK TO 0!!!!!!!!

    # sets all entries in a matrix instance to a random int between 0 and 9
    def randomize(self):
        for row in range(self.rows):
            for entry in range(self.columns):
                self.matrix[row][entry] = random.randint(1, 9)

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


    # Takes a tuple (rows, columns) for position. Returns the determinant of
    # the minor matrix of a position
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

    # returns the adjugate matrix
    def get_adjoint_matrix(self):
        t1 = self
        # put determinant of all of t1's minor matrices in adj
        adj = Matrix(self.rows, self.columns)
        for row in range(m1.rows):
            for col in range(m1.columns):
                # if both row and col are even, number is unmodified before input
                if row % 2 == 0 and col % 2 == 0:
                    adj.matrix[row][col] = m1.fetch_minor_matrix((row, col))
                # if both row and col are odd, number is unmodified before input
                elif row % 2 != 0 and col % 2 != 0:
                    adj.matrix[row][col] = m1.fetch_minor_matrix((row, col))
                # if row and col aren't both even or odd, number is multiplied by -1 before input
                else:
                    adj.matrix[row][col] = m1.fetch_minor_matrix((row, col)) * -1

        adj = adj.transpose()

        return adj

    # returns the inverse of a matrix. Returns false if there is no inverse
    def inverse(self):
        adj = self.get_adjoint_matrix()
        det = self.determinant()
        if det != 0:
            if adj.get_size() != (2, 2):
                scalar = frac(1, det)
                # convert all numbers in adj to fractions
                for row in range(adj.rows):
                    for col in range(adj.columns):
                        adj.matrix[row][col] = frac(adj.matrix[row][col])
                # scale adj to scalar
                inv = adj.scale(scalar)
                return inv
            else:
                scalar = frac(1, det)
                # switch (0, 0) and (1, 1), multiply (0, 1) and (1, 0) by -1
                adj = self
                values = []
                for row in range(adj.rows):
                    for col in range(adj.columns):
                        values.append(adj.matrix[row][col])
                adj.matrix[0][0] = values[3]
                adj.matrix[0][1] = values[1] * -1
                adj.matrix[1][0] = values[2] * -1
                adj.matrix[1][1] = values[0]
                # convert all numbers in adj to fractions
                for row in range(adj.rows):
                    for col in range(adj.columns):
                        adj.matrix[row][col] = frac(adj.matrix[row][col])
                # scale adj to scalar
                inv = adj.scale(scalar)
                return inv

        else:
            return False

    # converts all entries in matrix to fractions
    def convert_to_fractions(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.matrix[row][col] = frac(self.matrix[row][col])
        return self

    # switches the positions of row1 and row2 in a matrix instance
    def switch_row(self, row1, row2):
        r1 = self.matrix[row1]
        r2 = self.matrix[row2]
        self.matrix[row1] = r2
        self.matrix[row2] = r1

    # takes the given row 'row_pos' and subtracts it from all the rows underneath
    # it in a matrix instance
    def subtract_down_from_row(self, row_pos):
        m = self
        #print self.matrix[row_pos]
        for row in range(row_pos + 1, self.rows):
            for entry in range(self.columns):
                m.matrix[row][entry] = m.matrix[row][entry] - m.matrix[row_pos][entry]
        return m

    # factors out the column value of a row in a matrix instance. Returns a tuple with
    # the factored matrix and the factor
    def factor_row(self, row_pos, col_pos):
        factored_matrix = self.convert_to_fractions()
        factor = self.matrix[row_pos][col_pos]
        #print "factor: " + str(factor)
        for entry in range(self.columns):
            if factor != 0:
                factored_matrix.matrix[row_pos][entry] = factored_matrix.matrix[row_pos][entry] / factor
            else:
                # find row with a nonzero entry where we are and add that row to the working row
                pass
                factored_matrix.matrix[row_pos][entry] = factored_matrix.matrix[row_pos][entry] / factor

        return (factored_matrix, factor)

    # uses factor_row() to factor out the entries of a whole column below the row = to column
    def factor_column(self, col):
        factored_column_matrix = self
        factor = 1
        for row in range(col, self.rows):
            factor *= factored_column_matrix.matrix[row][col]
            factored_column_matrix, _ = factored_column_matrix.factor_row(row, col)

        return (factored_column_matrix, factor)

    def determinant_row_reduction(self):
        echelon_matrix = self
        multiplier = 1

        for col in range(echelon_matrix.columns):
            echelon_matrix, factor = echelon_matrix.factor_column(col)
            multiplier *= factor
            echelon_matrix = echelon_matrix.subtract_down_from_row(col)

        print("\nDeterminant: " + str(multiplier))
        #echelon_matrix.show_self()


####################################################################################
ROWS = 3
COLS = ROWS
CYCLES = 1000
PERC = CYCLES / 10

print "Start"

time = 0
perc = 0
for i in range(CYCLES):
    m1 = Matrix(ROWS, COLS)
    m1.randomize()
    start = datetime.datetime.now()
    det = m1.determinant()
    end = datetime.datetime.now()
    time = time + (end - start).total_seconds() * 1000
    if i % PERC == 0:
        print str(i/PERC) + "%"

print "Total time: " + str(time)
print "Average runtime: " + str(time/CYCLES)
print "End"
