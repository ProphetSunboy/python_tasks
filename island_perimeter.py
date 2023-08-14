class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """
        You are given row x col grid representing a map where grid[i][j] = 1
        represents land and grid[i][j] = 0 represents water. Determine the
        perimeter of the island.

        Grid cells are connected horizontally/vertically (not diagonally).
        The grid is completely surrounded by water, and there is exactly one
        island (i.e., one or more connected land cells).


        :param list[list[int]] grid: row x col grid representing a map of island
        :returns int perimeter: perimeter of the island


        Time complexity: O(n^2)
        Space complexity: O(1)

        LeetCode: Beats 92.16%
        """
        p = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        p += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        p += 1
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        p += 1
                    if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                        p += 1

        return p
