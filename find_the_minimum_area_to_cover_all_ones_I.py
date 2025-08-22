class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        """
        Given a 2D binary list `grid`, find the smallest-area axis-aligned rectangle that covers all the 1's in the grid.

        Returns the minimum possible area of such a rectangle.

        Args:
            grid (list[list[int]]): 2D list of 0's and 1's.

        Returns:
            int: The minimum area of a rectangle that covers all 1's in the grid.

        Example:
            >>> minimumArea([[0,1,0],[1,0,1]])
            6

        Time Complexity: O(m * n), where m and n are the dimensions of the grid.
        Space Complexity: O(1)

        LeetCode: Beats 90.65% of submissions
        """
        up, low, left, right = 10**4, -1, 10**4, -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i < up:
                        up = i
                    if i > low:
                        low = i
                    if j < left:
                        left = j
                    if j > right:
                        right = j

        return (right - left + 1) * (low - up + 1)
