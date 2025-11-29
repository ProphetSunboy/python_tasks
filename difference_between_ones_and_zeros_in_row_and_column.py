class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Given a 0-indexed m x n binary matrix grid, construct the difference
        matrix diff, where for each cell (i, j):
            Let ones_row[i]   = number of ones in row i
            Let ones_col[j]   = number of ones in column j
            Let zeros_row[i]  = number of zeros in row i
            Let zeros_col[j]  = number of zeros in column j

            diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]

        Args:
            grid (List[List[int]]): A 2D binary matrix representing the grid,
            where grid[i][j] is either 0 or 1.

        Returns:
            List[List[int]]: The resulting m x n difference matrix diff.

        Example:
            Input: grid = [
                [0,1,1],
                [1,0,1],
                [0,0,1]
            ]
            Output: [
                [0,0,4],
                [0,0,4],
                [-2,-2,2]
            ]

        Time Complexity: O(m * n), where m and n are the dimensions of grid.
        Space Complexity: O(m + n) for auxiliary row and column sums.
        """
        ones_row = [0] * len(grid)
        ones_col = [0] * len(grid[0])
        zeros_row = [0] * len(grid)
        zeros_col = [0] * len(grid[0])
        diff = [[0] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones_row[i] += 1
                    ones_col[j] += 1
                else:
                    zeros_row[i] += 1
                    zeros_col[j] += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]

        return diff
