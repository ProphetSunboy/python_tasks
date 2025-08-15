# First solution
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


# Second solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Determines if the given integer n is a power of four.

        An integer n is a power of four if there exists an integer x such that n == 4 ** x.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if n is a power of four, False otherwise.

        Example:
            >>> isPowerOfFour(16)
            True
            >>> isPowerOfFour(5)
            False

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        if n <= 0:
            return False

        nums = [
            1,
            4,
            16,
            64,
            256,
            1024,
            4096,
            16384,
            65536,
            262144,
            1048576,
            4194304,
            16777216,
            67108864,
            268435456,
            1073741824,
        ]

        return n in nums
