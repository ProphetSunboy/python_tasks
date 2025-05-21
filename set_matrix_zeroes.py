class Solution:
    """
    Given an m x n integer matrix matrix, if an element is 0, set its entire row
    and column to 0's.


    LeetCode Beats 100%
    """

    def setRowColZero(self, matrix: list[list[int]], row: int, col: int) -> None:
        """Set entire row and column to zero."""
        matrix[row] = [0] * len(matrix[0])

        for i in range(len(matrix)):
            matrix[i][col] = 0

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Set rows and columns to 0 if they contain a 0.
        Modifies matrix in-place.
        """
        # Find all zero positions
        zeros = [
            (i, j)
            for i in range(len(matrix))
            for j in range(len(matrix[0]))
            if matrix[i][j] == 0
        ]

        # Set corresponding rows and columns to zero
        for row, col in zeros:
            self.setRowColZero(matrix, row, col)
