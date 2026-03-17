import numpy as np
import random

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    D_matrix = None
    method = random.randint(1,2)
    print(method)
    if method == 1:
        D_matrix = np.zeros((n,n))
        for index in range(n):
            D_matrix[index][index] = v[index]

    else:
        D_matrix = np.diag(v)

    return D_matrix
