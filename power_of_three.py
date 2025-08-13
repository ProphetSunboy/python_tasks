# First solution
class Solution:
    def divide_by_three(self, n):
        while n % 3 == 0:
            n //= 3
        return n

    def isPowerOfThree(self, n: int) -> bool:
        """
        Given an integer n, return true if it is a power of three.
        Otherwise, return false.
        """
        if n <= 0:
            return False
        return self.divide_by_three(n) == 1


# Second solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Determines if the given integer n is a power of three.

        An integer n is a power of three if there exists an integer x such that n == 3 ** x.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if n is a power of three, False otherwise.

        Example:
            >>> isPowerOfThree(27)
            True
            >>> isPowerOfThree(0)
            False
            >>> isPowerOfThree(9)
            True
            >>> isPowerOfThree(45)
            False

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 92.65% of submissions
        """
        pows = [
            1,
            3,
            9,
            27,
            81,
            243,
            729,
            2187,
            6561,
            19683,
            59049,
            177147,
            531441,
            1594323,
            4782969,
            14348907,
            43046721,
            129140163,
            387420489,
            1162261467,
        ]

        return n in pows
