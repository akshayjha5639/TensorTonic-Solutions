import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    a,b=np.unique(y_train,return_counts=True)
    return [a[np.argmax(b)]]*len(X_test)
    pass