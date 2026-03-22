import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x=np.sort(np.array(x))
    return np.percentile(x,q,method='linear')
    pass