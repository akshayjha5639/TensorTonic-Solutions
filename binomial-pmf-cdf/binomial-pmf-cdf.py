import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    a,b=0,0
    for i in range(0,k+1):
        a=comb(n,i)
        a=a*pow(p,i)*pow(1-p,n-i)
        b+=a
    return [a,b]
    pass