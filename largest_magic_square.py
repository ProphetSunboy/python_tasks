class Solution:
    def largestMagicSquare(self, grid):
        """
        Finds the size of the largest magic square subgrid within the given grid.

        A k x k magic square is a k x k grid filled with integers such that every row sum,
        every column sum, and both diagonal sums are all equal. The integers in the magic
        square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

        Args:
            grid (List[List[int]]): A 2D list representing the m x n integer grid.

        Returns:
            int: The side length k of the largest magic square found within the grid.

        Example:
            Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
            Output: 3

        Time Complexity: O(m * n * min(m, n)), where m and n are the grid dimensions.
        Space Complexity: O(m * n), for prefix sums and auxiliary lists.
        """
        m, n = len(grid), len(grid[0])

        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        def is_magic(i, j, k):
            target = row[i][j + k] - row[i][j]

            for r in range(i, i + k):
                if row[r][j + k] - row[r][j] != target:
                    return False

            for c in range(j, j + k):
                if col[i + k][c] - col[i][c] != target:
                    return False

            d1 = diag1[i + k][j + k] - diag1[i][j]
            d2 = diag2[i + k][j] - diag2[i][j + k]

            return d1 == target and d2 == target

        for k in range(min(m, n), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic(i, j, k):
                        return k

        return 1
