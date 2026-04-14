import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    fpr = np.array(fpr)
    tpr = np.array(tpr)
    
    # Sort by fpr (important if not sorted)
    idx = np.argsort(fpr)
    fpr = fpr[idx]
    tpr = tpr[idx]
    
    # Apply trapezoidal rule
    area = np.sum((fpr[1:] - fpr[:-1]) * (tpr[1:] + tpr[:-1]) / 2)
    
    return area
    pass