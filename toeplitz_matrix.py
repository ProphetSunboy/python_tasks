class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        """
        Given an m x n matrix, return True if the matrix is Toeplitz. Otherwise,
        return False.

        A matrix is Toeplitz if every diagonal from top-left to bottom-right has
        the same elements.

        :param list[list[int]] matrix: m x n matrix
        :returns bool is_toeplitz: every diagonal of matrix from top-left to
        bottom-right has the same elements

        Time complexity: O(m*n)
        Space complexity: O(1)

        LeetCode: Beats 99.35%
        """

        for j in range(len(matrix[0])):
            curr = matrix[0][j]
            i, k = 1, j + 1

            while i < len(matrix) and k < len(matrix[0]):
                if matrix[i][k] != curr:
                    return False

                i += 1
                k += 1

        for i in range(len(matrix)):
            curr = matrix[i][0]
            k, j = i + 1, 1

            while j < len(matrix[0]) and k < len(matrix):
                if matrix[k][j] != curr:
                    return False

                j += 1
                k += 1

        return True


class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        """
        Given an m x n matrix, return True if the matrix is Toeplitz. Otherwise,
        return False.

        A matrix is Toeplitz if every diagonal from top-left to bottom-right has
        the same elements.

        :param list[list[int]] matrix: m x n matrix
        :returns bool is_toeplitz: every diagonal of matrix from top-left to
        bottom-right has the same elements

        Time complexity: O(m*n)
        Space complexity: O(1)

        LeetCode: Beats 94.47%
        """

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True


class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        """
        Given an m x n matrix, return True if the matrix is Toeplitz. Otherwise,
        return False.

        A matrix is Toeplitz if every diagonal from top-left to bottom-right has
        the same elements.

        :param list[list[int]] matrix: m x n matrix
        :returns bool is_toeplitz: every diagonal of matrix from top-left to
        bottom-right has the same elements

        Time complexity: O(m*n)
        Space complexity: O(1)

        LeetCode: Beats 99.35%
        """

        for i in range(1, len(matrix)):
            if matrix[i][1:] != matrix[i - 1][:-1]:
                return False

        return True
