import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    m,n=X.shape
    w=np.zeros(n)
    b=0.0
    for i in range(steps):
        z=_sigmoid(np.dot(X,w)+b)
        z=(z-y)
        b-=lr*np.sum(z)/m
        w-=lr*np.dot(X.T,z)/m
    return w,b
    pass