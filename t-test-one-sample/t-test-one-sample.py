import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x=np.array(x)
    xm=np.mean(x)
    n=len(x)
    s=np.sqrt(np.sum((x-xm)**2)/(n-1))
    t=(xm-mu0)/(s/np.sqrt(n))
    return t
    pass