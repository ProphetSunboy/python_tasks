class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        """
        Calculates the number of paths in a grid from the top-left to the bottom-right corner,
        moving only down or right, such that the sum of the elements along each path is divisible by k.

        Each move adds the value of the cell to the current path sum.
        The result is returned modulo 10^9 + 7 due to potentially large outputs.

        Args:
            grid (List[List[int]]): A 2D integer matrix representing the grid.
            k (int): The divisor to check divisibility of the path sum.

        Returns:
            int: The number of valid paths whose sums are divisible by k, modulo 10^9 + 7.

        Example:
            Input: grid = [
                               [5, 2, 4],
                               [3, 0, 5],
                               [0, 7, 2]
                           ], k = 3
            Output: 2
            (There are 2 valid paths from (0,0) to (2,2) whose sum is divisible by 3.)

        Time Complexity: O(m * n * k), where m and n are the dimensions of the grid.
        Space Complexity: O(m * n * k).
        """
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if dp[i][j][r] > 0:
                        if i + 1 < m:
                            new_r = (r + grid[i + 1][j]) % k
                            dp[i + 1][j][new_r] = (
                                dp[i + 1][j][new_r] + dp[i][j][r]
                            ) % mod
                        if j + 1 < n:
                            new_r = (r + grid[i][j + 1]) % k
                            dp[i][j + 1][new_r] = (
                                dp[i][j + 1][new_r] + dp[i][j][r]
                            ) % mod

        return dp[m - 1][n - 1][0]
