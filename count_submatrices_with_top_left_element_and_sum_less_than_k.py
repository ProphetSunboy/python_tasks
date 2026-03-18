class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        """
        Given a 0-indexed integer matrix grid and an integer k, return the
        number of submatrices that contain the top-left element of the grid
        and have a sum less than or equal to k.

        Args:
            grid (List[List[int]]): The input matrix.
            k (int): The integer threshold for the sum of submatrices.

        Returns:
            int: The number of submatrices containing the top-left element with
                sum less than or equal to k.

        Example:
            Input: grid = [[7,6,3],[6,6,1]], k = 18
            Output: 4

        Time Complexity: O(R * C), where R and C are the number of rows and
        columns in grid.
        Space Complexity: O(1)

        LeetCode: Beats 92.41% of submissions.
        """
        R, C = len(grid), len(grid[0])
        res = 0

        for r in range(R):
            row_sum = 0
            for c in range(C):
                row_sum += grid[r][c]

                if r > 0:
                    grid[r][c] = row_sum + grid[r - 1][c]
                else:
                    grid[r][c] = row_sum

                if grid[r][c] <= k:
                    res += 1
                else:
                    break

        return res
