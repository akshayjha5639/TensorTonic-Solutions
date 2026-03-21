import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    predictions=np.array(predictions)
    m,n=predictions.shape
    ans=[]
    for i in range(n):
        ans.append(np.argmax(np.bincount(predictions[:,i])))
    return ans