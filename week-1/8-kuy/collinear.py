def collinearity(x1, y1, x2, y2):
    """Check if two vectors are collinear."""
    if x1 == 0 and y1 == 0:
        return True  # (0, 0) is collinear with all vectors
    elif x2 == 0 and y2 == 0:
        return True  # Any vector is collinear with (0, 0)
    if x1 == 0 and x2 == 0:
        return False  # Not collinear if both x are zero
    # Special case: If one x-coordinate is zero, the other must have the same y sign
    if x1 == 0:
        return y2 == 0  # Both on y-axis (y2 can't be zero due to previous check)
    elif x2 == 0:
        return y1 == 0  # Both on y-axis (y1 can't be zero due to previous check)
    # General case: Check proportionality considering both directions
    return abs(y1 * x2) == abs(y2 * x1)
