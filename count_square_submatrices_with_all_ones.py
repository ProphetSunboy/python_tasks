class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        """
        Counts the number of square submatrices with all ones in a given binary matrix.

        Args:
            matrix (list[list[int]]): A 2D list representing the binary matrix (containing only 0s and 1s).

        Returns:
            int: The total number of square submatrices where all elements are 1.

        Example:
            >>> countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])
            15

        Time Complexity: O(m * n * min(m, n)), where m and n are the dimensions of the matrix.
        Space Complexity: O(1)
        """
        sqr_sub = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    sqr_sub += 1
                    k = j + 1
                    if k == len(matrix[0]) or matrix[i][k] == 0:
                        continue

                    while k < len(matrix[0]) - 1 and matrix[i][k] == 1:
                        k += 1

                    if matrix[i][k] == 0:
                        k -= 1

                    for p in range(k - j + 1, 1, -1):
                        sqr = True
                        for l in range(j, j + p):
                            if not sqr:
                                break
                            for h in range(i + 1, i + p):
                                if h == len(matrix) or matrix[h][l] == 0:
                                    sqr = False
                                    break

                        sqr_sub += sqr

        return sqr_sub
