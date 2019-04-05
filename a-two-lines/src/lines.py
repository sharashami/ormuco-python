
def overlap(x1, x2, x3,x4):
    """Check whether two lines on the x-axis overlap.
    
    Args:
        x1 (float): First line's start value.
        x2 (float): First line's end value.
        x3 (float): Second line's start value.
        x4 (float): Second line's end value.

    Raises:
        ValueError: If the line has the same start and end value OR an invalid input was given.

    Returns:
        True: If lines overlap.
        False: otherwise.

    """

    try:
        float(x1)
        float(x2)
        float(x3)
        float(x4)
    except ValueError:
        raise ValueError('ValueError. You should give me 4 numbers (x1,x2,x3,x4) as input that means the two lines (x1,x2) and (x3,x4) on the x-axis. Then, I will check whether they overlap.')

    if x1 == x2 or x3 == x4:
        raise ValueError('A line cannot have the same start and end value.')
    
    line1 = [x1 , x2]
    line1.sort()
    line2 = [x3 , x4]
    line2.sort()
    return ( line1[0] >= line2[0] and line1[0] <= line2[1] ) or ( line1[1] >= line2[0] and line1[1] <= line2[1] )
        
    