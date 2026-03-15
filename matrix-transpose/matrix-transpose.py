import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m = len(A)
    n = len(A[0])
    narray = np.zeros((n, m))
    for rows in range(0, n):
        for cols in range(0, m):
            narray[rows][cols] = A[cols][rows]

    return narray
