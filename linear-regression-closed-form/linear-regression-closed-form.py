import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    xt=np.transpose(X)
    return np.linalg.inv(xt@X)@xt@y
    pass