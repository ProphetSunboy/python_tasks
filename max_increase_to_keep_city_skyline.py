class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        Given an n x n grid representing the heights of buildings in a city,
        return the maximum total sum that the height of the buildings can be
        increased by without affecting the city's skyline from any cardinal
        direction (north, south, east, west).

        The city's skyline is defined as the outer contour when viewing the city
        from a distance along each cardinal direction. You may increase the height
        of any building (including those of height 0) by any amount, as long as
        the skyline remains unchanged.

        Args:
            grid (List[List[int]]): 2D list where grid[r][c] is the height of the
                building at row r and column c.

        Returns:
            int: The maximum total sum that the heights of buildings can be increased
                without changing the skyline.

        Example:
            Input: grid = [[3, 0, 8, 4],
                           [2, 4, 5, 7],
                           [9, 2, 6, 3],
                           [0, 3, 1, 0]]
            Output: 35

        Time Complexity: O(n^2), where n is the number of rows/columns in grid.
        Space Complexity: O(n), for storing row and column maxima.

        LeetCode: Beats 100% of submissions
        """
        n = len(grid)
        max_rows = [0] * n
        max_cols = [0] * n

        for i in range(n):
            max_rows[i] = max(grid[i])

        for j in range(n):
            curr_max = 0

            for i in range(n):
                if grid[i][j] > curr_max:
                    curr_max = grid[i][j]

            max_cols[j] = curr_max

        max_sum = 0
        for i in range(n):
            for j in range(n):
                max_sum += max(0, min(max_rows[i], max_cols[j]) - grid[i][j])

        return max_sum
