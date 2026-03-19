class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        """
        Given a 2D character matrix `grid`, where each element is 'X', 'Y',
        or '.', return the number of submatrices that contain:
            - grid[0][0]
            - An equal frequency of 'X' and 'Y'
            - At least one 'X'

        Args:
            grid (List[List[str]]): 2D list representing the matrix.

        Returns:
            int: Number of submatrices meeting the criteria.

        Example:
            Input: grid = [["X","Y","."],["Y",".","."]]
            Output: 3

        Time Complexity: O(R * C), where R is the number of rows and C is the
        number of columns in the grid.
        Space Complexity: O(R * C), for the prefix sum lists.
        """
        R, C = len(grid), len(grid[0])

        prefX = [[0] * C for _ in range(R)]
        prefY = [[0] * C for _ in range(R)]
        res = 0

        for r in range(R):
            rowX, rowY = 0, 0
            for c in range(C):
                if grid[r][c] == "X":
                    rowX += 1
                if grid[r][c] == "Y":
                    rowY += 1

                if r > 0:
                    prefX[r][c] = rowX + prefX[r - 1][c]
                    prefY[r][c] = rowY + prefY[r - 1][c]
                else:
                    prefX[r][c] = rowX
                    prefY[r][c] = rowY

                if prefX[r][c] > 0 and prefX[r][c] == prefY[r][c]:
                    res += 1

        return res
