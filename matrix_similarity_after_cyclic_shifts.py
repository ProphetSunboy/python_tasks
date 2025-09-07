class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        """
        Determines if a matrix remains unchanged after performing k cyclic shifts on its rows.

        Given an m x n integer matrix `mat` and an integer `k`, perform the following process k times:
            - Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left by 1 position.
            - Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right by 1 position.

        After k such operations, return True if the resulting matrix is identical to the original matrix, otherwise return False.

        Args:
            mat (List[List[int]]): The input m x n matrix.
            k (int): The number of times to perform the cyclic shift process.

        Returns:
            bool: True if the matrix is unchanged after k operations, False otherwise.

        Example:
            >>> areSimilar([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2)
            True

        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
        Space Complexity: O(n), for temporary row storage.

        LeetCode: Beats 100% of submissions
        """
        for i in range(len(mat)):
            curr_row = [0] * len(mat[0])
            for j in range(len(mat[0])):
                if i % 2:
                    curr_row[(j + k) % len(mat[0])] = mat[i][j]
                else:
                    if j < k:
                        curr_row[-(abs(j - k) % len(mat[0]))] = mat[i][j]
                    else:
                        curr_row[(j - k) % len(mat[0])] = mat[i][j]

            if curr_row != mat[i]:
                return False

        return True
