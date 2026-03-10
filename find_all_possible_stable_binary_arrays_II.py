class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        """
        Given a list of unique binary strings `nums` containing n binary
        strings, each of length n, return a binary string of length n that does
        not appear in `nums`.
        If there are multiple answers, you may return any of them.

        Args:
            nums (List[str]): List of unique binary strings of length n.

        Returns:
            str: A binary string of length n not present in `nums`.

        Example:
            Input: nums = ["01", "10"]
            Output: "00" or "11"

        Time Complexity: O(n), where n is the length of each string and the
                count of strings.
        Space Complexity: O(1), as only a constant amount of extra space is
                used.
        """
        MOD = 10**9 + 7

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                res0 = dp0[i - 1][j] + dp1[i - 1][j]
                if i > limit:
                    res0 -= dp1[i - limit - 1][j]
                dp0[i][j] = res0 % MOD

                res1 = dp0[i][j - 1] + dp1[i][j - 1]
                if j > limit:
                    res1 -= dp0[i][j - limit - 1]
                dp1[i][j] = res1 % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
