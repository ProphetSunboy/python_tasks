class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Given a 2D grid of size m x n and an integer k. You need to shift the
        grid k times.

        In one shift operation:

        Element at grid[i][j] moves to grid[i][j + 1].
        Element at grid[i][n - 1] moves to grid[i + 1][0].
        Element at grid[m - 1][n - 1] moves to grid[0][0].
        Return the 2D grid after applying shift operation k times.

        LeetCode Beats 100%
        """
        g = []
        m, n = len(grid), len(grid[0])
        for _ in range(m):
            g.append([0] * n)

        for i in range(m):
            for j in range(n):
                shift = (n * i) + j + k
                row = shift // n % m
                col = shift % n
                g[row][col] = grid[i][j]

        return g
