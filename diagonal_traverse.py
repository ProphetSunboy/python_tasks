class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        """
        Given an m x n matrix mat, return a list of all elements of the matrix in diagonal order.

        The traversal starts at the top-left element and proceeds diagonally up-right and down-left alternately,
        covering all diagonals of the matrix.

        Args:
            mat (List[List[int]]): The input 2D matrix.

        Returns:
            List[int]: The elements of the matrix in diagonal order.

        Example:
            >>> findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
            [1,2,4,7,5,3,6,8,9]

        Time Complexity: O(m * n), where m and n are the dimensions of mat.
        Space Complexity: O(m * n)

        LeetCode: Beats 97.55% of submissions
        """
        diag_ord = []
        up = True
        i, j = 0, 0

        while i < len(mat) and j < len(mat[0]):
            diag_ord.append(mat[i][j])

            if up:
                i -= 1
                j += 1
                if i < 0 or j == len(mat[0]):
                    up = False
                    if j <= len(mat[0]) - 1:
                        i = 0
                    else:
                        i = i + 2
                        j -= 1
            else:
                i += 1
                j -= 1
                if j < 0 or i == len(mat):
                    up = True
                    if i <= len(mat) - 1:
                        j = 0
                    else:
                        i -= 1
                        j = j + 2

        return diag_ord
