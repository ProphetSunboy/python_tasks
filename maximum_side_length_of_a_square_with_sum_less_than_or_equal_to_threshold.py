class Solution:
    def maxSideLength(self, mat, threshold):
        """
        Given an m x n matrix 'mat' and an integer 'threshold',
        return the maximum side-length of a square with a sum less than or equal to threshold.
        Return 0 if no such square exists.

        Args:
            mat (List[List[int]]): 2D grid of integers.
            threshold (int): Maximum allowed sum for the square.

        Returns:
            int: The largest possible side length of a square that meets the sum requirement.

        Example:
            Input: mat = [[1,3,1],[4,2,1],[2,1,1]], threshold = 4
            Output: 1

        Time Complexity: O(m * n * log(min(m, n))), where m and n are the dimensions of mat.
        Space Complexity: O(m * n)
        """
        m, n = len(mat), len(mat[0])

        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = (
                    mat[i - 1][j - 1]
                    + pref[i - 1][j]
                    + pref[i][j - 1]
                    - pref[i - 1][j - 1]
                )

        def can(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        pref[i + k][j + k]
                        - pref[i][j + k]
                        - pref[i + k][j]
                        + pref[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 0, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
