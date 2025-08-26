class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        """
        Given a 2D 0-indexed integer list `dimensions`, where each element
        is a list [length, width] representing a rectangle:

        Returns the area of the rectangle with the longest diagonal.
        If multiple rectangles share the longest diagonal, returns the area of the
        rectangle with the largest area among them.

        Args:
            dimensions (list[list[int]]): List of [length, width] pairs for each rectangle.

        Returns:
            int: Area of the rectangle with the longest diagonal (and largest area if tied).

        Example:
            >>> areaOfMaxDiagonal([[9,3],[6,8]])
            48

        Time Complexity: O(n), where n is the number of rectangles.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        max_diag = 0
        max_area = 0

        for d in dimensions:
            curr_diag = (d[0] ** 2 + d[1] ** 2) ** 0.5
            curr_area = d[0] * d[1]

            if curr_diag > max_diag:
                max_diag = curr_diag
                max_area = curr_area
            elif curr_diag == max_diag and curr_area > max_area:
                max_area = curr_area

        return max_area
