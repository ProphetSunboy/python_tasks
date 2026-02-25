class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Sorts each matrix diagonal in ascending order and returns the resulting
        matrix.

        A matrix diagonal is a diagonal line of cells starting from some cell
        in either the topmost row or leftmost column and going in the
        bottom-right direction until reaching the matrix's end.
        For example, the matrix diagonal starting from mat[2][0], where mat is
        a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

        Args:
            mat (List[List[int]]): The input m x n matrix of integers.

        Returns:
            List[List[int]]: The matrix with each diagonal sorted in ascending
            order.

        Example:
            Input:
                mat = [
                    [3, 3, 1, 1],
                    [2, 2, 1, 2],
                    [1, 1, 1, 2]
                ]
            Output:
                [
                    [1, 1, 1, 1],
                    [1, 2, 2, 2],
                    [1, 2, 3, 3]
                ]

        Time Complexity: O(m * n * log k), where k is the length of the
            diagonal, m is the number of rows, and n is the number of columns.
        Space Complexity: O(m * n), for the output matrix and temporary storage.

        LeetCode: Beats 93.35% of submissions.
        """
        sorted_mat = [[0] * len(mat[0]) for _ in range(len(mat))]

        for j in range(len(mat[0])):
            curr_diag = []

            i = 0
            while i < len(mat) and j + i < len(mat[0]):
                curr_diag.append(mat[i][j + i])
                i += 1

            curr_diag.sort(reverse=True)

            i = 0
            while i < len(mat) and j + i < len(mat[0]):
                sorted_mat[i][j + i] = curr_diag.pop()
                i += 1

        for i in range(1, len(mat)):
            curr_diag = []

            j = 0
            while j < len(mat[0]) and i + j < len(mat):
                curr_diag.append(mat[i + j][j])
                j += 1

            curr_diag.sort(reverse=True)

            j = 0
            while j < len(mat[0]) and i + j < len(mat):
                sorted_mat[i + j][j] = curr_diag.pop()
                j += 1

        return sorted_mat
