class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        """
        Checks if a 2D grid satisfies the following conditions for every cell grid[i][j]:
            1. If there is a cell below (i.e., i + 1 < m), then grid[i][j] == grid[i + 1][j].
            2. If there is a cell to the right (i.e., j + 1 < n), then grid[i][j] != grid[i][j + 1].

        Returns True if all cells satisfy these conditions, otherwise returns False.

        Args:
            grid (list[list[int]]): 2D list of integers representing the grid.

        Returns:
            bool: True if the grid satisfies the conditions, False otherwise.

        Example:
            >>> satisfiesConditions([[1,0,2],[1,0,2]])
            True

        Time Complexity: O(m * n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i < len(grid) - 1:
                    if grid[i][j] != grid[i + 1][j]:
                        return False
                if j < len(grid[0]) - 1:
                    if grid[i][j] == grid[i][j + 1]:
                        return False

        return True
