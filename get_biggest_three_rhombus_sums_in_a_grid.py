class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        """
        Given an m x n integer matrix grid, returns the biggest three distinct
        rhombus border sums in the grid in descending order.
        A rhombus sum is defined as the sum of the elements that form the
        border of a regular rhombus (a square rotated 45 degrees), with each
        corner centered in a grid cell. The rhombus can have an area of 0
        (single cell).

        If there are fewer than three distinct rhombus sums,
        returns all of them.

        Args:
            grid (list[list[int]]): 2D grid of integers.

        Returns:
            list[int]: The largest three distinct rhombus border sums in
            descending order.

        Example:
            Input: grid = [[3,4,5,1,3],
                           [3,3,4,2,3],
                           [20,30,200,40,10],
                           [1,5,5,4,1],
                           [4,3,2,2,5]]
            Output: [228,216,211]

        Time Complexity: O(m * n * min(m, n)), where m and n are the number of
                rows and columns.
        Space Complexity: O(m * n), due to auxiliary lists for diagonals.
        """
        m, n = len(grid), len(grid[0])
        d1 = [[0] * (n + 2) for _ in range(m + 2)]
        d2 = [[0] * (n + 2) for _ in range(m + 2)]

        for r in range(m):
            for c in range(n):
                d1[r + 1][c + 1] = grid[r][c] + d1[r][c]
                d2[r + 1][c + 1] = grid[r][c] + d2[r][c + 2]

        top_sums = set()

        for r in range(m):
            for c in range(n):
                top_sums.add(grid[r][c])

                for L in range(1, m):
                    top_r, top_c = r, c
                    bott_r, bott_c = r + 2 * L, c
                    left_r, left_c = r + L, c - L
                    right_r, right_c = r + L, c + L

                    if bott_r >= m or left_c < 0 or right_c >= n:
                        break

                    s1 = d2[left_r + 1][left_c + 1] - d2[top_r][top_c + 2]
                    s2 = d1[bott_r + 1][bott_c + 1] - d1[left_r][left_c]
                    s3 = d2[bott_r + 1][bott_c + 1] - d2[right_r][right_c + 2]
                    s4 = d1[right_r + 1][right_c + 1] - d1[top_r][top_c]

                    current_sum = (
                        s1
                        + s2
                        + s3
                        + s4
                        - grid[top_r][top_c]
                        - grid[bott_r][bott_c]
                        - grid[left_r][left_c]
                        - grid[right_r][right_c]
                    )
                    top_sums.add(current_sum)

        return sorted(list(top_sums), reverse=True)[:3]
