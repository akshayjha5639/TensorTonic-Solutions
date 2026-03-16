def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    m,n=len(points),len(centroids)
    D=len(points[0])
    a=[-1 for i in range(m)]
    for i in range(m):
        b=float('inf')
        c=0
        for j in range(n):
            e=sum((points[i][d]-centroids[j][d])**2 for d in range(D))
            if (e<b) :
                b=e
                c=j
        a[i]=c
    return a