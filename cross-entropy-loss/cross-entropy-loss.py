import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_pred=np.array(y_pred)
    return -np.mean(np.log(y_pred[np.arange(y_pred.shape[0]),y_true]))
    pass