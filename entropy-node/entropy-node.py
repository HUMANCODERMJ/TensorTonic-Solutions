import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if y == []: return 0.0
    H = 0 # H -> entropy
    labels, counts = np.unique(y, return_counts=True)
    proportions = [count / len(y) for count in counts]

    print(proportions)

    for proportion in proportions:
        print(f"class label->{proportion}")
        if proportion == 0:
            H -= 0
        else:
            H -= proportion*np.log2(proportion)
        print(f"entropy->{H} \n")
    return H
    