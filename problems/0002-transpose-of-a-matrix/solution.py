def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # If the matrix is empty, return an empty list
    if not a or not a[0]:
        return []
        
    # zip(*a) takes each row and pairs their matching elements together into columns
    return [list(row) for row in zip(*a)]
