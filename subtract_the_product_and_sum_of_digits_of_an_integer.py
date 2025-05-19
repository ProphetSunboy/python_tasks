class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        Given an integer number n, return the difference between the product of
        its digits and the sum of its digits.

        LeetCode Beats 100%
        """
        mul = 1
        s = 0

        while n > 0:
            digit = n % 10
            mul *= digit
            s += digit

            n //= 10

        return mul - s
