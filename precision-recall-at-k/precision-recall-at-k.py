def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    
    relevancy_set = set()
    relevancy_count = 0
    for i in range(k):
        relevancy_set.add(recommended[i])

    for ele in relevant:
        if ele in relevancy_set:
            relevancy_count += 1
        
    precision_score = relevancy_count/k

    recall_score = relevancy_count/len(relevant)

    return [precision_score, recall_score]