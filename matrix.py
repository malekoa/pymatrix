import random
from fractions import Fraction

class Matrix:
    # initializes a zero matrix
    def __init__(self, rows = 1, columns = 1):
        self.data = []
        self.rows = rows
        self.columns = columns

        for row in range(self.rows):
            self.data.append([])
            for _ in range(self.columns):
                self.data[row].append(Fraction(0, 1))

    # prints the matrix to the console. Converts each fraction to a string representation when needed
    def show_self(self):
        string_matrix = Matrix(self.rows, self.columns)
        for row in range(string_matrix.rows):
            for col in range(string_matrix.columns):
                if self.data[row][col].as_integer_ratio()[1] == 1:
                    # if denominator == 1, returns only the numerator
                    string_matrix.data[row][col] = self.data[row][col].as_integer_ratio()[0]
                else:
                    # if denominator != 1, returns a string "numerator/denominator"
                    string_matrix.data[row][col] = str(self.data[row][col].as_integer_ratio()[0]) + "/" + \
                                                   str(self.data[row][col].as_integer_ratio()[1])
        # prints the rows
        for row in range(string_matrix.rows):
            print(string_matrix.data[row])

    # sets all entries in the matrix to a random integer
    def randomize(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.data[row][col] = Fraction(random.randint(1, 9), 1)

    # returns the specified column in a matrix
    def get_column(self, col):
        column = []
        for row in self.data:
            column.append(row[col])
        return column

    # returns a Matrix that is the transpose of self
    def transpose(self):
        columns = []
        for col in range(self.columns):
            columns.append(self.get_column(col))
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = columns
        return transposed_matrix

    # returns a Matrix that is the sum of itself and other_matrix
    def add(self, other_matrix):
        result_matrix = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for col in range(self.columns):
                result_matrix.data[row][col] = self.data[row][col] + other_matrix.data[row][col]
        return result_matrix

    # returns a Matrix that is the difference of itself and other_matrix
    def subtract(self, other_matrix):
        result_matrix = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for col in range(self.columns):
                result_matrix.data[row][col] = self.data[row][col] - other_matrix.data[row][col]
        return result_matrix

    def scale(self, scalar):
        result_matrix = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for col in range(self.columns):
                result_matrix.data[row][col] = self.data[row][col] * scalar
        return result_matrix

    # returns the product of self and other_matrix
    def multiply(self, other_matrix):
        result_matrix = Matrix(self.rows, other_matrix.columns)
        
        for row in range(self.rows):
            for col in range(other_matrix.columns):
                product_sum = 0
                for entry in range(len(self.data[row])):
                    product_sum += self.data[row][entry] * other_matrix.get_column(col)[entry]
                
                result_matrix.data[row][col] = product_sum
        
        return result_matrix

    # returns a matrix instance that is the minor of self in relation to position
    def minor(self, position):
        result_matrix = Matrix(self.rows - 1, self.columns - 1)
        values = []

        for row in range(self.rows):
            for col in range(self.columns):
                if row != position[0] and col != position[1]:
                    values.append(self.data[row][col])

        counter = 0
        for row in range(result_matrix.rows):
            for col in range(result_matrix.columns):
                result_matrix.data[row][col] = values[counter]
                counter += 1

        return result_matrix

    # returns the determinant of a matrix using laplace expansion
    def determinant(self):
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        result = Fraction(0, 1)
        
        if self.rows >= 3:
            for row in range(self.rows):
                if (row % 2 == 0):
                    result += self.data[row][0] * self.minor( (row, 0) ).determinant()
                else:
                    result -= self.data[row][0] * self.minor( (row, 0) ).determinant()
        
        return result

#--------------------------------------------------------------------------------

m1 = Matrix(3, 3)
m1.randomize()
m1.show_self()
print("determinant: " + str(m1.determinant()))

