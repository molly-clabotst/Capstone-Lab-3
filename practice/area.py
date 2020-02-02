def triangle_area(height, base):
    """ 
    Compute the area of a triangle with the given height and base.
    Raises a ValueErro if either height or base are negative.
    """
    
    if height < 0 or base < 0:
        raise ValueError('Base and height must be positive')
    return height * base * 0.5