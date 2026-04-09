def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    a=recommended[0:k]
    b=0
    relevant=set(relevant)
    for i in a:
        if i in relevant:
            b+=1
    return [b/k,b/len(relevant)]