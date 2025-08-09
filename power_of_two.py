from math import log


# First solution
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Given an integer n, return true if it is a power of two.
        Otherwise, return false.
        """
        if n <= 0:
            return False
        val = round(log(n, 2), 10)
        return val == int(val)


# Second solution
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Determines if the given integer n is a power of two.

        An integer n is a power of two if there exists an integer x such that n == 2 ** x.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if n is a power of two, False otherwise.

        Examples:
            >>> isPowerOfTwo(1)
            True
            >>> isPowerOfTwo(16)
            True
            >>> isPowerOfTwo(18)
            False

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for i in range(32):
            if n == 2**i:
                return True

        return False
