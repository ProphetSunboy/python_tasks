class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        """
        Determines if it is possible to change at most one cell in a 3x3 grid of 'B' (black) and 'W' (white)
        so that there exists a 2x2 square where all four cells are the same color.

        Args:
            grid (list[list[str]]): A 3x3 matrix containing only 'B' and 'W' characters.

        Returns:
            bool: True if it is possible to form a 2x2 square of the same color with at most one change, False otherwise.

        Example:
            >>> canMakeSquare([['B','W','B'],['B','W','W'],['B','W','B']])
            True

        Time Complexity: O(1) (since the grid size is fixed at 3x3)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for i in range(len(grid) - 1):
            for j in range(len(grid[0]) - 1):
                colors = {"B": 0, "W": 0}

                colors[grid[i][j]] += 1
                colors[grid[i][j + 1]] += 1
                colors[grid[i + 1][j]] += 1
                colors[grid[i + 1][j + 1]] += 1

                if colors["B"] >= 3 or colors["W"] >= 3:
                    return True

        return False
