# Pymatrix

For learning python, linear algebra, and git all in one go!

### To do:
- **Matrix Constructor**
    - [x] Construct zero matrix
    - [x] Construct identity matrix
    - [ ] Create matrix with specific entries
      - [x] Set specific entry
- **Matrix Operations**
  - [x] Randomize matrix entries
  - [x] Matrix addition
  - [x] Matrix subtraction
  - [x] Scalar multiplication
  - [x] Matrix multiplication
  - [x] Transpose operation
  - [ ] Matrix inversion
  - [x] Adjoint calculation
  - [x] Determinant calculation
  - [ ] Cofactor calculation
- **Vector Operations**
  - [ ] Norm (length) calculation for vectors
  - [ ] Unit vectors
  - [ ] Dot product
- **Special methods**
  - [x] Matrix addition
  - [x] Matrix subtraction
  - [x] Matrix multiplication
- **Unit tests**
  - [ ] Matrix Operations
  - [ ] Vector Operations

## Usage

### Creating a matrix instance using the *Matrix()* class
The first parameter is rows and the second parameter is columns. The third parameter is optional and declares the type of matrix to create.

```python
# Create a 3x3 zero matrix using the optional third parameter
new_matrix_instance = Matrix(rows = 3, columns = 3, matrixType = "zero")
# OR without the optional third parameter
new_matrix_instance = Matrix(3, 3)

# Create a 4x4 identity matrix
new_identity_matrix_instance = Matrix(4, 4, "identity")

# Raises exception "Identity matrices must be square" if rows != columns
new_identity_matrix_instance = Matrix(3, 4, "identity")

```

### Matrix instance methods

#### .show_self()
Prints the matrix instance to console.

```python
matrix = Matrix(2, 2)
matrix.show_self()
```

#### .randomize()
Sets every entry in the matrix instance to a random integer between 0 and 9.

```python
matrix = Matrix(3, 3)
matrix.randomize()
```

#### .set_entry()
Sets a specified entry in the matrix to the given number. First parameter is a tuple containing the position of the entry to be changed. Second parameter is the value you want to change that entry to.

```python
# create matrix
matrix = Matrix(3, 3)
# set entry on row 0, column 0 to 10
matrix.set_entry((0, 0), 10)
```

#### .get_size()
Returns a tuple with the amount of rows and columns in the matrix instance.

```python
matrix = Matrix(4, 2)
matrix.get_size()
```

#### .transpose()
Returns a matrix instance that is the transpose of the original matrix. Used as a helper function by *.get_adjoint_matrix()*

```python
matrix = Matrix(3, 2)
matrix.transpose()
```

#### .add_matrix(second_matrix)
Returns a matrix instance that is the sum of self with second_matrix. Raises an exception if matrices are of different sizes.

```python
# create matrices
matrix1 = Matrix(2, 2)
matrix1.randomize()
matrix2 = Matrix(2, 2)
matrix2.randomize()
# matrix1 + matrix2
sum_of_matrices = matrix1.add_matrix(matrix2)
```

The addition operator ``+`` can also be used.

```python
# create matrices
matrix1 = Matrix(2, 2)
matrix1.randomize()
matrix2 = Matrix(2, 2)
matrix2.randomize()
# matrix1 + matrix2
sum_of_matrices = matrix1 + matrix2
```

#### .subtract_matrix(second_matrix)
Returns a matrix instance that is the difference of self with second_matrix. Raises an exception if matrices are of different sizes.

```python
# create matrices
matrix1 = Matrix(2, 2)
matrix1.randomize()
matrix2 = Matrix(2, 2)
matrix2.randomize()
# matrix1 - matrix2
difference_of_matrices = matrix1.subtract_matrix(matrix2)
```

The subtraction operator ``-`` can also be used.

```python
# create matrices
matrix1 = Matrix(2, 2)
matrix1.randomize()
matrix2 = Matrix(2, 2)
matrix2.randomize()
# matrix1 - matrix2
difference_of_matrices = matrix1 - matrix2
```

#### .multiply_matrix(second_matrix)
Returns a matrix instance that is the difference of self with second_matrix. Raises an exception if matrices are of different sizes.

```python
# create matrices
matrix1 = Matrix(2, 2)
matrix1.randomize()
matrix2 = Matrix(2, 2)
matrix2.randomize()
# matrix1 * matrix2
product_of_matrices = matrix1.multiply_matrix(matrix2)
```

The multiplication operator ``*`` can also be used.

```python
# create matrices
matrix1 = Matrix(2, 2)
matrix1.randomize()
matrix2 = Matrix(2, 2)
matrix2.randomize()
# matrix1 * matrix2
product_of_matrices = matrix1 * matrix2
```

#### .scale(scalar)
Returns the product of a matrix and a scalar.
```python
# create matrix
matrix1 = Matrix(2, 2)
matrix1.randomize()
# scale the matrix by 2
scaled_matrix = matrix1.scale(2)
```

#### .determinant()
Returns the determinant of the matrix using cofactor expansion. Complexity is O(n!) so it gets very slow very quickly as the matrix grows. Uses *.fetch_minor_matrix()* as a helper function.

```python
# create matrix
matrix1 = Matrix(4, 4)
matrix1.randomize()
# calculate the determinant
determinant_of_matrix1 = matrix1.determinant()
```

#### .fetch_minor_matrix()
Helper function for *.determinant()* and *.get_adjoint_matrix()*. Fetches the minor matrices of the original matrix and returns their determinants.

#### .get_adjoint_matrix()
Returns the adjoint of the matrix. Uses *.fetch_minor_matrix()* and *.transpose()* as helper functions.

```python
# create matrix
matrix1 = Matrix(4, 4)
matrix1.randomize()
# calculate the determinant
determinant_of_matrix1 = matrix1.determinant()
```
