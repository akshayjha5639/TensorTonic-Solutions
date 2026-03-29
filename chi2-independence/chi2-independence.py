import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C=np.array(C)
    row=C.sum(axis=1,keepdims=True)
    col=C.sum(axis=0,keepdims=True)
    tot=C.sum()
    exp=(row@col)/tot
    chi=np.sum(((C-exp)**2)/exp)
    return chi,exp
    pass