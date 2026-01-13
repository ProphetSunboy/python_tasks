class Solution:
    def separateSquares(self, squares):
        """
        Given a 2D integer list `squares` where each entry is [xi, yi, li]
        representing the coordinates of the bottom-left point and the side
        length of a square aligned with the axes.

        Finds the minimum y-coordinate of a horizontal line such that the total
        area of the squares above the line equals the total area of the squares
        below the line.

        Answers within 1e-5 of the actual answer are accepted.

        Note:
            Squares may overlap, and overlapping areas should be counted
            multiple times.

        Args:
            squares (List[List[int]]): List of [x, y, l] describing squares.

        Returns:
            float: The minimum y-coordinate for such a horizontal line.

        Example:
            Input: squares = [[0, 0, 2], [1, 1, 1]]
            Output: 1.16667

        Time Complexity: O(n), where n is the number of squares.
        Space Complexity: O(1).
        """
        total_area = 0
        min_y = float("inf")
        max_y = float("-inf")

        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        half = total_area / 2.0

        def area_below(Y):
            area = 0.0
            for x, y, l in squares:
                if Y <= y:
                    continue
                elif Y >= y + l:
                    area += l * l
                else:
                    area += l * (Y - y)
            return area

        left, right = min_y, max_y
        for _ in range(60):
            mid = (left + right) / 2
            if area_below(mid) < half:
                left = mid
            else:
                right = mid

        return left
