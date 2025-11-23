class Solution:
    def sumAndMultiply(self, n: int) -> int:
        """
        Given an integer n, construct a new integer x by concatenating all
        non-zero digits of n in their original order.
        If there are no non-zero digits, then x = 0.

        Let sum_x be the sum of digits in x.
        Return the value of x * sum_x.

        Args:
            n (int): The input integer.

        Returns:
            int: The product of x and the sum of its digits.

        Example:
            Input: n = 102304
            Non-zero digits: 1, 2, 3, 4 => x = 1234
            Sum of digits in x: 1 + 2 + 3 + 4 = 10
            Output: 1234 * 10 = 12340

            Input: n = 0
            Output: 0

        Time Complexity: O(k), where k is the number of digits in n.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        x_sum = 0
        x = 0
        curr_pow = 0

        while n > 0:
            d = n % 10
            if d > 0:
                x_sum += d
                x += d * 10**curr_pow
                curr_pow += 1

            n //= 10

        return x * x_sum
