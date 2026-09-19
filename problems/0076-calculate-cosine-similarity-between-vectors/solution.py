import numpy as np

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Calculate the cosine similarity of two vectors.
    Args:
        v1 (numpy.ndarray): 1D array representing the first vector.
        v2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine similarity of the two vectors.
    """
    # 1. Calculate the dot product (the top part of the formula)
    dot_product = np.dot(v1, v2)
    
    # 2. Calculate the L2 norm (length) of each vector (the bottom part)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    # 3. Prevent dividing by zero if one of the vectors is completely empty/zero
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
        
    # 4. Divide the dot product by the multiplied lengths
    similarity = dot_product / (norm_v1 * norm_v2)
    
    return float(similarity)
