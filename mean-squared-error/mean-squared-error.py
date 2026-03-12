import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    n=len(y_pred)
    for i in range(n):
        y_pred[i]=(y_pred[i]-y_true[i])**2
        
    return np.sum(y_pred)/n
    pass
