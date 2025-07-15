class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        """Checks if an n x n matrix is valid, meaning every row and every column contains all the integers from 1 to n (inclusive).

        Args:
            matrix (list[list[int]]): The n x n matrix to validate.

        Returns:
            bool: True if the matrix is valid, False otherwise.

        Example:
            >>> checkValid([[1,2,3],[3,1,2],[2,3,1]])
            True
            >>> Solution().checkValid([[1,1,1],[1,2,3],[1,2,3]])
            False

        Time complexity: O(n^2), where n is the size of the matrix.
        Space complexity: O(1).
        """
        row_prod = math.prod(range(1, len(matrix) + 1))

        for i in range(len(matrix)):
            if math.prod(matrix[i]) != row_prod:
                return False

        for j in range(len(matrix[0])):
            if math.prod([matrix[i][j] for i in range(len(matrix))]) != row_prod:
                return False

        return True
