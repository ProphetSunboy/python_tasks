class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Finds the size of the largest subset of binary strings from `strs` such
        that the subset contains at most `m` zeros and `n` ones.

        Args:
            strs (List[str]): List of binary strings.
            m (int): Maximum number of zeros allowed in the subset.
            n (int): Maximum number of ones allowed in the subset.

        Returns:
            int: The size of the largest subset meeting the constraints.

        Example:
            Input: strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
            Output: 4
            Explanation: The largest subset is ["10", "0001", "1", "0"], which has at most 5 zeros and 3 ones.

        Time Complexity: O(l * m * n), where l is the number of strings in strs.
        Space Complexity: O(m * n).
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
