class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        """
        Given a 0-indexed m x n integer matrix `grid`, computes the width of each column.
        The width of a column is defined as the maximum number of characters needed to represent any integer in that column,
        including the negative sign for negative numbers.

        For example, for grid = [[-10], [3], [12]], the width of the only column is 3, since "-10" has 3 characters.

        Args:
            grid (List[List[int]]): The matrix of integers.

        Returns:
            List[int]: A list of size n where the i-th element is the width of the i-th column.

        Example:
            >>> findColumnWidth([[-15,1,3],[15,7,12],[5,6,-2]])
            [3, 1, 2]

        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
        Space Complexity: O(n), for the output list.

        LeetCode: Beats 100% of submissions
        """
        ans = []

        for j in range(len(grid[0])):
            max_width = 0
            for i in range(len(grid)):
                row_width = len(str(grid[i][j]))

                if row_width > max_width:
                    max_width = row_width

            ans.append(max_width)

        return ans
