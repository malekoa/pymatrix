# Pymatrix

### Linear algebra matrix module

For learning python, linear algebra, and git all in one go!

#### To do:
- [x] Create matrix class
    - [x] Create identity matrix
    - [x] Randomize matrix entries
- [x] Matrix addition
- [x] Matrix subtraction
- [ ] Matrix multiplication
- [ ] Determinant calculation
- [ ] Minor calculation
- [ ] Cofactor calculation

## Usage

#### Creating a matrix instance
First parameter is rows, second parameter is columns. Third parameter is matrix type and is optional. Creates a zero matrix by default. There are two possible types:
1. zero
2. identity

```python
# Create a 3x3 zero matrix
matrix = Matrix(3, 3, "zero")
# OR
matrix = Matrix(3, 3)

# Create a 4x4 identity matrix
identity_matrix = Matrix(4, 4, "identity")

# Raises exception "Identity matrices must be square"
exception_matrix = Matrix(3, 4, "identity")

```

#### Matrix instance methods

##### .show_self()
Prints the matrix instance to console.

##### .randomize()
Sets every entry in the matrix instance to a random integer between 0 and 9.

##### .get_size()
Returns a tuple with the amount of rows and columns in the matrix instance.

##### .add_matrix(second_matrix)
Returns the sum of the matrix instance with second_matrix. Returns a new matrix instance. Raises an exception if matrices are of different sizes.

##### .subtract_matrix(second_matrix)
Returns the difference of the matrix instance with second_matrix. Returns a new matrix instance. Raises an exception if matrices are of different sizes.
