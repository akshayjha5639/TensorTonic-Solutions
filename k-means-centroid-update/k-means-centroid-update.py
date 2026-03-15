import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    points=np.array(points)
    assignments=np.array(assignments)
    clusters=np.zeros((k,points.shape[1]))
    for i in range(k):
        clusters[i]=np.mean(points[assignments==i],axis=0)
    return clusters.tolist()
    