class FasterSolution:
    def construct2Dlist(self, original: list[int], m: int, n: int) -> list[list[int]]:
        """
        You are given a 0-indexed 1-dimensional (1D) integer list original, and
        two integers, m and n. You are tasked with creating a 2-dimensional (2D)
        list with  m rows and n columns using all the elements from original.

        The elements from indices 0 to n - 1 (inclusive) of original should form
        the first row of the constructed 2D list, the elements from indices n
        to 2 * n - 1 (inclusive) should form the second row of the constructed
        2D list, and so on.

        Return an m x n 2D list constructed according to the above procedure,
        or an empty 2D list if it is impossible.


        :param list[int] original: original list
        :param int m: number of rows in reshaped list
        :param int n: number of columns in reshaped list
        :returns list[list[int]] matrix: reshaped list if possible, otherwise empty list

        Time complexity: O((len(original) % n) * n)
        Space complexity: O(m * n)

        LeetCode: Beats 100%
        """
        if len(original) != m * n:
            return []

        matrix = []
        for i in range(0, len(original), n):
            matrix.append(original[i : i + n])

        return matrix


class SlowerSolution:
    def construct2Dlist(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []

        matrix = []
        for _ in range(m):
            matrix.append([0] * n)

        k = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = original[k]
                k += 1

        return matrix
