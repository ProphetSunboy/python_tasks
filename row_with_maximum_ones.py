class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        """
        Given a m x n binary matrix mat, find the 0-indexed position of the row that
        contains the maximum number of ones, and the number of ones in that row.

        If multiple rows have the same maximum count of ones, return the row with the smallest index.

        Args:
            mat (list[list[int]]): A binary matrix of size m x n.

        Returns:
            list[int]: A list [row_index, ones_count], where row_index is the index
            of the row with the most ones, and ones_count is the number of ones in that row.

        Example:
            >>> rowAndMaximumOnes([[0,1],[1,0]])
            [0, 1]
            >>> rowAndMaximumOnes([[0,0,0],[0,1,1]])
            [1, 2]

        Time complexity: O(m * n), where m is the number of rows and n is the number of columns.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        max_row = [0, sum(mat[0])]

        for i in range(1, len(mat)):
            curr_ones = sum(mat[i])

            if curr_ones > max_row[1]:
                max_row[0] = i
                max_row[1] = curr_ones

        return max_row
