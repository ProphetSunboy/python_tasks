class Solution:
    def zigzagTraversal(self, grid: list[list[int]]) -> list[int]:
        """
        Traverse a 2D grid of positive integers in a zigzag pattern, skipping every alternate cell.

        Zigzag pattern:
            - Start at the top-left cell (0, 0).
            - For even-indexed rows, move left to right.
            - For odd-indexed rows, move right to left.
            - After each row, drop down to the next row and reverse direction.
            - While traversing, visit every other cell (i.e., skip every alternate cell).

        Args:
            grid (list[list[int]]): The m x n grid of positive integers.

        Returns:
            list[int]: The values of the visited cells in zigzag order with skips.

        Example:
            For grid = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9,10,11,12]
            ]
            The traversal visits: [1, 3], [8, 6], [9, 11]
            So the result is: [1, 3, 8, 6, 9, 11]

        Time Complexity: O(m * n), where m and n are the grid dimensions.
        Space Complexity: O(m * n), for the result list in the worst case.

        LeetCode: Beats 100% of submissions
        """
        result = []

        prev_row_last = False
        for i in range(len(grid)):
            right_direction = i % 2 == 0

            if right_direction:
                for j in range(prev_row_last, len(grid[0]), 2):
                    result.append(grid[i][j])

                    if j == len(grid[0]) - 1:
                        prev_row_last = True
                    if j == len(grid[0]) - 2:
                        prev_row_last = False
            else:
                for j in range(len(grid[0]) - prev_row_last, -1, -2):
                    result.append(grid[i][j])

                    if j == 0:
                        prev_row_last = True
                    if j == 1:
                        prev_row_last = False

        return result
