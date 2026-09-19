def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    """
    Multiply every entry of a 2D matrix by a given scalar value.
    
    Args:
        matrix: A 2D list of integers or floats.
        scalar: The number to multiply each element by.
        
    Returns:
        A new 2D list containing the scaled elements.
    """
    # Outer loop iterates through each row, inner loop scales each element 'val'
    return [[val * scalar for val in row] for row in matrix]
