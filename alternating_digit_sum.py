class Solution:
    def alternateDigitSum(self, n: int) -> int:
        """
        You are given a positive integer n. Each digit of n has a sign according
        to the following rules:

            The most significant digit is assigned a positive sign.
            Each other digit has an opposite sign to its adjacent digits.

        Return the sum of all digits with their corresponding sign.

        :param int n: integer number
        :returns int alt_sum: alternating digit sum

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 98.30%
        """
        alt_sum = 0
        sign = 1 if len(str(n)) % 2 else -1

        while n >= 1:
            n, m = n // 10, n % 10
            alt_sum += sign * m
            sign = -sign

        return alt_sum
