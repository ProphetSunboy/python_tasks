class FasterSolution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        """
        You are given an m x n matrix mat and two integers r and c representing
        the number of rows and the number of columns of the wanted reshaped
        matrix.

        The reshaped matrix should be filled with all the elements of the
        original matrix in the same row-traversing order as they were.

        If the reshape operation with given parameters is possible and legal,
        return the new reshaped matrix; Otherwise, return the original matrix.


        :param list[list[int]] mat: original matrix
        :param int r: number of rows in reshaped matrix
        :param int c: number of columns in reshaped matrix
        :returns list[list[int]] reshaped: reshaped matrix if possible, otherwise mat

        Time complexity: O(r * c)
        Space complexity: O(r * c)

        LeetCode: Beats 97.44%
        """
        if len(mat) * len(mat[0]) != r * c:
            return mat

        reshaped = []

        for _ in range(r):
            reshaped.append([0] * c)

        k, l = 0, 0
        for i in range(r):
            for j in range(c):
                reshaped[i][j] = mat[k][l]
                l = (l + 1) % len(mat[0])
                k += l == 0

        return reshaped


class SlowerSolution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        reshaped = [[]]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(reshaped[-1]) == c:
                    reshaped.append([])

                reshaped[-1].append(mat[i][j])

        return reshaped
