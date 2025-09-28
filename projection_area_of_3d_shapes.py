class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        """
        Given an n x n grid representing stacks of 1 x 1 x 1 cubes aligned with the x, y, and z axes,
        where grid[i][j] is the height of the stack at cell (i, j):

        Compute the total area of the projections of these cubes onto the xy, yz, and zx planes.

        - The projection onto the xy-plane (top view) counts the number of grid cells with at least one cube.
        - The projection onto the yz-plane (front view) is the sum of the tallest stack in each row.
        - The projection onto the zx-plane (side view) is the sum of the tallest stack in each column.

        Args:
            grid (List[List[int]]): 2D list representing the heights of cube stacks.

        Returns:
            int: The total area of all three projections.

        Example:
            >>> projectionArea([[1,2],[3,4]])
            17

        Time Complexity: O(n^2), where n is the size of the grid.
        Space Complexity: O(n), for storing column maxima.

        LeetCode: Beats 100% of submissions
        """
        proj_area = 0

        cols_max = [0] * len(grid[0])
        rows_proj = 0
        for i in range(len(grid)):
            curr_row_max = 0
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    proj_area += 1

                    if grid[i][j] > curr_row_max:
                        curr_row_max = grid[i][j]
                    if grid[i][j] > cols_max[j]:
                        cols_max[j] = grid[i][j]

            rows_proj += curr_row_max

        return proj_area + rows_proj + sum(cols_max)
