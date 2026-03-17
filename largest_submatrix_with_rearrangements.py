class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        Given a binary matrix of size m x n, where you are allowed to rearrange
        the columns in any order, return the area of the largest submatrix made
        up of only 1's after optimally reordering the columns.

        Args:
            matrix (List[List[int]]): Binary matrix (m x n).

        Returns:
            int: The area of the largest submatrix consisting only of
            1's after optimally reordering columns.

        Example:
            Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
            Output: 4

        Time Complexity: O(m * n log n)
        Space Complexity: O(m * n)
        """
        m, n = len(matrix), len(matrix[0])
        ans = 0

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        for i in range(m):
            heights = sorted(matrix[i], reverse=True)
            for j, h in enumerate(heights):
                if h == 0:
                    break
                ans = max(ans, h * (j + 1))

        return ans
