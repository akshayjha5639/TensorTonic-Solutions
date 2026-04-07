import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a=np.array(a)
    b=np.array(b)
    d=np.dot(a,b)
    a=np.linalg.norm(a)
    b=np.linalg.norm(b)
    if(a==0 or b==0) :
        return 0
    return d/(a*b)
    pass