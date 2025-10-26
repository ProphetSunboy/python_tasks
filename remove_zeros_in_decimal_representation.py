class Solution:
    def removeZeros(self, n: int) -> int:
        """
        Remove all zeros from the decimal representation of a given positive integer.

        Args:
            n (int): A positive integer.

        Returns:
            int: The integer obtained by removing all zeros from the decimal representation of n.

        Example:
            >>> removeZeros(102030)
            123
            >>> removeZeros(1000)
            1
            >>> removeZeros(507)
            57

        Time Complexity: O(log n) — processes each digit of n.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        num = 0
        curr_pow = 0

        while n > 0:
            d = n % 10
            n //= 10

            if d > 0:
                num += d * (10**curr_pow)
                curr_pow += 1

        return num
