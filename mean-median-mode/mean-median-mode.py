import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    a=[0.0,0.0,0.0]
    a[0]=np.mean(x)
    a[1]=np.median(x)
    values, counts = np.unique(x, return_counts=True)
    a[2] = values[np.argmax(counts)]
    return a
    pass