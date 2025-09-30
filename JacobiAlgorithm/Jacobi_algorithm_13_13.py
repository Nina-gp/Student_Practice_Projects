
"""Solves the equation Ax=b via the Jacobi iterative method for 13*13 coefficient matrix."""

import numpy as np
from numpy.linalg import inv, norm, LinAlgError

def get_user_matrix(rows, cols):
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            element_str = input(f"Enter element [{i + 1}, {j + 1}]: ")
            matrix[i, j] = float(element_str)

    return matrix


def is_positive_definite(matrix):
    # Check if the matrix is square
    if not all(len(row) == len(matrix) for row in matrix):
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


def jacobi(A, b, error_treshold, X=None):
    
    # Create an initial guess like x = [0...0]T                                                                                                                                                           
    if X is None:
        X = np.zeros(len(A[0])).reshape(13, 1)
     
    # Jacobi's iterative method matrix equation: X_new = Hj.X + Cj which Hj=-inv(D)(L+U) and Cj=inv(D)b
    # To form the matrix equation of the Jacobi's iterative method, we need the polar form of A                                                                                                                                                                                                                                                                                                              
    D = np.diag(A)

    # D is stored in the form of a vector of the diagonals of the matrix A, and we use the X function to convert it into a polar matrix.
    D = np.diagflat(D)

    # (L+U):
    L_plus_U = A - D

    # Jacobi matrix equation:
    Hj = -np.dot(inv(D), L_plus_U)
    Cj = np.dot(inv(D), b)

    # Check if the diagonal matrix D is singular
    if any((d == 0) for d in np.diag(A)):
        raise LinAlgError("Singular matrix: Diagonal elements must be non-zero")
    
    # Iteration:   
    error = 1000                                                                                                                                                                      
    while error > error_treshold:
        X_new = np.dot(Hj, X) + Cj
        error = norm(X_new - X, np.inf)
        X = X_new
    return X

print('Welcome to the Jacobi iterative equation solving program.\nThis program is designed according to the request for a matrix of 13 by 13 coefficients.\n')
while True:

    start_button = input('If you want to start enter "start", otherwise enter "exit". (start/exit): ').lower()
    if start_button == "start":
        print('/////////////////////// START //////////////////////////\n')
        print('Please enter the coefficient matrix "A" of the equation')
        A = get_user_matrix(13, 13)
        print('Please enter the answer matrix "b" of the equation')
        b = get_user_matrix(13, 1)
        error_treshold = float(input('With what error do you want to approximate the answer?'))

        if is_positive_definite(A):
            Approximate_answer = jacobi(A,b,error_treshold )
            
            print('----------------------- Answer -------------------------')
            print(f'A:\n {A}')
            print(f'B:\n {b}')
            print(f'Approximate value of X:\n {Approximate_answer}')
        else: 
            print("!This matrix of coefficients is inappropriate for the existing method. Please try with other coefficients.")
    else:
        exit()