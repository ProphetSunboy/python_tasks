class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Given an n x n 2D matrix representing an image, rotate the image
        by 90 degrees (clockwise).

        You have to rotate the image in-place, which means you have to modify
        the input 2D matrix directly. DO NOT allocate another 2D matrix and do
        the rotation.

        :param list[list[int]] matrix: n x n 2D matrix representing an image
        :returns None


        Time complexity: O(n^2)
        Space complexity: O(1)

        LeetCode: Beats 97.86%
        """
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                (
                    matrix[i][j],
                    matrix[j][n - i - 1],
                    matrix[n - j - 1][i],
                    matrix[n - i - 1][n - j - 1],
                ) = (
                    matrix[n - j - 1][i],
                    matrix[i][j],
                    matrix[n - i - 1][n - j - 1],
                    matrix[j][n - i - 1],
                )
