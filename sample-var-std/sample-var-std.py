import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    a=np.mean(x)
    s2=np.sum((x-a)**2)/(len(x)-1)
    s=np.sqrt(s2)
    return [s2,s]
    pass