import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    ans=0.0
    b,c=np.unique(y,return_counts=True)
    c=c/len(y)
    for a in c:
        if(a==0 or a==1) :
            ans+= 0.0
        else :
            ans+=-a*np.log2(a)
        
    return ans
    pass