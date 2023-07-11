class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Given a 2D integer array matrix, return the transpose of matrix.

        The transpose of a matrix is the matrix flipped over its main diagonal,
        switching the matrix's row and column indices.
        """
        transposed = []

        for i in range(len(matrix[0])):
            transposed.append([0] * len(matrix))

        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                transposed[j][i] = matrix[i][j]

        return transposed