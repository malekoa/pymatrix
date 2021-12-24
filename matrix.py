from __future__ import annotations
from fractions import Fraction
from random import randint

class Matrix:
    # Initialize a matrix, if _type = "identity", it in itializes an identity matrix
    def __init__(self, rows: int = 1, columns: int = 1, data: [] = [], _type: str = None):
        self.rows = rows
        self.columns = columns
        self.data = [[Fraction(0) for col in range(columns)] for row in range(rows)]
        if data:
            self.set_data(data)
        if _type == "identity":
            if self.rows != self.columns:
                raise Exception("Identity Matrices must be square, where rows = columns")
            for row in range(self.rows):
                for col in range(self.columns):
                    if row == col:
                        self.set_entry(row, col, Fraction(1))

    # returns the sum of self and Matrix m
    def __add__(self, m: Matrix) -> Matrix:
        return self.add(m)
    def __radd__(self, m: Matrix) -> Matrix:
        return m.add(self)

    # returns the difference of self and Matrix m
    def __sub__(self, m: Matrix) -> Matrix:
        return self.subtract(m)
    def __rsub__(self, m: Matrix) -> Matrix:
        return m.subtract(self)

    # returns the product of self and Matrix m
    def __mul__(self, m: Matrix) -> Matrix:
        return self.multiply(m);
    def __rmul__(self, m: Matrix) -> Matrix:
        return m.multiply(self);

    # returns self^n
    def __pow__(self, n: int) -> Matrix:
        return self.power(n)
        # if n == 0:
        #     return Matrix(self.rows, self.columns, _type='identity')
        # if n > 0:
        #     return self.power(n)
        # if n < 0:
        #     return self.inverse().power(-n)

    def stringify_data(self):
        stringified_data = []
        for row in range(self.rows):
            stringified_data.append([])
            for col in range(self.columns):
                integer_ratio_repr = self.data[row][col].as_integer_ratio()
                string_repr = str(integer_ratio_repr[0]) + "/" + str(integer_ratio_repr[1])
                stringified_data[row].append(string_repr)

        return stringified_data

    # prints the matrix to the console
    def show_self(self) -> None:
        integer_ratio_repr = []
        for row in range(self.rows):
            integer_ratio_repr.append([])
            for col in range(self.columns):
                integer_ratio_repr[row].append(self.data[row][col].as_integer_ratio())
        for row in integer_ratio_repr:
            print([(str(entry[0]) + "/" + str(entry[1])) for entry in row])

    # sets entry at row and column in self to new_entry
    def set_entry(self, row: int, column: int, new_entry: Fraction) -> None:
        fraction_entry = Fraction(new_entry)
        self.data[row][column] = fraction_entry

    # sets all entries in the Matrix from supplied data.
    def set_data(self, data: []) -> None:
        if self.rows == len(data):
            for row in data:
                if len(row) != self.columns:
                    raise Exception("Supplied data does not coincide with Matrix dimensions")
        else:
            raise Exception("Supplied data does not coincide with Matrix dimensions")
        for row in range(self.rows):
            for col in range(self.columns):
                self.set_entry(row, col, data[row][col])

    # sets all entries in the matrix to random integers between lower_lim and upper_lim
    def randomize_entries(self, lower_lim: int, upper_lim: int) -> None:
        for row in range(self.rows):
            for col in range(self.columns):
                self.set_entry(row, col, Fraction(randint(lower_lim, upper_lim)))

    # checks if other_matrix has same dimensions as self
    def dimensions_are_equal(self, other_matrix: Matrix) -> bool:
        return self.rows == other_matrix.rows and self.columns == other_matrix.columns

    # retuns the sum of self and other_matrix
    def add(self, other_matrix: Matrix) -> Matrix:
        if self.dimensions_are_equal(other_matrix): 
            result = Matrix(self.rows, self.columns)
            
            for row in range(result.rows):
                for col in range(result.columns):
                    _sum = self.data[row][col] + other_matrix.data[row][col]
                    result.set_entry(row, col, Fraction(_sum))
            return result
        else:
            raise Exception("Matrix addition requires equal dimensions")

    # returns the difference of self and other_matrix
    def subtract(self, other_matrix: Matrix) -> Matrix:
        if self.dimensions_are_equal(other_matrix): 
            result = Matrix(self.rows, self.columns)
            for row in range(result.rows):
                for col in range(result.columns):
                    difference = self.data[row][col] - other_matrix.data[row][col]
                    result.set_entry(row, col, Fraction(difference))
            return result
        else:
            raise Exception("Matrix subtraction requires equal dimensions")

    # Creates a Matrix with same data as self, scales all entries in that matrix 
    # by the scalar, then returns that matrix
    def scale(self, scalar: Fraction) -> Matrix:
        result_matrix = Matrix(self.rows, self.columns, self.data.copy())
        
        for row in range(result_matrix.rows):
            for col in range(result_matrix.columns):
                scaled_entry = result_matrix.data[row][col] * scalar
                result_matrix.set_entry(row, col, scaled_entry)

        return result_matrix

    # Creates a Matrix with same data as self, scales all entries in that matrix 
    # by the scalar, then returns that matrix
    def scale(self, scalar: str) -> Matrix:
        scalar_frac = Fraction(scalar)

        result_matrix = Matrix(self.rows, self.columns, self.data.copy())
        
        for row in range(result_matrix.rows):
            for col in range(result_matrix.columns):
                scaled_entry = result_matrix.data[row][col] * scalar_frac
                result_matrix.set_entry(row, col, scaled_entry)

        return result_matrix

    # returns a list with the values in the specified column of matrix self
    def get_col(self, col: int) -> []:
        return [row[col] for row in self.data]

    # returns a list with the values in the specified row of matrix self
    def get_row(self, row: int) -> []:
        return self.data[row]

    # Returns the sum of the products of the respective entries in two lists.
    # Used in .multiply()
    def sum_of_products(self, list1: [], list2: []):
        if len(list1) != len(list2):
            raise Exception("Lists must have equal lengths")
        # return the sum of the products of each respective entry
        return (sum([(entry[0] * entry[1]) for entry in zip(list1, list2)]))

    # Returns the product of self and other_matrix
    def multiply(self, other_matrix: Matrix) -> Matrix:
        if self.columns != other_matrix.rows:
            raise Exception("self.columns must be equal to other_matrix.rows")
        
        result_matrix = Matrix(self.rows, other_matrix.columns)
        for row in range(result_matrix.rows):
            for col in range(result_matrix.columns):
                self_row_list = self.get_row(row)
                other_col_list = other_matrix.get_col(col)
                new_entry = Matrix().sum_of_products(self_row_list, other_col_list)
                result_matrix.set_entry(row, col, Fraction(new_entry))

        return result_matrix

    # Returns a Matrix self^n
    def power(self, n: Fraction) -> Matrix:
        result_matrix = Matrix(self.rows, self.columns, self.data.copy())
        if n == 0:
            return Matrix(self.rows, self.columns, _type='identity')
        if n < 0:
            result_matrix = result_matrix.inverse()
        for i in range(abs(n) - 1):
            result_matrix = result_matrix.multiply(self)
        return result_matrix
    
    # Returns a matrix that contains the same data as self with row r_col and
    # column r_col removed.
    def submatrix(self, r_row: int, r_col: int) -> Matrix:
        submatrix = Matrix(self.rows - 1, self.columns - 1)
        new_data = []
        for row in range(self.rows):
            for col in range(self.columns):
                if row != r_row and col != r_col:
                    new_data.append(self.data[row][col])
        index = 0
        for row in range(submatrix.rows):
            for col in range(submatrix.columns):
                new_entry = new_data[index]
                submatrix.set_entry(row, col, new_entry)
                index += 1
        return submatrix

    # Returns a matrix that is the transpose of self
    def transpose(self) -> Matrix:
        transposed_data = [self.get_col(col) for col in range(self.columns)]
        return Matrix(self.columns, self.rows, transposed_data)

    # Returns the determinant of the specified submatrix of self (row 'row' and 
    # column 'col' are removed)
    def minor(self, row: int, col: int) -> Fraction:
        return self.submatrix(row, col).determinant()

    # Returns the minor of the specified submatrix of self, taking signs into account
    def cofactor(self, row: int, col: int) -> Fraction:
        if (row + col) % 2 == 0:
            return self.minor(row, col)
        return -self.minor(row, col)
    
    # Returns the determinant of self using cofactor expansion (slow)
    def determinant(self) -> Fraction:
        if self.rows != self.columns:
            raise Exception("Rows must equal columns")
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        if self.rows >= 3:
            result = Fraction(0)
            for row in range(self.rows):
                result += self.data[row][0] * self.cofactor(row, 0)
            return result

    # Returns self's matrix of minors
    def matrix_of_minors(self) -> Matrix:
        result_matrix = Matrix(self.rows, self.columns)
        for row in range(result_matrix.rows):
            for col in range(result_matrix.columns):
                result_matrix.set_entry(row, col, self.minor(row, col))
        return result_matrix

    # Returns self's matrix of cofactors
    def matrix_of_cofactors(self) -> Matrix:
        result_matrix = Matrix(self.rows, self.columns)
        for row in range(result_matrix.rows):
            for col in range(result_matrix.columns):
                result_matrix.set_entry(row, col, self.cofactor(row, col))
        return result_matrix

    # Returns a matrix that is the inverse of self. Returns false if there is no inverse.
    def inverse(self) -> Matrix:
        det_self = self.determinant() 
        if det_self != 0:
            return self.matrix_of_cofactors().transpose().scale(Fraction(1, det_self))
        else:
            return False
