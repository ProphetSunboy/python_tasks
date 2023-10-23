class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Given an integer n, return True if it is a power of four. Otherwise,
        return False.

        An integer n is a power of four, if there exists an integer x such that
        n == 4x.

        :param int n: integer number
        :returns bool is_power: an integer n is a power of four

        Time complexity: O(logn)
        Space complexity: O(1)

        LeetCode: Beats 98.81%
        """
        if n == 1:
            return True
        elif n % 10 not in [4, 6]:
            return False

        val = 1
        while val < n:
            val *= 4

        return val == n
