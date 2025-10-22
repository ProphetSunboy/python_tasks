class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        """
        Compute the minimum number of operations required to make each column in
        the given grid strictly increasing.

        You are given an m x n matrix `grid` of non-negative integers.
        In one operation, you can increment any cell grid[i][j] by 1.
        The goal is to ensure that, for every column, each value is strictly greater than the one in the row above it.

        Args:
            grid (List[List[int]]): The m x n input matrix of non-negative integers.

        Returns:
            int: The minimum number of increment operations needed to make every column strictly increasing.

        Example:
            >>> minimumOperations([[3,2],[1,3],[3,4],[0,1]])
            15

        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
        Space Complexity: O(1)

        LeetCode: Beats 94.10% of submissions
        """
        ops = 0

        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i][j] <= grid[i - 1][j]:
                    ops += grid[i - 1][j] + 1 - grid[i][j]
                    grid[i][j] = grid[i - 1][j] + 1

        return ops
