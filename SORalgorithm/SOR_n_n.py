import numpy as np
from numpy.linalg import inv, norm


# for getting matrices as input:
def get_user_matrix(rows, cols):
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            element_str = input(f"Enter element [{i + 1}, {j + 1}]: ")
            matrix[i, j] = float(element_str)

    return matrix 


def is_tri_diag_and_positive(matrix):
    n = len(matrix)
    
    # Check the main diagonal
    for i in range(n):
        if matrix[i][i] <= 0:
            return False
    
    # Check the sub-diagonal
    for i in range(1, n):
        if matrix[i][i-1] != matrix[i-1][i]:
            return False

    # Check if the matrix is symmetric
    if not np.allclose(matrix, matrix.T):
        return False

    # Check if all leading principal minors have positive determinants
    for i in range(1, len(matrix) + 1):
        sub_matrix = matrix[:i, :i]
        if np.linalg.det(sub_matrix) <= 0:
            return False

    return True


def calculateOmega(A):

    #To calculate Omega, we must first create the Jacobi matrix
    # D is stored in the form of a vector of the diagonals of the matrix A, and we use the X function to convert it into a polar matrix.
    D = np.diag(A)
    D = np.diagflat(D)
    L_plus_U = A - D
    Hj = -np.dot(inv(D), L_plus_U)

    # Now we have to calculate the maximum eigenvalue of Jacobi matrix.
    eigenvalues, _ = np.linalg.eig(Hj)
    max_eigenvalue = max(abs(np.real(eigenvalues)))
    # omega = 2 / (1 + sqrt(1 - [p(Hj)]**2))
    omega_optimal = 2 / (1 + np.sqrt(1 - max_eigenvalue ** 2))
    return omega_optimal


def sorSolver(A, b, error_treshold, dimension):
    omega = calculateOmega(A)
    n = len(b)
    # Create an initial guess like x = [0...0]T 
    x = np.zeros(n).reshape(dimension, 1)
    # creat an empty list for approximate answer
    x_new = np.zeros(n)
    # Set an initial value to define variable error

    
    D = np.diag(A)
    D = np.diagflat(D)
    U = np.triu(A, k=1)
    L = np.tril(A, k=-1)

    # The SOR matrix is defined as follows:
    Hw = np.dot(inv(D + (omega*L)), (((1-omega)*D) - (omega*U)))
    Cw = np.dot((omega * inv(D + (omega*L))), b)

     # Iteration: 
    error = 1000
    while error > error_treshold:
        x_new = np.dot(Hw, x) + Cw
        error = norm(x_new - x, np.inf)
        x = x_new

    return x

print('Welcome to the SOR iterative equation solving program.\n')
print('!!! Note: The incoming matrix must be tridiagonal and positive definite in order to calculate omega in the usual way. !!!')
while True:
    start_button = input('If you want to start enter "start", otherwise enter "exit". (start/exit): ').lower()
    if start_button == "start":
        print('/////////////////////// START //////////////////////////\n')
        print('Please enter the coefficient matrix "A" of the equation')
        dimension = int(input("What is the dimension of your matrix?"))
        A = get_user_matrix(dimension, dimension)
        print('Please enter the answer matrix "b" of the equation')
        b = get_user_matrix(dimension, 1)
        error_treshold = float(input('With what error do you want to approximate the answer?'))

        if is_tri_diag_and_positive(A):
            print(f' Omega = {calculateOmega(A)}')
            Approximate_answer = sorSolver(A, b, error_treshold, dimension)
            print('----------------------- Answer -------------------------')
            print(f'A:\n {A}')
            print(f'B:\n {b}')
            print(f'Approximate value of X:\n {Approximate_answer}')
        else:
            print("Your matrix of coefficients is inappropriate for this method. Please try with other coefficients.")
    else:
        exit()
