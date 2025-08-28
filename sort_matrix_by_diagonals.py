class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Sorts the diagonals of a given n x n square matrix according to the following rules:

        - The diagonals in the bottom-left triangle (including the main diagonal) are sorted in non-increasing order.
        - The diagonals in the top-right triangle (excluding the main diagonal) are sorted in non-decreasing order.

        Args:
            grid (list[list[int]]): An n x n matrix of integers.

        Returns:
            list[list[int]]: The matrix after sorting its diagonals as specified.

        Example:
            >>> sortMatrix([
            ...     [3, 1, 2],
            ...     [4, 6, 5],
            ...     [9, 8, 7]
            ... ])
            [[7, 1, 2],
             [8, 6, 5],
             [9, 4, 3]]

        Time Complexity: O(n^2 log n), where n is the size of the matrix (due to sorting each diagonal).
        Space Complexity: O(n^2), for the output matrix.

        LeetCode: Beats 94.58% of submissions
        """
        s_matrix = [[0] * len(grid[0]) for _ in range(len(grid))]

        i = 0
        while i < len(grid):
            diag = []
            j = 0

            for k in range(i, len(grid)):
                diag.append(grid[k][j])
                j += 1

            diag.sort(reverse=True)

            j = 0
            for k in range(i, len(grid)):
                s_matrix[k][j] = diag[j]
                j += 1

            i += 1

        j = 1
        while j < len(grid[0]):
            diag = []
            i = 0

            for k in range(j, len(grid[0])):
                diag.append(grid[i][k])
                i += 1

            diag.sort()

            i = 0
            for k in range(j, len(grid[0])):
                s_matrix[i][k] = diag[i]
                i += 1

            j += 1

        return s_matrix
