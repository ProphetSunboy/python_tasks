class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Counts the number of negative numbers in a m x n matrix 'grid' where
        each row and column is sorted in non-increasing order.

        Args:
            grid (List[List[int]]): 2D matrix of integers, sorted
            non-increasingly both row-wise and column-wise.

        Returns:
            int: The total count of negative numbers in the matrix.

        Example:
            Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
            Output: 8
            Explanation: There are eight negative numbers in the matrix.

        Time Complexity: O(m + n), where m is the number of rows and n is the number of columns.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        count = 0
        n = len(grid[0])

        curr_row = n - 1
        for row in grid:
            while curr_row >= 0 and row[curr_row] < 0:
                curr_row -= 1
            count += n - (curr_row + 1)
        return count
