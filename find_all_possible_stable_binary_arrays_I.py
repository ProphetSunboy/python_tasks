class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        """
        Calculate the total number of stable binary lists.

        You are given three positive integers: zero, one, and limit.

        A binary list arr is called stable if:
            - The number of occurrences of 0 in arr is exactly zero.
            - The number of occurrences of 1 in arr is exactly one.
            - Each sublist of arr with a size greater than 'limit' contains
            both 0 and 1.

        Returns the total number of stable binary lists, modulo 10^9 + 7.

        Args:
            zero (int): Number of zeros in the list.
            one (int): Number of ones in the list.
            limit (int): Maximum allowed run length of a single digit.

        Returns:
            int: The number of stable binary lists modulo 10^9 + 7.

        Example:
            Input: zero = 1, one = 1, limit = 2
            Output: 2
            Explanation: There are two stable binary lists: [0, 1] and [1, 0].

        Time Complexity: O(zero * one)
        Space Complexity: O(zero * one)

        LeetCode: Beats 93.94% of submissions
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
