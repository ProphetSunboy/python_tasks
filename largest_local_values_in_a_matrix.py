# First attempt
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        """Finds the largest value in each 3x3 submatrix of a given grid.

        For each position (i,j) in the output matrix, finds the maximum value in the 3x3
        submatrix of the input grid centered at position (i+1,j+1).

        Args:
            grid (list[list[int]]): Input n x n matrix of integers

        Returns:
            list[list[int]]: (n-2) x (n-2) matrix containing maximum values of each 3x3 submatrix

        Examples:
            >>> largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
            [[9,9],[8,6]]  # Maximum values in each 3x3 submatrix
            >>> largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])
            [[2,2,2],[2,2,2],[2,2,2]]  # All 3x3 submatrices contain 2 as maximum

        Time complexity: O(n²) - where n is the size of input matrix
        Space complexity: O(n²) - for storing the output matrix
        """
        max_local = []

        for _ in range(len(grid) - 2):
            max_local.append([0] * (len(grid[0]) - 2))

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                for l in range(i - 1, i + 2):
                    for k in range(j - 1, j + 2):
                        if grid[l][k] > max_local[i - 1][j - 1]:
                            max_local[i - 1][j - 1] = grid[l][k]

        return max_local


# Second attempt
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        max_local = []

        for _ in range(len(grid) - 2):
            max_local.append([0] * (len(grid[0]) - 2))

        for i in range(len(grid) - 2):
            for j in range(len(grid) - 2):
                max1 = max(grid[i][j], grid[i][j + 1], grid[i][j + 2])
                max2 = max(grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2])
                max3 = max(grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2])

                max_local[i][j] = max(max1, max2, max3)

        return max_local
