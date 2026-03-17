import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    a_array = np.asarray(A)
    trace = 0
    for index in range(len(a_array[0])):
        trace += a_array[index][index]

    return trace
    
    
