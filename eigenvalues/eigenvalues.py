import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        mat=np.array(matrix)
        mat[0,0]
    except:
        return None
    if(mat.shape[0]!=mat.shape[1]):
        return None
    return np.linalg.eigvals(mat)
    pass