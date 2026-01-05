class Solution:
    def maxMatrixSum(self, matrix):
        """
        Given an n x n integer matrix, you can perform the following operation
        any number of times:
            Choose any two adjacent elements of the matrix and multiply each of
            them by -1.
        Two elements are considered adjacent if and only if they share a border.

        The goal is to maximize the sum of the matrix's elements.
        Return the maximum sum of the matrix's elements that can be achieved
        using the allowed operations.

        Args:
            matrix (List[List[int]]): An n x n list of lists of integers.

        Returns:
            int: The maximum sum of the matrix's elements after applying any
            number of allowed operations.

        Example:
            Input: matrix = [[1, -1], [-1, 1]]
            Output: 4
            # By flipping the two -1's, all elements become 1, sum is 4.

        Time Complexity: O(n^2), where n is the number of rows in the matrix.
        Space Complexity: O(1), except for the input and minor variables.
        """
        total = 0
        min_abs = float("inf")
        neg_count = 0

        for row in matrix:
            for x in row:
                total += abs(x)
                min_abs = min(min_abs, abs(x))
                if x < 0:
                    neg_count += 1

        if neg_count % 2 == 1:
            total -= 2 * min_abs

        return total
