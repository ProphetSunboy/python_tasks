class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        Given an m x n integer matrix grid and an integer k, for every
        contiguous k x k submatrix of grid, compute the minimum absolute
        difference between any two distinct values within that submatrix.

        Returns a 2D list ans of size (m - k + 1) x (n - k + 1), where ans[i][j]
        is the minimum absolute difference in the submatrix whose top-left
        corner is (i, j) in grid.

        Note:
            - If all elements in the submatrix have the same value,
            the answer is 0.
            - A submatrix (x1, y1, x2, y2) consists of all cells matrix[x][y]
              where x1 <= x <= x2 and y1 <= y <= y2.

        Args:
            grid (list[list[int]]): The input matrix.
            k (int): The size of the submatrix.

        Returns:
            list[list[int]]: The minimum absolute difference for each k x k
            submatrix.

        Example:
            Input: grid = [[1,8],[3,-2]], k = 2
            Output: [[2]]

        Time Complexity: O((m - k + 1) * (n - k + 1) * k^2 * log(k^2)).
        Space Complexity: O(k^2) for each submatrix processed.
        """
        m, n = len(grid), len(grid[0])
        res = []

        for i in range(m - k + 1):
            row_results = []
            for j in range(n - k + 1):
                sub = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        sub.append(grid[r][c])

                unique_sorted = sorted(list(set(sub)))

                if len(unique_sorted) < 2:
                    row_results.append(0)
                    continue

                min_diff = float("inf")
                for idx in range(len(unique_sorted) - 1):
                    diff = unique_sorted[idx + 1] - unique_sorted[idx]
                    min_diff = min(min_diff, diff)

                row_results.append(min_diff)
            res.append(row_results)

        return res
