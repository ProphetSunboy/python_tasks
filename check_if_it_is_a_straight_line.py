class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:  
        """
        You are given an array coordinates, coordinates[i] = [x, y], where
        [x, y] represents the coordinate of a point. Check if these points make
        a straight line in the XY plane.
        """      
        if len(coordinates) == 2:
            return True

        x_equality = True
        y_equality = True

        for coord in coordinates[1:]:
            if coord[0] != coordinates[0][0]:
                x_equality = False

            if coord[1] != coordinates[0][1]:
                y_equality = False

            if not x_equality and not y_equality:
                break

        if x_equality or y_equality:
            return True

        s_coords = sorted(coordinates)

        slope = (s_coords[1][1] - s_coords[0][1]) / ((s_coords[1][0] - s_coords[0][0]) if (s_coords[1][0] - s_coords[0][0]) != 0 else -10)

        for i, coord in enumerate(coordinates[1:], 1):
            if (s_coords[i][1] - s_coords[i-1][1]) / ((s_coords[i][0] - s_coords[i-1][0]) if (s_coords[i][0] - s_coords[i-1][0]) else -10) != slope:
                return False
        
        return True