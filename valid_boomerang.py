def isBoomerang(points: list[list[int]]) -> bool:
    """
    Given an array points where points[i] = [xi, yi] represents a point on the
    X-Y plane, return true if these points are a boomerang.

    A boomerang is a set of three points that are all distinct and not in a
    straight line.
    """
    # Check if the points are distinct
    if points[0][0] == points[1][0] == points[2][0] or points[0][1] == points[1][1] == points[2][1] or points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False

    points.sort()

    # Calculate lines slope
    f_slope = (points[1][1] - points[0][1]) / (-10 if points[1][0] - points[0][0] == 0 else points[1][0] - points[0][0])
    s_slope = (points[2][1] - points[1][1]) / (-10 if points[2][0] - points[1][0] == 0 else points[2][0] - points[1][0])
        
    if f_slope == s_slope:
        return False
            
    return True