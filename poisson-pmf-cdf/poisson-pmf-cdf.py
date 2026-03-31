import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    a,b=0,0
    for i in range(k+1):
        a=(np.exp(-lam)*np.pow(lam,i))/np.exp(np.sum(np.log(np.arange(1,i+1))))
        b+=a
    return a,b
    pass