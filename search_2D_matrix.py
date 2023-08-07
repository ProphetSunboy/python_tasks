class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Given an integer target, return True if target is in matrix or False
        otherwise.

        You are given an m x n integer matrix matrix with the following two
        properties:

            Each row is sorted in non-decreasing order.
            The first integer of each row is greater than the last integer of
            the previous row.

        :param list[list[int]] matrix: matrix of integer numbers
        :param int target: number to be found
        :returns bool res: is the target in the matrix

        Time complexity: O(nlog(n))
        Space complexity: O(1)


        LeetCode: Beats 99.72%
        """
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                return target in matrix[mid]
