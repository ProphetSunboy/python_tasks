class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        """
        Given m, n, and indices, return the number of odd-valued cells in the
        matrix after applying the increment to all locations in indices.

        There is an m x n matrix that is initialized to all 0's. There is also a
        2D array indices where each indices[i] = [ri, ci] represents a 0-indexed
        location to perform some increment operations on the matrix.

        For each location indices[i], do both of the following:

            Increment all the cells on row ri.
            Increment all the cells on column ci.

        :param int m: number of rows in matrix
        :param int n: number of columns in matrix
        :param list[list[int]] indices: locations to perform some increment
        operations on the matrix
        :returns int number_odds: the number of odd-valued cells in the matrix
        after applying the increment to all locations in indices

        Time complexity: O(k*(m+n)), where k = len(indices)
        Space complexity: O(1)

        LeetCode: Beats 96.75%
        """
        number_odds = 0
        matrix = []

        for _ in range(m):
            matrix.append([0] * n)

        for idx in indices:
            for j in range(n):
                matrix[idx[0]][j] += 1

            for i in range(m):
                matrix[i][idx[1]] += 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2:
                    number_odds += 1

        return number_odds
