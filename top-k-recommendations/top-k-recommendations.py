def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    unrated_scores = [(score, i) for i, score in enumerate(scores) if i not in rated_indices]
    
    unrated_scores.sort(key=lambda x: x[0], reverse=True)

    top_k_indices = [pair[1] for pair in unrated_scores[:k]]
    
    return top_k_indices
    