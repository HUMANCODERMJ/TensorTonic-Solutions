import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    if isinstance(x,list):
        narray = np.asarray(x, dtype=float)
        eles=[]
        for i in narray:
            formula = 1/(1+np.exp(-i))
            ans = formula
    
            eles.append(ans)  
            
        return np.asarray(eles)
    else:
        return 1/(1+np.exp(-x))