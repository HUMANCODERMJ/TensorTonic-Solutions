from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x_array = np.array(x)
    counter = Counter(x)
    mode = min(key for key, count in counter.items() if count == max(counter.values()))
    return {
        "mean": float(np.mean(x_array, dtype=np.float64)),
        "median": float(np.median(x_array)),
        "mode" : float(mode)
    }