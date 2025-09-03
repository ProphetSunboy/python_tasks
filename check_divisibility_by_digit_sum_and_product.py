class Solution:
    def checkDivisibility(self, n: int) -> bool:
        """
        Determines if a positive integer n is divisible by the sum of its digit sum and digit product.

        The digit sum is the sum of all digits in n.
        The digit product is the product of all digits in n.

        Returns True if n is divisible by (digit sum + digit product), otherwise returns False.

        Args:
            n (int): The positive integer to check.

        Returns:
            bool: True if n is divisible by (digit sum + digit product), False otherwise.

        Example:
            >>> checkDivisibility(135)
            False

        Time Complexity: O(log n), where n is the number of digits in the input.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        num = n
        d_sum = 0
        d_prod = 1

        while num > 0:
            d = num % 10
            d_sum += d
            d_prod *= d
            num //= 10

        return n % (d_sum + d_prod) == 0
