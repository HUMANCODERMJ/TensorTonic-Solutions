import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    return np.mean(np.square(np.asarray(y_pred) - np.asarray(y_true)))
