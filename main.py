from user_input import user_input_int, user_input_float

def main():
    """ Demonstration of matrix addition. """
    print("   MATRIX ADDITION")
    print("---------------------")
    print("Define matrix A:")
    matrix_a = get_matrix()
    print()
    print_matrix(matrix_a)
    print()
    print("Define matrix B")
    matrix_b = get_matrix()
    print()
    print_matrix(matrix_b)
    print()
    print("Adding matrices...")
    matrix_c = add_matrix(matrix_a, matrix_b)
    if matrix_c is None:
        print("Matrices could not be added:")
        print(f"Matrix A had dimensions {matrix_height(matrix_a)}x{matrix_width(matrix_a)}.")
        print(f"Matrix B had dimensions {matrix_height(matrix_b)}x{matrix_width(matrix_b)}.")
    else:
        print_matrix(matrix_a)
        print("+")
        print_matrix(matrix_b)
        print("=")
        print_matrix(matrix_c)
    print()
    print("Done!")

def matrix_width(matrix):
    """ Returns the amount of columns of the matrix. """
    return len(matrix[0])

def matrix_height(matrix):
    """ Returns the amount of rows of the matrix. """
    return len(matrix)

def new_matrix(width, height):
    """ Creates a new matrix with the specified width and height, initializing values to 0. """
    return [[0 for i in range(width)] for j in range(height)]

def matrix_positions(width, height):
    """ Generates row and column pairs to iterate through a matrix with size width by height. """
    for i in range(height):
        for j in range(width):
            yield (i, j)

def add_matrix(matrix1, matrix2):
    """ Adds matrix1 and matrix2 together. Returns None if their dimensions do not match. """
    width_of_1 = matrix_width(matrix1)
    height_of_1 = matrix_height(matrix1)
    width_of_2 = matrix_width(matrix2)
    height_of_2 = matrix_height(matrix2)
    if width_of_1 != width_of_2 or height_of_1 != height_of_2:
        return None
    result = new_matrix(width_of_1, height_of_1)
    for (i, j) in matrix_positions(width_of_1, height_of_1):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def get_matrix():
    """ Creates and returns a user-defined matrix. """
    print("How many rows?")
    matrix_height = user_input_int(1, 10)
    print("How many columns?")
    matrix_width = user_input_int(1, 10)
    matrix = new_matrix(matrix_width, matrix_height)
    for (i, j) in matrix_positions(matrix_width, matrix_height):
        print(f"What value for position [{i+1}][{j+1}]?")
        user_input = user_input_float()
        matrix[i][j] = user_input
    return matrix

def matrix_string(matrix):
    """ Returns a readable string representation of the matrix. """
    matrix_string = ""
    for i in range(matrix_height(matrix)):
        matrix_string += '[ '
        for j in range(matrix_width(matrix)):
            matrix_string += str(matrix[i][j]) + ' '
        matrix_string += ']\n'
    return matrix_string

def print_matrix(matrix):
    """ Prints the matrix in a readable format. """
    print(matrix_string(matrix), end='')

if __name__ == "__main__":
    main()