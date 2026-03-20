import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    dot_product = np.dot(x1, x2)
    # Calculate the L2 norms (magnitudes) of both vectors
    norm_vec1 = np.linalg.norm(x1)
    norm_vec2 = np.linalg.norm(x2)
    
    # Calculate cosine similarity
    # Ensure norms are not zero to avoid division by zero errors
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0
        
    similarity = dot_product / (norm_vec1 * norm_vec2)
    if label == 1:
        return 1 - similarity
    else:
        return max(0, similarity - margin)
    
    