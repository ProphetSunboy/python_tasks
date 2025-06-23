class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        """Finds the missing and repeated values in a grid containing numbers from 1 to n^2.

        The grid is a 2D list of integers where one number is missing and one number is repeated.
        The function returns a list [repeated, missing].

        Args:
            grid (list[list[int]]): 2D grid of integers with one missing and one repeated value.

        Returns:
            list[int]: [repeated_value, missing_value]

        Example:
            >>> findMissingAndRepeatedValues([[1,3],[2,2]])
            [2, 4]

        Time complexity: O(N^2), where N is the length of one grid dimension.
        Space complexity: O(N^2), for storing counts of numbers.

        LeetCode: Beats 92.54% of submissions
        """
        ans = [0, 0]
        d = {key: 1 for key in range(1, len(grid) ** 2 + 1)}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not d.pop(grid[i][j], 0):
                    ans[0] = grid[i][j]

        for key in d.keys():
            ans[1] = key

        return ans
