class Solution:
    def get_column_max(self, matrix: list[list[int]], col: int) -> int:
        """
        Returns the maximum value in the specified column of the given matrix.

        Args:
            matrix (list[list[int]]): The 2D list of integers to search.
            col (int): The column index for which to find the maximum value.

        Returns:
            int: The maximum value found in the specified column.

        Example:
            >>> get_column_max([[1, 2], [3, 4]], 1)
            4
        """
        col_max = 0

        for i in range(len(matrix)):
            if matrix[i][col] > col_max:
                col_max = matrix[i][col]

        return col_max

    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Given a 0-indexed m x n integer matrix, create a new matrix called answer.
        The answer matrix is initially a copy of the input matrix, but every element
        with the value -1 is replaced by the maximum element in its respective column.

        Args:
            matrix (list[list[int]]): The input 2D list of integers.

        Returns:
            list[list[int]]: The modified matrix with -1s replaced by the column maximums.

        Example:
            >>> modifiedMatrix([[1, -1], [3, 4]])
            [[1, 4], [3, 4]]

        Time complexity: O(m * n), where m is the number of rows and n is the number of columns.
        Space complexity: O(m * n), for the answer matrix.

        LeetCode: Beats 100% of submissions
        """
        cols_max = [-1] * len(matrix[0])
        answer = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(answer)):
            for j in range(len(answer[0])):
                if matrix[i][j] != -1:
                    answer[i][j] = matrix[i][j]
                else:
                    if cols_max[j] != -1:
                        answer[i][j] = cols_max[j]
                    else:
                        col_max = self.get_column_max(matrix, j)
                        answer[i][j] = col_max
                        cols_max[j] = col_max

        return answer
