class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """
        Given an n x n zero-filled integer matrix, increment specified submatrices
        by one for a set of queries and return the final matrix.

        For each query [row1, col1, row2, col2], add 1 to every element in the
        submatrix from (row1, col1) to (row2, col2), inclusive.

        Args:
            n (int): Size of the square matrix.
            queries (List[List[int]]): List of queries, each specifying
                a submatrix as [row1, col1, row2, col2].

        Returns:
            List[List[int]]: The matrix after applying all queries.

        Example:
            Input:  n = 3, queries = [[1,1,2,2],[0,0,1,1]]
            Output: [[1,1,0],[1,2,1],[0,1,1]]

        Time Complexity: O(n^2 + k), where k is the number of queries.
        Space Complexity: O(n^2)
        """
        mat = [[0] * n for _ in range(n)]

        for row1, col1, row2, col2 in queries:
            mat[row1][col1] += 1
            if col2 + 1 < n:
                mat[row1][col2 + 1] -= 1
            if row2 + 1 < n:
                mat[row2 + 1][col1] -= 1
            if row2 + 1 < n and col2 + 1 < n:
                mat[row2 + 1][col2 + 1] += 1

        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]

        for j in range(n):
            for i in range(1, n):
                mat[i][j] += mat[i - 1][j]

        return mat
