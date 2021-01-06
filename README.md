# Pymatrix

### Linear algebra matrix module

For learning python, linear algebra, and git all in one go!

#### To do:
- [x] Create matrix class
    - [x] Matrix types (identity & zero)
    - [x] Randomize matrix entries
    - [ ] Create matrix with specific entries
- [x] Matrix addition
- [x] Matrix subtraction
- [ ] Matrix multiplication
  - [ ] Scalar multiplication
- [x] Transpose operation
- [ ] Determinant calculation
- [ ] Minor calculation
- [ ] Cofactor calculation

## Usage

#### Creating a matrix instance using the *Matrix()* class
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

#### Matrix instance methods

##### .show_self()
Prints the matrix instance to console.

##### .randomize()
Sets every entry in the matrix instance to a random integer between 0 and 9.

##### .get_size()
Returns a tuple with the amount of rows and columns in the matrix instance.

##### .transpose()
Returns a matrix instance that is the transpose of the original matrix.

##### .add_matrix(second_matrix)
Returns a matrix instance that is the sum of self with second_matrix. Raises an exception if matrices are of different sizes.

##### .subtract_matrix(second_matrix)
Returns a matrix instance that is the difference of self with second_matrix. Raises an exception if matrices are of different sizes.
