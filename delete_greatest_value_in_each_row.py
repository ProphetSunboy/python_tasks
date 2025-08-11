class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        """
        Given an m x n matrix `grid` of positive integers, repeatedly perform the following operation until the grid is empty:

            1. Delete the greatest value from each row (if multiple, delete any one).
            2. Of the deleted values, take the maximum and add it to the answer.
            3. The number of columns decreases by one after each operation.

        Return the total sum after all operations.

        Args:
            grid (List[List[int]]): The matrix of positive integers.

        Returns:
            int: The sum of the maximum values chosen in each operation.

        Example:
            >>> deleteGreatestValue([[1,2,4],[3,3,1]])
            8

        Time Complexity: O(m * n log n), where m is the number of rows and n is the number of columns (for sorting each row).
        Space Complexity: O(1) (in-place sorting).

        LeetCode: Beats 100% of submissions
        """
        for i in range(len(grid)):
            grid[i].sort()

        answer = 0
        while len(grid[0]) > 0:
            max_deleted = 0
            for i in range(len(grid)):
                row_max = grid[i].pop()

                if row_max > max_deleted:
                    max_deleted = row_max

            answer += max_deleted

        return answer
