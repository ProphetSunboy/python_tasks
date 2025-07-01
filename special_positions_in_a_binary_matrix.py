class Solution:
    def sum_of_col(self, mat: list[list[int]], col: int) -> int:
        """Calculates the sum of all elements in a specified column of a binary matrix.

        Args:
            mat (list[list[int]]): The binary matrix (list of lists of integers).
            col (int): The index of the column to sum.

        Returns:
            int: The sum of the elements in the specified column.

        Example:
            >>> sum_of_col([[1,0,0],[0,1,0],[1,0,0]], 0)
            2
            >>> sum_of_col([[1,0],[0,1]], 1)
            1
        """
        col_sum = 0

        for i in range(len(mat)):
            col_sum += mat[i][col]

        return col_sum

    def numSpecial(self, mat: list[list[int]]) -> int:
        """Returns the number of special positions in a binary matrix.

        A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0.

        Args:
            mat (list[list[int]]): An m x n binary matrix.

        Returns:
            int: The number of special positions in the matrix.

        Example:
            >>> numSpecial([[1,0,0],[0,0,1],[1,0,0]])
            1
            >>> numSpecial([[1,0,0],[0,1,0],[0,0,1]])
            3

        LeetCode: Beats 96.34% of submissions
        """
        special = 0

        for i in range(len(mat)):
            if sum(mat[i]) == 1:
                for j in range(len(mat[0])):
                    if mat[i][j] == 1:
                        if self.sum_of_col(mat, j) == 1:
                            special += 1

        return special
