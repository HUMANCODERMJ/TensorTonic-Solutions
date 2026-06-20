import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    normalized_array = []
    # axis = None -> return None
    arr = np.array(matrix)
    if len(arr.shape) == 1 or arr.ndim != 2 or norm_type not in ['l1', 'l2', 'max'] or (axis is not None and (not isinstance(axis, int) or axis < 0 or axis >= arr.ndim)):
        return None
    
    if norm_type == 'l1':
        if axis !=0 and axis != 1 :
            global_max_array = np.max(np.array(matrix), keepdims=True) 
            normalized_array = matrix/global_max_array
        else:
            sums = np.abs(matrix).sum(axis=axis, keepdims=True)
            normalized_array = matrix / sums
        return np.nan_to_num(normalized_array)

    elif norm_type == 'l2':
        if axis is None :
            eucl_norm = np.linalg.norm(matrix)
            normalized_array = matrix / eucl_norm
        else:
            eucl_norm = np.linalg.norm(matrix, axis=axis, keepdims=True)
            normalized_array = matrix / eucl_norm
    
        return np.nan_to_num(normalized_array)

    else:
        global_max_array = None
        if axis !=0 and axis != 1 :
            global_max_array = np.max(np.array(matrix), keepdims=True) 
        else:
            global_max_array = np.max(np.array(matrix), axis = axis,  keepdims=True) 
        normalized_array = matrix / global_max_array
        return np.nan_to_num(normalized_array)