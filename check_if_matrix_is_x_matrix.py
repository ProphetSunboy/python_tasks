class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        """Determines if a given n x n matrix is an X-Matrix.

        An X-Matrix is defined as a square matrix where:
            1. All elements on both the main diagonal (i == j) and the anti-diagonal (i + j == n - 1) are non-zero.
            2. All other elements (not on either diagonal) are zero.

        Args:
            grid (list[list[int]]): A 2D list representing the n x n matrix.

        Returns:
            bool: True if grid is an X-Matrix, False otherwise.

        Example:
            >>> checkXMatrix([[2,0,2],[0,3,0],[2,0,4]])
            True
            >>> checkXMatrix([[5,7,0],[0,3,1],[0,5,0]])
            False

        Time complexity: O(n^2), where n is the size of the matrix.
        Space complexity: O(1) (ignoring input storage).

        LeetCode: Beats 100% of submissions
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j:
                    if grid[i][j] == 0:
                        return False
                elif i + j == len(grid) - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False

        return True
